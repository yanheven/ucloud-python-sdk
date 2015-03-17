'''
ucloud python sdk client.
'''
import utils
import base
import uhost
import umon
import unet


class Client(object):
    '''
    ucloud python sdk client.
    '''
    def __init__(self,base_url,public_key,private_key):
        self.base_url=base_url
        self.private_key=private_key
        self.public_key=public_key

        self.uhost=uhost.UhostManager(self)
        self.unet=unet.UnetManager(self)
        self.client=base.HTTPClient(base_url)

if __name__=='__main__':
    public_key='ucloud344736086@qq.com1384962117261566439'
    private_key='302fb5e1dc497482450fbb0fbf1ed3bc90fd926c'
    base_url='https://api.ucloud.cn'
    region='cn-north-03'
    c=Client(base_url,public_key,private_key)
    image_id='uimage-3gzxij'
    print(c.uhost.get(region))
    print(c.uhost.get_price(region,image_id,2,2048,1,'Month'))


