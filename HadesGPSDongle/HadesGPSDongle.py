# Auto-generated SKiDL script from HadesGPSDongle_original.net
# Source: Philip M. Salmony - Hades GPS Dongle
# 27 components, 27 nets, 84 connections

from skidl import *

# ── Named nets (Net.fetch prevents auto-suffixing) ────────────
net_N_3_3V = Net.fetch("+3.3V")
net_ANT_ACTIVE = Net.fetch("ANT_ACTIVE")
net_ANT_PASSIVE = Net.fetch("ANT_PASSIVE")
net_GND = Net.fetch("GND")
net_GPS_RST = Net.fetch("GPS_!RST")
net_GPS_PPS = Net.fetch("GPS_PPS")
net_GPS_WAKEUP = Net.fetch("GPS_WAKEUP")
net_LNA_OUT = Net.fetch("LNA_OUT")
net_Net_C7_Pad1 = Net.fetch("Net-(C7-Pad1)")
net_Net_D1_K = Net.fetch("Net-(D1-K)")
net_Net_D2_K = Net.fetch("Net-(D2-K)")
net_Net_J1_Pin_5 = Net.fetch("Net-(J1-Pin_5)")
net_Net_Q2_B = Net.fetch("Net-(Q2-B)")
net_Net_Q2_C = Net.fetch("Net-(Q2-C)")
net_Net_U1_ANT_OFF = Net.fetch("Net-(U1-ANT_OFF)")
net_Net_U1_RX = Net.fetch("Net-(U1-RX)")
net_Net_U1_TX = Net.fetch("Net-(U1-TX)")
net_Net_U2_RFIN = Net.fetch("Net-(U2-RFIN)")
net_Net_U2_RFOUT_slash_SHDN = Net.fetch("Net-(U2-RFOUT{slash}~{SHDN})")
net_UART_RX = Net.fetch("UART_RX")
net_UART_TX = Net.fetch("UART_TX")
net_VCC = Net.fetch("VCC")
net_VCC_RF = Net.fetch("VCC_RF")

# ── Unconnected pins ──────────────────────────────────────────
net_unconnected_U1_RESERVED_1_Pad15 = Net("unconnected-(U1-RESERVED_1-Pad15)")
net_unconnected_U1_RESERVED_2_Pad18 = Net("unconnected-(U1-RESERVED_2-Pad18)")
net_unconnected_U1_SCL_Pad17 = Net("unconnected-(U1-SCL-Pad17)")
net_unconnected_U1_SDA_Pad16 = Net("unconnected-(U1-SDA-Pad16)")

# ── Components ────────────────────────────────────────────────
# C1 - 2u2
C1_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C1 = C1_tmpl()
C1.ref = "C1"
C1.value = "2u2"

# C2 - 100n
C2_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C2 = C2_tmpl()
C2.ref = "C2"
C2.value = "100n"

