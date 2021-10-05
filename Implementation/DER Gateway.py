import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.ssl_ import create_urllib3_context
from xml.etree.ElementTree import Element, tostring, dump, ElementTree, fromstring

Domain = 'https://www.sane-kim.com'
Domain_post = 'https://www.sane-kim.com/post/'

# https 통신에서, 클라이언트가 본인이 쓸 수 있는 cipher 를 제시하면,
# 서버가 클라이언트가 제시한 cipher 중 본인이 제공할 수 있는 cipher를 통해 통신하게 된다.
CIPHERS = (
    'ECDHE-ECDSA-AES128-CCM8'
)

# Get data from DER (Use sock programming later with Dr.Choi)
# 추후에 이 클라이언트를 서버로 돌려서 정기적으로 라즈베리파이에서 정보를 받게끔 하고, 받았을 경우 작동하도록 함
# 현재는 예시임
mfModel = 'Test'
batteryStatus = '4'
changedTime = '1487812095'
currentPowerSource = '1'
command = '0'
'''
def getSystemData(self, batteryStatus, changedTime, currentPowerSource):
    self.batteryStatus = batteryStatus
    self.changedTime = changedTime
    self.currentPowerSource = currentPowerSource
    ...
'''

COMMEND_FROM_SERVER = '' # command from server

# Make DER data to xml format
def makeXml():
    root = Element('DERControlList')

    mf = Element('mfModel')
    mf.text = mfModel
    bs = Element('batteryStatus')
    bs.text = batteryStatus
    ct = Element('changedTime')
    ct.text = changedTime
    cPS = Element('currentPowerSource')
    cPS.text = currentPowerSource
    cm = Element('command')
    cm.text = command

    root.append(mf)
    root.append(bs)
    root.append(ct)
    root.append(cPS)
    root.append(cm)

    return tostring(root)

# Python의 requests 모듈을 사용하면 REST api를 사용할 수 있음
# 아래 코드는 requests에 TLS connection 및 cipher suite를 선택해
# 통신 가능하도록 하게 만듦
class DESAdapter(HTTPAdapter):
    """
    A TransportAdapter that re-enables 3DES support in Requests.
    """
    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)

# Get method. 서버 연결 확인용, 현재 저장된 데이터 불러오기
def GET():
    session = requests.Session()
    session.mount(Domain, DESAdapter())
    response = session.get(Domain_post)
    #GetCommand(response.text)
    print("Status: {} and reason: {}".format(response.status_code, response.reason))

# Get command for certain data
def getCom():
    certainDomain = Domain + '/getCommand/2/' # '/number/'
    session = requests.Session()
    session.mount(Domain, DESAdapter())
    response = session.get(certainDomain)
    c = getCommand()
    COMMEND_FROM_SERVER = c.getCommand(response.text)
    print("command from server: " + COMMEND_FROM_SERVER)
    print("Status: {} and reason: {}".format(response.status_code, response.reason))

class getCommand():
    def getCommand(self, com):
        tree = ElementTree(fromstring(com))
        root = tree.getroot()
        res = root.find('command').text
        return res

# POST system data
def POST_Data():
    headers = {'Content-Type': 'application/xml'}
    session = requests.Session()
    session.mount(Domain, DESAdapter())
    response = session.post(Domain_post, makeXml(), headers=headers)
    print("Status: {} and reason: {}".format(response.status_code, response.reason))


#POST_Data() # posting data
#GET() # get list of data
getCom() # get command for certain data