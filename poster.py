import time

import xlrd,requests

wb = xlrd.open_workbook('./jobdetail.xlsx')


sheet_jobs = wb.sheet_by_name('job')
sheet_train = wb.sheet_by_name('train')
fields = sheet_jobs.row_values(0)


jobs_url = "http://www.lanxiangren.net/api/jobs/"
jobs_detail_url = "http://www.lanxiangren.net/api/jobdetail/"
jobs_urls = [jobs_url, jobs_detail_url]

train_url = 'http://www.lanxiangren.net/train/jobs/'
train_detail_url = 'http://www.lanxiangren.net/train/jobsdetail/'
train_urls = [train_url, train_detail_url]

types = ('overview', 'detail')


def poster(sheet, type, urls):

    row_num = sheet.nrows
    col_num = sheet.ncols
    for i in range(1,row_num):
        dict = {}
        for j in range(col_num):
            if type != types[0] and j==6:
                continue
            else:
                dict.setdefault(fields[j], sheet.cell(i,j).value)
            if type == types[0]:
                dict.setdefault('href', 'http://www.lanxiangren.net/user/jobdetail/?id=%d'%i)
            if type == types[0] and j == 6:
                break

        res = None
        if type == types[0]:
            print ("overview",dict)
            res = requests.post(urls[0],dict)
            print(res.text)
            pass
        else:
            print ("detail",dict)
            res = requests.post(urls[1], dict)
            print(res.text)
            pass



if __name__ == '__main__':
    for i in types:
        poster(sheet_train, i, train_urls)