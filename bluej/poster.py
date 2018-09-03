import time

import xlrd,requests

sheet = xlrd.open_workbook('./jobdetail.xlsx').sheet_by_name("Sheet2")
fields = sheet.row_values(0)
row_num = sheet.nrows
col_num = sheet.ncols

jobs_url = "http://106.12.11.136:80/api/jobs/"
detail_url = "http://106.12.11.136:80/api/jobdetail/"


def poster(type):
    for i in range(1,row_num):
        dict = {}
        for j in range(col_num):
            dict.setdefault(fields[j], sheet.cell(i,j).value)
            if type == 'jobs':
                dict.setdefault('href', 'http://106.12.11.136:8000/user/jobdetail/?id=%d'%i)

            if type == 'jobs' and j == 5:
                # requests.post(jobs_url, dict)
                dict.setdefault('img','http://www.lanxiangren.net/logo/text2.png')
                # print(dict)
                break

            # res = requests.post(jobs_url, data = dict)

        res = None
        if type == 'jobs':
            res = requests.post(jobs_url,dict)
            pass
        else:
            res = requests.post(detail_url, dict)
            pass
        print(res,dict)


if __name__ == '__main__':
    poster('jobs')
    poster('')