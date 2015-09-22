# ndd
Network Device Discovery

## ONVIF Device Discovery [[ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf) Section 7. Excerpts

### Terms and Definitions

Defined below are the basic definitions for the terms used in
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html).
* **Target Service** - An endpoint that makes itself available for discovery.
* **Client** - An endpoint that searches for Target Service(s).
* **Discovery Proxy** - An endpoint that facilitates discovery of Target
    Services by Clients.
* **Hello** - A message sent by a Target Service when it joins a network;
    this message contains key information for the Target Service. A Hello
    message is also sent by a Discovery Proxy to reduce multicast traffic on an
    ad hoc network; this message contains key information about the Discovery
    Proxy.
* **Bye** - A best-effort message sent by a Target Service when it leaves a
    network.
* **Probe** - A message sent by a Client searching for a Target Service by Type
    and/or Scope.
* **Resolve** - A message sent by a Client searching for a Target Service by
    name.
* **Type** - An identifier for a set of messages an endpoint sends and/or
    receives (e.g., a WSDL 1.1 portType, see [[WSDL 1.1]](http://www.w3.org/TR/2001/NOTE-wsdl-20010315#_porttypes)).
* **Scope** - An extensibility point that allows Target Services to be organized
    into logical groups.
* **Metadata** - Information about the Target Service; includes, but is not
    limited to, transports and protocols a Target Service understands, Types it
    implements, and Scopes it is in.
* **Ad hoc Mode** - An operational mode of discovery in which the Hello, Bye,
    Probe and Resolve messages are sent multicast.
* **Managed Mode** - An operational mode of discovery in which the Hello, Bye,
    Probe and Resolve messages are sent unicast to a Discovery Proxy.
* **Ad hoc Network** - A network in which discovery is performed in an ad hoc
    mode.
* **Managed Network** - A network in which discovery is performed in a managed
    mode.

### 1. General
A client searches for available devices using the dynamic [Web Services discovery protocol [WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html).

A device compliant with [ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf)
shall implement the Target Service role as specified in
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html),
namely, support for messages such as:
* [Hello](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231822)
* [Bye](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231826)
* [Probe](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231833)
* [Probe Match](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231836)
* [Resolve](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231842)
* [Resolve Match](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231845)

A client compliant with [ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf)
shall implement the Client role as specified in
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html),
namely, support for messages such as:
* [Hello](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231823)
* [Bye](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231827)
* [Probe](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231832)
* [Resolve](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231841)

Discovery Proxy role as described in
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html)
**shall not be supported** by a device or a client (**an alternative Discovery
Proxy role** is introduced in
[ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf),
see Section 7.4). A device that implements the client role ignores the
interaction scheme with the Discovery Proxy as described in
[Section 2 in [WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231809).
Instead, [ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf)
defines a new Discovery Proxy role that allows remote discovery. The remote
discovery relies on the presence of a Discovery Proxy and a system provider that
would like to offer remote discovery in the system should implement the
Discovery Proxy role as specified in Section 7.4.


[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html)
describes the Universally Unique Identifier (UUID): URI format recommendation
for endpoint references in [Section 2.1](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231810),
but [ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf)
overrides this recommendation. Instead, the Uniform Resource Name: Universally
Unique Identifier (URN:UUID) format is used
[RFC4122](http://tools.ietf.org/html/rfc4122) (see
[ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf)
Section 7.3.1).

### 2. Modes of operation

The device shall be able to operate in two modes:
* Discoverable
* Non-discoverable

A device in discoverable mode sends multicast Hello messages once connected to
the network or sends its Status changes according to
[WS-Discovery Section 2.2.1](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231812).
In addition it always listens for Probe and Resolve messages and sends responses
accordingly. A device in non-discoverable shall not listen to
[WS-Discovery Section 2.2.1](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html#_Toc234231812)
messages or send such messages. The devices default behaviour shall be the
discoverable mode. In order to thwart denial-of-service attacks, it shall be
possible to set a device into non-discoverable mode through the operation
defined in
[ONVIF Core Specification](http://www.onvif.org/specs/core/ONVIF-Core-Specification-v260.pdf)
Section 8.3.19.


### Protocol Assignments

#### Ad hoc mode over IP multicast

If IP multicast is used to send multicast messages described in
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html),
they MUST be sent using the following assignments:
* DISCOVERY_PORT: port 3702 [[IANA](http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml)]
* IPv4 multicast address: 239.255.255.250
* IPv6 multicast address: FF02::C (link-local scope)
Other address bindings MAY be defined but are beyond the scope of
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html)
specification.

Messages sent over UDP MUST be sent using SOAP over UDP
[[SOAP/UDP](http://docs.oasis-open.org/ws-dd/soapoverudp/1.1/os/wsdd-soapoverudp-1.1-spec-os.html)].
To compensate for possible UDP unreliability, senders MUST use the example
transmission algorithm in [Appendix A of SOAP over UDP](http://docs.oasis-open.org/ws-dd/soapoverudp/1.1/os/wsdd-soapoverudp-1.1-spec-os.html#_Toc229451838).
In order to improve interoperability and network efficiency use of
[SOAP 1.2 protocol [SOAP 1.2]](http://www.w3.org/TR/2007/REC-soap12-part1-20070427/)
is RECOMMENDED.

#### Managed mode over HTTP

If the messages described  in
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html)
are sent unicast using HTTP protocol, they MUST be sent using SOAP HTTP Binding
as defined in
[Section 7 of SOAP 1.2 Part 2 [SOAP 1.2 Part 2]](http://www.w3.org/TR/2007/REC-soap12-part2-20070427/#soapinhttp).

#### Application Level Transmission Delay

Before sending some message types defined in
[[WS-Discovery]](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-spec-os.html),
a Target Service MUST wait for a timer to elapse before sending the message
using the bindings described above. This timer MUST be set to a random value
between 0 and APP_MAX_DELAY. The default value for APP_MAX_DELAY parameter is
500 milliseconds. The default value MAY be revised by other specifications.




[WSDL](http://docs.oasis-open.org/ws-dd/discovery/1.1/os/wsdd-discovery-1.1-wsdl-os.wsdl)
[Multicast](https://en.wikipedia.org/wiki/Multicast) протокол поиска устройств
в локальной сети. Работает по протоколам TCP и UDP через порт **3702** и
использует ip 239.255.255.250. Связь между узлами реализуется стандартами
[Web-Services](https://en.wikipedia.org/wiki/Web_service), а именно
[SOAP-over-UDP](http://docs.oasis-open.org/ws-dd/soapoverudp/1.1/os/wsdd-soapoverudp-1.1-spec-os.html).

A device compliant with this specification shall implement the Target Service role as specified
in [WS-Discovery].

