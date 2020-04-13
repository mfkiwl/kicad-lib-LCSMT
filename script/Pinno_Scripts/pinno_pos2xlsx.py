#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
try: 
    import openpyxl
except: 
    os.system("pip install openpyxl")
import time

# 打印输出基本信息
print('pos转xlsx工具')
print('')
print('Written by：Naisu and changed by fuhua.chen for pinno')
print('Created date：2018.07.09 / Changed date: 2020.04.05')
print('')
print('该工具用于将KiCad PCB编辑器中导出的坐标文件（.pos）转换为表格（.xlsx）,用于贴片机识别坐标')
print('this tool is used to transform the .pos file generated by KiCad to .xlsx file which for SMT')
print('')
print('使用该工具前请确保pos文件和该工具在同一目录下')
print('please confirm that .pos file and this tool are in the same directory')
print('')

userPos = sys.argv[1]
print('正在打开文件……')

try:
    posFile = open(userPos,mode="r")
    print('打开文件成功！')
    print('load file successfully！')
except:
    print('打开文件失败，请检查文件位置及名称！')
    print('load file fail')
    exit()
print('')

# 读取坐标文件内容
print('正在读取文件……')
print('reading file……')
posContent = posFile.readlines()
posData = []
for x in range(5, len(posContent)-1):
    posData.append(posContent[x].split())

posFile.close()
print('完成文件读取！')
print('End of Reading!')
print('')

# 将数据写入xlsx
print('正在将数据写入xlsx文件……')
print('Writing data to .xlsx……')
wb = openpyxl.Workbook()
sheet = wb.active

sheet.column_dimensions['A'].width = 10
sheet.column_dimensions['B'].width = 10
sheet.column_dimensions['C'].width = 30
sheet.column_dimensions['D'].width = 15
sheet.column_dimensions['E'].width = 15
sheet.column_dimensions['F'].width = 15
sheet.column_dimensions['G'].width = 10

sheet.merge_cells('A1:G1')
sheet['A1'] = posContent[2][3:]

sheet['A2'] = 'Ref'
sheet['B2'] = 'Value'
sheet['C2'] = 'Package'
sheet['D2'] = 'PosX'
sheet['E2'] = 'PosY'
sheet['F2'] = 'Rot'
sheet['G2'] = 'Side'

for x in range(len(posData)):
    sheet['A'+str(x+3)] = posData[x][0]
    sheet['B'+str(x+3)] = posData[x][1]
    sheet['C'+str(x+3)] = posData[x][2]
    sheet['D'+str(x+3)] = posData[x][3]
    sheet['E'+str(x+3)] = posData[x][4]
    sheet['F'+str(x+3)] = posData[x][5]
    sheet['G'+str(x+3)] = posData[x][6]

wb.save(userPos[:-4] + '_SMT坐标'+'.xlsx')
wb.close()
print('完成写入并生成xlsx文件！')
print('Successed!！')

exit()