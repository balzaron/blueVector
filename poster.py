import time

import xlrd,requests

sheet = xlrd.open_workbook('./jobdetail.xlsx').sheet_by_index(0)
fields = sheet.row_values(0)
row_num = sheet.nrows
col_num = sheet.ncols
print(row_num,col_num)

jobs_url = "http://106.12.11.136:8000/api/jobs/"
detail_url = "http://106.12.11.136:8000/api/jobdetail/"


def poster(type):
    for i in range(1,row_num):
        dict = {}
        for j in range(col_num):
            if type != "jobs" and j==6:
                continue
            else:
                dict.setdefault(fields[j], sheet.cell(i,j).value)
            if type == 'jobs':
                dict.setdefault('href', 'http://106.12.11.136:8000/user/jobdetail/?id=%d'%i)
            if type == 'jobs' and j == 6:
                # requests.post(jobs_url, dict)
                # dict.setdefault('img','http://www.lanxiangren.net/logo/text2.png')
                # print(dict)
                break


            # res = requests.post(jobs_url, data = dict)

        res = None
        if type == 'jobs':
            print ("jobs",dict)
            # res = requests.post(jobs_url,dict)
            pass
        else:
            print ("detail",dict)
            # res = requests.post(detail_url, dict)
            pass
        # print(res,dict)


if __name__ == '__main__':
    poster('jobs')