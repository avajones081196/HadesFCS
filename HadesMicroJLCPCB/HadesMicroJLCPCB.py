# Auto-generated SKiDL script from HadesMicroJLCPCB_original.net
# Source: Philip M. Salmony - Hades Micro JLCPCB
# 84 components, 175 nets, 363 connections

from skidl import *

# ── Named nets (Net.fetch prevents auto-suffixing) ────────────
net_N_3V3 = Net.fetch("+3V3")
net_BAR_NRST = Net.fetch("BAR_NRST")
net_BOOT0 = Net.fetch("BOOT0")
net_BOOT1 = Net.fetch("BOOT1")
net_FLASH_H = Net.fetch("FLASH_!H")
net_FLASH_WP = Net.fetch("FLASH_!WP")
net_GND = Net.fetch("GND")
net_HSE_IN = Net.fetch("HSE_IN")
net_HSE_OUT = Net.fetch("HSE_OUT")
net_I2C1_SCL = Net.fetch("I2C1_SCL")
net_I2C1_SDA = Net.fetch("I2C1_SDA")
net_I2C3_SCL = Net.fetch("I2C3_SCL")
net_I2C3_SDA = Net.fetch("I2C3_SDA")
net_INT_ACC = Net.fetch("INT_ACC")
net_INT_BAR = Net.fetch("INT_BAR")
net_INT_GYR = Net.fetch("INT_GYR")
net_INT_MAG = Net.fetch("INT_MAG")
net_LED_A = Net.fetch("LED_A")
net_LED_B = Net.fetch("LED_B")
net_LED_C = Net.fetch("LED_C")
net_LED_D = Net.fetch("LED_D")
net_NRST = Net.fetch("NRST")
net_Net_BOOT1_C = Net.fetch("Net-(BOOT1-C)")
net_Net_BOOT2_C = Net.fetch("Net-(BOOT2-C)")
net_Net_C21_Pad1 = Net.fetch("Net-(C21-Pad1)")
net_Net_D1_A = Net.fetch("Net-(D1-A)")
net_Net_D2_K = Net.fetch("Net-(D2-K)")
net_Net_D3_K = Net.fetch("Net-(D3-K)")
net_Net_D4_K = Net.fetch("Net-(D4-K)")
net_Net_D5_K = Net.fetch("Net-(D5-K)")
net_Net_D6_A = Net.fetch("Net-(D6-A)")
net_Net_D7_A = Net.fetch("Net-(D7-A)")
net_Net_D7_K = Net.fetch("Net-(D7-K)")
net_Net_F1_Pad1 = Net.fetch("Net-(F1-Pad1)")
net_Net_IC1_VO_POS = Net.fetch("Net-(IC1-VO+)")
net_Net_IC1_VO_NEG = Net.fetch("Net-(IC1-VO-)")
net_Net_MCU1_PH0 = Net.fetch("Net-(MCU1-PH0)")
net_Net_MCU1_PH1 = Net.fetch("Net-(MCU1-PH1)")
net_Net_MCU1_VSS_Pad18 = Net.fetch("Net-(MCU1-VSS-Pad18)")
net_Net_PWM_PWR1_Pin_1 = Net.fetch("Net-(PWM_PWR1-Pin_1)")
net_Net_PWM_SIGNAL1_Pin_1 = Net.fetch("Net-(PWM_SIGNAL1-Pin_1)")
net_Net_PWM_SIGNAL1_Pin_2 = Net.fetch("Net-(PWM_SIGNAL1-Pin_2)")
net_Net_PWM_SIGNAL1_Pin_3 = Net.fetch("Net-(PWM_SIGNAL1-Pin_3)")
net_Net_PWM_SIGNAL1_Pin_4 = Net.fetch("Net-(PWM_SIGNAL1-Pin_4)")
net_Net_PWM_SIGNAL1_Pin_5 = Net.fetch("Net-(PWM_SIGNAL1-Pin_5)")
net_Net_PWM_SIGNAL1_Pin_6 = Net.fetch("Net-(PWM_SIGNAL1-Pin_6)")
net_Net_PWM_SIGNAL1_Pin_7 = Net.fetch("Net-(PWM_SIGNAL1-Pin_7)")
net_Net_PWM_SIGNAL1_Pin_8 = Net.fetch("Net-(PWM_SIGNAL1-Pin_8)")
net_Net_PWR1_K = Net.fetch("Net-(PWR1-K)")
net_Net_U6_RX = Net.fetch("Net-(U6-RX)")
net_Net_U6_TX = Net.fetch("Net-(U6-TX)")
net_Net_U6_V3 = Net.fetch("Net-(U6-V3)")
net_Net_USB1_VBUS = Net.fetch("Net-(USB1-VBUS)")
net_SPI1_CS = Net.fetch("SPI1_CS")
net_SPI1_MISO = Net.fetch("SPI1_MISO")
net_SPI1_MOSI = Net.fetch("SPI1_MOSI")
net_SPI1_SCK = Net.fetch("SPI1_SCK")
net_SPI2_CS = Net.fetch("SPI2_CS")
net_SPI2_MISO = Net.fetch("SPI2_MISO")
net_SPI2_MOSI = Net.fetch("SPI2_MOSI")
net_SPI2_SCK = Net.fetch("SPI2_SCK")
net_SPI3_CSACC = Net.fetch("SPI3_CSACC")
net_SPI3_CSGYR = Net.fetch("SPI3_CSGYR")
net_SPI3_CSMAG = Net.fetch("SPI3_CSMAG")
net_SPI3_MISO = Net.fetch("SPI3_MISO")
net_SPI3_MOSI = Net.fetch("SPI3_MOSI")
net_SPI3_SCK = Net.fetch("SPI3_SCK")
net_SWCLK = Net.fetch("SWCLK")
net_SWDIO = Net.fetch("SWDIO")
net_TIM2_CH1 = Net.fetch("TIM2_CH1")
net_TIM2_CH2 = Net.fetch("TIM2_CH2")
net_TIM4_CH1 = Net.fetch("TIM4_CH1")
net_TIM4_CH2 = Net.fetch("TIM4_CH2")
net_UART1_RX = Net.fetch("UART1_RX")
net_UART1_TX = Net.fetch("UART1_TX")
net_UART2_RX = Net.fetch("UART2_RX")
net_UART2_TX = Net.fetch("UART2_TX")
net_UART3_RX = Net.fetch("UART3_RX")
net_UART3_RX_INV = Net.fetch("UART3_RX_INV")
net_UART3_TX = Net.fetch("UART3_TX")
net_USB_CONN_D_POS = Net.fetch("USB_CONN_D+")
net_USB_CONN_D_NEG = Net.fetch("USB_CONN_D-")
net_USB_CONV_D_POS = Net.fetch("USB_CONV_D+")
net_USB_CONV_D_NEG = Net.fetch("USB_CONV_D-")
net_VCC = Net.fetch("VCC")
net_VDDA = Net.fetch("VDDA")

