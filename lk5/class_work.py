# import json
# from pprint import pprint
#
# data = None
# with open('test_json.json') as file:
#     data = json.load(file)
#     pprint(data, indent=4)
#     print(type(data))
#
#     print(data['widget']['debug'])
#
# data['widget']['debug'] = 'off'
# print(data['widget']['debug'])
#
# with open('test_json.json', 'w') as file:
#     json.dump(data, file, indent=4)


# with open('test_json.json') as file:
#     print(file.read())
#     print(type(file.read()))
# import yaml
#
# data = None
# with open('test_yaml.yaml') as file:
#     data = yaml.safe_load(file)
#     print(data)
#
# data['laptop']['CPU'] = 16
# with open('test_yaml.yaml', 'w') as file:
#     yaml.safe_dump(data, file)


# CSV
# import csv
#
# data_list = [[1, 2], 'kjsndkjcv', [3, 4]]
# with open('test.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerows(data_list)

# для exel xlsxwriter
import xlsxwriter

headers = ('ID', 'created_at', 'updated_at', 'vin', 'color', 'name', 'car_number', 'model', 'make',
                        'production_year', 'status')
workbook = xlsxwriter.Workbook('file.xlsx')
work_sheet = workbook.add_worksheet('list1')
cell_format = workbook.add_format({'bold': True})
worksheet = workbook.add_worksheet()
col = 0
for header in headers:
    worksheet.set_column(0, col, 30)
    worksheet.write(0, col, header, cell_format)
    col+=1
workbook.close()


