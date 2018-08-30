#coding=utf-8
import requests
import sys

data = [['普工','4500-5500/月','上海昌硕','上海','18-40岁','不限学历'],
['普工','4500-5500/月','上海达丰','上海','18-40岁','不限学历'],
['普工','4500-5500/月','上海英华达','上海','18-38岁','不限学历'],
['普工','4200-5000/月','昆山世硕','昆山','18-40岁','不限学历'],
['普工','4200-5000/月','苏州华硕 ','苏州','16-45岁','不限学历'],
['普工','4000-5000/月','苏州佳世达','苏州','16-45岁','不限学历'],
['普工','4000-5000/月','常熟达富','常熟','18-40岁','不限学历'],
['普工','4500-5500/月','深圳观澜富士康','深圳','18-48岁','不限学历'],
['普工','4500-5500/月','深圳龙华富士康','深圳','18-48岁','不限学历'],
['普工','4200-5000/月','郑州富士康','郑州','18-45岁','不限学历'],
['普工','4200-5000/月','成都富士康','成都','18-48岁','不限学历'],
['普工','月薪5000以上','上海汽配','上海','16-45岁','不限学历'],
['普工','月薪5000以上','上海苏泊尔','上海','18-48岁','不限学历'],
['普工','4500-5500/月','上海捷普','上海','18-48岁','不限学历'],
['普工','月薪6000左右','杭州下沙电子厂','杭州','16-45岁','不限学历'],
['普工','20元一个小时','上海永亿','上海','18-48岁','不限学历'],
['普工','4500-5500/月','昆山联滔','昆山','男18-40岁，女18-43岁','不限学历'],
['普工','4500-5500/月','昆山华至欧','昆山','18-38岁','不限学历'],
['普工','4500-5500/月','嘉善富士康','嘉善','18-45岁','不限学历'],
['普工','4500-5500/月','苏州美特','苏州','男18-38周岁，女18-40周岁','不限学历'],
['普工','4500-5500/月','太原富士康','太原','男16.5-54岁，女16.5-49岁','不限学历'],
['普工','4500-5500/月','上海富士康','上海','18-38岁','不限学历'],
['普工','4500-5500/月','苏州华硕','苏州','16-45岁','不限学历'],
['普工','4500-5500/月','新世电子','上海','女18-45岁','不限学历'],
['普工','4500-5500/月','无锡优科多','无锡','18-45岁','不限学历'],
['普工','4500-5500/月','松江日沛／日腾','上海','17-46周岁','不限学历'],
['普工','月薪5000以上','嘉兴闻泰通迅','嘉兴','16-47','不限学历'],
['普工','4500-5500/月','盐城东山维信','盐城','18-48岁','不限学历'],
['普工','4500-5500/月','泰州可胜','泰州','18-45岁','不限学历'],
['普工','综合工资5000元以上','上海皮划艇厂','上海','25-48周岁','不限学历'],
['普工','月薪5000-6000以上','品牌化妆品包装公司','南通','40岁以下','不限学历'],
['数控机床专业（实习生）','月薪4500左右','上海日铭','上海','17周岁以上','不限学历'],
['普工（实习生）','月薪4500左右','上海日月光','上海','17岁以上','不限学历'],
['普工（实习生）','月薪4500左右','上海保利马科技','上海','16岁以上','不限学历'],
['普工（实习生）','月薪4500左右','上海赫比','上海','16岁以上','不限学历'],
['普工（实习生）','月薪4500左右','上海/芜湖汽车线束厂','上海','18岁以上','不限学历'],
['普工（实习生）','月薪4500左右','江苏光伏企业','江苏','18岁以上','不限学历'],
['普工（实习生）','月薪4500左右','南通化妆品厂','南通','16岁以上','不限学历'],
['普工（实习生）','月薪4500左右','南通大地汽车线束','南通','16岁以上','不限学历'],
['焊工类培训学校实习生','月薪4500左右','中集集团-上海厂区/南通厂区','上海南通','18岁以上','不限学历'],]