# ── Unconnected pins ──────────────────────────────────────────
net_unconnected_IC1_NC1_Pad11 = Net("unconnected-(IC1-NC1-Pad11)")
net_unconnected_IC1_NC2_Pad5 = Net("unconnected-(IC1-NC2-Pad5)")
net_unconnected_IMU1_INT2_Pad1 = Net("unconnected-(IMU1-INT2-Pad1)")
net_unconnected_IMU1_INT4_Pad15 = Net("unconnected-(IMU1-INT4-Pad15)")
net_unconnected_IMU1_INT5_Pad10 = Net("unconnected-(IMU1-INT5-Pad10)")
net_unconnected_IMU1_NC_1_Pad8 = Net("unconnected-(IMU1-NC_1-Pad8)")
net_unconnected_IMU1_NC_2_Pad18 = Net("unconnected-(IMU1-NC_2-Pad18)")
net_unconnected_MCU1_BOOT0_Pad60 = Net("unconnected-(MCU1-BOOT0-Pad60)")
net_unconnected_MCU1_NRST_Pad7 = Net("unconnected-(MCU1-NRST-Pad7)")
net_unconnected_MCU1_PA0_Pad14 = Net("unconnected-(MCU1-PA0-Pad14)")
net_unconnected_MCU1_PA1_Pad15 = Net("unconnected-(MCU1-PA1-Pad15)")
net_unconnected_MCU1_PA10_Pad43 = Net("unconnected-(MCU1-PA10-Pad43)")
net_unconnected_MCU1_PA11_Pad44 = Net("unconnected-(MCU1-PA11-Pad44)")
net_unconnected_MCU1_PA12_Pad45 = Net("unconnected-(MCU1-PA12-Pad45)")
net_unconnected_MCU1_PA13_Pad46 = Net("unconnected-(MCU1-PA13-Pad46)")
net_unconnected_MCU1_PA14_Pad49 = Net("unconnected-(MCU1-PA14-Pad49)")
net_unconnected_MCU1_PA15_Pad50 = Net("unconnected-(MCU1-PA15-Pad50)")
net_unconnected_MCU1_PA2_Pad16 = Net("unconnected-(MCU1-PA2-Pad16)")
net_unconnected_MCU1_PA3_Pad17 = Net("unconnected-(MCU1-PA3-Pad17)")
net_unconnected_MCU1_PA4_Pad20 = Net("unconnected-(MCU1-PA4-Pad20)")
net_unconnected_MCU1_PA5_Pad21 = Net("unconnected-(MCU1-PA5-Pad21)")
net_unconnected_MCU1_PA6_Pad22 = Net("unconnected-(MCU1-PA6-Pad22)")
net_unconnected_MCU1_PA7_Pad23 = Net("unconnected-(MCU1-PA7-Pad23)")
net_unconnected_MCU1_PA8_Pad41 = Net("unconnected-(MCU1-PA8-Pad41)")
net_unconnected_MCU1_PA9_Pad42 = Net("unconnected-(MCU1-PA9-Pad42)")
net_unconnected_MCU1_PB0_Pad26 = Net("unconnected-(MCU1-PB0-Pad26)")
net_unconnected_MCU1_PB1_Pad27 = Net("unconnected-(MCU1-PB1-Pad27)")
net_unconnected_MCU1_PB10_Pad29 = Net("unconnected-(MCU1-PB10-Pad29)")
net_unconnected_MCU1_PB11_Pad30 = Net("unconnected-(MCU1-PB11-Pad30)")
net_unconnected_MCU1_PB12_Pad33 = Net("unconnected-(MCU1-PB12-Pad33)")
net_unconnected_MCU1_PB13_Pad34 = Net("unconnected-(MCU1-PB13-Pad34)")
net_unconnected_MCU1_PB14_Pad35 = Net("unconnected-(MCU1-PB14-Pad35)")
net_unconnected_MCU1_PB15_Pad36 = Net("unconnected-(MCU1-PB15-Pad36)")
net_unconnected_MCU1_PB2_Pad28 = Net("unconnected-(MCU1-PB2-Pad28)")
net_unconnected_MCU1_PB3_Pad55 = Net("unconnected-(MCU1-PB3-Pad55)")
net_unconnected_MCU1_PB4_Pad56 = Net("unconnected-(MCU1-PB4-Pad56)")
net_unconnected_MCU1_PB5_Pad57 = Net("unconnected-(MCU1-PB5-Pad57)")
net_unconnected_MCU1_PB6_Pad58 = Net("unconnected-(MCU1-PB6-Pad58)")
net_unconnected_MCU1_PB7_Pad59 = Net("unconnected-(MCU1-PB7-Pad59)")
net_unconnected_MCU1_PB8_Pad61 = Net("unconnected-(MCU1-PB8-Pad61)")
net_unconnected_MCU1_PB9_Pad62 = Net("unconnected-(MCU1-PB9-Pad62)")
net_unconnected_MCU1_PC0_Pad8 = Net("unconnected-(MCU1-PC0-Pad8)")
net_unconnected_MCU1_PC1_Pad9 = Net("unconnected-(MCU1-PC1-Pad9)")
net_unconnected_MCU1_PC10_Pad51 = Net("unconnected-(MCU1-PC10-Pad51)")
net_unconnected_MCU1_PC11_Pad52 = Net("unconnected-(MCU1-PC11-Pad52)")
net_unconnected_MCU1_PC12_Pad53 = Net("unconnected-(MCU1-PC12-Pad53)")
net_unconnected_MCU1_PC13_Pad2 = Net("unconnected-(MCU1-PC13-Pad2)")
net_unconnected_MCU1_PC14_Pad3 = Net("unconnected-(MCU1-PC14-Pad3)")
net_unconnected_MCU1_PC15_Pad4 = Net("unconnected-(MCU1-PC15-Pad4)")
net_unconnected_MCU1_PC2_Pad10 = Net("unconnected-(MCU1-PC2-Pad10)")
net_unconnected_MCU1_PC3_Pad11 = Net("unconnected-(MCU1-PC3-Pad11)")
net_unconnected_MCU1_PC4_Pad24 = Net("unconnected-(MCU1-PC4-Pad24)")
net_unconnected_MCU1_PC5_Pad25 = Net("unconnected-(MCU1-PC5-Pad25)")
net_unconnected_MCU1_PC6_Pad37 = Net("unconnected-(MCU1-PC6-Pad37)")
net_unconnected_MCU1_PC7_Pad38 = Net("unconnected-(MCU1-PC7-Pad38)")
net_unconnected_MCU1_PC8_Pad39 = Net("unconnected-(MCU1-PC8-Pad39)")
net_unconnected_MCU1_PC9_Pad40 = Net("unconnected-(MCU1-PC9-Pad40)")
net_unconnected_MCU1_PD2_Pad54 = Net("unconnected-(MCU1-PD2-Pad54)")
net_unconnected_MCU1_VCAP_1_Pad31 = Net("unconnected-(MCU1-VCAP_1-Pad31)")
net_unconnected_MCU1_VCAP_2_Pad47 = Net("unconnected-(MCU1-VCAP_2-Pad47)")
net_unconnected_MCU1_VDD_Pad19 = Net("unconnected-(MCU1-VDD-Pad19)")
net_unconnected_MCU1_VDD_Pad32 = Net("unconnected-(MCU1-VDD-Pad32)")
net_unconnected_MCU1_VDD_Pad48 = Net("unconnected-(MCU1-VDD-Pad48)")
net_unconnected_MCU1_VDD_Pad64 = Net("unconnected-(MCU1-VDD-Pad64)")
net_unconnected_MCU1_VDDA_Pad13 = Net("unconnected-(MCU1-VDDA-Pad13)")
net_unconnected_MCU1_VSSA_Pad12 = Net("unconnected-(MCU1-VSSA-Pad12)")
net_unconnected_SWD1_Pin_4_Pad4 = Net("unconnected-(SWD1-Pin_4-Pad4)")
net_unconnected_SWD1_Pin_7_Pad7 = Net("unconnected-(SWD1-Pin_7-Pad7)")
net_unconnected_SWD1_Pin_8_Pad8 = Net("unconnected-(SWD1-Pin_8-Pad8)")
net_unconnected_U1_NC_Pad4 = Net("unconnected-(U1-NC-Pad4)")
net_unconnected_U2_EXTCLK_Pad25 = Net("unconnected-(U2-EXTCLK-Pad25)")
net_unconnected_U2_LED10_Pad17 = Net("unconnected-(U2-LED10-Pad17)")
net_unconnected_U2_LED11_Pad18 = Net("unconnected-(U2-LED11-Pad18)")
net_unconnected_U2_LED12_Pad19 = Net("unconnected-(U2-LED12-Pad19)")
net_unconnected_U2_LED13_Pad20 = Net("unconnected-(U2-LED13-Pad20)")
net_unconnected_U2_LED14_Pad21 = Net("unconnected-(U2-LED14-Pad21)")
net_unconnected_U2_LED15_Pad22 = Net("unconnected-(U2-LED15-Pad22)")
net_unconnected_U2_LED8_Pad15 = Net("unconnected-(U2-LED8-Pad15)")
net_unconnected_U2_LED9_Pad16 = Net("unconnected-(U2-LED9-Pad16)")
net_unconnected_U4_GND_Pad2 = Net("unconnected-(U4-GND-Pad2)")
net_unconnected_U4_I_slash_O1_Pad1 = Net("unconnected-(U4-I{slash}O1-Pad1)")
net_unconnected_U4_I_slash_O1_Pad6 = Net("unconnected-(U4-I{slash}O1-Pad6)")
net_unconnected_U4_I_slash_O2_Pad3 = Net("unconnected-(U4-I{slash}O2-Pad3)")
net_unconnected_U4_I_slash_O2_Pad4 = Net("unconnected-(U4-I{slash}O2-Pad4)")
net_unconnected_U4_VBUS_Pad5 = Net("unconnected-(U4-VBUS-Pad5)")
net_unconnected_U5_Pad1 = Net("unconnected-(U5-~-Pad1)")
net_unconnected_U6_CTS_Pad5 = Net("unconnected-(U6-CTS-Pad5)")
net_unconnected_U6_RTS_Pad4 = Net("unconnected-(U6-RTS-Pad4)")
net_unconnected_USB1_ID_Pad4 = Net("unconnected-(USB1-ID-Pad4)")

