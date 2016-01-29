#coding=utf-8
import pymssql
import xlwt
import os
import StringIO
import datetime,time

def set_style(name,height,color=0,bold=False,borderleft=0,borderright=0,top=0,bottom=0):
    style = xlwt.XFStyle() # 初始化样式#
    font = xlwt.Font() # 为样式创建字体
    font.name = name # 'Times New Roman'
    font.bold = bold
    font.colour_index = color
    font.height = height
    borders= xlwt.Borders()   #
    borders.left= borderleft   #
    borders.right= borderright   #
    borders.top= top   #
    borders.bottom= bottom
    borders.left=xlwt.Borders.DASHED
    borders.right=xlwt.Borders.THIN
    borders.top=xlwt.Borders.DASHED
    borders.bottom=xlwt.Borders.THIN
    style.font = font   #
    style.borders = borders
    return style
def create_xls(cx_date,c_date):
    file_path=os.getcwd()
    f=xlwt.Workbook()
    sheet1=f.add_sheet(u'销售流水',cell_overwrite_ok=True)
    conn = pymssql.connect(host='192.168.0.236',user='select',password='Sl83517668',database='UFTData810145_000002',charset='utf8')
    viplist=conn.cursor()
    today=datetime.datetime.now()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    date_yesterday=yesterday.date()
    Sql='select * from V_Shop_InventorySaleDetail WHERE ' + ' orderdate between '+'\''+str(cx_date)+' 00:00:00'+'\''+'and '+'\''+str(c_date)+' 00:00:00'+'\''+' ORDER by shop'
    print Sql
    viplist.execute(Sql)
    rows=[u'店铺',u'单据日期',u'星期',u'商品编码',u'商品名称',u'一级分类',u'二级分类',u'三级分类',u'数量',u'含税单价',u'含税金额',u'零售价',u'零售金额',u'折扣',u'导购']
    for j in range(len(rows)):
        sheet1.write(0,j ,rows[j],set_style('Arial',220,2,True,1,1,1,1))
    row=1
    for shop,orderdate,orderweekday,item_no,item_name,firstclass,secondclass,thirdclass,quantity,saleprice,saleamount,price,amount,discount,emoplyee in viplist.fetchall():
        sheet1.write(row,0,shop,set_style('Dotum',220,0,False,1,0,1,0))
        sheet1.write(row,1,orderdate,set_style('Dotum',220,0,False,0,0,0,0))
        sheet1.write(row,2,orderweekday,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,3,item_no,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,4,item_name,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,5,firstclass,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,6,secondclass,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,7,thirdclass,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,8,quantity,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,9,saleprice,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,10,saleamount,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,11,price,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,12,amount,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,13,discount,set_style('Dotum',220,0,False,1,1,1,1))
        sheet1.write(row,14,emoplyee,set_style('Dotum',220,0,False,1,1,1,1))
        row+=1
    f.save(file_path+str(cx_date)+'.xls')




r=create_xls('2016-01-01','2016-01-25')
r