for solo in data:
    print (solo)
    url ="http://www.lanxiangren.net:8000/api/jobs/"
    payload={
                "href": "http://www.lanxiangren.net",
                "img": "http://www.lanxiangren.net/logo/text2.png",
                "title": solo[0],
                "salary":solo[1],
                "name": solo[2],
                "msg1": solo[3],
                "msg2": solo[4],
                "msg3": solo[5]
            }
    response = requests.request("POST", url, data=payload, )
    print (response.text)


# a = '''
# 普工	4500-5500	上海昌硕	上海	18-40岁	不限学历
# 普工	4500-5500	上海达丰	上海	18-40岁	不限学历
# 普工	4500-5500	上海英华达	上海	18-38岁	不限学历
# 普工	4200-5000	昆山世硕	昆山	18-40岁	不限学历
# 普工	4200-5000	苏州华硕 	苏州	16-45岁	不限学历
# 普工	4000-5000	苏州佳世达	苏州	16-45岁	不限学历
# 普工	4000-5000	常熟达富	常熟	18-40岁	不限学历
# 普工	4500-5500	深圳观澜富士康	深圳	18-48岁	不限学历
# 普工	4500-5500	深圳龙华富士康	深圳	18-48岁	不限学历
# 普工	4200-5000	郑州富士康	郑州	18-45岁	不限学历
# 普工	4200-5000	成都富士康	成都	18-48岁	不限学历
# 普工	月薪5000以上	上海汽配	上海	16-45岁	不限学历
# 普工	月薪5000以上	上海苏泊尔	上海	18-48岁	不限学历
# 普工	4500-5500	上海捷普	上海	18-48岁	不限学历
# 普工	月薪6000左右	杭州下沙电子厂	杭州	16-45岁	不限学历
# 普工	20元一个小时	上海永亿	上海	18-48岁	不限学历
# 普工	4500-5500	昆山联滔	昆山	男18-40岁，女18-43岁	不限学历
# 普工	4500-5500	昆山华至欧	昆山	18-38岁	不限学历
# 普工	4500-5500	嘉善富士康	嘉善	18-45岁	不限学历
# 普工	4500-5500	苏州美特	苏州	男18-38周岁，女18-40周岁	不限学历
# 普工	4500-5500	太原富士康	太原	男16.5-54岁，女16.5-49岁	不限学历
# 普工	4500-5500	上海富士康	上海	18-38岁	不限学历
# 普工	4500-5500	苏州华硕	苏州	16-45岁	不限学历
# 普工	4500-5500	新世电子	上海	女18-45岁	不限学历
# 普工	4500-5500	无锡优科多	无锡	18-45岁	不限学历
# 普工	4500-5500	松江日沛／日腾	上海	17-46周岁	不限学历
# 普工	月薪5000以上	嘉兴闻泰通迅	嘉兴	16-47	不限学历
# 普工	4500-5500	盐城东山维信	盐城	18-48岁	不限学历
# 普工	4500-5500	泰州可胜	泰州	18-45岁	不限学历
# 普工	综合工资5000元以上	上海皮划艇厂	上海	25-48周岁	不限学历
# 普工	月薪5000-6000以上	品牌化妆品包装公司	南通	40岁以下	不限学历
# 数控机床专业（实习生）	月薪4500左右	上海日铭	上海	17周岁以上	不限学历
# 普工（实习生）	月薪4500左右	上海日月光	上海	17岁以上	不限学历
# 普工（实习生）	月薪4500左右	上海保利马科技	上海	16岁以上	不限学历
# 普工（实习生）	月薪4500左右	上海赫比	上海	16岁以上	不限学历
# 普工（实习生）	月薪4500左右	上海/芜湖汽车线束厂	上海	18岁以上	不限学历
# 普工（实习生）	月薪4500左右	江苏光伏企业	江苏	18岁以上	不限学历
# 普工（实习生）	月薪4500左右	南通化妆品厂	南通	16岁以上	不限学历
# 普工（实习生）	月薪4500左右	南通大地汽车线束	南通	16岁以上	不限学历
# 焊工类培训学校实习生	月薪4500左右	中集集团-上海厂区/南通厂区	上海南通	18岁以上	不限学历
# '''
# a=a.replace("	","\',\'")
# a=a.replace("\n","'],\n[\'")
# print (a)
# print