# C3 - 10n
C3_tmpl = Part(tool=SKIDL, name="10n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C3 = C3_tmpl()
C3.ref = "C3"
C3.value = "10n"

# C4 - 56p
C4_tmpl = Part(tool=SKIDL, name="56p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C4 = C4_tmpl()
C4.ref = "C4"
C4.value = "56p"

# C5 - 56p
C5_tmpl = Part(tool=SKIDL, name="56p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C5 = C5_tmpl()
C5.ref = "C5"
C5.value = "56p"

# C6 - 10p
C6_tmpl = Part(tool=SKIDL, name="10p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C6 = C6_tmpl()
C6.ref = "C6"
C6.value = "10p"

# C7 - 100p
C7_tmpl = Part(tool=SKIDL, name="100p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C7 = C7_tmpl()
C7.ref = "C7"
C7.value = "100p"

# C8 - 100p
C8_tmpl = Part(tool=SKIDL, name="100p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C8 = C8_tmpl()
C8.ref = "C8"
C8.value = "100p"

# D1 - GREEN
D1_tmpl = Part(tool=SKIDL, name="GREEN", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D1 = D1_tmpl()
D1.ref = "D1"
D1.value = "GREEN"

# D2 - BLUE
D2_tmpl = Part(tool=SKIDL, name="BLUE", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D2 = D2_tmpl()
D2.ref = "D2"
D2.value = "BLUE"

# J1 - JSTGH
J1_tmpl = Part(tool=SKIDL, name="JSTGH", footprint="Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
J1 = J1_tmpl()
J1.ref = "J1"
J1.value = "JSTGH"

# J2 - CONUFL001-SMD-T
J2_tmpl = Part(tool=SKIDL, name="CONUFL001-SMD-T", footprint="CONUFL001-SMD-T:CONUFL001-SMD",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
J2 = J2_tmpl()
J2.ref = "J2"
J2.value = "CONUFL001-SMD-T"

# J3 - CONSMA002
J3_tmpl = Part(tool=SKIDL, name="CONSMA002", footprint="CONSMA002:CONSMA002",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN)], dest=TEMPLATE)
J3 = J3_tmpl()
J3.ref = "J3"
J3.value = "CONSMA002"

# L1 - 27n
L1_tmpl = Part(tool=SKIDL, name="27n", footprint="Inductor_SMD:L_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
L1 = L1_tmpl()
L1.ref = "L1"
L1.value = "27n"

# L2 - 88n
L2_tmpl = Part(tool=SKIDL, name="88n", footprint="Inductor_SMD:L_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
L2 = L2_tmpl()
L2.ref = "L2"
L2.value = "88n"

# Q1 - AO3401A
Q1_tmpl = Part(tool=SKIDL, name="AO3401A", footprint="Package_TO_SOT_SMD:SOT-23",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
Q1 = Q1_tmpl()
Q1.ref = "Q1"
Q1.value = "AO3401A"

# Q2 - MMBT3904
Q2_tmpl = Part(tool=SKIDL, name="MMBT3904", footprint="Package_TO_SOT_SMD:SOT-23",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
Q2 = Q2_tmpl()
Q2.ref = "Q2"
Q2.value = "MMBT3904"

# R1 - 2k2
R1_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R1 = R1_tmpl()
R1.ref = "R1"
R1.value = "2k2"

# R2 - 10k
R2_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R2 = R2_tmpl()
R2.ref = "R2"
R2.value = "10k"

# R3 - 10k
R3_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R3 = R3_tmpl()
R3.ref = "R3"
R3.value = "10k"

# R4 - 10k
R4_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R4 = R4_tmpl()
R4.ref = "R4"
R4.value = "10k"

# R5 - 22
R5_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R5 = R5_tmpl()
R5.ref = "R5"
R5.value = "22"

# R6 - 22
R6_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R6 = R6_tmpl()
R6.ref = "R6"
R6.value = "22"

# R7 - 1k
R7_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R7 = R7_tmpl()
R7.ref = "R7"
R7.value = "1k"

# R8 - 2k2
R8_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R8 = R8_tmpl()
R8.ref = "R8"
R8.value = "2k2"

# U1 - TESEO-LIV3R
U1_tmpl = Part(tool=SKIDL, name="TESEO-LIV3R", footprint="TESEO-LIV3R:TESEOLIV3R",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN)], dest=TEMPLATE)
U1 = U1_tmpl()
U1.ref = "U1"
U1.value = "TESEO-LIV3R"

# U2 - MAX2674EWT+T
U2_tmpl = Part(tool=SKIDL, name="MAX2674EWT+T", footprint="SchmillipKiCADLibrary:MAX2674EWT+T",
    pins=[Pin(num="A1", func=Pin.types.PWRIN), Pin(num="A2", func=Pin.types.PWRIN), Pin(num="B1", func=Pin.types.PWRIN), Pin(num="B2", func=Pin.types.PWRIN), Pin(num="C1", func=Pin.types.PWRIN), Pin(num="C2", func=Pin.types.PWRIN)], dest=TEMPLATE)
U2 = U2_tmpl()
U2.ref = "U2"
U2.value = "MAX2674EWT+T"

# ── Connections ───────────────────────────────────────────────
C1["1"] += net_N_3_3V
C1["2"] += net_GND

C2["1"] += net_N_3_3V
C2["2"] += net_GND

C3["1"] += net_N_3_3V
C3["2"] += net_GND

C4["1"] += net_VCC
C4["2"] += net_GND

C5["1"] += net_VCC_RF
C5["2"] += net_GND

C6["1"] += net_VCC_RF
C6["2"] += net_GND

C7["1"] += net_Net_C7_Pad1
C7["2"] += net_ANT_PASSIVE

C8["1"] += net_LNA_OUT
C8["2"] += net_Net_U2_RFOUT_slash_SHDN

D1["1"] += net_Net_D1_K
D1["2"] += net_N_3_3V

D2["1"] += net_Net_D2_K
D2["2"] += net_N_3_3V

J1["1"] += net_GPS_RST
J1["2"] += net_GPS_WAKEUP
J1["3"] += net_UART_RX
J1["4"] += net_UART_TX
J1["5"] += net_Net_J1_Pin_5
J1["6"] += net_GND

J2["1"] += net_ANT_PASSIVE
J2["2"] += net_GND
J2["3"] += net_GND

J3["1"] += net_ANT_ACTIVE
J3["2"] += net_GND
J3["3"] += net_GND
J3["4"] += net_GND
J3["5"] += net_GND

L1["1"] += net_VCC
L1["2"] += net_N_3_3V

L2["1"] += net_Net_C7_Pad1
L2["2"] += net_Net_U2_RFIN

Q1["1"] += net_GND
Q1["2"] += net_N_3_3V
Q1["3"] += net_Net_J1_Pin_5

Q2["1"] += net_Net_Q2_B
Q2["2"] += net_GND
Q2["3"] += net_Net_Q2_C

R1["1"] += net_Net_D1_K
R1["2"] += net_GND

R2["1"] += net_N_3_3V
R2["2"] += net_GPS_RST

R3["1"] += net_N_3_3V
R3["2"] += net_GPS_WAKEUP

R4["1"] += net_Net_U1_ANT_OFF
R4["2"] += net_GND

R5["1"] += net_Net_U1_RX
R5["2"] += net_UART_RX

R6["1"] += net_Net_U1_TX
R6["2"] += net_UART_TX

R7["1"] += net_GPS_PPS
R7["2"] += net_Net_Q2_B

R8["1"] += net_Net_D2_K
R8["2"] += net_Net_Q2_C

U1["1"] += net_GND
U1["2"] += net_Net_U1_TX
U1["3"] += net_Net_U1_RX
U1["4"] += net_GPS_PPS
U1["5"] += net_GPS_WAKEUP
U1["6"] += net_VCC
U1["7"] += net_VCC
U1["8"] += net_VCC
U1["9"] += net_GPS_RST
U1["10"] += net_GND
U1["11"] += net_LNA_OUT
U1["12"] += net_GND
U1["13"] += net_Net_U1_ANT_OFF
U1["14"] += net_VCC_RF
U1["15"] += net_unconnected_U1_RESERVED_1_Pad15
U1["16"] += net_unconnected_U1_SDA_Pad16
U1["17"] += net_unconnected_U1_SCL_Pad17
U1["18"] += net_unconnected_U1_RESERVED_2_Pad18

U2["A1"] += net_VCC_RF
U2["A2"] += net_Net_U2_RFOUT_slash_SHDN
U2["B1"] += net_Net_U2_RFIN
U2["B2"] += net_GND
U2["C1"] += net_GND
U2["C2"] += net_ANT_ACTIVE


generate_netlist()