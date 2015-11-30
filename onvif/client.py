import os.path
import urlparse
import urllib

from suds.client import Client

from onvif.exceptions import ONVIFError


def test():
    url = 'schemas/www.onvif.org/onvif/ver10/analyticsdevice.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/deviceio.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/display.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/receiver.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/recording.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/replay.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/search.wsdl'

    url = 'schemas/www.onvif.org/onvif/ver10/device/wsdl/devicemgmt.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/events/wsdl/event.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/media/wsdl/media.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/network/wsdl/remotediscovery.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver10/schema/onvif.xsd'

    url = 'schemas/www.onvif.org/onvif/ver20/analytics/wsdl/analytics.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver20/imaging/wsdl/imaging.wsdl'
    url = 'schemas/www.onvif.org/onvif/ver20/ptz/wsdl/ptz.wsdl'

    url = 'schemas/www.onvif.org/ver10/accessrules/wsdl/accessrules.wsdl'
    url = 'schemas/www.onvif.org/ver10/advancedsecurity/wsdl/advancedsecurity.wsdl'
    url = 'schemas/www.onvif.org/ver10/credential/wsdl/credential.wsdl'
    url = 'schemas/www.onvif.org/ver10/schedule/wsdl/schedule.wsdl'
    url = 'schemas/www.onvif.org/ver10/pacs/accesscontrol.wsdl'
    url = 'schemas/www.onvif.org/ver10/pacs/doorcontrol.wsdl'
    url = 'schemas/www.onvif.org/ver10/pacs/types.xsd'
    url = 'schemas/www.onvif.org/ver10/actionengine.wsdl'

    # print os.path.dirname(os.path.abspath(__file__))
    # print os.path.join(os.path.dirname(os.path.abspath(__file__)), 'wsdl/accesscontrol.wsdl')
    url = os.path.join(os.path.dirname(os.path.abspath(__file__)), url)

    if not os.path.isfile(url):
        raise ONVIFError('%s doesn`t exist!' % url)

    url = urlparse.urljoin('file:', urllib.pathname2url(url))
    client = Client(url)
    print client
