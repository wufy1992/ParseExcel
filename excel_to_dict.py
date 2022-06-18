# -*- coding:utf-8 -*-
import pandas as pd


class ExcelToDict:
    def __init__(self, file_name=None, sheet_index=0):
        if not file_name:
            return
        self.excel_data = pd.read_excel(file_name, sheet_index)

    def get_dict_data(self):
        return self.excel_data.to_dict(orient ='dict')

    def get_list_data(self):
        return self.excel_data.to_dict(orient='list')


if __name__ == '__main__':
    test_excel = ExcelToDict('test_data/A_B_Report.xlsx', 1)
    dict_data = test_excel.get_dict_data()
    print(dict_data)