# ── Components ────────────────────────────────────────────────
# BOOT1 - TDD01H0SB1R
BOOT1_tmpl = Part(tool=SKIDL, name="TDD01H0SB1R", footprint="TDD01H0SB1R:SOT175P420X230-3N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
BOOT1 = BOOT1_tmpl()
BOOT1.ref = "BOOT1"
BOOT1.value = "TDD01H0SB1R"

# BOOT2 - TDD01H0SB1R
BOOT2_tmpl = Part(tool=SKIDL, name="TDD01H0SB1R", footprint="TDD01H0SB1R:SOT175P420X230-3N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
BOOT2 = BOOT2_tmpl()
BOOT2.ref = "BOOT2"
BOOT2.value = "TDD01H0SB1R"

# C1 - 1u
C1_tmpl = Part(tool=SKIDL, name="1u", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C1 = C1_tmpl()
C1.ref = "C1"
C1.value = "1u"

# C2 - 1u
C2_tmpl = Part(tool=SKIDL, name="1u", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C2 = C2_tmpl()
C2.ref = "C2"
C2.value = "1u"

# C3 - 10u
C3_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C3 = C3_tmpl()
C3.ref = "C3"
C3.value = "10u"

# C4 - 100n
C4_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C4 = C4_tmpl()
C4.ref = "C4"
C4.value = "100n"

# C5 - 100n
C5_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C5 = C5_tmpl()
C5.ref = "C5"
C5.value = "100n"

# C6 - 100n
C6_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C6 = C6_tmpl()
C6.ref = "C6"
C6.value = "100n"

# C7 - 100n
C7_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C7 = C7_tmpl()
C7.ref = "C7"
C7.value = "100n"

# C8 - 100n
C8_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C8 = C8_tmpl()
C8.ref = "C8"
C8.value = "100n"

# C9 - 100n
C9_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C9 = C9_tmpl()
C9.ref = "C9"
C9.value = "100n"

# C10 - 100n
C10_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C10 = C10_tmpl()
C10.ref = "C10"
C10.value = "100n"

# C11 - 100n
C11_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C11 = C11_tmpl()
C11.ref = "C11"
C11.value = "100n"

# C12 - 100n
C12_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C12 = C12_tmpl()
C12.ref = "C12"
C12.value = "100n"

# C13 - 100n
C13_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C13 = C13_tmpl()
C13.ref = "C13"
C13.value = "100n"

# C14 - 2u2
C14_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C14 = C14_tmpl()
C14.ref = "C14"
C14.value = "2u2"

# C15 - 2u2
C15_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C15 = C15_tmpl()
C15.ref = "C15"
C15.value = "2u2"

# C16 - 100n
C16_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C16 = C16_tmpl()
C16.ref = "C16"
C16.value = "100n"

# C17 - 100n
C17_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C17 = C17_tmpl()
C17.ref = "C17"
C17.value = "100n"

# C18 - 100n
C18_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C18 = C18_tmpl()
C18.ref = "C18"
C18.value = "100n"

# C19 - 100n
C19_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C19 = C19_tmpl()
C19.ref = "C19"
C19.value = "100n"

# C20 - 10p
C20_tmpl = Part(tool=SKIDL, name="10p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C20 = C20_tmpl()
C20.ref = "C20"
C20.value = "10p"

# C21 - 10p
C21_tmpl = Part(tool=SKIDL, name="10p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C21 = C21_tmpl()
C21.ref = "C21"
C21.value = "10p"

# C22 - 1u
C22_tmpl = Part(tool=SKIDL, name="1u", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C22 = C22_tmpl()
C22.ref = "C22"
C22.value = "1u"

# C23 - 100n
C23_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C23 = C23_tmpl()
C23.ref = "C23"
C23.value = "100n"

# C24 - 1n
C24_tmpl = Part(tool=SKIDL, name="1n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C24 = C24_tmpl()
C24.ref = "C24"
C24.value = "1n"

# C25 - 100n
C25_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C25 = C25_tmpl()
C25.ref = "C25"
C25.value = "100n"

# C26 - 100n
C26_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C26 = C26_tmpl()
C26.ref = "C26"
C26.value = "100n"

# C27 - 100n
C27_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C27 = C27_tmpl()
C27.ref = "C27"
C27.value = "100n"

# C28 - 100n
C28_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C28 = C28_tmpl()
C28.ref = "C28"
C28.value = "100n"

# C29 - 100n
C29_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C29 = C29_tmpl()
C29.ref = "C29"
C29.value = "100n"

# C30 - 100n
C30_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C30 = C30_tmpl()
C30.ref = "C30"
C30.value = "100n"

# D1 - D_Schottky
D1_tmpl = Part(tool=SKIDL, name="D_Schottky", footprint="Diode_SMD:D_SOD-323",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D1 = D1_tmpl()
D1.ref = "D1"
D1.value = "D_Schottky"

# D2 - GR
D2_tmpl = Part(tool=SKIDL, name="GR", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D2 = D2_tmpl()
D2.ref = "D2"
D2.value = "GR"

# D3 - RE
D3_tmpl = Part(tool=SKIDL, name="RE", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D3 = D3_tmpl()
D3.ref = "D3"
D3.value = "RE"

# D4 - BL
D4_tmpl = Part(tool=SKIDL, name="BL", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D4 = D4_tmpl()
D4.ref = "D4"
D4.value = "BL"

# D5 - BL
D5_tmpl = Part(tool=SKIDL, name="BL", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D5 = D5_tmpl()
D5.ref = "D5"
D5.value = "BL"

# D6 - D_Schottky
D6_tmpl = Part(tool=SKIDL, name="D_Schottky", footprint="Diode_SMD:D_SOD-323",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D6 = D6_tmpl()
D6.ref = "D6"
D6.value = "D_Schottky"

# D7 - YE
D7_tmpl = Part(tool=SKIDL, name="YE", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D7 = D7_tmpl()
D7.ref = "D7"
D7.value = "YE"

# F1 - Fuse
F1_tmpl = Part(tool=SKIDL, name="Fuse", footprint="Fuse:Fuse_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
F1 = F1_tmpl()
F1.ref = "F1"
F1.value = "Fuse"

# FB1 - FB_Small
FB1_tmpl = Part(tool=SKIDL, name="FB_Small", footprint="Inductor_SMD:L_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
FB1 = FB1_tmpl()
FB1.ref = "FB1"
FB1.value = "FB_Small"

# FB2 - FB_Small
FB2_tmpl = Part(tool=SKIDL, name="FB_Small", footprint="Inductor_SMD:L_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
FB2 = FB2_tmpl()
FB2.ref = "FB2"
FB2.value = "FB_Small"

# FLASH1 - W25N01GVZEIG_TR
FLASH1_tmpl = Part(tool=SKIDL, name="W25N01GVZEIG_TR", footprint="W25N01GVZEIG_TR:SON127P800X600X80-9N-D",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN)], dest=TEMPLATE)
FLASH1 = FLASH1_tmpl()
FLASH1.ref = "FLASH1"
FLASH1.value = "W25N01GVZEIG_TR"

# GPS1 - Conn_01x04
GPS1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
GPS1 = GPS1_tmpl()
GPS1.ref = "GPS1"
GPS1.value = "Conn_01x04"

# HSE1 - 16MHz
HSE1_tmpl = Part(tool=SKIDL, name="16MHz", footprint="Crystal:Crystal_SMD_Abracon_ABM8G-4Pin_3.2x2.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
HSE1 = HSE1_tmpl()
HSE1.ref = "HSE1"
HSE1.value = "16MHz"

# I2C1 - Conn_01x04
I2C1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
I2C1 = I2C1_tmpl()
I2C1.ref = "I2C1"
I2C1.value = "Conn_01x04"

# IC1 - MPRLS0015PA0000SA
IC1_tmpl = Part(tool=SKIDL, name="MPRLS0015PA0000SA", footprint="MPRLS0015PA0000SA:MPRLS0015PA0000SA",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN)], dest=TEMPLATE)
IC1 = IC1_tmpl()
IC1.ref = "IC1"
IC1.value = "MPRLS0015PA0000SA"

# IMU1 - BMX055
IMU1_tmpl = Part(tool=SKIDL, name="BMX055", footprint="BMX055:LGA_PACKAGE_20_PINS",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN)], dest=TEMPLATE)
IMU1 = IMU1_tmpl()
IMU1.ref = "IMU1"
IMU1.value = "BMX055"

# JP1 - Jumper_NO_Small
JP1_tmpl = Part(tool=SKIDL, name="Jumper_NO_Small", footprint="Connector_PinHeader_1.27mm:PinHeader_1x02_P1.27mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
JP1 = JP1_tmpl()
JP1.ref = "JP1"
JP1.value = "Jumper_NO_Small"

# MCU1 - STM32F405RGT6
MCU1_tmpl = Part(tool=SKIDL, name="STM32F405RGT6", footprint="Package_QFP:LQFP-64_10x10mm_P0.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN), Pin(num="21", func=Pin.types.PWRIN), Pin(num="22", func=Pin.types.PWRIN), Pin(num="23", func=Pin.types.PWRIN), Pin(num="24", func=Pin.types.PWRIN), Pin(num="25", func=Pin.types.PWRIN), Pin(num="26", func=Pin.types.PWRIN), Pin(num="27", func=Pin.types.PWRIN), Pin(num="28", func=Pin.types.PWRIN), Pin(num="29", func=Pin.types.PWRIN), Pin(num="30", func=Pin.types.PWRIN), Pin(num="31", func=Pin.types.PWRIN), Pin(num="32", func=Pin.types.PWRIN), Pin(num="33", func=Pin.types.PWRIN), Pin(num="34", func=Pin.types.PWRIN), Pin(num="35", func=Pin.types.PWRIN), Pin(num="36", func=Pin.types.PWRIN), Pin(num="37", func=Pin.types.PWRIN), Pin(num="38", func=Pin.types.PWRIN), Pin(num="39", func=Pin.types.PWRIN), Pin(num="40", func=Pin.types.PWRIN), Pin(num="41", func=Pin.types.PWRIN), Pin(num="42", func=Pin.types.PWRIN), Pin(num="43", func=Pin.types.PWRIN), Pin(num="44", func=Pin.types.PWRIN), Pin(num="45", func=Pin.types.PWRIN), Pin(num="46", func=Pin.types.PWRIN), Pin(num="47", func=Pin.types.PWRIN), Pin(num="48", func=Pin.types.PWRIN), Pin(num="49", func=Pin.types.PWRIN), Pin(num="50", func=Pin.types.PWRIN), Pin(num="51", func=Pin.types.PWRIN), Pin(num="52", func=Pin.types.PWRIN), Pin(num="53", func=Pin.types.PWRIN), Pin(num="54", func=Pin.types.PWRIN), Pin(num="55", func=Pin.types.PWRIN), Pin(num="56", func=Pin.types.PWRIN), Pin(num="57", func=Pin.types.PWRIN), Pin(num="58", func=Pin.types.PWRIN), Pin(num="59", func=Pin.types.PWRIN), Pin(num="60", func=Pin.types.PWRIN), Pin(num="61", func=Pin.types.PWRIN), Pin(num="62", func=Pin.types.PWRIN), Pin(num="63", func=Pin.types.PWRIN), Pin(num="64", func=Pin.types.PWRIN)], dest=TEMPLATE)
MCU1 = MCU1_tmpl()
MCU1.ref = "MCU1"
MCU1.value = "STM32F405RGT6"

# PWM_PWR1 - Conn_02x08_Odd_Even
PWM_PWR1_tmpl = Part(tool=SKIDL, name="Conn_02x08_Odd_Even", footprint="Connector_PinHeader_2.54mm:PinHeader_2x08_P2.54mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN)], dest=TEMPLATE)
PWM_PWR1 = PWM_PWR1_tmpl()
PWM_PWR1.ref = "PWM_PWR1"
PWM_PWR1.value = "Conn_02x08_Odd_Even"

# PWM_SIGNAL1 - Conn_01x08
PWM_SIGNAL1_tmpl = Part(tool=SKIDL, name="Conn_01x08", footprint="Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
PWM_SIGNAL1 = PWM_SIGNAL1_tmpl()
PWM_SIGNAL1.ref = "PWM_SIGNAL1"
PWM_SIGNAL1.value = "Conn_01x08"

# PWR1 - GR
PWR1_tmpl = Part(tool=SKIDL, name="GR", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
PWR1 = PWR1_tmpl()
PWR1.ref = "PWR1"
PWR1.value = "GR"

# R1 - 2k2
R1_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R1 = R1_tmpl()
R1.ref = "R1"
R1.value = "2k2"

# R2 - 2k2
R2_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R2 = R2_tmpl()
R2.ref = "R2"
R2.value = "2k2"

# R3 - 1k
R3_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R3 = R3_tmpl()
R3.ref = "R3"
R3.value = "1k"

# R4 - 1k
R4_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R4 = R4_tmpl()
R4.ref = "R4"
R4.value = "1k"

# R5 - 1k
R5_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R5 = R5_tmpl()
R5.ref = "R5"
R5.value = "1k"

# R6 - 2k2
R6_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R6 = R6_tmpl()
R6.ref = "R6"
R6.value = "2k2"

# R7 - 2k2
R7_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R7 = R7_tmpl()
R7.ref = "R7"
R7.value = "2k2"

# R8 - 2k2
R8_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R8 = R8_tmpl()
R8.ref = "R8"
R8.value = "2k2"

# R9 - 2k2
R9_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R9 = R9_tmpl()
R9.ref = "R9"
R9.value = "2k2"

# R10 - 470
R10_tmpl = Part(tool=SKIDL, name="470", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R10 = R10_tmpl()
R10.ref = "R10"
R10.value = "470"

# R11 - 22
R11_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R11 = R11_tmpl()
R11.ref = "R11"
R11.value = "22"

# R12 - 10k
R12_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R12 = R12_tmpl()
R12.ref = "R12"
R12.value = "10k"

# R13 - 22
R13_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R13 = R13_tmpl()
R13.ref = "R13"
R13.value = "22"

# R14 - 10k
R14_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R14 = R14_tmpl()
R14.ref = "R14"
R14.value = "10k"

# R15 - 2k2
R15_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R15 = R15_tmpl()
R15.ref = "R15"
R15.value = "2k2"

# R16 - 10k
R16_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R16 = R16_tmpl()
R16.ref = "R16"
R16.value = "10k"

# R17 - 10k
R17_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R17 = R17_tmpl()
R17.ref = "R17"
R17.value = "10k"

# RC1 - Conn_01x04
RC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
RC1 = RC1_tmpl()
RC1.ref = "RC1"
RC1.value = "Conn_01x04"

# RESET1 - SKRPANE010
RESET1_tmpl = Part(tool=SKIDL, name="SKRPANE010", footprint="SKRPANE010:SKRPADE010",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
RESET1 = RESET1_tmpl()
RESET1.ref = "RESET1"
RESET1.value = "SKRPANE010"

# SBUS1 - Conn_01x04
SBUS1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
SBUS1 = SBUS1_tmpl()
SBUS1.ref = "SBUS1"
SBUS1.value = "Conn_01x04"

# SERVO1 - TrmnlBlck
SERVO1_tmpl = Part(tool=SKIDL, name="TrmnlBlck", footprint="TerminalBlock_Phoenix:TerminalBlock_Phoenix_PT-1,5-2-3.5-H_1x02_P3.50mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
SERVO1 = SERVO1_tmpl()
SERVO1.ref = "SERVO1"
SERVO1.value = "TrmnlBlck"

# SWD1 - Conn_02x05_Counter_Clockwise
SWD1_tmpl = Part(tool=SKIDL, name="Conn_02x05_Counter_Clockwise", footprint="Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical_SMD",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN)], dest=TEMPLATE)
SWD1 = SWD1_tmpl()
SWD1.ref = "SWD1"
SWD1.value = "Conn_02x05_Counter_Clockwise"

# TELEM1 - Conn_01x04
TELEM1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
TELEM1 = TELEM1_tmpl()
TELEM1.ref = "TELEM1"
TELEM1.value = "Conn_01x04"

# U1 - AP2112K-3.3
U1_tmpl = Part(tool=SKIDL, name="AP2112K-3.3", footprint="Package_TO_SOT_SMD:SOT-23-5",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN)], dest=TEMPLATE)
U1 = U1_tmpl()
U1.ref = "U1"
U1.value = "AP2112K-3.3"

# U2 - PCA9685PW
U2_tmpl = Part(tool=SKIDL, name="PCA9685PW", footprint="Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN), Pin(num="21", func=Pin.types.PWRIN), Pin(num="22", func=Pin.types.PWRIN), Pin(num="23", func=Pin.types.PWRIN), Pin(num="24", func=Pin.types.PWRIN), Pin(num="25", func=Pin.types.PWRIN), Pin(num="26", func=Pin.types.PWRIN), Pin(num="27", func=Pin.types.PWRIN), Pin(num="28", func=Pin.types.PWRIN)], dest=TEMPLATE)
U2 = U2_tmpl()
U2.ref = "U2"
U2.value = "PCA9685PW"

# U3 - CAT24C256
U3_tmpl = Part(tool=SKIDL, name="CAT24C256", footprint="Package_SO:SOIC-8_3.9x4.9mm_P1.27mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
U3 = U3_tmpl()
U3.ref = "U3"
U3.value = "CAT24C256"

# U4 - USBLC6-2SC6
U4_tmpl = Part(tool=SKIDL, name="USBLC6-2SC6", footprint="Package_TO_SOT_SMD:SOT-23-6",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
U4 = U4_tmpl()
U4.ref = "U4"
U4.value = "USBLC6-2SC6"

# U5 - 74AHC1GU04GW,125
U5_tmpl = Part(tool=SKIDL, name="74AHC1GU04GW,125", footprint="74AHC1GU04GW_125:SOT65P212X110-5N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN)], dest=TEMPLATE)
U5 = U5_tmpl()
U5.ref = "U5"
U5.value = "74AHC1GU04GW,125"

# U6 - CH340E
U6_tmpl = Part(tool=SKIDL, name="CH340E", footprint="CH340E:MSOP10",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN)], dest=TEMPLATE)
U6 = U6_tmpl()
U6.ref = "U6"
U6.value = "CH340E"

# USB1 - USB_B_Micro
USB1_tmpl = Part(tool=SKIDL, name="USB_B_Micro", footprint="Connector_USB:USB_Micro-B_Wuerth_629105150521_CircularHoles",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="SH", func=Pin.types.PWRIN)], dest=TEMPLATE)
USB1 = USB1_tmpl()
USB1.ref = "USB1"
USB1.value = "USB_B_Micro"

# VIN1 - Conn_01x02
VIN1_tmpl = Part(tool=SKIDL, name="Conn_01x02", footprint="Connector_Molex:Molex_PicoBlade_53048-0210_1x02_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
VIN1 = VIN1_tmpl()
VIN1.ref = "VIN1"
VIN1.value = "Conn_01x02"

# ── Connections ───────────────────────────────────────────────
BOOT1["1"] += net_N_3V3
BOOT1["2"] += net_GND
BOOT1["3"] += net_Net_BOOT1_C

BOOT2["1"] += net_N_3V3
BOOT2["2"] += net_GND
BOOT2["3"] += net_Net_BOOT2_C

C1["1"] += net_VCC
C1["2"] += net_GND

C2["1"] += net_N_3V3
C2["2"] += net_GND

C3["1"] += net_N_3V3
C3["2"] += net_GND

C4["1"] += net_N_3V3
C4["2"] += net_GND

C5["1"] += net_N_3V3
C5["2"] += net_GND

C6["1"] += net_N_3V3
C6["2"] += net_GND

C7["1"] += net_N_3V3
C7["2"] += net_GND

C8["1"] += net_N_3V3
C8["2"] += net_GND

C9["1"] += net_N_3V3
C9["2"] += net_GND

C10["1"] += net_N_3V3
C10["2"] += net_GND

C11["1"] += net_N_3V3
C11["2"] += net_GND

C12["1"] += net_N_3V3
C12["2"] += net_GND

C13["1"] += net_N_3V3
C13["2"] += net_GND

C14["1"] += net_Net_MCU1_PH0
C14["2"] += net_GND

C15["1"] += net_Net_MCU1_PH1
C15["2"] += net_GND

C16["1"] += net_N_3V3
C16["2"] += net_GND

C17["1"] += net_Net_D6_A
C17["2"] += net_GND

C18["1"] += net_N_3V3
C18["2"] += net_GND

C19["1"] += net_N_3V3
C19["2"] += net_GND

C20["1"] += net_HSE_IN
C20["2"] += net_GND

C21["1"] += net_Net_C21_Pad1
C21["2"] += net_GND

C22["1"] += net_VDDA
C22["2"] += net_GND

C23["1"] += net_VDDA
C23["2"] += net_GND

C24["1"] += net_Net_IC1_VO_NEG
C24["2"] += net_Net_IC1_VO_POS

C25["1"] += net_GND
C25["2"] += net_N_3V3

C26["1"] += net_Net_U6_V3
C26["2"] += net_GND

C27["1"] += net_N_3V3
C27["2"] += net_GND

C28["1"] += net_N_3V3
C28["2"] += net_GND

C29["1"] += net_N_3V3
C29["2"] += net_GND

C30["1"] += net_NRST
C30["2"] += net_GND

D1["1"] += net_VCC
D1["2"] += net_Net_D1_A

D2["1"] += net_Net_D2_K
D2["2"] += net_LED_A

D3["1"] += net_Net_D3_K
D3["2"] += net_LED_B

D4["1"] += net_Net_D4_K
D4["2"] += net_LED_C

D5["1"] += net_Net_D5_K
D5["2"] += net_LED_D

D6["1"] += net_VCC
D6["2"] += net_Net_D6_A

D7["1"] += net_Net_D7_K
D7["2"] += net_Net_D7_A

F1["1"] += net_Net_F1_Pad1
F1["2"] += net_Net_USB1_VBUS

FB1["1"] += net_Net_D6_A
FB1["2"] += net_Net_F1_Pad1

FB2["1"] += net_VDDA
FB2["2"] += net_N_3V3

FLASH1["1"] += net_SPI1_CS
FLASH1["2"] += net_SPI1_MISO
FLASH1["3"] += net_FLASH_WP
FLASH1["4"] += net_GND
FLASH1["5"] += net_SPI1_MOSI
FLASH1["6"] += net_SPI1_SCK
FLASH1["7"] += net_FLASH_H
FLASH1["8"] += net_N_3V3
FLASH1["9"] += net_GND

GPS1["1"] += net_N_3V3
GPS1["2"] += net_GND
GPS1["3"] += net_UART2_TX
GPS1["4"] += net_UART2_RX

HSE1["1"] += net_HSE_IN
HSE1["2"] += net_GND
HSE1["3"] += net_Net_C21_Pad1
HSE1["4"] += net_GND

I2C1["1"] += net_N_3V3
I2C1["2"] += net_GND
I2C1["3"] += net_I2C3_SCL
I2C1["4"] += net_I2C3_SDA

IC1["1"] += net_SPI2_CS
IC1["2"] += net_SPI2_MOSI
IC1["3"] += net_SPI2_SCK
IC1["4"] += net_Net_IC1_VO_POS
IC1["5"] += net_unconnected_IC1_NC2_Pad5
IC1["6"] += net_Net_IC1_VO_NEG
IC1["7"] += net_SPI2_MISO
IC1["8"] += net_INT_BAR
IC1["9"] += net_BAR_NRST
IC1["10"] += net_GND
IC1["11"] += net_unconnected_IC1_NC1_Pad11
IC1["12"] += net_N_3V3

IMU1["1"] += net_unconnected_IMU1_INT2_Pad1
IMU1["2"] += net_INT_MAG
IMU1["3"] += net_N_3V3
IMU1["4"] += net_GND
IMU1["5"] += net_SPI3_CSGYR
IMU1["6"] += net_GND
IMU1["7"] += net_GND
IMU1["8"] += net_unconnected_IMU1_NC_1_Pad8
IMU1["9"] += net_SPI3_SCK
IMU1["10"] += net_unconnected_IMU1_INT5_Pad10
IMU1["11"] += net_SPI3_MOSI
IMU1["12"] += net_SPI3_MISO
IMU1["13"] += net_N_3V3
IMU1["14"] += net_INT_GYR
IMU1["15"] += net_unconnected_IMU1_INT4_Pad15
IMU1["16"] += net_SPI3_CSACC
IMU1["17"] += net_SPI3_MISO
IMU1["18"] += net_unconnected_IMU1_NC_2_Pad18
IMU1["19"] += net_INT_ACC
IMU1["20"] += net_SPI3_CSMAG

JP1["1"] += net_Net_PWM_PWR1_Pin_1
JP1["2"] += net_Net_D1_A

MCU1["1"] += net_N_3V3
MCU1["2"] += net_unconnected_MCU1_PC13_Pad2
MCU1["3"] += net_unconnected_MCU1_PC14_Pad3
MCU1["4"] += net_unconnected_MCU1_PC15_Pad4
MCU1["5"] += net_Net_MCU1_PH0
MCU1["6"] += net_Net_MCU1_PH1
MCU1["7"] += net_unconnected_MCU1_NRST_Pad7
MCU1["8"] += net_unconnected_MCU1_PC0_Pad8
MCU1["9"] += net_unconnected_MCU1_PC1_Pad9
MCU1["10"] += net_unconnected_MCU1_PC2_Pad10
MCU1["11"] += net_unconnected_MCU1_PC3_Pad11
MCU1["12"] += net_unconnected_MCU1_VSSA_Pad12
MCU1["13"] += net_unconnected_MCU1_VDDA_Pad13
MCU1["14"] += net_unconnected_MCU1_PA0_Pad14
MCU1["15"] += net_unconnected_MCU1_PA1_Pad15
MCU1["16"] += net_unconnected_MCU1_PA2_Pad16
MCU1["17"] += net_unconnected_MCU1_PA3_Pad17
MCU1["18"] += net_Net_MCU1_VSS_Pad18
MCU1["19"] += net_unconnected_MCU1_VDD_Pad19
MCU1["20"] += net_unconnected_MCU1_PA4_Pad20
MCU1["21"] += net_unconnected_MCU1_PA5_Pad21
MCU1["22"] += net_unconnected_MCU1_PA6_Pad22
MCU1["23"] += net_unconnected_MCU1_PA7_Pad23
MCU1["24"] += net_unconnected_MCU1_PC4_Pad24
MCU1["25"] += net_unconnected_MCU1_PC5_Pad25
MCU1["26"] += net_unconnected_MCU1_PB0_Pad26
MCU1["27"] += net_unconnected_MCU1_PB1_Pad27
MCU1["28"] += net_unconnected_MCU1_PB2_Pad28
MCU1["29"] += net_unconnected_MCU1_PB10_Pad29
MCU1["30"] += net_unconnected_MCU1_PB11_Pad30
MCU1["31"] += net_unconnected_MCU1_VCAP_1_Pad31
MCU1["32"] += net_unconnected_MCU1_VDD_Pad32
MCU1["33"] += net_unconnected_MCU1_PB12_Pad33
MCU1["34"] += net_unconnected_MCU1_PB13_Pad34
MCU1["35"] += net_unconnected_MCU1_PB14_Pad35
MCU1["36"] += net_unconnected_MCU1_PB15_Pad36
MCU1["37"] += net_unconnected_MCU1_PC6_Pad37
MCU1["38"] += net_unconnected_MCU1_PC7_Pad38
MCU1["39"] += net_unconnected_MCU1_PC8_Pad39
MCU1["40"] += net_unconnected_MCU1_PC9_Pad40
MCU1["41"] += net_unconnected_MCU1_PA8_Pad41
MCU1["42"] += net_unconnected_MCU1_PA9_Pad42
MCU1["43"] += net_unconnected_MCU1_PA10_Pad43
MCU1["44"] += net_unconnected_MCU1_PA11_Pad44
MCU1["45"] += net_unconnected_MCU1_PA12_Pad45
MCU1["46"] += net_unconnected_MCU1_PA13_Pad46
MCU1["47"] += net_unconnected_MCU1_VCAP_2_Pad47
MCU1["48"] += net_unconnected_MCU1_VDD_Pad48
MCU1["49"] += net_unconnected_MCU1_PA14_Pad49
MCU1["50"] += net_unconnected_MCU1_PA15_Pad50
MCU1["51"] += net_unconnected_MCU1_PC10_Pad51
MCU1["52"] += net_unconnected_MCU1_PC11_Pad52
MCU1["53"] += net_unconnected_MCU1_PC12_Pad53
MCU1["54"] += net_unconnected_MCU1_PD2_Pad54
MCU1["55"] += net_unconnected_MCU1_PB3_Pad55
MCU1["56"] += net_unconnected_MCU1_PB4_Pad56
MCU1["57"] += net_unconnected_MCU1_PB5_Pad57
MCU1["58"] += net_unconnected_MCU1_PB6_Pad58
MCU1["59"] += net_unconnected_MCU1_PB7_Pad59
MCU1["60"] += net_unconnected_MCU1_BOOT0_Pad60
MCU1["61"] += net_unconnected_MCU1_PB8_Pad61
MCU1["62"] += net_unconnected_MCU1_PB9_Pad62
MCU1["63"] += net_Net_MCU1_VSS_Pad18
MCU1["64"] += net_unconnected_MCU1_VDD_Pad64

PWM_PWR1["1"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["2"] += net_GND
PWM_PWR1["3"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["4"] += net_GND
PWM_PWR1["5"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["6"] += net_GND
PWM_PWR1["7"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["8"] += net_GND
PWM_PWR1["9"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["10"] += net_GND
PWM_PWR1["11"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["12"] += net_GND
PWM_PWR1["13"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["14"] += net_GND
PWM_PWR1["15"] += net_Net_PWM_PWR1_Pin_1
PWM_PWR1["16"] += net_GND

PWM_SIGNAL1["1"] += net_Net_PWM_SIGNAL1_Pin_1
PWM_SIGNAL1["2"] += net_Net_PWM_SIGNAL1_Pin_2
PWM_SIGNAL1["3"] += net_Net_PWM_SIGNAL1_Pin_3
PWM_SIGNAL1["4"] += net_Net_PWM_SIGNAL1_Pin_4
PWM_SIGNAL1["5"] += net_Net_PWM_SIGNAL1_Pin_5
PWM_SIGNAL1["6"] += net_Net_PWM_SIGNAL1_Pin_6
PWM_SIGNAL1["7"] += net_Net_PWM_SIGNAL1_Pin_7
PWM_SIGNAL1["8"] += net_Net_PWM_SIGNAL1_Pin_8

PWR1["1"] += net_Net_PWR1_K
PWR1["2"] += net_N_3V3

R1["1"] += net_GND
R1["2"] += net_Net_PWR1_K

R2["1"] += net_Net_D2_K
R2["2"] += net_GND

R3["1"] += net_Net_D3_K
R3["2"] += net_GND

R4["1"] += net_Net_D4_K
R4["2"] += net_GND

R5["1"] += net_Net_D5_K
R5["2"] += net_GND

R6["1"] += net_N_3V3
R6["2"] += net_I2C1_SCL

R7["1"] += net_N_3V3
R7["2"] += net_I2C1_SDA

R8["1"] += net_N_3V3
R8["2"] += net_I2C3_SCL

R9["1"] += net_N_3V3
R9["2"] += net_I2C3_SDA

R10["1"] += net_HSE_OUT
R10["2"] += net_Net_C21_Pad1

R11["1"] += net_UART1_TX
R11["2"] += net_Net_U6_RX

R12["1"] += net_N_3V3
R12["2"] += net_FLASH_WP

R13["1"] += net_UART1_RX
R13["2"] += net_Net_U6_TX

R14["1"] += net_FLASH_H
R14["2"] += net_N_3V3

R15["1"] += net_GND
R15["2"] += net_Net_D7_K

R16["1"] += net_Net_BOOT1_C
R16["2"] += net_BOOT0

R17["1"] += net_Net_BOOT2_C
R17["2"] += net_BOOT1

RC1["1"] += net_TIM2_CH1
RC1["2"] += net_TIM2_CH2
RC1["3"] += net_TIM4_CH1
RC1["4"] += net_TIM4_CH2

RESET1["1"] += net_NRST
RESET1["2"] += net_NRST
RESET1["3"] += net_GND
RESET1["4"] += net_GND

SBUS1["1"] += net_N_3V3
SBUS1["2"] += net_GND
SBUS1["3"] += net_UART3_TX
SBUS1["4"] += net_UART3_RX_INV

SERVO1["1"] += net_Net_PWM_PWR1_Pin_1
SERVO1["2"] += net_GND

SWD1["1"] += net_N_3V3
SWD1["2"] += net_GND
SWD1["3"] += net_GND
SWD1["4"] += net_unconnected_SWD1_Pin_4_Pad4
SWD1["5"] += net_GND
SWD1["6"] += net_NRST
SWD1["7"] += net_unconnected_SWD1_Pin_7_Pad7
SWD1["8"] += net_unconnected_SWD1_Pin_8_Pad8
SWD1["9"] += net_SWCLK
SWD1["10"] += net_SWDIO

TELEM1["1"] += net_N_3V3
TELEM1["2"] += net_GND
TELEM1["3"] += net_UART1_TX
TELEM1["4"] += net_UART1_RX

U1["1"] += net_VCC
U1["2"] += net_GND
U1["3"] += net_VCC
U1["4"] += net_unconnected_U1_NC_Pad4
U1["5"] += net_N_3V3

U2["1"] += net_GND
U2["2"] += net_GND
U2["3"] += net_GND
U2["4"] += net_GND
U2["5"] += net_GND
U2["6"] += net_Net_PWM_SIGNAL1_Pin_1
U2["7"] += net_Net_PWM_SIGNAL1_Pin_2
U2["8"] += net_Net_PWM_SIGNAL1_Pin_3
U2["9"] += net_Net_PWM_SIGNAL1_Pin_4
U2["10"] += net_Net_PWM_SIGNAL1_Pin_5
U2["11"] += net_Net_PWM_SIGNAL1_Pin_6
U2["12"] += net_Net_PWM_SIGNAL1_Pin_7
U2["13"] += net_Net_PWM_SIGNAL1_Pin_8
U2["14"] += net_GND
U2["15"] += net_unconnected_U2_LED8_Pad15
U2["16"] += net_unconnected_U2_LED9_Pad16
U2["17"] += net_unconnected_U2_LED10_Pad17
U2["18"] += net_unconnected_U2_LED11_Pad18
U2["19"] += net_unconnected_U2_LED12_Pad19
U2["20"] += net_unconnected_U2_LED13_Pad20
U2["21"] += net_unconnected_U2_LED14_Pad21
U2["22"] += net_unconnected_U2_LED15_Pad22
U2["23"] += net_GND
U2["24"] += net_GND
U2["25"] += net_unconnected_U2_EXTCLK_Pad25
U2["26"] += net_I2C1_SCL
U2["27"] += net_I2C1_SDA
U2["28"] += net_N_3V3

U3["1"] += net_GND
U3["2"] += net_GND
U3["3"] += net_GND
U3["4"] += net_GND
U3["5"] += net_I2C1_SDA
U3["6"] += net_I2C1_SCL
U3["7"] += net_GND
U3["8"] += net_N_3V3

U4["1"] += net_unconnected_U4_I_slash_O1_Pad1
U4["2"] += net_unconnected_U4_GND_Pad2
U4["3"] += net_unconnected_U4_I_slash_O2_Pad3
U4["4"] += net_unconnected_U4_I_slash_O2_Pad4
U4["5"] += net_unconnected_U4_VBUS_Pad5
U4["6"] += net_unconnected_U4_I_slash_O1_Pad6

U5["1"] += net_unconnected_U5_Pad1
U5["2"] += net_UART3_RX_INV
U5["3"] += net_GND
U5["4"] += net_UART3_RX
U5["5"] += net_N_3V3

U6["1"] += net_USB_CONV_D_POS
U6["2"] += net_USB_CONV_D_NEG
U6["3"] += net_GND
U6["4"] += net_unconnected_U6_RTS_Pad4
U6["5"] += net_unconnected_U6_CTS_Pad5
U6["6"] += net_Net_D7_A
U6["7"] += net_N_3V3
U6["8"] += net_Net_U6_TX
U6["9"] += net_Net_U6_RX
U6["10"] += net_Net_U6_V3

USB1["1"] += net_Net_USB1_VBUS
USB1["2"] += net_USB_CONN_D_NEG
USB1["3"] += net_USB_CONN_D_POS
USB1["4"] += net_unconnected_USB1_ID_Pad4
USB1["5"] += net_GND
USB1["SH"] += net_GND

VIN1["1"] += net_VCC
VIN1["2"] += net_GND


generate_netlist()