import pprint
from spyne.application import Application
from spyne.decorator import rpc
#from spyne.decorator import srpc
from spyne.service import ServiceBase
from spyne.model.primitive import Integer
from spyne.model.primitive import Unicode
from spyne.model.primitive import String
from spyne.model.complex import ComplexModel
from spyne.model.complex import Iterable
from spyne.model.complex import XmlData
from spyne.model.complex import XmlAttribute
from spyne.protocol.soap import Soap11
from spyne.protocol.xml import XmlDocument
from spyne.server.wsgi import WsgiApplication

class ShortTest(ServiceBase):
    @rpc(String, String, String, _returns=String, _body_style='out_bare')
    def getQuestionMetadata(ctx, questionID, questionVersion,
                            questionBaseURL):
        print "Called getQuestionMetadata(", questionID, questionVersion, questionBaseURL, ")"
        print "ctx is", pprint.pprint(ctx)
        return "Return a bare string.."

application = Application([ShortTest],
                          tns="http://om.open.ac.uk/",
                          in_protocol=Soap11(validator='lxml',
                                             pretty_print=True,
                          ),
	                  out_protocol=Soap11()
)

if __name__ == '__main__':
    import logging
    from wsgiref.simple_server import make_server
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger('spyne.interface.wsdl11').setLevel(logging.DEBUG)
    logging.getLogger('spyne.protocol.xml').setLevel(logging.DEBUG)
    logging.getLogger('spyne.application').setLevel(logging.DEBUG)
    logging.getLogger('spyne.methodcontext').setLevel(logging.DEBUG)

    wsgi_app = WsgiApplication(application)
    server = make_server('0.0.0.0', 4444, wsgi_app)
    print "Start serving"
    server.serve_forever()
