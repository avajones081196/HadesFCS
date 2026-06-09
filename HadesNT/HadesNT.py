# Auto-generated SKiDL script from HadesNT_original.net
# Source: Philip M. Salmony - Hades NT
# 102 components, 144 nets, 406 connections

from skidl import *

# ── Named nets (Net.fetch prevents auto-suffixing) ────────────
net_N_3V3 = Net.fetch("+3V3")
net_N_5V = Net.fetch("+5V")
net_ACC_CS = Net.fetch("ACC_!CS")
net_ACC_INT = Net.fetch("ACC_INT")
net_BOOT0 = Net.fetch("BOOT0")
net_GND = Net.fetch("GND")
net_GPIO_A = Net.fetch("GPIO_A")
net_GPIO_B = Net.fetch("GPIO_B")
net_GYR_CS = Net.fetch("GYR_!CS")
net_GYR_INT = Net.fetch("GYR_INT")
net_HSE_IN = Net.fetch("HSE_IN")
net_HSE_OUT = Net.fetch("HSE_OUT")
net_I2C1_SCL = Net.fetch("I2C1_SCL")
net_I2C1_SDA = Net.fetch("I2C1_SDA")
net_I2C2_SCL = Net.fetch("I2C2_SCL")
net_I2C2_SDA = Net.fetch("I2C2_SDA")
net_LED_A = Net.fetch("LED_A")
net_LED_B = Net.fetch("LED_B")
net_LED_C = Net.fetch("LED_C")
net_LED_D = Net.fetch("LED_D")
net_MAGD_DRDY = Net.fetch("MAGD_DRDY")
net_MAG_CS = Net.fetch("MAG_!CS")
net_MAG_INT = Net.fetch("MAG_INT")
net_NRST = Net.fetch("NRST")
net_Net_C29_Pad1 = Net.fetch("Net-(C29-Pad1)")
net_Net_D1_K = Net.fetch("Net-(D1-K)")
net_Net_D2_K = Net.fetch("Net-(D2-K)")
net_Net_D4_K = Net.fetch("Net-(D4-K)")
net_Net_D5_K = Net.fetch("Net-(D5-K)")
net_Net_D6_K = Net.fetch("Net-(D6-K)")
net_Net_D7_K = Net.fetch("Net-(D7-K)")
net_Net_D8_A = Net.fetch("Net-(D8-A)")
net_Net_D8_K = Net.fetch("Net-(D8-K)")
net_Net_F1_Pad2 = Net.fetch("Net-(F1-Pad2)")
net_Net_Q2_B = Net.fetch("Net-(Q2-B)")
net_Net_Q2_C = Net.fetch("Net-(Q2-C)")
net_Net_Q3_B = Net.fetch("Net-(Q3-B)")
net_Net_Q3_C = Net.fetch("Net-(Q3-C)")
net_Net_Q4_B = Net.fetch("Net-(Q4-B)")
net_Net_Q4_C = Net.fetch("Net-(Q4-C)")
net_Net_Q5_B = Net.fetch("Net-(Q5-B)")
net_Net_Q5_C = Net.fetch("Net-(Q5-C)")
net_Net_Q6_B = Net.fetch("Net-(Q6-B)")
net_Net_Q7_B = Net.fetch("Net-(Q7-B)")
net_Net_U1_IN = Net.fetch("Net-(U1-IN+)")
net_Net_U2_BST = Net.fetch("Net-(U2-BST)")
net_Net_U2_EN = Net.fetch("Net-(U2-EN)")
net_Net_U2_FB = Net.fetch("Net-(U2-FB)")
net_Net_U7_VCAP_1 = Net.fetch("Net-(U7-VCAP_1)")
net_Net_U7_VCAP_2 = Net.fetch("Net-(U7-VCAP_2)")
net_QSPI_CS = Net.fetch("QSPI_!CS")
net_QSPI_CLK = Net.fetch("QSPI_CLK")
net_QSPI_IO0 = Net.fetch("QSPI_IO0")
net_QSPI_IO1 = Net.fetch("QSPI_IO1")
net_QSPI_IO2 = Net.fetch("QSPI_IO2")
net_QSPI_IO3 = Net.fetch("QSPI_IO3")
net_SBUS_RX = Net.fetch("SBUS_RX")
net_SBUS_TX = Net.fetch("SBUS_TX")
net_SPI1_CS = Net.fetch("SPI1_!CS")
net_SPI1_MISO = Net.fetch("SPI1_MISO")
net_SPI1_MOSI = Net.fetch("SPI1_MOSI")
net_SPI1_SCK = Net.fetch("SPI1_SCK")
net_SPI2_CS = Net.fetch("SPI2_!CS")
net_SPI2_MISO = Net.fetch("SPI2_MISO")
net_SPI2_MOSI = Net.fetch("SPI2_MOSI")
net_SPI2_SCK = Net.fetch("SPI2_SCK")
net_SPI4_MISO = Net.fetch("SPI4_MISO")
net_SPI4_MOSI = Net.fetch("SPI4_MOSI")
net_SPI4_SCK = Net.fetch("SPI4_SCK")
net_SWCLK = Net.fetch("SWCLK")
net_SWDIO = Net.fetch("SWDIO")
net_SWO = Net.fetch("SWO")
net_TIM1_CH3 = Net.fetch("TIM1_CH3")
net_TIM1_CH4 = Net.fetch("TIM1_CH4")
net_TIM3_CH1 = Net.fetch("TIM3_CH1")
net_TIM3_CH2 = Net.fetch("TIM3_CH2")
net_TIM3_CH3 = Net.fetch("TIM3_CH3")
net_TIM3_CH4 = Net.fetch("TIM3_CH4")
net_TIM4_CH1 = Net.fetch("TIM4_CH1")
net_TIM4_CH2 = Net.fetch("TIM4_CH2")
net_TIM4_CH3 = Net.fetch("TIM4_CH3")
net_TIM4_CH4 = Net.fetch("TIM4_CH4")
net_TIM8_CH1 = Net.fetch("TIM8_CH1")
net_TIM8_CH2 = Net.fetch("TIM8_CH2")
net_TIM8_CH3 = Net.fetch("TIM8_CH3")
net_TIM8_CH4 = Net.fetch("TIM8_CH4")
net_UART2_RX = Net.fetch("UART2_RX")
net_UART2_TX = Net.fetch("UART2_TX")
net_UART3_RX = Net.fetch("UART3_RX")
net_UART3_TX = Net.fetch("UART3_TX")
net_UART4_RX = Net.fetch("UART4_RX")
net_UART4_TX = Net.fetch("UART4_TX")
net_USB_D_POS = Net.fetch("USB_D+")
net_USB_D_NEG = Net.fetch("USB_D-")
net_VBUS = Net.fetch("VBUS")
net_VCC = Net.fetch("VCC")
net_VDD = Net.fetch("VDD")
net_VDDA = Net.fetch("VDDA")
net_VS = Net.fetch("VS")

