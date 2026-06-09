from collections import defaultdict
from skidl import Pin, Part, Alias, SchLib, SKIDL, TEMPLATE

from skidl.pin import pin_types

SKIDL_lib_version = '0.0.1'

HadesGPSDongle = SchLib(tool=SKIDL).add_parts(*[
        Part(**{ 'name':'2u2', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'2u2'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Capacitor_SMD:C_0603_1608Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'100n', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'100n'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Capacitor_SMD:C_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'10n', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'10n'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Capacitor_SMD:C_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'56p', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'56p'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Capacitor_SMD:C_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'10p', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'10p'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Capacitor_SMD:C_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'100p', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'100p'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Capacitor_SMD:C_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'GREEN', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'GREEN'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'LED_SMD:LED_0603_1608Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'BLUE', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'BLUE'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'LED_SMD:LED_0603_1608Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'JSTGH', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'JSTGH'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN),
            Pin(num='3',func=pin_types.PWRIN),
            Pin(num='4',func=pin_types.PWRIN),
            Pin(num='5',func=pin_types.PWRIN),
            Pin(num='6',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'CONUFL001-SMD-T', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'CONUFL001-SMD-T'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'CONUFL001-SMD-T:CONUFL001-SMD', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN),
            Pin(num='3',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'CONSMA002', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'CONSMA002'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'CONSMA002:CONSMA002', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN),
            Pin(num='3',func=pin_types.PWRIN),
            Pin(num='4',func=pin_types.PWRIN),
            Pin(num='5',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'27n', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'27n'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Inductor_SMD:L_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'88n', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'88n'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Inductor_SMD:L_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'AO3401A', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'AO3401A'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Package_TO_SOT_SMD:SOT-23', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN),
            Pin(num='3',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'MMBT3904', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MMBT3904'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Package_TO_SOT_SMD:SOT-23', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN),
            Pin(num='3',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'2k2', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'2k2'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Resistor_SMD:R_0603_1608Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'10k', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'10k'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Resistor_SMD:R_0603_1608Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'22', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'22'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Resistor_SMD:R_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'1k', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'1k'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'Resistor_SMD:R_0402_1005Metric', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'TESEO-LIV3R', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'TESEO-LIV3R'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'TESEO-LIV3R:TESEOLIV3R', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='1',func=pin_types.PWRIN),
            Pin(num='2',func=pin_types.PWRIN),
            Pin(num='3',func=pin_types.PWRIN),
            Pin(num='4',func=pin_types.PWRIN),
            Pin(num='5',func=pin_types.PWRIN),
            Pin(num='6',func=pin_types.PWRIN),
            Pin(num='7',func=pin_types.PWRIN),
            Pin(num='8',func=pin_types.PWRIN),
            Pin(num='9',func=pin_types.PWRIN),
            Pin(num='10',func=pin_types.PWRIN),
            Pin(num='11',func=pin_types.PWRIN),
            Pin(num='12',func=pin_types.PWRIN),
            Pin(num='13',func=pin_types.PWRIN),
            Pin(num='14',func=pin_types.PWRIN),
            Pin(num='15',func=pin_types.PWRIN),
            Pin(num='16',func=pin_types.PWRIN),
            Pin(num='17',func=pin_types.PWRIN),
            Pin(num='18',func=pin_types.PWRIN)] }),
        Part(**{ 'name':'MAX2674EWT+T', 'dest':TEMPLATE, 'tool':SKIDL, 'aliases':Alias({'MAX2674EWT+T'}), 'ref_prefix':'U', 'fplist':None, 'footprint':'SchmillipKiCADLibrary:MAX2674EWT+T', 'keywords':None, 'description':'', 'datasheet':None, 'pins':[
            Pin(num='A1',func=pin_types.PWRIN),
            Pin(num='A2',func=pin_types.PWRIN),
            Pin(num='B1',func=pin_types.PWRIN),
            Pin(num='B2',func=pin_types.PWRIN),
            Pin(num='C1',func=pin_types.PWRIN),
            Pin(num='C2',func=pin_types.PWRIN)] })])