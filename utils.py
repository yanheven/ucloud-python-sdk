#-*- encoding:utf-8 -*-
import hashlib


public_key="ucloud344736086@qq.com1384962117261566439"
private_key="302fb5e1dc497482450fbb0fbf1ed3bc90fd926c"
region="cn-north-03"
region="cn-east-01"
region="hk-01"
region="us-west-01"
'''
数据中心名称	API名称	数据中心网络带宽线路
北京BGP-A	cn-north-01	Bgp: BGP线路
北京BGP-B	cn-north-02	Bgp: BGP线路
北京BGP-C	cn-north-03	Bgp: BGP线路
华东双线	cn-east-01	Duplet: 双线, Unicom: 网通, Telecom: 电信
华南双线	cn-south-01	Duplet: 双线, Unicom: 网通, Telecom: 电信
亚太	hk-01	International: 国际线路
北美	us-west-01	International: 国际线路
'''

def get_token(private_key, params):
    items=params.items()
    # 请求参数串
    items.sort()
    # 将参数串排序

    params_data = "";
    for key, value in items:
        params_data = params_data + str(key) + str(value)
    params_data = params_data + private_key

    sign = hashlib.sha1()
    sign.update(params_data)
    signature = sign.hexdigest()

    return signature
    # 生成的Signature值