# ── Unconnected pins ──────────────────────────────────────────
net_unconnected_H1_Pad1 = Net("unconnected-(H1-Pad1)")
net_unconnected_H2_Pad1 = Net("unconnected-(H2-Pad1)")
net_unconnected_H3_Pad1 = Net("unconnected-(H3-Pad1)")
net_unconnected_H4_Pad1 = Net("unconnected-(H4-Pad1)")
net_unconnected_J1_ID_Pad4 = Net("unconnected-(J1-ID-Pad4)")
net_unconnected_J1_Shield_PadSH = Net("unconnected-(J1-Shield-PadSH)")
net_unconnected_J3_Pin_7_Pad7 = Net("unconnected-(J3-Pin_7-Pad7)")
net_unconnected_J3_Pin_8_Pad8 = Net("unconnected-(J3-Pin_8-Pad8)")
net_unconnected_S1_PadMP1 = Net("unconnected-(S1-PadMP1)")
net_unconnected_S1_PadMP2 = Net("unconnected-(S1-PadMP2)")
net_unconnected_S1_PadMP3 = Net("unconnected-(S1-PadMP3)")
net_unconnected_S1_PadMP4 = Net("unconnected-(S1-PadMP4)")
net_unconnected_U4_CLK_Pad6 = Net("unconnected-(U4-CLK-Pad6)")
net_unconnected_U4_DI_slash_IO_0_Pad5 = Net("unconnected-(U4-DI{slash}IO_{0}-Pad5)")
net_unconnected_U4_DO_slash_IO_1_Pad2 = Net("unconnected-(U4-DO{slash}IO_{1}-Pad2)")
net_unconnected_U4_GND_Pad4 = Net("unconnected-(U4-GND-Pad4)")
net_unconnected_U4_VCC_Pad8 = Net("unconnected-(U4-VCC-Pad8)")
net_unconnected_U4_CS_Pad1 = Net("unconnected-(U4-~{CS}-Pad1)")
net_unconnected_U4_HOLD_slash_RESET_slash_IO_3_Pad7 = Net("unconnected-(U4-~{HOLD}{slash}~{RESET}{slash}IO_{3}-Pad7)")
net_unconnected_U4_WP_slash_IO_2_Pad3 = Net("unconnected-(U4-~{WP}{slash}IO_{2}-Pad3)")
net_unconnected_U6_INT2_Pad1 = Net("unconnected-(U6-INT2-Pad1)")
net_unconnected_U6_INT4_Pad15 = Net("unconnected-(U6-INT4-Pad15)")
net_unconnected_U6_NC_1_Pad8 = Net("unconnected-(U6-NC_1-Pad8)")
net_unconnected_U6_NC_2_Pad18 = Net("unconnected-(U6-NC_2-Pad18)")
net_unconnected_U7_PA10_Pad69 = Net("unconnected-(U7-PA10-Pad69)")
net_unconnected_U7_PA15_Pad77 = Net("unconnected-(U7-PA15-Pad77)")
net_unconnected_U7_PA8_Pad67 = Net("unconnected-(U7-PA8-Pad67)")
net_unconnected_U7_PA9_Pad68 = Net("unconnected-(U7-PA9-Pad68)")
net_unconnected_U7_PB2_Pad36 = Net("unconnected-(U7-PB2-Pad36)")
net_unconnected_U7_PC0_Pad15 = Net("unconnected-(U7-PC0-Pad15)")
net_unconnected_U7_PC1_Pad16 = Net("unconnected-(U7-PC1-Pad16)")
net_unconnected_U7_PC10_Pad78 = Net("unconnected-(U7-PC10-Pad78)")
net_unconnected_U7_PC12_Pad80 = Net("unconnected-(U7-PC12-Pad80)")
net_unconnected_U7_PC13_Pad7 = Net("unconnected-(U7-PC13-Pad7)")
net_unconnected_U7_PC14_OSC32_IN_Pad8 = Net("unconnected-(U7-PC14-OSC32_IN-Pad8)")
net_unconnected_U7_PC15_OSC32_OUT_Pad9 = Net("unconnected-(U7-PC15-OSC32_OUT-Pad9)")
net_unconnected_U7_PC2_C_Pad17 = Net("unconnected-(U7-PC2_C-Pad17)")
net_unconnected_U7_PC3_C_Pad18 = Net("unconnected-(U7-PC3_C-Pad18)")
net_unconnected_U7_PD4_Pad85 = Net("unconnected-(U7-PD4-Pad85)")
net_unconnected_U7_PD5_Pad86 = Net("unconnected-(U7-PD5-Pad86)")
net_unconnected_U7_PD6_Pad87 = Net("unconnected-(U7-PD6-Pad87)")
net_unconnected_U7_PD7_Pad88 = Net("unconnected-(U7-PD7-Pad88)")
net_unconnected_U7_PE1_Pad98 = Net("unconnected-(U7-PE1-Pad98)")
net_unconnected_U7_PE12_Pad42 = Net("unconnected-(U7-PE12-Pad42)")
net_unconnected_U7_PE15_Pad45 = Net("unconnected-(U7-PE15-Pad45)")

# ── Components ────────────────────────────────────────────────
# C1 - 10u
C1_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_1206_3216Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C1 = C1_tmpl()
C1.ref = "C1"
C1.value = "10u"

# C2 - 10u
C2_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_1206_3216Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C2 = C2_tmpl()
C2.ref = "C2"
C2.value = "10u"

# C3 - 100n
C3_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C3 = C3_tmpl()
C3.ref = "C3"
C3.value = "100n"

