import os.path
import urlparse
import urllib

from suds.client import Client

from onvif.exceptions import ONVIFError


def test():
    url = 'wsdl/devicemgmt.wsdl'
    # print os.path.dirname(os.path.abspath(__file__))
    # print os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wsdl/accesscontrol.wsdl')
    url = os.path.join(os.path.dirname(os.path.abspath(__file__)), url)

    if not os.path.isfile(url):
        raise ONVIFError('%s doesn`t exist!' % url)

    url = urlparse.urljoin('file:', urllib.pathname2url(url))
    client = Client(url)
    print client