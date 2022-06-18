# -*- coding:utf-8 -*-
from excel_to_dict import ExcelToDict

info_data = ExcelToDict('../test_data/A_B_Report.xlsx', 0).get_list_data()
target_data = ExcelToDict('../test_data/A_B_Report.xlsx', 1).get_list_data()
target_set = set()
for gene_name in target_data['Gene']:
    target_set.add(gene_name)
print("target")
for gene_name in info_data['Gene']:
    print(gene_name in target_set)


