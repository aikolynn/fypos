#coding=utf-8
import sys
import xlwt
from django.shortcuts import render,HttpResponse
from django.template.loader import get_template
import pymssql
from django.core.paginator import *

def sale_flow(request):
    #重载sys
    reload(sys)
    #设置默认编码为utf-8
    sys.setdefaultencoding('utf-8')
    #获取查询日期
    global cx_startdate
    cx_startdate = request.GET.get('startdate','')
    global cx_enddate
    cx_enddate=request.GET.get('enddate','')
    #获取查询店铺
    global shop
    shop = request.GET.get('shop','')
    #类别合计查询
    group_sql='select firstclass,sum(saleamount),sum(amount),sum(quantity) from V_Shop_InventorySaleDetail WHERE shop like' + '\'%' +shop+ '%\'' +'and orderdate between '+'\''+str(cx_startdate)+' 00:00:00'+'\''+' and \''+str(cx_enddate)+' 00:00:00'+'\''+'group by firstclass'
    #导购合计查询
    group_emoplyee='select employee,sum(saleamount),sum(quantity) from V_Shop_InventorySaleDetail WHERE shop LIKE ' + '\'%' +shop+ '%\'' +'and orderdate between '+'\''+str(cx_startdate)+' 00:00:00'+'\''+' and \''+str(cx_enddate)+' 00:00:00'+'\''+'group by employee'
    #销售总额查询语句
    sum_sql='select sum(saleamount),sum(quantity) from V_Shop_InventorySaleDetail WHERE shop LIKE ' + '\'%' +shop+ '%\'' +'and orderdate between '+'\''+str(cx_startdate)+' 00:00:00'+'\''+' and \''+str(cx_enddate)+' 00:00:00'+'\''
    #销售流水查询语句
    cx_sql='select * from V_Shop_InventorySaleDetail WHERE shop LIKE ' + '\'%' +shop+ '%\'' +'and orderdate between '+'\''+str(cx_startdate)+' 00:00:00'+'\''+' and \''+str(cx_enddate)+' 00:00:00'+'\''+' ORDER by shop'
    #建立数据库连接
    conn = pymssql.connect(host='192.168.0.236',user='select',password='Sl83517668',database='UFTData810145_000002',charset="utf8")
    #获取游标
    cursor_link=conn.cursor()
    #获取销售流水
    cursor_link.execute(cx_sql)
    row =cursor_link.fetchall()
    #获取销售总额
    cursor_link.execute(sum_sql)
    sumq=cursor_link.fetchall()
    #获取类别销售统计
    cursor_link.execute(group_sql)
    groupq=cursor_link.fetchall()
    #获取导购销售统计
    cursor_link.execute(group_emoplyee)
    emoplyeeq=cursor_link.fetchall()
    #销售流水分页
    pagelist=Paginator(row,30)
    row=None
    page=None
    try:
        page=int(request.GET.get('page',1))
        row=pagelist.page(page)
    except (PageNotAnInteger,EmptyPage,InvalidPage):
        row=pagelist.page(1)
    tem=get_template('index.html')
    cont={'cx_startdate':cx_startdate,'cx_enddate':cx_enddate, 'shop':shop, 'row': row,'page':page,'pagelist':pagelist,'emoplyeeq':emoplyeeq,'sumq':sumq,'groupq':groupq }

    content=tem.render(cont)
    return HttpResponse(content)

def export_xls(request):
     conn = pymssql.connect(host='192.168.0.236',user='select',password='Sl83517668',database='UFTData810145_000002',charset="utf8")
     cx_sql='select * from V_Shop_InventorySaleDetail WHERE shop LIKE ' + '\'%' +shop+ '%\'' +'and orderdate between '+'\''+str(cx_startdate)+' 00:00:00'+'\''+' and \''+str(cx_enddate)+' 00:00:00'+'\''+' ORDER by shop'
     print cx_sql
     list=conn.cursor()
     list.execute(cx_sql)
     row = list.fetchall()
     _lst=[]
     _lst.extend(row[:])
     _lst.insert(0,[u'店铺',u'单据日期',u'星期',u'商品编码',u'商品名称',u'一级分类',u'二级分类',u'三级分类',u'数量',u'含税单价',u'含税金额',u'零售价',u'零售金额',u'折扣',u'导购'])
     #将数据写入Excel表
     book=xlwt.Workbook(encoding='utf-8')
     sheet=book.add_sheet(u'销售流水')
     for rowlist,rowdata in enumerate(_lst):
        for col,val in enumerate(rowdata):
            sheet.write(rowlist,col,val,style=xlwt.Style.default_style)
     #将表格传到浏览器
     response=HttpResponse(content_type='application/vnd.ms-excel')
     response['Content-Disposition']='attachment; filename=销售流水.xls'
     book.save(response)
     return response