# C4 - 33p
C4_tmpl = Part(tool=SKIDL, name="33p", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C4 = C4_tmpl()
C4.ref = "C4"
C4.value = "33p"

# C5 - 100n
C5_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C5 = C5_tmpl()
C5.ref = "C5"
C5.value = "100n"

# C6 - 4u7
C6_tmpl = Part(tool=SKIDL, name="4u7", footprint="Capacitor_SMD:C_1206_3216Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C6 = C6_tmpl()
C6.ref = "C6"
C6.value = "4u7"

# C7 - 10u
C7_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_1206_3216Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C7 = C7_tmpl()
C7.ref = "C7"
C7.value = "10u"

# C8 - 1u
C8_tmpl = Part(tool=SKIDL, name="1u", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C8 = C8_tmpl()
C8.ref = "C8"
C8.value = "1u"

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

# C14 - 10u
C14_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C14 = C14_tmpl()
C14.ref = "C14"
C14.value = "10u"

# C15 - 100n
C15_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C15 = C15_tmpl()
C15.ref = "C15"
C15.value = "100n"

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

# C20 - 100n
C20_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C20 = C20_tmpl()
C20.ref = "C20"
C20.value = "100n"

# C21 - 100n
C21_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C21 = C21_tmpl()
C21.ref = "C21"
C21.value = "100n"

# C22 - 100n
C22_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C22 = C22_tmpl()
C22.ref = "C22"
C22.value = "100n"

# C23 - 100n
C23_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C23 = C23_tmpl()
C23.ref = "C23"
C23.value = "100n"

# C24 - 100n
C24_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C24 = C24_tmpl()
C24.ref = "C24"
C24.value = "100n"

# C25 - 100n
C25_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C25 = C25_tmpl()
C25.ref = "C25"
C25.value = "100n"

# C26 - 1u
C26_tmpl = Part(tool=SKIDL, name="1u", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C26 = C26_tmpl()
C26.ref = "C26"
C26.value = "1u"

# C27 - 100n
C27_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C27 = C27_tmpl()
C27.ref = "C27"
C27.value = "100n"

# C28 - 12p
C28_tmpl = Part(tool=SKIDL, name="12p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C28 = C28_tmpl()
C28.ref = "C28"
C28.value = "12p"

# C29 - 12p
C29_tmpl = Part(tool=SKIDL, name="12p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C29 = C29_tmpl()
C29.ref = "C29"
C29.value = "12p"

# C30 - 2u2
C30_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C30 = C30_tmpl()
C30.ref = "C30"
C30.value = "2u2"

# C31 - 2u2
C31_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C31 = C31_tmpl()
C31.ref = "C31"
C31.value = "2u2"

# C32 - 100n
C32_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C32 = C32_tmpl()
C32.ref = "C32"
C32.value = "100n"

# D1 - B5819W
D1_tmpl = Part(tool=SKIDL, name="B5819W", footprint="Diode_SMD:D_SOD-123",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D1 = D1_tmpl()
D1.ref = "D1"
D1.value = "B5819W"

# D2 - GR
D2_tmpl = Part(tool=SKIDL, name="GR", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D2 = D2_tmpl()
D2.ref = "D2"
D2.value = "GR"

# D3 - B5819W
D3_tmpl = Part(tool=SKIDL, name="B5819W", footprint="Diode_SMD:D_SOD-123",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D3 = D3_tmpl()
D3.ref = "D3"
D3.value = "B5819W"

# D4 - RE
D4_tmpl = Part(tool=SKIDL, name="RE", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D4 = D4_tmpl()
D4.ref = "D4"
D4.value = "RE"

# D5 - YE
D5_tmpl = Part(tool=SKIDL, name="YE", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D5 = D5_tmpl()
D5.ref = "D5"
D5.value = "YE"

# D6 - GR
D6_tmpl = Part(tool=SKIDL, name="GR", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D6 = D6_tmpl()
D6.ref = "D6"
D6.value = "GR"

# D7 - BL
D7_tmpl = Part(tool=SKIDL, name="BL", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D7 = D7_tmpl()
D7.ref = "D7"
D7.value = "BL"

# D8 - RE
D8_tmpl = Part(tool=SKIDL, name="RE", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D8 = D8_tmpl()
D8.ref = "D8"
D8.value = "RE"

# F1 - 500mA
F1_tmpl = Part(tool=SKIDL, name="500mA", footprint="Inductor_SMD:L_1206_3216Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
F1 = F1_tmpl()
F1.ref = "F1"
F1.value = "500mA"

# FB1 - 100 @ 100 MHz
FB1_tmpl = Part(tool=SKIDL, name="100 @ 100 MHz", footprint="Inductor_SMD:L_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
FB1 = FB1_tmpl()
FB1.ref = "FB1"
FB1.value = "100 @ 100 MHz"

# H1 - MountingHole_Pad
H1_tmpl = Part(tool=SKIDL, name="MountingHole_Pad", footprint="MountingHole:MountingHole_4.3mm_M4_Pad_Via",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
H1 = H1_tmpl()
H1.ref = "H1"
H1.value = "MountingHole_Pad"

# H2 - MountingHole_Pad
H2_tmpl = Part(tool=SKIDL, name="MountingHole_Pad", footprint="MountingHole:MountingHole_4.3mm_M4_Pad_Via",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
H2 = H2_tmpl()
H2.ref = "H2"
H2.value = "MountingHole_Pad"

# H3 - MountingHole_Pad
H3_tmpl = Part(tool=SKIDL, name="MountingHole_Pad", footprint="MountingHole:MountingHole_4.3mm_M4_Pad_Via",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
H3 = H3_tmpl()
H3.ref = "H3"
H3.value = "MountingHole_Pad"

# H4 - MountingHole_Pad
H4_tmpl = Part(tool=SKIDL, name="MountingHole_Pad", footprint="MountingHole:MountingHole_4.3mm_M4_Pad_Via",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
H4 = H4_tmpl()
H4.ref = "H4"
H4.value = "MountingHole_Pad"

# J1 - USB_B_Micro
J1_tmpl = Part(tool=SKIDL, name="USB_B_Micro", footprint="10118193-0001LF:101181930001LF",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="SH", func=Pin.types.PWRIN)], dest=TEMPLATE)
J1 = J1_tmpl()
J1.ref = "J1"
J1.value = "USB_B_Micro"

# J2 - Conn_01x02
J2_tmpl = Part(tool=SKIDL, name="Conn_01x02", footprint="Connector_JST:JST_GH_SM02B-GHS-TB_1x02-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
J2 = J2_tmpl()
J2.ref = "J2"
J2.value = "Conn_01x02"

# J3 - Conn_02x05_Odd_Even
J3_tmpl = Part(tool=SKIDL, name="Conn_02x05_Odd_Even", footprint="Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN)], dest=TEMPLATE)
J3 = J3_tmpl()
J3.ref = "J3"
J3.value = "Conn_02x05_Odd_Even"

# J4 - Conn_01x04
J4_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_JST:JST_GH_SM04B-GHS-TB_1x04-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
J4 = J4_tmpl()
J4.ref = "J4"
J4.value = "Conn_01x04"

# J5 - Conn_01x04
J5_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_JST:JST_GH_SM04B-GHS-TB_1x04-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
J5 = J5_tmpl()
J5.ref = "J5"
J5.value = "Conn_01x04"

# J6 - Conn_01x06
J6_tmpl = Part(tool=SKIDL, name="Conn_01x06", footprint="Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
J6 = J6_tmpl()
J6.ref = "J6"
J6.value = "Conn_01x06"

# J7 - Conn_01x04
J7_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_JST:JST_GH_SM04B-GHS-TB_1x04-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
J7 = J7_tmpl()
J7.ref = "J7"
J7.value = "Conn_01x04"

# J8 - Conn_01x06
J8_tmpl = Part(tool=SKIDL, name="Conn_01x06", footprint="Connector_JST:JST_GH_SM06B-GHS-TB_1x06-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
J8 = J8_tmpl()
J8.ref = "J8"
J8.value = "Conn_01x06"

# J9 - Conn_01x08
J9_tmpl = Part(tool=SKIDL, name="Conn_01x08", footprint="Connector_JST:JST_GH_SM08B-GHS-TB_1x08-1MP_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
J9 = J9_tmpl()
J9.ref = "J9"
J9.value = "Conn_01x08"

# J10 - Conn_02x08_Odd_Even
J10_tmpl = Part(tool=SKIDL, name="Conn_02x08_Odd_Even", footprint="Connector_PinHeader_2.54mm:PinHeader_2x08_P2.54mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN)], dest=TEMPLATE)
J10 = J10_tmpl()
J10.ref = "J10"
J10.value = "Conn_02x08_Odd_Even"

# J11 - Conn_01x08
J11_tmpl = Part(tool=SKIDL, name="Conn_01x08", footprint="Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
J11 = J11_tmpl()
J11.ref = "J11"
J11.value = "Conn_01x08"

# L1 - 10u
L1_tmpl = Part(tool=SKIDL, name="10u", footprint="MWSA0503-100MT:INDPM5452X300N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
L1 = L1_tmpl()
L1.ref = "L1"
L1.value = "10u"

# L2 - 68n
L2_tmpl = Part(tool=SKIDL, name="68n", footprint="Inductor_SMD:L_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
L2 = L2_tmpl()
L2.ref = "L2"
L2.value = "68n"

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

# Q3 - MMBT3904
Q3_tmpl = Part(tool=SKIDL, name="MMBT3904", footprint="Package_TO_SOT_SMD:SOT-23",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
Q3 = Q3_tmpl()
Q3.ref = "Q3"
Q3.value = "MMBT3904"

# Q4 - MMBT3904
Q4_tmpl = Part(tool=SKIDL, name="MMBT3904", footprint="Package_TO_SOT_SMD:SOT-23",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
Q4 = Q4_tmpl()
Q4.ref = "Q4"
Q4.value = "MMBT3904"

# Q5 - MMBT3904
Q5_tmpl = Part(tool=SKIDL, name="MMBT3904", footprint="Package_TO_SOT_SMD:SOT-23",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
Q5 = Q5_tmpl()
Q5.ref = "Q5"
Q5.value = "MMBT3904"

# Q6 - MMBT3904
Q6_tmpl = Part(tool=SKIDL, name="MMBT3904", footprint="Package_TO_SOT_SMD:SOT-23",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
Q6 = Q6_tmpl()
Q6.ref = "Q6"
Q6.value = "MMBT3904"

# Q7 - MMBT3904
Q7_tmpl = Part(tool=SKIDL, name="MMBT3904", footprint="Package_TO_SOT_SMD:SOT-23",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
Q7 = Q7_tmpl()
Q7.ref = "Q7"
Q7.value = "MMBT3904"

# R1 - 0.25
R1_tmpl = Part(tool=SKIDL, name="0.25", footprint="Resistor_SMD:R_1206_3216Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R1 = R1_tmpl()
R1.ref = "R1"
R1.value = "0.25"

# R2 - 120k
R2_tmpl = Part(tool=SKIDL, name="120k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R2 = R2_tmpl()
R2.ref = "R2"
R2.value = "120k"

# R3 - 39k
R3_tmpl = Part(tool=SKIDL, name="39k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R3 = R3_tmpl()
R3.ref = "R3"
R3.value = "39k"

# R4 - 100k
R4_tmpl = Part(tool=SKIDL, name="100k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R4 = R4_tmpl()
R4.ref = "R4"
R4.value = "100k"

# R5 - DNP
R5_tmpl = Part(tool=SKIDL, name="DNP", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R5 = R5_tmpl()
R5.ref = "R5"
R5.value = "DNP"

# R6 - 1k
R6_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R6 = R6_tmpl()
R6.ref = "R6"
R6.value = "1k"

# R7 - 47
R7_tmpl = Part(tool=SKIDL, name="47", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R7 = R7_tmpl()
R7.ref = "R7"
R7.value = "47"

# R8 - 1k
R8_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R8 = R8_tmpl()
R8.ref = "R8"
R8.value = "1k"

# R9 - 10k
R9_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R9 = R9_tmpl()
R9.ref = "R9"
R9.value = "10k"

# R10 - 1k
R10_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R10 = R10_tmpl()
R10.ref = "R10"
R10.value = "1k"

# R11 - 10k
R11_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R11 = R11_tmpl()
R11.ref = "R11"
R11.value = "10k"

# R12 - 1k
R12_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R12 = R12_tmpl()
R12.ref = "R12"
R12.value = "1k"

# R13 - 10k
R13_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R13 = R13_tmpl()
R13.ref = "R13"
R13.value = "10k"

# R14 - 1k
R14_tmpl = Part(tool=SKIDL, name="1k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R14 = R14_tmpl()
R14.ref = "R14"
R14.value = "1k"

# R15 - 10k
R15_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R15 = R15_tmpl()
R15.ref = "R15"
R15.value = "10k"

# R16 - 10k
R16_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R16 = R16_tmpl()
R16.ref = "R16"
R16.value = "10k"

# R17 - 4k7
R17_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R17 = R17_tmpl()
R17.ref = "R17"
R17.value = "4k7"

# R18 - 10k
R18_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R18 = R18_tmpl()
R18.ref = "R18"
R18.value = "10k"

# R19 - 4k7
R19_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R19 = R19_tmpl()
R19.ref = "R19"
R19.value = "4k7"

# R20 - 2k2
R20_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R20 = R20_tmpl()
R20.ref = "R20"
R20.value = "2k2"

# R21 - 2k2
R21_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R21 = R21_tmpl()
R21.ref = "R21"
R21.value = "2k2"

# R22 - 2k2
R22_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R22 = R22_tmpl()
R22.ref = "R22"
R22.value = "2k2"

# R23 - 2k2
R23_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R23 = R23_tmpl()
R23.ref = "R23"
R23.value = "2k2"

# R24 - 10k
R24_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R24 = R24_tmpl()
R24.ref = "R24"
R24.value = "10k"

# R25 - 2k2
R25_tmpl = Part(tool=SKIDL, name="2k2", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R25 = R25_tmpl()
R25.ref = "R25"
R25.value = "2k2"

# S1 - MSS3-V-T_R
S1_tmpl = Part(tool=SKIDL, name="MSS3-V-T_R", footprint="MSS3-V-T_R:MSS3VTR",
    pins=[Pin(num="A1", func=Pin.types.PWRIN), Pin(num="B1", func=Pin.types.PWRIN), Pin(num="C1", func=Pin.types.PWRIN), Pin(num="MP1", func=Pin.types.PWRIN), Pin(num="MP2", func=Pin.types.PWRIN), Pin(num="MP3", func=Pin.types.PWRIN), Pin(num="MP4", func=Pin.types.PWRIN)], dest=TEMPLATE)
S1 = S1_tmpl()
S1.ref = "S1"
S1.value = "MSS3-V-T_R"

# SP1 - SolderPad
SP1_tmpl = Part(tool=SKIDL, name="SolderPad", footprint="TestPoint:TestPoint_Pad_2.0x2.0mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
SP1 = SP1_tmpl()
SP1.ref = "SP1"
SP1.value = "SolderPad"

# SP2 - SolderPad
SP2_tmpl = Part(tool=SKIDL, name="SolderPad", footprint="TestPoint:TestPoint_Pad_2.0x2.0mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
SP2 = SP2_tmpl()
SP2.ref = "SP2"
SP2.value = "SolderPad"

# U1 - INA219AIDCNR
U1_tmpl = Part(tool=SKIDL, name="INA219AIDCNR", footprint="Package_TO_SOT_SMD:SOT-23-8",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
U1 = U1_tmpl()
U1.ref = "U1"
U1.value = "INA219AIDCNR"

# U2 - MP2451DT-LF-Z
U2_tmpl = Part(tool=SKIDL, name="MP2451DT-LF-Z", footprint="MP2451DT-LF-Z:SOT95P280X145-6N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
U2 = U2_tmpl()
U2.ref = "U2"
U2.value = "MP2451DT-LF-Z"

# U3 - SRV05-4
U3_tmpl = Part(tool=SKIDL, name="SRV05-4", footprint="Package_TO_SOT_SMD:SOT-23-6",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
U3 = U3_tmpl()
U3.ref = "U3"
U3.value = "SRV05-4"

# U4 - W25Q128JVS
U4_tmpl = Part(tool=SKIDL, name="W25Q128JVS", footprint="Package_SO:SOIC-8_5.23x5.23mm_P1.27mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
U4 = U4_tmpl()
U4.ref = "U4"
U4.value = "W25Q128JVS"

# U5 - BMP280
U5_tmpl = Part(tool=SKIDL, name="BMP280", footprint="Package_LGA:Bosch_LGA-8_2x2.5mm_P0.65mm_ClockwisePinNumbering",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
U5 = U5_tmpl()
U5.ref = "U5"
U5.value = "BMP280"

# U6 - BMX055
U6_tmpl = Part(tool=SKIDL, name="BMX055", footprint="BMX055:LGA_PACKAGE_20_PINS",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN)], dest=TEMPLATE)
U6 = U6_tmpl()
U6.ref = "U6"
U6.value = "BMX055"

# U7 - STM32H750VBT6
U7_tmpl = Part(tool=SKIDL, name="STM32H750VBT6", footprint="STM32H750VBT6:QFP50P1600X1600X160-100N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN), Pin(num="21", func=Pin.types.PWRIN), Pin(num="22", func=Pin.types.PWRIN), Pin(num="23", func=Pin.types.PWRIN), Pin(num="24", func=Pin.types.PWRIN), Pin(num="25", func=Pin.types.PWRIN), Pin(num="26", func=Pin.types.PWRIN), Pin(num="27", func=Pin.types.PWRIN), Pin(num="28", func=Pin.types.PWRIN), Pin(num="29", func=Pin.types.PWRIN), Pin(num="30", func=Pin.types.PWRIN), Pin(num="31", func=Pin.types.PWRIN), Pin(num="32", func=Pin.types.PWRIN), Pin(num="33", func=Pin.types.PWRIN), Pin(num="34", func=Pin.types.PWRIN), Pin(num="35", func=Pin.types.PWRIN), Pin(num="36", func=Pin.types.PWRIN), Pin(num="37", func=Pin.types.PWRIN), Pin(num="38", func=Pin.types.PWRIN), Pin(num="39", func=Pin.types.PWRIN), Pin(num="40", func=Pin.types.PWRIN), Pin(num="41", func=Pin.types.PWRIN), Pin(num="42", func=Pin.types.PWRIN), Pin(num="43", func=Pin.types.PWRIN), Pin(num="44", func=Pin.types.PWRIN), Pin(num="45", func=Pin.types.PWRIN), Pin(num="46", func=Pin.types.PWRIN), Pin(num="47", func=Pin.types.PWRIN), Pin(num="48", func=Pin.types.PWRIN), Pin(num="49", func=Pin.types.PWRIN), Pin(num="50", func=Pin.types.PWRIN), Pin(num="51", func=Pin.types.PWRIN), Pin(num="52", func=Pin.types.PWRIN), Pin(num="53", func=Pin.types.PWRIN), Pin(num="54", func=Pin.types.PWRIN), Pin(num="55", func=Pin.types.PWRIN), Pin(num="56", func=Pin.types.PWRIN), Pin(num="57", func=Pin.types.PWRIN), Pin(num="58", func=Pin.types.PWRIN), Pin(num="59", func=Pin.types.PWRIN), Pin(num="60", func=Pin.types.PWRIN), Pin(num="61", func=Pin.types.PWRIN), Pin(num="62", func=Pin.types.PWRIN), Pin(num="63", func=Pin.types.PWRIN), Pin(num="64", func=Pin.types.PWRIN), Pin(num="65", func=Pin.types.PWRIN), Pin(num="66", func=Pin.types.PWRIN), Pin(num="67", func=Pin.types.PWRIN), Pin(num="68", func=Pin.types.PWRIN), Pin(num="69", func=Pin.types.PWRIN), Pin(num="70", func=Pin.types.PWRIN), Pin(num="71", func=Pin.types.PWRIN), Pin(num="72", func=Pin.types.PWRIN), Pin(num="73", func=Pin.types.PWRIN), Pin(num="74", func=Pin.types.PWRIN), Pin(num="75", func=Pin.types.PWRIN), Pin(num="76", func=Pin.types.PWRIN), Pin(num="77", func=Pin.types.PWRIN), Pin(num="78", func=Pin.types.PWRIN), Pin(num="79", func=Pin.types.PWRIN), Pin(num="80", func=Pin.types.PWRIN), Pin(num="81", func=Pin.types.PWRIN), Pin(num="82", func=Pin.types.PWRIN), Pin(num="83", func=Pin.types.PWRIN), Pin(num="84", func=Pin.types.PWRIN), Pin(num="85", func=Pin.types.PWRIN), Pin(num="86", func=Pin.types.PWRIN), Pin(num="87", func=Pin.types.PWRIN), Pin(num="88", func=Pin.types.PWRIN), Pin(num="89", func=Pin.types.PWRIN), Pin(num="90", func=Pin.types.PWRIN), Pin(num="91", func=Pin.types.PWRIN), Pin(num="92", func=Pin.types.PWRIN), Pin(num="93", func=Pin.types.PWRIN), Pin(num="94", func=Pin.types.PWRIN), Pin(num="95", func=Pin.types.PWRIN), Pin(num="96", func=Pin.types.PWRIN), Pin(num="97", func=Pin.types.PWRIN), Pin(num="98", func=Pin.types.PWRIN), Pin(num="99", func=Pin.types.PWRIN), Pin(num="100", func=Pin.types.PWRIN)], dest=TEMPLATE)
U7 = U7_tmpl()
U7.ref = "U7"
U7.value = "STM32H750VBT6"

# Y1 - 16 MHz
Y1_tmpl = Part(tool=SKIDL, name="16 MHz", footprint="Crystal:Crystal_SMD_3225-4Pin_3.2x2.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
Y1 = Y1_tmpl()
Y1.ref = "Y1"
Y1.value = "16 MHz"

# ── Connections ───────────────────────────────────────────────
C1["1"] += net_Net_U1_IN
C1["2"] += net_GND

C2["1"] += net_Net_U1_IN
C2["2"] += net_GND

C3["1"] += net_N_3V3
C3["2"] += net_GND

C4["1"] += net_Net_U2_FB
C4["2"] += net_N_3V3

C5["1"] += net_Net_U2_BST
C5["2"] += net_Net_D1_K

C6["1"] += net_VDD
C6["2"] += net_GND

C7["1"] += net_N_3V3
C7["2"] += net_GND

C8["1"] += net_N_5V
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

C14["1"] += net_N_3V3
C14["2"] += net_GND

C15["1"] += net_N_3V3
C15["2"] += net_GND

C16["1"] += net_N_3V3
C16["2"] += net_GND

C17["1"] += net_N_3V3
C17["2"] += net_GND

C18["1"] += net_N_3V3
C18["2"] += net_GND

C19["1"] += net_N_3V3
C19["2"] += net_GND

C20["1"] += net_N_3V3
C20["2"] += net_GND

C21["1"] += net_N_3V3
C21["2"] += net_GND

C22["1"] += net_N_3V3
C22["2"] += net_GND

C23["1"] += net_N_3V3
C23["2"] += net_GND

C24["1"] += net_N_3V3
C24["2"] += net_GND

C25["1"] += net_N_3V3
C25["2"] += net_GND

C26["1"] += net_VDDA
C26["2"] += net_GND

C27["1"] += net_VDDA
C27["2"] += net_GND

C28["1"] += net_HSE_IN
C28["2"] += net_GND

C29["1"] += net_Net_C29_Pad1
C29["2"] += net_GND

C30["1"] += net_Net_U7_VCAP_2
C30["2"] += net_GND

C31["1"] += net_Net_U7_VCAP_1
C31["2"] += net_GND

C32["1"] += net_NRST
C32["2"] += net_GND

D1["1"] += net_Net_D1_K
D1["2"] += net_GND

D2["1"] += net_Net_D2_K
D2["2"] += net_N_3V3

D3["1"] += net_VS
D3["2"] += net_N_5V

D4["1"] += net_Net_D4_K
D4["2"] += net_N_3V3

D5["1"] += net_Net_D5_K
D5["2"] += net_N_3V3

D6["1"] += net_Net_D6_K
D6["2"] += net_N_3V3

D7["1"] += net_Net_D7_K
D7["2"] += net_N_3V3

D8["1"] += net_Net_D8_K
D8["2"] += net_Net_D8_A

F1["1"] += net_VS
F1["2"] += net_Net_F1_Pad2

FB1["1"] += net_Net_U1_IN
FB1["2"] += net_Net_F1_Pad2

H1["1"] += net_unconnected_H1_Pad1

H2["1"] += net_unconnected_H2_Pad1

H3["1"] += net_unconnected_H3_Pad1

H4["1"] += net_unconnected_H4_Pad1

J1["1"] += net_N_5V
J1["2"] += net_USB_D_NEG
J1["3"] += net_USB_D_POS
J1["4"] += net_unconnected_J1_ID_Pad4
J1["5"] += net_GND
J1["SH"] += net_unconnected_J1_Shield_PadSH

J2["1"] += net_GND
J2["2"] += net_VCC

J3["1"] += net_N_3V3
J3["2"] += net_SWDIO
J3["3"] += net_GND
J3["4"] += net_SWCLK
J3["5"] += net_GND
J3["6"] += net_SWO
J3["7"] += net_unconnected_J3_Pin_7_Pad7
J3["8"] += net_unconnected_J3_Pin_8_Pad8
J3["9"] += net_GND
J3["10"] += net_NRST

J4["1"] += net_GND
J4["2"] += net_N_3V3
J4["3"] += net_SBUS_RX
J4["4"] += net_SBUS_TX

J5["1"] += net_GND
J5["2"] += net_N_3V3
J5["3"] += net_UART2_RX
J5["4"] += net_UART2_TX

J6["1"] += net_GND
J6["2"] += net_N_3V3
J6["3"] += net_UART3_RX
J6["4"] += net_UART3_TX
J6["5"] += net_GPIO_A
J6["6"] += net_GPIO_B

J7["1"] += net_GND
J7["2"] += net_N_3V3
J7["3"] += net_I2C2_SDA
J7["4"] += net_I2C2_SCL

J8["1"] += net_GND
J8["2"] += net_N_3V3
J8["3"] += net_SPI2_CS
J8["4"] += net_SPI2_SCK
J8["5"] += net_SPI2_MISO
J8["6"] += net_SPI2_MOSI

J9["1"] += net_GND
J9["2"] += net_N_3V3
J9["3"] += net_TIM3_CH1
J9["4"] += net_TIM3_CH2
J9["5"] += net_TIM3_CH3
J9["6"] += net_TIM3_CH4
J9["7"] += net_TIM1_CH3
J9["8"] += net_TIM1_CH4

J10["1"] += net_GND
J10["2"] += net_VBUS
J10["3"] += net_GND
J10["4"] += net_VBUS
J10["5"] += net_GND
J10["6"] += net_VBUS
J10["7"] += net_GND
J10["8"] += net_VBUS
J10["9"] += net_GND
J10["10"] += net_VBUS
J10["11"] += net_GND
J10["12"] += net_VBUS
J10["13"] += net_GND
J10["14"] += net_VBUS
J10["15"] += net_GND
J10["16"] += net_VBUS

J11["1"] += net_TIM8_CH4
J11["2"] += net_TIM8_CH3
J11["3"] += net_TIM8_CH2
J11["4"] += net_TIM8_CH1
J11["5"] += net_TIM4_CH4
J11["6"] += net_TIM4_CH3
J11["7"] += net_TIM4_CH2
J11["8"] += net_TIM4_CH1

L1["1"] += net_Net_D1_K
L1["2"] += net_N_3V3

L2["1"] += net_N_3V3
L2["2"] += net_VDDA

Q1["1"] += net_GND
Q1["2"] += net_VS
Q1["3"] += net_VCC

Q2["1"] += net_Net_Q2_B
Q2["2"] += net_GND
Q2["3"] += net_Net_Q2_C

Q3["1"] += net_Net_Q3_B
Q3["2"] += net_GND
Q3["3"] += net_Net_Q3_C

Q4["1"] += net_Net_Q4_B
Q4["2"] += net_GND
Q4["3"] += net_Net_Q4_C

Q5["1"] += net_Net_Q5_B
Q5["2"] += net_GND
Q5["3"] += net_Net_Q5_C

Q6["1"] += net_Net_Q6_B
Q6["2"] += net_GND
Q6["3"] += net_UART4_RX

Q7["1"] += net_Net_Q7_B
Q7["2"] += net_GND
Q7["3"] += net_SBUS_TX

R1["1"] += net_VDD
R1["2"] += net_Net_U1_IN

R2["1"] += net_N_3V3
R2["2"] += net_Net_U2_FB

R3["1"] += net_GND
R3["2"] += net_Net_U2_FB

R4["1"] += net_Net_U2_EN
R4["2"] += net_VDD

R5["1"] += net_GND
R5["2"] += net_Net_U2_EN

R6["1"] += net_GND
R6["2"] += net_Net_D2_K

R7["1"] += net_Net_C29_Pad1
R7["2"] += net_HSE_OUT

R8["1"] += net_Net_Q2_C
R8["2"] += net_Net_D4_K

R9["1"] += net_LED_A
R9["2"] += net_Net_Q2_B

R10["1"] += net_Net_Q3_C
R10["2"] += net_Net_D5_K

R11["1"] += net_LED_B
R11["2"] += net_Net_Q3_B

R12["1"] += net_Net_Q4_C
R12["2"] += net_Net_D6_K

R13["1"] += net_LED_C
R13["2"] += net_Net_Q4_B

R14["1"] += net_Net_Q5_C
R14["2"] += net_Net_D7_K

R15["1"] += net_LED_D
R15["2"] += net_Net_Q5_B

R16["1"] += net_UART4_RX
R16["2"] += net_N_3V3

R17["1"] += net_Net_Q6_B
R17["2"] += net_SBUS_RX

R18["1"] += net_SBUS_TX
R18["2"] += net_N_3V3

R19["1"] += net_Net_Q7_B
R19["2"] += net_UART4_TX

R20["1"] += net_I2C1_SDA
R20["2"] += net_N_3V3

R21["1"] += net_I2C1_SCL
R21["2"] += net_N_3V3

R22["1"] += net_I2C2_SDA
R22["2"] += net_N_3V3

R23["1"] += net_I2C2_SCL
R23["2"] += net_N_3V3

R24["1"] += net_BOOT0
R24["2"] += net_Net_D8_A

R25["1"] += net_GND
R25["2"] += net_Net_D8_K

S1["A1"] += net_N_3V3
S1["B1"] += net_Net_D8_A
S1["C1"] += net_GND
S1["MP1"] += net_unconnected_S1_PadMP1
S1["MP2"] += net_unconnected_S1_PadMP2
S1["MP3"] += net_unconnected_S1_PadMP3
S1["MP4"] += net_unconnected_S1_PadMP4

SP1["1"] += net_GND

SP2["1"] += net_VBUS

U1["1"] += net_Net_U1_IN
U1["2"] += net_VDD
U1["3"] += net_GND
U1["4"] += net_N_3V3
U1["5"] += net_I2C1_SCL
U1["6"] += net_I2C1_SDA
U1["7"] += net_GND
U1["8"] += net_GND

U2["1"] += net_Net_U2_BST
U2["2"] += net_GND
U2["3"] += net_Net_U2_FB
U2["4"] += net_Net_U2_EN
U2["5"] += net_VDD
U2["6"] += net_Net_D1_K

U3["1"] += net_USB_D_NEG
U3["2"] += net_GND
U3["3"] += net_USB_D_POS
U3["4"] += net_USB_D_POS
U3["5"] += net_N_5V
U3["6"] += net_USB_D_NEG

U4["1"] += net_unconnected_U4_CS_Pad1
U4["2"] += net_unconnected_U4_DO_slash_IO_1_Pad2
U4["3"] += net_unconnected_U4_WP_slash_IO_2_Pad3
U4["4"] += net_unconnected_U4_GND_Pad4
U4["5"] += net_unconnected_U4_DI_slash_IO_0_Pad5
U4["6"] += net_unconnected_U4_CLK_Pad6
U4["7"] += net_unconnected_U4_HOLD_slash_RESET_slash_IO_3_Pad7
U4["8"] += net_unconnected_U4_VCC_Pad8

U5["1"] += net_GND
U5["2"] += net_SPI1_CS
U5["3"] += net_SPI1_MOSI
U5["4"] += net_SPI1_SCK
U5["5"] += net_SPI1_MISO
U5["6"] += net_N_3V3
U5["7"] += net_GND
U5["8"] += net_N_3V3

U6["1"] += net_unconnected_U6_INT2_Pad1
U6["2"] += net_MAGD_DRDY
U6["3"] += net_N_3V3
U6["4"] += net_GND
U6["5"] += net_GYR_CS
U6["6"] += net_GND
U6["7"] += net_GND
U6["8"] += net_unconnected_U6_NC_1_Pad8
U6["9"] += net_SPI4_SCK
U6["10"] += net_MAG_INT
U6["11"] += net_SPI4_MOSI
U6["12"] += net_SPI4_MISO
U6["13"] += net_N_3V3
U6["14"] += net_GYR_INT
U6["15"] += net_unconnected_U6_INT4_Pad15
U6["16"] += net_ACC_CS
U6["17"] += net_SPI4_MISO
U6["18"] += net_unconnected_U6_NC_2_Pad18
U6["19"] += net_ACC_INT
U6["20"] += net_MAG_CS

U7["1"] += net_SPI4_SCK
U7["2"] += net_ACC_CS
U7["3"] += net_GYR_CS
U7["4"] += net_SPI4_MISO
U7["5"] += net_SPI4_MOSI
U7["6"] += net_N_3V3
U7["7"] += net_unconnected_U7_PC13_Pad7
U7["8"] += net_unconnected_U7_PC14_OSC32_IN_Pad8
U7["9"] += net_unconnected_U7_PC15_OSC32_OUT_Pad9
U7["10"] += net_GND
U7["11"] += net_N_3V3
U7["12"] += net_HSE_IN
U7["13"] += net_HSE_OUT
U7["14"] += net_NRST
U7["15"] += net_unconnected_U7_PC0_Pad15
U7["16"] += net_unconnected_U7_PC1_Pad16
U7["17"] += net_unconnected_U7_PC2_C_Pad17
U7["18"] += net_unconnected_U7_PC3_C_Pad18
U7["19"] += net_GND
U7["20"] += net_VDDA
U7["21"] += net_VDDA
U7["22"] += net_UART4_TX
U7["23"] += net_UART4_RX
U7["24"] += net_UART2_TX
U7["25"] += net_UART2_RX
U7["26"] += net_GND
U7["27"] += net_N_3V3
U7["28"] += net_SPI1_CS
U7["29"] += net_SPI1_SCK
U7["30"] += net_SPI1_MISO
U7["31"] += net_SPI1_MOSI
U7["32"] += net_MAGD_DRDY
U7["33"] += net_MAG_INT
U7["34"] += net_TIM3_CH3
U7["35"] += net_TIM3_CH4
U7["36"] += net_unconnected_U7_PB2_Pad36
U7["37"] += net_QSPI_CLK
U7["38"] += net_QSPI_IO0
U7["39"] += net_QSPI_IO1
U7["40"] += net_QSPI_IO2
U7["41"] += net_QSPI_IO3
U7["42"] += net_unconnected_U7_PE12_Pad42
U7["43"] += net_TIM1_CH3
U7["44"] += net_TIM1_CH4
U7["45"] += net_unconnected_U7_PE15_Pad45
U7["46"] += net_I2C2_SCL
U7["47"] += net_I2C2_SDA
U7["48"] += net_Net_U7_VCAP_1
U7["49"] += net_GND
U7["50"] += net_N_3V3
U7["51"] += net_SPI2_CS
U7["52"] += net_SPI2_SCK
U7["53"] += net_SPI2_MISO
U7["54"] += net_SPI2_MOSI
U7["55"] += net_UART3_TX
U7["56"] += net_UART3_RX
U7["57"] += net_GPIO_A
U7["58"] += net_GPIO_B
U7["59"] += net_TIM4_CH1
U7["60"] += net_TIM4_CH2
U7["61"] += net_TIM4_CH3
U7["62"] += net_TIM4_CH4
U7["63"] += net_TIM8_CH1
U7["64"] += net_TIM8_CH2
U7["65"] += net_TIM8_CH3
U7["66"] += net_TIM8_CH4
U7["67"] += net_unconnected_U7_PA8_Pad67
U7["68"] += net_unconnected_U7_PA9_Pad68
U7["69"] += net_unconnected_U7_PA10_Pad69
U7["70"] += net_USB_D_NEG
U7["71"] += net_USB_D_POS
U7["72"] += net_SWDIO
U7["73"] += net_Net_U7_VCAP_2
U7["74"] += net_GND
U7["75"] += net_N_3V3
U7["76"] += net_SWCLK
U7["77"] += net_unconnected_U7_PA15_Pad77
U7["78"] += net_unconnected_U7_PC10_Pad78
U7["79"] += net_QSPI_CS
U7["80"] += net_unconnected_U7_PC12_Pad80
U7["81"] += net_LED_A
U7["82"] += net_LED_B
U7["83"] += net_ACC_INT
U7["84"] += net_GYR_INT
U7["85"] += net_unconnected_U7_PD4_Pad85
U7["86"] += net_unconnected_U7_PD5_Pad86
U7["87"] += net_unconnected_U7_PD6_Pad87
U7["88"] += net_unconnected_U7_PD7_Pad88
U7["89"] += net_SWO
U7["90"] += net_TIM3_CH1
U7["91"] += net_TIM3_CH2
U7["92"] += net_LED_C
U7["93"] += net_LED_D
U7["94"] += net_BOOT0
U7["95"] += net_I2C1_SCL
U7["96"] += net_I2C1_SDA
U7["97"] += net_MAG_CS
U7["98"] += net_unconnected_U7_PE1_Pad98
U7["99"] += net_GND
U7["100"] += net_N_3V3

Y1["1"] += net_HSE_IN
Y1["2"] += net_GND
Y1["3"] += net_Net_C29_Pad1
Y1["4"] += net_GND


generate_netlist()