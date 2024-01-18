# -*- coding: utf-8 -*-
import xlsxwriter as xw


def xw_toExcel(data, fileName):  # xlsxwriter库储存数据到excel
    workbook = xw.Workbook(fileName)  # 创建工作簿
    worksheet1 = workbook.add_worksheet("sheet1")  # 创建子表
    worksheet1.activate()  # 激活表
    title = ['问题', '答案', '选项', '解析']  # 设置表头
    worksheet1.write_row('A1', title)  # 从A1单元格开始写入表头
    i = 2  # 从第二行开始写入数据
    for j in range(len(data)):
        insertData = [data[j]["title"], data[j]["answer_"], data[j]["answer"], data[j]["info"]]
        row = 'A' + str(i)
        worksheet1.write_row(row, insertData)
        if data[j]["path"]:
            image_options = {
                'x_offset': 0,  # 图片在单元格中的水平偏移量
                'y_offset': 0,  # 图片在单元格中的垂直偏移量
                'x_scale': 0.08,  # 图片的水平缩放比例
                'y_scale': 0.08,  # 图片的垂直缩放比例
            }
            worksheet1.insert_image(row+f"E{i}", data[j]["path"], image_options)
        i += 1
    workbook.close()  # 关闭表
