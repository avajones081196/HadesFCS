# Auto-generated SKiDL script from Hades_original.net
# Source: Philip M. Salmony - Hades FCS
# 195 components, 316 nets, 767 connections

from skidl import *

# ── Named nets (Net.fetch prevents auto-suffixing) ────────────
net_N_3_3V = Net.fetch("+3.3V")
net_N_3V3 = Net.fetch("+3V3")
net_N_5V = Net.fetch("+5V")
net_ADC3_0_FCC = Net.fetch("ADC3_0_FCC")
net_ADC3_1_FCC = Net.fetch("ADC3_1_FCC")
net_BAR_NRST_NAVC = Net.fetch("BAR_NRST_NAVC")
net_BOOT0_FCC = Net.fetch("BOOT0_FCC")
net_BOOT0_NAVC = Net.fetch("BOOT0_NAVC")
net_BOOT1_NAVC = Net.fetch("BOOT1_NAVC")
net_GND = Net.fetch("GND")
net_GPIO_A_FCC = Net.fetch("GPIO_A_FCC")
net_GPIO_A_NAVC = Net.fetch("GPIO_A_NAVC")
net_GPIO_B_FCC = Net.fetch("GPIO_B_FCC")
net_GPIO_B_NAVC = Net.fetch("GPIO_B_NAVC")
net_GPIO_C_FCC = Net.fetch("GPIO_C_FCC")
net_GPIO_C_NAVC = Net.fetch("GPIO_C_NAVC")
net_GPIO_D_FCC = Net.fetch("GPIO_D_FCC")
net_GPIO_D_NAVC = Net.fetch("GPIO_D_NAVC")
net_GPIO_E_FCC = Net.fetch("GPIO_E_FCC")
net_GPIO_E_NAVC = Net.fetch("GPIO_E_NAVC")
net_GPIO_F_FCC = Net.fetch("GPIO_F_FCC")
net_GPIO_F_NAVC = Net.fetch("GPIO_F_NAVC")
net_GPIO_G_FCC = Net.fetch("GPIO_G_FCC")
net_GPIO_G_NAVC = Net.fetch("GPIO_G_NAVC")
net_GPIO_H_FCC = Net.fetch("GPIO_H_FCC")
net_GPIO_H_NAVC = Net.fetch("GPIO_H_NAVC")
net_GPS_BAT_BACKUP = Net.fetch("GPS_BAT_BACKUP")
net_GPS_LNA_EN_NAVC = Net.fetch("GPS_LNA_EN_NAVC")
net_GPS_NRST_NAVC = Net.fetch("GPS_NRST_NAVC")
net_GPS_PPS_NAVC = Net.fetch("GPS_PPS_NAVC")
net_HSE_IN_FCC = Net.fetch("HSE_IN_FCC")
net_HSE_IN_NAVC = Net.fetch("HSE_IN_NAVC")
net_HSE_OUT_FCC = Net.fetch("HSE_OUT_FCC")
net_HSE_OUT_NAVC = Net.fetch("HSE_OUT_NAVC")
net_I2C1_SCL_FCC = Net.fetch("I2C1_SCL_FCC")
net_I2C1_SCL_NAVC = Net.fetch("I2C1_SCL_NAVC")
net_I2C1_SDA_FCC = Net.fetch("I2C1_SDA_FCC")
net_I2C1_SDA_NAVC = Net.fetch("I2C1_SDA_NAVC")
net_I2C2_SCL_FCC = Net.fetch("I2C2_SCL_FCC")
net_I2C2_SCL_NAVC = Net.fetch("I2C2_SCL_NAVC")
net_I2C2_SDA_FCC = Net.fetch("I2C2_SDA_FCC")
net_I2C2_SDA_NAVC = Net.fetch("I2C2_SDA_NAVC")
net_I2C3_SCL_FCC = Net.fetch("I2C3_SCL_FCC")
net_I2C3_SCL_NAVC = Net.fetch("I2C3_SCL_NAVC")
net_I2C3_SDA_FCC = Net.fetch("I2C3_SDA_FCC")
net_I2C3_SDA_NAVC = Net.fetch("I2C3_SDA_NAVC")
net_INT_ACC_NAVC = Net.fetch("INT_ACC_NAVC")
net_INT_BAR_NAVC = Net.fetch("INT_BAR_NAVC")
net_INT_GYR_NAVC = Net.fetch("INT_GYR_NAVC")
net_INT_MAG_NAVC = Net.fetch("INT_MAG_NAVC")
net_LED_A_FCC = Net.fetch("LED_A_FCC")
net_LED_A_NAVC = Net.fetch("LED_A_NAVC")
net_LED_B_FCC = Net.fetch("LED_B_FCC")
net_LED_B_NAVC = Net.fetch("LED_B_NAVC")
net_LED_C_FCC = Net.fetch("LED_C_FCC")
net_LED_C_NAVC = Net.fetch("LED_C_NAVC")
net_LED_D_FCC = Net.fetch("LED_D_FCC")
net_LED_D_NAVC = Net.fetch("LED_D_NAVC")
net_LED_E_FCC = Net.fetch("LED_E_FCC")
net_LED_F_FCC = Net.fetch("LED_F_FCC")
net_NRST_FCC = Net.fetch("NRST_FCC")
net_NRST_NAVC = Net.fetch("NRST_NAVC")
net_Net_ANT1_Pad1 = Net.fetch("Net-(ANT1-Pad1)")
net_Net_C33_Pad1 = Net.fetch("Net-(C33-Pad1)")
net_Net_C53_Pad1 = Net.fetch("Net-(C53-Pad1)")
net_Net_C6_Pad2 = Net.fetch("Net-(C6-Pad2)")
net_Net_D1_A = Net.fetch("Net-(D1-A)")
net_Net_D2_A = Net.fetch("Net-(D2-A)")
net_Net_D3_A = Net.fetch("Net-(D3-A)")
net_Net_D4_A = Net.fetch("Net-(D4-A)")
net_Net_D5_A = Net.fetch("Net-(D5-A)")
net_Net_FCC1_PH0 = Net.fetch("Net-(FCC1-PH0)")
net_Net_JP3_C = Net.fetch("Net-(JP3-C)")
net_Net_L2_Pad1 = Net.fetch("Net-(L2-Pad1)")
net_Net_LED1_K = Net.fetch("Net-(LED1-K)")
net_Net_LED10_K = Net.fetch("Net-(LED10-K)")
net_Net_LED11_K = Net.fetch("Net-(LED11-K)")
net_Net_LED12_K = Net.fetch("Net-(LED12-K)")
net_Net_LED13_K = Net.fetch("Net-(LED13-K)")
net_Net_LED14_K = Net.fetch("Net-(LED14-K)")
net_Net_LED2_K = Net.fetch("Net-(LED2-K)")
net_Net_LED3_K = Net.fetch("Net-(LED3-K)")
net_Net_LED4_K = Net.fetch("Net-(LED4-K)")
net_Net_LED5_K = Net.fetch("Net-(LED5-K)")
net_Net_LED6_K = Net.fetch("Net-(LED6-K)")
net_Net_LED7_K = Net.fetch("Net-(LED7-K)")
net_Net_LED8_K = Net.fetch("Net-(LED8-K)")
net_Net_LED9_K = Net.fetch("Net-(LED9-K)")
net_Net_NAVC1_PH0 = Net.fetch("Net-(NAVC1-PH0)")
net_Net_NAVC1_PH1 = Net.fetch("Net-(NAVC1-PH1)")
net_Net_NAVC1_VSS_Pad18 = Net.fetch("Net-(NAVC1-VSS-Pad18)")
net_Net_REG1_PVDD = Net.fetch("Net-(REG1-PVDD)")
net_Net_SW2_C = Net.fetch("Net-(SW2-C)")
net_Net_SW3_C = Net.fetch("Net-(SW3-C)")
net_Net_SW4_C = Net.fetch("Net-(SW4-C)")
net_Net_U10_RF_IN = Net.fetch("Net-(U10-RF_IN)")
net_Net_U10_VCC_RF = Net.fetch("Net-(U10-VCC_RF)")
net_Net_U4_HOLD_IO3 = Net.fetch("Net-(U4-~{HOLD_(IO3}))")
net_Net_U4_WP_IO2 = Net.fetch("Net-(U4-~{WP_(IO2}))")
net_Net_U7_VO_POS = Net.fetch("Net-(U7-VO+)")
net_Net_U7_VO_NEG = Net.fetch("Net-(U7-VO-)")
net_Net_U8_C1 = Net.fetch("Net-(U8-C1)")
net_Net_USB1_D_POS = Net.fetch("Net-(USB1-D+)")
net_Net_USB1_D_NEG = Net.fetch("Net-(USB1-D-)")
net_Net_USB1_ID = Net.fetch("Net-(USB1-ID)")
net_Net_USB2_D_POS = Net.fetch("Net-(USB2-D+)")
net_Net_USB2_D_NEG = Net.fetch("Net-(USB2-D-)")
net_Net_USB2_ID = Net.fetch("Net-(USB2-ID)")
net_PWM_0 = Net.fetch("PWM_0")
net_PWM_1 = Net.fetch("PWM_1")
net_PWM_2 = Net.fetch("PWM_2")
net_PWM_3 = Net.fetch("PWM_3")
net_PWM_4 = Net.fetch("PWM_4")
net_PWM_5 = Net.fetch("PWM_5")
net_PWM_6 = Net.fetch("PWM_6")
net_PWM_7 = Net.fetch("PWM_7")
net_REG_BST = Net.fetch("REG_BST")
net_REG_CS = Net.fetch("REG_CS")
net_REG_EN = Net.fetch("REG_EN")
net_REG_FB = Net.fetch("REG_FB")
net_REG_PG = Net.fetch("REG_PG")
net_REG_VIN = Net.fetch("REG_VIN")
net_SPI1_CS_FLASH_FCC = Net.fetch("SPI1_CS_FLASH_FCC")
net_SPI1_MISO_FCC = Net.fetch("SPI1_MISO_FCC")
net_SPI1_MOSI_FCC = Net.fetch("SPI1_MOSI_FCC")
net_SPI1_SCK_FCC = Net.fetch("SPI1_SCK_FCC")
net_SWCLK_FCC = Net.fetch("SWCLK_FCC")
net_SWCLK_NAVC = Net.fetch("SWCLK_NAVC")
net_SWDIO_FCC = Net.fetch("SWDIO_FCC")
net_SWDIO_NAVC = Net.fetch("SWDIO_NAVC")
net_TIM4_CH1_FCC = Net.fetch("TIM4_CH1_FCC")
net_TIM4_CH2_FCC = Net.fetch("TIM4_CH2_FCC")
net_TIM4_CH3_FCC = Net.fetch("TIM4_CH3_FCC")
net_TIM4_CH4_FCC = Net.fetch("TIM4_CH4_FCC")
net_UART1_RX_NAVC = Net.fetch("UART1_RX_NAVC")
net_UART1_TX_FCC = Net.fetch("UART1_TX_FCC")
net_UART1_TX_NAVC = Net.fetch("UART1_TX_NAVC")
net_UART2_RX_FCC = Net.fetch("UART2_RX_FCC")
net_UART2_RX_NAVC = Net.fetch("UART2_RX_NAVC")
net_UART2_TX_FCC = Net.fetch("UART2_TX_FCC")
net_UART2_TX_NAVC = Net.fetch("UART2_TX_NAVC")
net_UART3_RX_FCC = Net.fetch("UART3_RX_FCC")
net_UART3_TX_FCC = Net.fetch("UART3_TX_FCC")
net_UART4_RX_FCC = Net.fetch("UART4_RX_FCC")
net_UART4_RX_NAVC = Net.fetch("UART4_RX_NAVC")
net_UART4_TX_FCC = Net.fetch("UART4_TX_FCC")
net_UART4_TX_NAVC = Net.fetch("UART4_TX_NAVC")
net_UART5_RX_FCC = Net.fetch("UART5_RX_FCC")
net_UART5_TX_FCC = Net.fetch("UART5_TX_FCC")
net_USB_DM_FCC = Net.fetch("USB_DM_FCC")
net_USB_DM_NAVC = Net.fetch("USB_DM_NAVC")
net_USB_DP_FCC = Net.fetch("USB_DP_FCC")
net_USB_DP_NAVC = Net.fetch("USB_DP_NAVC")
net_USB_ID_FCC = Net.fetch("USB_ID_FCC")
net_USB_ID_NAVC = Net.fetch("USB_ID_NAVC")
net_USB_VBUS_FCC = Net.fetch("USB_VBUS_FCC")
net_USB_VBUS_NAVC = Net.fetch("USB_VBUS_NAVC")
net_VDDA_FCC = Net.fetch("VDDA_FCC")
net_VDDA_NAVC = Net.fetch("VDDA_NAVC")
net_VIN = Net.fetch("VIN+")
net_VREF_FCC = Net.fetch("VREF+_FCC")

# ── Unconnected pins (NC nets) ────────────────────────────────
net_unconnected_C13_Pad1 = Net("unconnected-(C13-Pad1)")
net_unconnected_C69_Pad2 = Net("unconnected-(C69-Pad2)")
net_unconnected_C71_Pad2 = Net("unconnected-(C71-Pad2)")
net_unconnected_D2_K_Pad1 = Net("unconnected-(D2-K-Pad1)")
net_unconnected_D3_K_Pad1 = Net("unconnected-(D3-K-Pad1)")
net_unconnected_D4_K_Pad1 = Net("unconnected-(D4-K-Pad1)")
net_unconnected_D5_K_Pad1 = Net("unconnected-(D5-K-Pad1)")
net_unconnected_FCC1_BOOT0_Pad94 = Net("unconnected-(FCC1-BOOT0-Pad94)")
net_unconnected_FCC1_NRST_Pad14 = Net("unconnected-(FCC1-NRST-Pad14)")
net_unconnected_FCC1_PA0_Pad22 = Net("unconnected-(FCC1-PA0-Pad22)")
net_unconnected_FCC1_PB0_Pad34 = Net("unconnected-(FCC1-PB0-Pad34)")
net_unconnected_FCC1_PB10_Pad46 = Net("unconnected-(FCC1-PB10-Pad46)")
net_unconnected_FCC1_PB9_Pad96 = Net("unconnected-(FCC1-PB9-Pad96)")
net_unconnected_FCC1_PC0_Pad15 = Net("unconnected-(FCC1-PC0-Pad15)")
net_unconnected_FCC1_PC1_Pad16 = Net("unconnected-(FCC1-PC1-Pad16)")
net_unconnected_FCC1_PC11_Pad79 = Net("unconnected-(FCC1-PC11-Pad79)")
net_unconnected_FCC1_PC12_Pad80 = Net("unconnected-(FCC1-PC12-Pad80)")
net_unconnected_FCC1_PC13_Pad7 = Net("unconnected-(FCC1-PC13-Pad7)")
net_unconnected_FCC1_PC14_Pad8 = Net("unconnected-(FCC1-PC14-Pad8)")
net_unconnected_FCC1_PC15_Pad9 = Net("unconnected-(FCC1-PC15-Pad9)")
net_unconnected_FCC1_PC2_C_Pad17 = Net("unconnected-(FCC1-PC2_C-Pad17)")
net_unconnected_FCC1_PC5_Pad33 = Net("unconnected-(FCC1-PC5-Pad33)")
net_unconnected_FCC1_PC6_Pad63 = Net("unconnected-(FCC1-PC6-Pad63)")
net_unconnected_FCC1_PC7_Pad64 = Net("unconnected-(FCC1-PC7-Pad64)")
net_unconnected_FCC1_PC8_Pad65 = Net("unconnected-(FCC1-PC8-Pad65)")
net_unconnected_FCC1_PC9_Pad66 = Net("unconnected-(FCC1-PC9-Pad66)")
net_unconnected_FCC1_PD0_Pad81 = Net("unconnected-(FCC1-PD0-Pad81)")
net_unconnected_FCC1_PD1_Pad82 = Net("unconnected-(FCC1-PD1-Pad82)")
net_unconnected_FCC1_PD2_Pad83 = Net("unconnected-(FCC1-PD2-Pad83)")
net_unconnected_FCC1_PD3_Pad84 = Net("unconnected-(FCC1-PD3-Pad84)")
net_unconnected_FCC1_PD4_Pad85 = Net("unconnected-(FCC1-PD4-Pad85)")
net_unconnected_FCC1_PD5_Pad86 = Net("unconnected-(FCC1-PD5-Pad86)")
net_unconnected_FCC1_PD6_Pad87 = Net("unconnected-(FCC1-PD6-Pad87)")
net_unconnected_FCC1_PD7_Pad88 = Net("unconnected-(FCC1-PD7-Pad88)")
net_unconnected_FCC1_PD8_Pad55 = Net("unconnected-(FCC1-PD8-Pad55)")
net_unconnected_FCC1_PE0_Pad97 = Net("unconnected-(FCC1-PE0-Pad97)")
net_unconnected_FCC1_PE1_Pad98 = Net("unconnected-(FCC1-PE1-Pad98)")
net_unconnected_FCC1_PE10_Pad40 = Net("unconnected-(FCC1-PE10-Pad40)")
net_unconnected_FCC1_PE11_Pad41 = Net("unconnected-(FCC1-PE11-Pad41)")
net_unconnected_FCC1_PE12_Pad42 = Net("unconnected-(FCC1-PE12-Pad42)")
net_unconnected_FCC1_PE13_Pad43 = Net("unconnected-(FCC1-PE13-Pad43)")
net_unconnected_FCC1_PE14_Pad44 = Net("unconnected-(FCC1-PE14-Pad44)")
net_unconnected_FCC1_PE15_Pad45 = Net("unconnected-(FCC1-PE15-Pad45)")
net_unconnected_FCC1_PE2_Pad1 = Net("unconnected-(FCC1-PE2-Pad1)")
net_unconnected_FCC1_PE3_Pad2 = Net("unconnected-(FCC1-PE3-Pad2)")
net_unconnected_FCC1_PE4_Pad3 = Net("unconnected-(FCC1-PE4-Pad3)")
net_unconnected_FCC1_PE5_Pad4 = Net("unconnected-(FCC1-PE5-Pad4)")
net_unconnected_FCC1_PE8_Pad38 = Net("unconnected-(FCC1-PE8-Pad38)")
net_unconnected_FCC1_PE9_Pad39 = Net("unconnected-(FCC1-PE9-Pad39)")
net_unconnected_FCC1_VBAT_Pad6 = Net("unconnected-(FCC1-VBAT-Pad6)")
net_unconnected_FCC1_VDD_Pad100 = Net("unconnected-(FCC1-VDD-Pad100)")
net_unconnected_FCC1_VDD_Pad11 = Net("unconnected-(FCC1-VDD-Pad11)")
net_unconnected_FCC1_VDD_Pad27 = Net("unconnected-(FCC1-VDD-Pad27)")
net_unconnected_FCC1_VDD_Pad50 = Net("unconnected-(FCC1-VDD-Pad50)")
net_unconnected_FCC1_VDD_Pad75 = Net("unconnected-(FCC1-VDD-Pad75)")
net_unconnected_FCC1_VDDA_Pad21 = Net("unconnected-(FCC1-VDDA-Pad21)")
net_unconnected_FCC1_VREF_Pad20 = Net("unconnected-(FCC1-VREF+-Pad20)")
net_unconnected_GPS_BAT1_Pin_1_Pad1 = Net("unconnected-(GPS_BAT1-Pin_1-Pad1)")
net_unconnected_JP4_A_Pad1 = Net("unconnected-(JP4-A-Pad1)")
net_unconnected_JP4_B_Pad3 = Net("unconnected-(JP4-B-Pad3)")
net_unconnected_NAVC1_BOOT0_Pad60 = Net("unconnected-(NAVC1-BOOT0-Pad60)")
net_unconnected_NAVC1_NRST_Pad7 = Net("unconnected-(NAVC1-NRST-Pad7)")
net_unconnected_NAVC1_PA0_Pad14 = Net("unconnected-(NAVC1-PA0-Pad14)")
net_unconnected_NAVC1_PA1_Pad15 = Net("unconnected-(NAVC1-PA1-Pad15)")
net_unconnected_NAVC1_PA10_Pad43 = Net("unconnected-(NAVC1-PA10-Pad43)")
net_unconnected_NAVC1_PA11_Pad44 = Net("unconnected-(NAVC1-PA11-Pad44)")
net_unconnected_NAVC1_PA12_Pad45 = Net("unconnected-(NAVC1-PA12-Pad45)")
net_unconnected_NAVC1_PA13_Pad46 = Net("unconnected-(NAVC1-PA13-Pad46)")
net_unconnected_NAVC1_PA14_Pad49 = Net("unconnected-(NAVC1-PA14-Pad49)")
net_unconnected_NAVC1_PA15_Pad50 = Net("unconnected-(NAVC1-PA15-Pad50)")
net_unconnected_NAVC1_PA2_Pad16 = Net("unconnected-(NAVC1-PA2-Pad16)")
net_unconnected_NAVC1_PA3_Pad17 = Net("unconnected-(NAVC1-PA3-Pad17)")
net_unconnected_NAVC1_PA4_Pad20 = Net("unconnected-(NAVC1-PA4-Pad20)")
net_unconnected_NAVC1_PA5_Pad21 = Net("unconnected-(NAVC1-PA5-Pad21)")
net_unconnected_NAVC1_PA6_Pad22 = Net("unconnected-(NAVC1-PA6-Pad22)")
net_unconnected_NAVC1_PA7_Pad23 = Net("unconnected-(NAVC1-PA7-Pad23)")
net_unconnected_NAVC1_PA8_Pad41 = Net("unconnected-(NAVC1-PA8-Pad41)")
net_unconnected_NAVC1_PA9_Pad42 = Net("unconnected-(NAVC1-PA9-Pad42)")
net_unconnected_NAVC1_PB0_Pad26 = Net("unconnected-(NAVC1-PB0-Pad26)")
net_unconnected_NAVC1_PB1_Pad27 = Net("unconnected-(NAVC1-PB1-Pad27)")
net_unconnected_NAVC1_PB10_Pad29 = Net("unconnected-(NAVC1-PB10-Pad29)")
net_unconnected_NAVC1_PB11_Pad30 = Net("unconnected-(NAVC1-PB11-Pad30)")
net_unconnected_NAVC1_PB12_Pad33 = Net("unconnected-(NAVC1-PB12-Pad33)")
net_unconnected_NAVC1_PB13_Pad34 = Net("unconnected-(NAVC1-PB13-Pad34)")
net_unconnected_NAVC1_PB14_Pad35 = Net("unconnected-(NAVC1-PB14-Pad35)")
net_unconnected_NAVC1_PB15_Pad36 = Net("unconnected-(NAVC1-PB15-Pad36)")
net_unconnected_NAVC1_PB2_Pad28 = Net("unconnected-(NAVC1-PB2-Pad28)")
net_unconnected_NAVC1_PB3_Pad55 = Net("unconnected-(NAVC1-PB3-Pad55)")
net_unconnected_NAVC1_PB4_Pad56 = Net("unconnected-(NAVC1-PB4-Pad56)")
net_unconnected_NAVC1_PB5_Pad57 = Net("unconnected-(NAVC1-PB5-Pad57)")
net_unconnected_NAVC1_PB6_Pad58 = Net("unconnected-(NAVC1-PB6-Pad58)")
net_unconnected_NAVC1_PB7_Pad59 = Net("unconnected-(NAVC1-PB7-Pad59)")
net_unconnected_NAVC1_PB8_Pad61 = Net("unconnected-(NAVC1-PB8-Pad61)")
net_unconnected_NAVC1_PB9_Pad62 = Net("unconnected-(NAVC1-PB9-Pad62)")
net_unconnected_NAVC1_PC0_Pad8 = Net("unconnected-(NAVC1-PC0-Pad8)")
net_unconnected_NAVC1_PC1_Pad9 = Net("unconnected-(NAVC1-PC1-Pad9)")
net_unconnected_NAVC1_PC10_Pad51 = Net("unconnected-(NAVC1-PC10-Pad51)")
net_unconnected_NAVC1_PC11_Pad52 = Net("unconnected-(NAVC1-PC11-Pad52)")
net_unconnected_NAVC1_PC12_Pad53 = Net("unconnected-(NAVC1-PC12-Pad53)")
net_unconnected_NAVC1_PC13_Pad2 = Net("unconnected-(NAVC1-PC13-Pad2)")
net_unconnected_NAVC1_PC14_Pad3 = Net("unconnected-(NAVC1-PC14-Pad3)")
net_unconnected_NAVC1_PC15_Pad4 = Net("unconnected-(NAVC1-PC15-Pad4)")
net_unconnected_NAVC1_PC2_Pad10 = Net("unconnected-(NAVC1-PC2-Pad10)")
net_unconnected_NAVC1_PC3_Pad11 = Net("unconnected-(NAVC1-PC3-Pad11)")
net_unconnected_NAVC1_PC4_Pad24 = Net("unconnected-(NAVC1-PC4-Pad24)")
net_unconnected_NAVC1_PC5_Pad25 = Net("unconnected-(NAVC1-PC5-Pad25)")
net_unconnected_NAVC1_PC6_Pad37 = Net("unconnected-(NAVC1-PC6-Pad37)")
net_unconnected_NAVC1_PC7_Pad38 = Net("unconnected-(NAVC1-PC7-Pad38)")
net_unconnected_NAVC1_PC8_Pad39 = Net("unconnected-(NAVC1-PC8-Pad39)")
net_unconnected_NAVC1_PC9_Pad40 = Net("unconnected-(NAVC1-PC9-Pad40)")
net_unconnected_NAVC1_PD2_Pad54 = Net("unconnected-(NAVC1-PD2-Pad54)")
net_unconnected_NAVC1_VCAP_1_Pad31 = Net("unconnected-(NAVC1-VCAP_1-Pad31)")
net_unconnected_NAVC1_VCAP_2_Pad47 = Net("unconnected-(NAVC1-VCAP_2-Pad47)")
net_unconnected_NAVC1_VDD_Pad19 = Net("unconnected-(NAVC1-VDD-Pad19)")
net_unconnected_NAVC1_VDD_Pad32 = Net("unconnected-(NAVC1-VDD-Pad32)")
net_unconnected_NAVC1_VDD_Pad48 = Net("unconnected-(NAVC1-VDD-Pad48)")
net_unconnected_NAVC1_VDD_Pad64 = Net("unconnected-(NAVC1-VDD-Pad64)")
net_unconnected_NAVC1_VSSA_Pad12 = Net("unconnected-(NAVC1-VSSA-Pad12)")
net_unconnected_REG1_NC_Pad3 = Net("unconnected-(REG1-NC-Pad3)")
net_unconnected_REG2_PG_Pad4 = Net("unconnected-(REG2-PG-Pad4)")
net_unconnected_SWD1_Pin_6_Pad6 = Net("unconnected-(SWD1-Pin_6-Pad6)")
net_unconnected_SWD1_Pin_7_Pad7 = Net("unconnected-(SWD1-Pin_7-Pad7)")
net_unconnected_SWD1_Pin_8_Pad8 = Net("unconnected-(SWD1-Pin_8-Pad8)")
net_unconnected_SWD2_Pin_6_Pad6 = Net("unconnected-(SWD2-Pin_6-Pad6)")
net_unconnected_SWD2_Pin_7_Pad7 = Net("unconnected-(SWD2-Pin_7-Pad7)")
net_unconnected_SWD2_Pin_8_Pad8 = Net("unconnected-(SWD2-Pin_8-Pad8)")
net_unconnected_U10_EXTINT_Pad5 = Net("unconnected-(U10-EXTINT-Pad5)")
net_unconnected_U10_RES_Pad15 = Net("unconnected-(U10-RES-Pad15)")
net_unconnected_U10_SCL_Pad17 = Net("unconnected-(U10-SCL-Pad17)")
net_unconnected_U10_SDA_Pad16 = Net("unconnected-(U10-SDA-Pad16)")
net_unconnected_U2_EXTCLK_Pad25 = Net("unconnected-(U2-EXTCLK-Pad25)")
net_unconnected_U2_LED10_Pad17 = Net("unconnected-(U2-LED10-Pad17)")
net_unconnected_U2_LED11_Pad18 = Net("unconnected-(U2-LED11-Pad18)")
net_unconnected_U2_LED12_Pad19 = Net("unconnected-(U2-LED12-Pad19)")
net_unconnected_U2_LED13_Pad20 = Net("unconnected-(U2-LED13-Pad20)")
net_unconnected_U2_LED14_Pad21 = Net("unconnected-(U2-LED14-Pad21)")
net_unconnected_U2_LED15_Pad22 = Net("unconnected-(U2-LED15-Pad22)")
net_unconnected_U2_LED8_Pad15 = Net("unconnected-(U2-LED8-Pad15)")
net_unconnected_U2_LED9_Pad16 = Net("unconnected-(U2-LED9-Pad16)")
net_unconnected_U3_NC_Pad5 = Net("unconnected-(U3-NC-Pad5)")
net_unconnected_U5_CSB2_Pad5 = Net("unconnected-(U5-CSB2-Pad5)")
net_unconnected_U5_INT2_Pad1 = Net("unconnected-(U5-INT2-Pad1)")
net_unconnected_U5_INT4_Pad13 = Net("unconnected-(U5-INT4-Pad13)")
net_unconnected_U7_MISO_Pad7 = Net("unconnected-(U7-MISO-Pad7)")
net_unconnected_U7_SS_Pad1 = Net("unconnected-(U7-SS-Pad1)")
net_unconnected_U8_NC_1_Pad2 = Net("unconnected-(U8-NC_1-Pad2)")
net_unconnected_U8_NC_2_Pad11 = Net("unconnected-(U8-NC_2-Pad11)")
net_unconnected_U8_NC_3_Pad12 = Net("unconnected-(U8-NC_3-Pad12)")
net_unconnected_U9_NC_Pad5 = Net("unconnected-(U9-NC-Pad5)")
net_unconnected_USB3_D_Pad3 = Net("unconnected-(USB3-D+-Pad3)")
net_unconnected_USB3_D_Pad2 = Net("unconnected-(USB3-D--Pad2)")
net_unconnected_USB3_ID_Pad4 = Net("unconnected-(USB3-ID-Pad4)")
net_unconnected_USB4_D_Pad3 = Net("unconnected-(USB4-D+-Pad3)")
net_unconnected_USB4_D_Pad2 = Net("unconnected-(USB4-D--Pad2)")
net_unconnected_USB4_ID_Pad4 = Net("unconnected-(USB4-ID-Pad4)")

# ── Components ────────────────────────────────────────────────
# BAT1 - XT60-M
BAT1_tmpl = Part(tool=SKIDL, name="XT60-M", footprint="XT60-M:AMASS_XT60-M",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
BAT1 = BAT1_tmpl()
BAT1.ref = "BAT1"
BAT1.value = "XT60-M"

# C1 - 100u
C1_tmpl = Part(tool=SKIDL, name="100u", footprint="Capacitor_SMD:C_Elec_6.3x7.7",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C1 = C1_tmpl()
C1.ref = "C1"
C1.value = "100u"

# C2 - 47u
C2_tmpl = Part(tool=SKIDL, name="47u", footprint="Capacitor_SMD:C_1210_3225Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C2 = C2_tmpl()
C2.ref = "C2"
C2.value = "47u"

# C3 - 2u2
C3_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C3 = C3_tmpl()
C3.ref = "C3"
C3.value = "2u2"

# C4 - 2u2
C4_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C4 = C4_tmpl()
C4.ref = "C4"
C4.value = "2u2"

# C5 - 100n
C5_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C5 = C5_tmpl()
C5.ref = "C5"
C5.value = "100n"

# C6 - 100n
C6_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C6 = C6_tmpl()
C6.ref = "C6"
C6.value = "100n"

# C7 - 4n7
C7_tmpl = Part(tool=SKIDL, name="4n7", footprint="Capacitor_SMD:C_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C7 = C7_tmpl()
C7.ref = "C7"
C7.value = "4n7"

# C8 - 100u
C8_tmpl = Part(tool=SKIDL, name="100u", footprint="Capacitor_SMD:C_Elec_6.3x7.7",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C8 = C8_tmpl()
C8.ref = "C8"
C8.value = "100u"

# C9 - 47u
C9_tmpl = Part(tool=SKIDL, name="47u", footprint="Capacitor_SMD:C_1210_3225Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C9 = C9_tmpl()
C9.ref = "C9"
C9.value = "47u"

# C10 - 100n
C10_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C10 = C10_tmpl()
C10.ref = "C10"
C10.value = "100n"

# C11 - 10u
C11_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C11 = C11_tmpl()
C11.ref = "C11"
C11.value = "10u"

# C12 - 10u
C12_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C12 = C12_tmpl()
C12.ref = "C12"
C12.value = "10u"

# D1 - SD103AWS
D1_tmpl = Part(tool=SKIDL, name="SD103AWS", footprint="Diode_SMD:D_SOD-323",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D1 = D1_tmpl()
D1.ref = "D1"
D1.value = "SD103AWS"

# L1 - 15u
L1_tmpl = Part(tool=SKIDL, name="15u", footprint="SRP1265A-150M:INDPM135125X650N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
L1 = L1_tmpl()
L1.ref = "L1"
L1.value = "15u"

# LED1 - G
LED1_tmpl = Part(tool=SKIDL, name="G", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED1 = LED1_tmpl()
LED1.ref = "LED1"
LED1.value = "G"

# LED2 - G
LED2_tmpl = Part(tool=SKIDL, name="G", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED2 = LED2_tmpl()
LED2.ref = "LED2"
LED2.value = "G"

# R1 - 0.01
R1_tmpl = Part(tool=SKIDL, name="0.01", footprint="Resistor_SMD:R_2512_6332Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R1 = R1_tmpl()
R1.ref = "R1"
R1.value = "0.01"

# R2 - 10k
R2_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R2 = R2_tmpl()
R2.ref = "R2"
R2.value = "10k"

# R3 - 10k
R3_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R3 = R3_tmpl()
R3.ref = "R3"
R3.value = "10k"

# R4 - 19k6
R4_tmpl = Part(tool=SKIDL, name="19k6", footprint="Resistor_SMD:R_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R4 = R4_tmpl()
R4.ref = "R4"
R4.value = "19k6"

# R5 - 6k8
R5_tmpl = Part(tool=SKIDL, name="6k8", footprint="Resistor_SMD:R_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R5 = R5_tmpl()
R5.ref = "R5"
R5.value = "6k8"

# R6 - 1k3
R6_tmpl = Part(tool=SKIDL, name="1k3", footprint="Resistor_SMD:R_0805_2012Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R6 = R6_tmpl()
R6.ref = "R6"
R6.value = "1k3"

# R7 - 560
R7_tmpl = Part(tool=SKIDL, name="560", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R7 = R7_tmpl()
R7.ref = "R7"
R7.value = "560"

# R8 - 240
R8_tmpl = Part(tool=SKIDL, name="240", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R8 = R8_tmpl()
R8.ref = "R8"
R8.value = "240"

# REG1 - MIC26903YJL-TR
REG1_tmpl = Part(tool=SKIDL, name="MIC26903YJL-TR", footprint="MIC26903YJL-TR:MIC24054YJLTR",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN), Pin(num="21", func=Pin.types.PWRIN), Pin(num="22", func=Pin.types.PWRIN), Pin(num="23", func=Pin.types.PWRIN), Pin(num="24", func=Pin.types.PWRIN), Pin(num="25", func=Pin.types.PWRIN), Pin(num="26", func=Pin.types.PWRIN), Pin(num="27", func=Pin.types.PWRIN), Pin(num="28", func=Pin.types.PWRIN), Pin(num="29", func=Pin.types.PWRIN), Pin(num="30", func=Pin.types.PWRIN), Pin(num="31", func=Pin.types.PWRIN)], dest=TEMPLATE)
REG1 = REG1_tmpl()
REG1.ref = "REG1"
REG1.value = "MIC26903YJL-TR"

# REG2 - LD39200PU33R
REG2_tmpl = Part(tool=SKIDL, name="LD39200PU33R", footprint="LD39200PU33R:SON95P300X300X100-7N-D",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN)], dest=TEMPLATE)
REG2 = REG2_tmpl()
REG2.ref = "REG2"
REG2.value = "LD39200PU33R"

# U1 - INA219AIDCNR
U1_tmpl = Part(tool=SKIDL, name="INA219AIDCNR", footprint="INA219AIDCNR:SOT65P280X145-8N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
U1 = U1_tmpl()
U1.ref = "U1"
U1.value = "INA219AIDCNR"

# C13 - 2u2
C13_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C13 = C13_tmpl()
C13.ref = "C13"
C13.value = "2u2"

# C14 - 2u2
C14_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C14 = C14_tmpl()
C14.ref = "C14"
C14.value = "2u2"

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

# C26 - 100n
C26_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C26 = C26_tmpl()
C26.ref = "C26"
C26.value = "100n"

# C28 - 100n
C28_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C28 = C28_tmpl()
C28.ref = "C28"
C28.value = "100n"

# C30 - 100n
C30_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C30 = C30_tmpl()
C30.ref = "C30"
C30.value = "100n"

# C31 - 100n
C31_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C31 = C31_tmpl()
C31.ref = "C31"
C31.value = "100n"

# C32 - 10p
C32_tmpl = Part(tool=SKIDL, name="10p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C32 = C32_tmpl()
C32.ref = "C32"
C32.value = "10p"

# C33 - 10p
C33_tmpl = Part(tool=SKIDL, name="10p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C33 = C33_tmpl()
C33.ref = "C33"
C33.value = "10p"

# FCC1 - STM32H753VITx
FCC1_tmpl = Part(tool=SKIDL, name="STM32H753VITx", footprint="Package_QFP:LQFP-100_14x14mm_P0.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN), Pin(num="21", func=Pin.types.PWRIN), Pin(num="22", func=Pin.types.PWRIN), Pin(num="23", func=Pin.types.PWRIN), Pin(num="24", func=Pin.types.PWRIN), Pin(num="25", func=Pin.types.PWRIN), Pin(num="26", func=Pin.types.PWRIN), Pin(num="27", func=Pin.types.PWRIN), Pin(num="28", func=Pin.types.PWRIN), Pin(num="29", func=Pin.types.PWRIN), Pin(num="30", func=Pin.types.PWRIN), Pin(num="31", func=Pin.types.PWRIN), Pin(num="32", func=Pin.types.PWRIN), Pin(num="33", func=Pin.types.PWRIN), Pin(num="34", func=Pin.types.PWRIN), Pin(num="35", func=Pin.types.PWRIN), Pin(num="36", func=Pin.types.PWRIN), Pin(num="37", func=Pin.types.PWRIN), Pin(num="38", func=Pin.types.PWRIN), Pin(num="39", func=Pin.types.PWRIN), Pin(num="40", func=Pin.types.PWRIN), Pin(num="41", func=Pin.types.PWRIN), Pin(num="42", func=Pin.types.PWRIN), Pin(num="43", func=Pin.types.PWRIN), Pin(num="44", func=Pin.types.PWRIN), Pin(num="45", func=Pin.types.PWRIN), Pin(num="46", func=Pin.types.PWRIN), Pin(num="47", func=Pin.types.PWRIN), Pin(num="48", func=Pin.types.PWRIN), Pin(num="49", func=Pin.types.PWRIN), Pin(num="50", func=Pin.types.PWRIN), Pin(num="51", func=Pin.types.PWRIN), Pin(num="52", func=Pin.types.PWRIN), Pin(num="53", func=Pin.types.PWRIN), Pin(num="54", func=Pin.types.PWRIN), Pin(num="55", func=Pin.types.PWRIN), Pin(num="56", func=Pin.types.PWRIN), Pin(num="57", func=Pin.types.PWRIN), Pin(num="58", func=Pin.types.PWRIN), Pin(num="59", func=Pin.types.PWRIN), Pin(num="60", func=Pin.types.PWRIN), Pin(num="61", func=Pin.types.PWRIN), Pin(num="62", func=Pin.types.PWRIN), Pin(num="63", func=Pin.types.PWRIN), Pin(num="64", func=Pin.types.PWRIN), Pin(num="65", func=Pin.types.PWRIN), Pin(num="66", func=Pin.types.PWRIN), Pin(num="67", func=Pin.types.PWRIN), Pin(num="68", func=Pin.types.PWRIN), Pin(num="69", func=Pin.types.PWRIN), Pin(num="70", func=Pin.types.PWRIN), Pin(num="71", func=Pin.types.PWRIN), Pin(num="72", func=Pin.types.PWRIN), Pin(num="73", func=Pin.types.PWRIN), Pin(num="74", func=Pin.types.PWRIN), Pin(num="75", func=Pin.types.PWRIN), Pin(num="76", func=Pin.types.PWRIN), Pin(num="77", func=Pin.types.PWRIN), Pin(num="78", func=Pin.types.PWRIN), Pin(num="79", func=Pin.types.PWRIN), Pin(num="80", func=Pin.types.PWRIN), Pin(num="81", func=Pin.types.PWRIN), Pin(num="82", func=Pin.types.PWRIN), Pin(num="83", func=Pin.types.PWRIN), Pin(num="84", func=Pin.types.PWRIN), Pin(num="85", func=Pin.types.PWRIN), Pin(num="86", func=Pin.types.PWRIN), Pin(num="87", func=Pin.types.PWRIN), Pin(num="88", func=Pin.types.PWRIN), Pin(num="89", func=Pin.types.PWRIN), Pin(num="90", func=Pin.types.PWRIN), Pin(num="91", func=Pin.types.PWRIN), Pin(num="92", func=Pin.types.PWRIN), Pin(num="93", func=Pin.types.PWRIN), Pin(num="94", func=Pin.types.PWRIN), Pin(num="95", func=Pin.types.PWRIN), Pin(num="96", func=Pin.types.PWRIN), Pin(num="97", func=Pin.types.PWRIN), Pin(num="98", func=Pin.types.PWRIN), Pin(num="99", func=Pin.types.PWRIN), Pin(num="100", func=Pin.types.PWRIN)], dest=TEMPLATE)
FCC1 = FCC1_tmpl()
FCC1.ref = "FCC1"
FCC1.value = "STM32H753VITx"

# HSE1 - 25MHz
HSE1_tmpl = Part(tool=SKIDL, name="25MHz", footprint="Crystal:Crystal_SMD_Abracon_ABM8G-4Pin_3.2x2.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
HSE1 = HSE1_tmpl()
HSE1.ref = "HSE1"
HSE1.value = "25MHz"

# LED3 - R
LED3_tmpl = Part(tool=SKIDL, name="R", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED3 = LED3_tmpl()
LED3.ref = "LED3"
LED3.value = "R"

# LED4 - R
LED4_tmpl = Part(tool=SKIDL, name="R", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED4 = LED4_tmpl()
LED4.ref = "LED4"
LED4.value = "R"

# LED5 - Y
LED5_tmpl = Part(tool=SKIDL, name="Y", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED5 = LED5_tmpl()
LED5.ref = "LED5"
LED5.value = "Y"

# LED6 - B
LED6_tmpl = Part(tool=SKIDL, name="B", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED6 = LED6_tmpl()
LED6.ref = "LED6"
LED6.value = "B"

# LED7 - B
LED7_tmpl = Part(tool=SKIDL, name="B", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED7 = LED7_tmpl()
LED7.ref = "LED7"
LED7.value = "B"

# LED8 - B
LED8_tmpl = Part(tool=SKIDL, name="B", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED8 = LED8_tmpl()
LED8.ref = "LED8"
LED8.value = "B"

# R9 - 4k7
R9_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R9 = R9_tmpl()
R9.ref = "R9"
R9.value = "4k7"

# R10 - 4k7
R10_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R10 = R10_tmpl()
R10.ref = "R10"
R10.value = "4k7"

# R11 - 4k7
R11_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R11 = R11_tmpl()
R11.ref = "R11"
R11.value = "4k7"

# R12 - 4k7
R12_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R12 = R12_tmpl()
R12.ref = "R12"
R12.value = "4k7"

# R13 - 4k7
R13_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R13 = R13_tmpl()
R13.ref = "R13"
R13.value = "4k7"

# R14 - 4k7
R14_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R14 = R14_tmpl()
R14.ref = "R14"
R14.value = "4k7"

# R15 - 330
R15_tmpl = Part(tool=SKIDL, name="330", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R15 = R15_tmpl()
R15.ref = "R15"
R15.value = "330"

# R16 - 330
R16_tmpl = Part(tool=SKIDL, name="330", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R16 = R16_tmpl()
R16.ref = "R16"
R16.value = "330"

# R17 - 330
R17_tmpl = Part(tool=SKIDL, name="330", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R17 = R17_tmpl()
R17.ref = "R17"
R17.value = "330"

# R18 - 100
R18_tmpl = Part(tool=SKIDL, name="100", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R18 = R18_tmpl()
R18.ref = "R18"
R18.value = "100"

# R19 - 100
R19_tmpl = Part(tool=SKIDL, name="100", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R19 = R19_tmpl()
R19.ref = "R19"
R19.value = "100"

# R20 - 100
R20_tmpl = Part(tool=SKIDL, name="100", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R20 = R20_tmpl()
R20.ref = "R20"
R20.value = "100"

# R21 - 47
R21_tmpl = Part(tool=SKIDL, name="47", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R21 = R21_tmpl()
R21.ref = "R21"
R21.value = "47"

# R22 - 10k
R22_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R22 = R22_tmpl()
R22.ref = "R22"
R22.value = "10k"

# R23 - 620
R23_tmpl = Part(tool=SKIDL, name="620", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R23 = R23_tmpl()
R23.ref = "R23"
R23.value = "620"

# SW1 - SKRPANE010
SW1_tmpl = Part(tool=SKIDL, name="SKRPANE010", footprint="SKRPANE010:SKRPADE010",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
SW1 = SW1_tmpl()
SW1.ref = "SW1"
SW1.value = "SKRPANE010"

# SW2 - TDD01H0SB1R
SW2_tmpl = Part(tool=SKIDL, name="TDD01H0SB1R", footprint="TDD01H0SB1R:SOT175P420X230-3N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
SW2 = SW2_tmpl()
SW2.ref = "SW2"
SW2.value = "TDD01H0SB1R"

# TP1 - I2C1
TP1_tmpl = Part(tool=SKIDL, name="I2C1", footprint="TestPoint:TestPoint_Pad_D1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
TP1 = TP1_tmpl()
TP1.ref = "TP1"
TP1.value = "I2C1"

# TP2 - I2C1
TP2_tmpl = Part(tool=SKIDL, name="I2C1", footprint="TestPoint:TestPoint_Pad_D1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
TP2 = TP2_tmpl()
TP2.ref = "TP2"
TP2.value = "I2C1"

# C37 - 2u2
C37_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C37 = C37_tmpl()
C37.ref = "C37"
C37.value = "2u2"

# C38 - 2u2
C38_tmpl = Part(tool=SKIDL, name="2u2", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C38 = C38_tmpl()
C38.ref = "C38"
C38.value = "2u2"

# C40 - 100n
C40_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C40 = C40_tmpl()
C40.ref = "C40"
C40.value = "100n"

# C41 - 100n
C41_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C41 = C41_tmpl()
C41.ref = "C41"
C41.value = "100n"

# C42 - 100n
C42_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C42 = C42_tmpl()
C42.ref = "C42"
C42.value = "100n"

# C43 - 100n
C43_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C43 = C43_tmpl()
C43.ref = "C43"
C43.value = "100n"

# C44 - 100n
C44_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C44 = C44_tmpl()
C44.ref = "C44"
C44.value = "100n"

# C45 - 100n
C45_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C45 = C45_tmpl()
C45.ref = "C45"
C45.value = "100n"

# C46 - 100n
C46_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C46 = C46_tmpl()
C46.ref = "C46"
C46.value = "100n"

# C47 - 100n
C47_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C47 = C47_tmpl()
C47.ref = "C47"
C47.value = "100n"

# C48 - 100n
C48_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C48 = C48_tmpl()
C48.ref = "C48"
C48.value = "100n"

# C49 - 100n
C49_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C49 = C49_tmpl()
C49.ref = "C49"
C49.value = "100n"

# C51 - 100n
C51_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C51 = C51_tmpl()
C51.ref = "C51"
C51.value = "100n"

# C52 - 10p
C52_tmpl = Part(tool=SKIDL, name="10p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C52 = C52_tmpl()
C52.ref = "C52"
C52.value = "10p"

# C53 - 10p
C53_tmpl = Part(tool=SKIDL, name="10p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C53 = C53_tmpl()
C53.ref = "C53"
C53.value = "10p"

# HSE2 - 25MHz
HSE2_tmpl = Part(tool=SKIDL, name="25MHz", footprint="Crystal:Crystal_SMD_Abracon_ABM8G-4Pin_3.2x2.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
HSE2 = HSE2_tmpl()
HSE2.ref = "HSE2"
HSE2.value = "25MHz"

# LED9 - R
LED9_tmpl = Part(tool=SKIDL, name="R", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED9 = LED9_tmpl()
LED9.ref = "LED9"
LED9.value = "R"

# LED10 - R
LED10_tmpl = Part(tool=SKIDL, name="R", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED10 = LED10_tmpl()
LED10.ref = "LED10"
LED10.value = "R"

# LED11 - Y
LED11_tmpl = Part(tool=SKIDL, name="Y", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED11 = LED11_tmpl()
LED11.ref = "LED11"
LED11.value = "Y"

# LED12 - B
LED12_tmpl = Part(tool=SKIDL, name="B", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED12 = LED12_tmpl()
LED12.ref = "LED12"
LED12.value = "B"

# NAVC1 - STM32F405RGTx
NAVC1_tmpl = Part(tool=SKIDL, name="STM32F405RGTx", footprint="Package_QFP:LQFP-64_10x10mm_P0.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN), Pin(num="21", func=Pin.types.PWRIN), Pin(num="22", func=Pin.types.PWRIN), Pin(num="23", func=Pin.types.PWRIN), Pin(num="24", func=Pin.types.PWRIN), Pin(num="25", func=Pin.types.PWRIN), Pin(num="26", func=Pin.types.PWRIN), Pin(num="27", func=Pin.types.PWRIN), Pin(num="28", func=Pin.types.PWRIN), Pin(num="29", func=Pin.types.PWRIN), Pin(num="30", func=Pin.types.PWRIN), Pin(num="31", func=Pin.types.PWRIN), Pin(num="32", func=Pin.types.PWRIN), Pin(num="33", func=Pin.types.PWRIN), Pin(num="34", func=Pin.types.PWRIN), Pin(num="35", func=Pin.types.PWRIN), Pin(num="36", func=Pin.types.PWRIN), Pin(num="37", func=Pin.types.PWRIN), Pin(num="38", func=Pin.types.PWRIN), Pin(num="39", func=Pin.types.PWRIN), Pin(num="40", func=Pin.types.PWRIN), Pin(num="41", func=Pin.types.PWRIN), Pin(num="42", func=Pin.types.PWRIN), Pin(num="43", func=Pin.types.PWRIN), Pin(num="44", func=Pin.types.PWRIN), Pin(num="45", func=Pin.types.PWRIN), Pin(num="46", func=Pin.types.PWRIN), Pin(num="47", func=Pin.types.PWRIN), Pin(num="48", func=Pin.types.PWRIN), Pin(num="49", func=Pin.types.PWRIN), Pin(num="50", func=Pin.types.PWRIN), Pin(num="51", func=Pin.types.PWRIN), Pin(num="52", func=Pin.types.PWRIN), Pin(num="53", func=Pin.types.PWRIN), Pin(num="54", func=Pin.types.PWRIN), Pin(num="55", func=Pin.types.PWRIN), Pin(num="56", func=Pin.types.PWRIN), Pin(num="57", func=Pin.types.PWRIN), Pin(num="58", func=Pin.types.PWRIN), Pin(num="59", func=Pin.types.PWRIN), Pin(num="60", func=Pin.types.PWRIN), Pin(num="61", func=Pin.types.PWRIN), Pin(num="62", func=Pin.types.PWRIN), Pin(num="63", func=Pin.types.PWRIN), Pin(num="64", func=Pin.types.PWRIN)], dest=TEMPLATE)
NAVC1 = NAVC1_tmpl()
NAVC1.ref = "NAVC1"
NAVC1.value = "STM32F405RGTx"

# R26 - 10k
R26_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R26 = R26_tmpl()
R26.ref = "R26"
R26.value = "10k"

# R27 - 10k
R27_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R27 = R27_tmpl()
R27.ref = "R27"
R27.value = "10k"

# R28 - 4k7
R28_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R28 = R28_tmpl()
R28.ref = "R28"
R28.value = "4k7"

# R29 - 4k7
R29_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R29 = R29_tmpl()
R29.ref = "R29"
R29.value = "4k7"

# R30 - 4k7
R30_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R30 = R30_tmpl()
R30.ref = "R30"
R30.value = "4k7"

# R31 - 4k7
R31_tmpl = Part(tool=SKIDL, name="4k7", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R31 = R31_tmpl()
R31.ref = "R31"
R31.value = "4k7"

# R32 - 620
R32_tmpl = Part(tool=SKIDL, name="620", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R32 = R32_tmpl()
R32.ref = "R32"
R32.value = "620"

# R33 - 330
R33_tmpl = Part(tool=SKIDL, name="330", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R33 = R33_tmpl()
R33.ref = "R33"
R33.value = "330"

# R34 - 330
R34_tmpl = Part(tool=SKIDL, name="330", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R34 = R34_tmpl()
R34.ref = "R34"
R34.value = "330"

# R35 - 330
R35_tmpl = Part(tool=SKIDL, name="330", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R35 = R35_tmpl()
R35.ref = "R35"
R35.value = "330"

# R36 - 100
R36_tmpl = Part(tool=SKIDL, name="100", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R36 = R36_tmpl()
R36.ref = "R36"
R36.value = "100"

# SW3 - TDD01H0SB1R
SW3_tmpl = Part(tool=SKIDL, name="TDD01H0SB1R", footprint="TDD01H0SB1R:SOT175P420X230-3N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
SW3 = SW3_tmpl()
SW3.ref = "SW3"
SW3.value = "TDD01H0SB1R"

# SW4 - TDD01H0SB1R
SW4_tmpl = Part(tool=SKIDL, name="TDD01H0SB1R", footprint="TDD01H0SB1R:SOT175P420X230-3N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
SW4 = SW4_tmpl()
SW4.ref = "SW4"
SW4.value = "TDD01H0SB1R"

# SW5 - SKRPANE010
SW5_tmpl = Part(tool=SKIDL, name="SKRPANE010", footprint="SKRPANE010:SKRPADE010",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
SW5 = SW5_tmpl()
SW5.ref = "SW5"
SW5.value = "SKRPANE010"

# TP3 - I2C1
TP3_tmpl = Part(tool=SKIDL, name="I2C1", footprint="TestPoint:TestPoint_Pad_D1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
TP3 = TP3_tmpl()
TP3.ref = "TP3"
TP3.value = "I2C1"

# TP4 - I2C1
TP4_tmpl = Part(tool=SKIDL, name="I2C1", footprint="TestPoint:TestPoint_Pad_D1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN)], dest=TEMPLATE)
TP4 = TP4_tmpl()
TP4.ref = "TP4"
TP4.value = "I2C1"

# C68 - 100n
C68_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C68 = C68_tmpl()
C68.ref = "C68"
C68.value = "100n"

# C69 - 100n
C69_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C69 = C69_tmpl()
C69.ref = "C69"
C69.value = "100n"

# C70 - 100n
C70_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C70 = C70_tmpl()
C70.ref = "C70"
C70.value = "100n"

# C71 - 100n
C71_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C71 = C71_tmpl()
C71.ref = "C71"
C71.value = "100n"

# D2 - SD103AWS
D2_tmpl = Part(tool=SKIDL, name="SD103AWS", footprint="Diode_SMD:D_SOD-323",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D2 = D2_tmpl()
D2.ref = "D2"
D2.value = "SD103AWS"

# D3 - SD103AWS
D3_tmpl = Part(tool=SKIDL, name="SD103AWS", footprint="Diode_SMD:D_SOD-323",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D3 = D3_tmpl()
D3.ref = "D3"
D3.value = "SD103AWS"

# D4 - SD103AWS
D4_tmpl = Part(tool=SKIDL, name="SD103AWS", footprint="Diode_SMD:D_SOD-323",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D4 = D4_tmpl()
D4.ref = "D4"
D4.value = "SD103AWS"

# D5 - SD103AWS
D5_tmpl = Part(tool=SKIDL, name="SD103AWS", footprint="Diode_SMD:D_SOD-323",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
D5 = D5_tmpl()
D5.ref = "D5"
D5.value = "SD103AWS"

# GPS_BAT1 - Conn_01x02
GPS_BAT1_tmpl = Part(tool=SKIDL, name="Conn_01x02", footprint="Connector_Molex:Molex_PicoBlade_53048-0210_1x02_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
GPS_BAT1 = GPS_BAT1_tmpl()
GPS_BAT1.ref = "GPS_BAT1"
GPS_BAT1.value = "Conn_01x02"

# JP1 - SolderJumper_2_Open
JP1_tmpl = Part(tool=SKIDL, name="SolderJumper_2_Open", footprint="Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
JP1 = JP1_tmpl()
JP1.ref = "JP1"
JP1.value = "SolderJumper_2_Open"

# JP2 - SolderJumper_2_Open
JP2_tmpl = Part(tool=SKIDL, name="SolderJumper_2_Open", footprint="Jumper:SolderJumper-2_P1.3mm_Open_RoundedPad1.0x1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
JP2 = JP2_tmpl()
JP2.ref = "JP2"
JP2.value = "SolderJumper_2_Open"

# JP4 - Jumper_3_Open
JP4_tmpl = Part(tool=SKIDL, name="Jumper_3_Open", footprint="Jumper:SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
JP4 = JP4_tmpl()
JP4.ref = "JP4"
JP4.value = "Jumper_3_Open"

# LED13 - G
LED13_tmpl = Part(tool=SKIDL, name="G", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED13 = LED13_tmpl()
LED13.ref = "LED13"
LED13.value = "G"

# LED14 - G
LED14_tmpl = Part(tool=SKIDL, name="G", footprint="LED_SMD:LED_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
LED14 = LED14_tmpl()
LED14.ref = "LED14"
LED14.value = "G"

# R40 - 10
R40_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R40 = R40_tmpl()
R40.ref = "R40"
R40.value = "10"

# R41 - 10
R41_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R41 = R41_tmpl()
R41.ref = "R41"
R41.value = "10"

# R42 - 10
R42_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R42 = R42_tmpl()
R42.ref = "R42"
R42.value = "10"

# R43 - 10
R43_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R43 = R43_tmpl()
R43.ref = "R43"
R43.value = "10"

# R44 - 10
R44_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R44 = R44_tmpl()
R44.ref = "R44"
R44.value = "10"

# R45 - 10
R45_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R45 = R45_tmpl()
R45.ref = "R45"
R45.value = "10"

# R46 - 10
R46_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R46 = R46_tmpl()
R46.ref = "R46"
R46.value = "10"

# R47 - 10
R47_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R47 = R47_tmpl()
R47.ref = "R47"
R47.value = "10"

# R48 - 10
R48_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R48 = R48_tmpl()
R48.ref = "R48"
R48.value = "10"

# R49 - 10
R49_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R49 = R49_tmpl()
R49.ref = "R49"
R49.value = "10"

# R50 - 0
R50_tmpl = Part(tool=SKIDL, name="0", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R50 = R50_tmpl()
R50.ref = "R50"
R50.value = "0"

# R51 - 0
R51_tmpl = Part(tool=SKIDL, name="0", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R51 = R51_tmpl()
R51.ref = "R51"
R51.value = "0"

# R52 - 22
R52_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R52 = R52_tmpl()
R52.ref = "R52"
R52.value = "22"

# R53 - 22
R53_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R53 = R53_tmpl()
R53.ref = "R53"
R53.value = "22"

# R54 - 560
R54_tmpl = Part(tool=SKIDL, name="560", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R54 = R54_tmpl()
R54.ref = "R54"
R54.value = "560"

# R55 - 22
R55_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R55 = R55_tmpl()
R55.ref = "R55"
R55.value = "22"

# R56 - 22
R56_tmpl = Part(tool=SKIDL, name="22", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R56 = R56_tmpl()
R56.ref = "R56"
R56.value = "22"

# R57 - 560
R57_tmpl = Part(tool=SKIDL, name="560", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R57 = R57_tmpl()
R57.ref = "R57"
R57.value = "560"

# R58 - 560
R58_tmpl = Part(tool=SKIDL, name="560", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R58 = R58_tmpl()
R58.ref = "R58"
R58.value = "560"

# R59 - 560
R59_tmpl = Part(tool=SKIDL, name="560", footprint="Resistor_SMD:R_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R59 = R59_tmpl()
R59.ref = "R59"
R59.value = "560"

# SWD1 - Conn_02x05_Odd_Even
SWD1_tmpl = Part(tool=SKIDL, name="Conn_02x05_Odd_Even", footprint="Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical_SMD",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN)], dest=TEMPLATE)
SWD1 = SWD1_tmpl()
SWD1.ref = "SWD1"
SWD1.value = "Conn_02x05_Odd_Even"

# SWD2 - Conn_02x05_Odd_Even
SWD2_tmpl = Part(tool=SKIDL, name="Conn_02x05_Odd_Even", footprint="Connector_PinHeader_1.27mm:PinHeader_2x05_P1.27mm_Vertical_SMD",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN)], dest=TEMPLATE)
SWD2 = SWD2_tmpl()
SWD2.ref = "SWD2"
SWD2.value = "Conn_02x05_Odd_Even"

# USB1 - USB_B_Micro
USB1_tmpl = Part(tool=SKIDL, name="USB_B_Micro", footprint="Connector_USB:USB_Micro-B_Wuerth_629105150521_CircularHoles",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="SH", func=Pin.types.PWRIN)], dest=TEMPLATE)
USB1 = USB1_tmpl()
USB1.ref = "USB1"
USB1.value = "USB_B_Micro"

# USB2 - USB_B_Micro
USB2_tmpl = Part(tool=SKIDL, name="USB_B_Micro", footprint="Connector_USB:USB_Micro-B_Wuerth_629105150521_CircularHoles",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="SH", func=Pin.types.PWRIN)], dest=TEMPLATE)
USB2 = USB2_tmpl()
USB2.ref = "USB2"
USB2.value = "USB_B_Micro"

# USB3 - USB_B_Micro
USB3_tmpl = Part(tool=SKIDL, name="USB_B_Micro", footprint="Connector_USB:USB_Micro-B_Wuerth_629105150521_CircularHoles",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="SH", func=Pin.types.PWRIN)], dest=TEMPLATE)
USB3 = USB3_tmpl()
USB3.ref = "USB3"
USB3.value = "USB_B_Micro"

# USB4 - USB_B_Micro
USB4_tmpl = Part(tool=SKIDL, name="USB_B_Micro", footprint="Connector_USB:USB_Micro-B_Wuerth_629105150521_CircularHoles",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="SH", func=Pin.types.PWRIN)], dest=TEMPLATE)
USB4 = USB4_tmpl()
USB4.ref = "USB4"
USB4.value = "USB_B_Micro"

# ADC_FCC1 - Conn_01x04
ADC_FCC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
ADC_FCC1 = ADC_FCC1_tmpl()
ADC_FCC1.ref = "ADC_FCC1"
ADC_FCC1.value = "Conn_01x04"

# C34 - 100n
C34_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C34 = C34_tmpl()
C34.ref = "C34"
C34.value = "100n"

# C35 - 100n
C35_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C35 = C35_tmpl()
C35.ref = "C35"
C35.value = "100n"

# C36 - 100n
C36_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C36 = C36_tmpl()
C36.ref = "C36"
C36.value = "100n"

# I2C3_FCC1 - Conn_01x04
I2C3_FCC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
I2C3_FCC1 = I2C3_FCC1_tmpl()
I2C3_FCC1.ref = "I2C3_FCC1"
I2C3_FCC1.value = "Conn_01x04"

# PWM_POW1 - Conn_02x08_Odd_Even
PWM_POW1_tmpl = Part(tool=SKIDL, name="Conn_02x08_Odd_Even", footprint="Connector_PinHeader_2.54mm:PinHeader_2x08_P2.54mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN)], dest=TEMPLATE)
PWM_POW1 = PWM_POW1_tmpl()
PWM_POW1.ref = "PWM_POW1"
PWM_POW1.value = "Conn_02x08_Odd_Even"

# PWM_SIG1 - 2.54mm
PWM_SIG1_tmpl = Part(tool=SKIDL, name="2.54mm", footprint="Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN)], dest=TEMPLATE)
PWM_SIG1 = PWM_SIG1_tmpl()
PWM_SIG1.ref = "PWM_SIG1"
PWM_SIG1.value = "2.54mm"

# R24 - 10k
R24_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R24 = R24_tmpl()
R24.ref = "R24"
R24.value = "10k"

# R25 - 10k
R25_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R25 = R25_tmpl()
R25.ref = "R25"
R25.value = "10k"

# RCIN_FCC1 - Conn_01x06
RCIN_FCC1_tmpl = Part(tool=SKIDL, name="Conn_01x06", footprint="Connector_Molex:Molex_PicoBlade_53048-0610_1x06_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
RCIN_FCC1 = RCIN_FCC1_tmpl()
RCIN_FCC1.ref = "RCIN_FCC1"
RCIN_FCC1.value = "Conn_01x06"

# U2 - PCA9685PW
U2_tmpl = Part(tool=SKIDL, name="PCA9685PW", footprint="Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN), Pin(num="19", func=Pin.types.PWRIN), Pin(num="20", func=Pin.types.PWRIN), Pin(num="21", func=Pin.types.PWRIN), Pin(num="22", func=Pin.types.PWRIN), Pin(num="23", func=Pin.types.PWRIN), Pin(num="24", func=Pin.types.PWRIN), Pin(num="25", func=Pin.types.PWRIN), Pin(num="26", func=Pin.types.PWRIN), Pin(num="27", func=Pin.types.PWRIN), Pin(num="28", func=Pin.types.PWRIN)], dest=TEMPLATE)
U2 = U2_tmpl()
U2.ref = "U2"
U2.value = "PCA9685PW"

# U3 - 24CW1280T-I_OT
U3_tmpl = Part(tool=SKIDL, name="24CW1280T-I_OT", footprint="24CW1280T-I_OT:SOT95P280X145-5N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN)], dest=TEMPLATE)
U3 = U3_tmpl()
U3.ref = "U3"
U3.value = "24CW1280T-I_OT"

# U4 - W25N01GVZEIG_TR
U4_tmpl = Part(tool=SKIDL, name="W25N01GVZEIG_TR", footprint="W25N01GVZEIG_TR:SON127P800X600X80-9N-D",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN)], dest=TEMPLATE)
U4 = U4_tmpl()
U4.ref = "U4"
U4.value = "W25N01GVZEIG_TR"

# UART3_FCC1 - Conn_01x04
UART3_FCC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
UART3_FCC1 = UART3_FCC1_tmpl()
UART3_FCC1.ref = "UART3_FCC1"
UART3_FCC1.value = "Conn_01x04"

# UART4_FCC1 - Conn_01x04
UART4_FCC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
UART4_FCC1 = UART4_FCC1_tmpl()
UART4_FCC1.ref = "UART4_FCC1"
UART4_FCC1.value = "Conn_01x04"

# UART5_FCC1 - Conn_01x04
UART5_FCC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
UART5_FCC1 = UART5_FCC1_tmpl()
UART5_FCC1.ref = "UART5_FCC1"
UART5_FCC1.value = "Conn_01x04"

# ANT1 - 5-1814832-1
ANT1_tmpl = Part(tool=SKIDL, name="5-1814832-1", footprint="5-1814832-1:TE_5-1814832-1",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN)], dest=TEMPLATE)
ANT1 = ANT1_tmpl()
ANT1.ref = "ANT1"
ANT1.value = "5-1814832-1"

# C54 - 100n
C54_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C54 = C54_tmpl()
C54.ref = "C54"
C54.value = "100n"

# C55 - 100n
C55_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C55 = C55_tmpl()
C55.ref = "C55"
C55.value = "100n"

# C56 - 100n
C56_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C56 = C56_tmpl()
C56.ref = "C56"
C56.value = "100n"

# C57 - 1n
C57_tmpl = Part(tool=SKIDL, name="1n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C57 = C57_tmpl()
C57.ref = "C57"
C57.value = "1n"

# C58 - 100n
C58_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C58 = C58_tmpl()
C58.ref = "C58"
C58.value = "100n"

# C59 - 220n
C59_tmpl = Part(tool=SKIDL, name="220n", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C59 = C59_tmpl()
C59.ref = "C59"
C59.value = "220n"

# C60 - 100n
C60_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C60 = C60_tmpl()
C60.ref = "C60"
C60.value = "100n"

# C61 - 100n
C61_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C61 = C61_tmpl()
C61.ref = "C61"
C61.value = "100n"

# C62 - 10u
C62_tmpl = Part(tool=SKIDL, name="10u", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C62 = C62_tmpl()
C62.ref = "C62"
C62.value = "10u"

# C63 - 100n
C63_tmpl = Part(tool=SKIDL, name="100n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C63 = C63_tmpl()
C63.ref = "C63"
C63.value = "100n"

# C64 - 1u
C64_tmpl = Part(tool=SKIDL, name="1u", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C64 = C64_tmpl()
C64.ref = "C64"
C64.value = "1u"

# C65 - 1u
C65_tmpl = Part(tool=SKIDL, name="1u", footprint="Capacitor_SMD:C_0603_1608Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C65 = C65_tmpl()
C65.ref = "C65"
C65.value = "1u"

# C66 - 22p
C66_tmpl = Part(tool=SKIDL, name="22p", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C66 = C66_tmpl()
C66.ref = "C66"
C66.value = "22p"

# C67 - 10n
C67_tmpl = Part(tool=SKIDL, name="10n", footprint="Capacitor_SMD:C_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
C67 = C67_tmpl()
C67.ref = "C67"
C67.value = "10n"

# GPS_NAVC1 - Conn_01x07
GPS_NAVC1_tmpl = Part(tool=SKIDL, name="Conn_01x07", footprint="Connector_Molex:Molex_PicoBlade_53048-0710_1x07_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN)], dest=TEMPLATE)
GPS_NAVC1 = GPS_NAVC1_tmpl()
GPS_NAVC1.ref = "GPS_NAVC1"
GPS_NAVC1.value = "Conn_01x07"

# I2C3_NAVC1 - Conn_01x04
I2C3_NAVC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
I2C3_NAVC1 = I2C3_NAVC1_tmpl()
I2C3_NAVC1.ref = "I2C3_NAVC1"
I2C3_NAVC1.value = "Conn_01x04"

# JP3 - SolderJumper_3_Open
JP3_tmpl = Part(tool=SKIDL, name="SolderJumper_3_Open", footprint="Jumper:SolderJumper-3_P1.3mm_Open_RoundedPad1.0x1.5mm",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN)], dest=TEMPLATE)
JP3 = JP3_tmpl()
JP3.ref = "JP3"
JP3.value = "SolderJumper_3_Open"

# L2 - 27n
L2_tmpl = Part(tool=SKIDL, name="27n", footprint="Inductor_SMD:L_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
L2 = L2_tmpl()
L2.ref = "L2"
L2.value = "27n"

# R37 - 10k
R37_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R37 = R37_tmpl()
R37.ref = "R37"
R37.value = "10k"

# R38 - 10k
R38_tmpl = Part(tool=SKIDL, name="10k", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R38 = R38_tmpl()
R38.ref = "R38"
R38.value = "10k"

# R39 - 10
R39_tmpl = Part(tool=SKIDL, name="10", footprint="Resistor_SMD:R_0402_1005Metric",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN)], dest=TEMPLATE)
R39 = R39_tmpl()
R39.ref = "R39"
R39.value = "10"

# U5 - BMI088
U5_tmpl = Part(tool=SKIDL, name="BMI088", footprint="BMI088:PQFN50P450X300X100-16N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN)], dest=TEMPLATE)
U5 = U5_tmpl()
U5.ref = "U5"
U5.value = "BMI088"

# U6 - TMP100
U6_tmpl = Part(tool=SKIDL, name="TMP100", footprint="Package_TO_SOT_SMD:SOT-23-6",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN)], dest=TEMPLATE)
U6 = U6_tmpl()
U6.ref = "U6"
U6.value = "TMP100"

# U7 - MPRLS0025PA00001A
U7_tmpl = Part(tool=SKIDL, name="MPRLS0025PA00001A", footprint="MPRLS0025PA00001A:XDCR_MPRLS0025PA00001A",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN)], dest=TEMPLATE)
U7 = U7_tmpl()
U7.ref = "U7"
U7.value = "MPRLS0025PA00001A"

# U8 - IIS2MDCTR
U8_tmpl = Part(tool=SKIDL, name="IIS2MDCTR", footprint="IIS2MDCTR:IIS2MDCTR",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN)], dest=TEMPLATE)
U8 = U8_tmpl()
U8.ref = "U8"
U8.value = "IIS2MDCTR"

# U9 - 24CW1280T-I_OT
U9_tmpl = Part(tool=SKIDL, name="24CW1280T-I_OT", footprint="24CW1280T-I_OT:SOT95P280X145-5N",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN)], dest=TEMPLATE)
U9 = U9_tmpl()
U9.ref = "U9"
U9.value = "24CW1280T-I_OT"

# U10 - u-blox MAX-8Q
U10_tmpl = Part(tool=SKIDL, name="u-blox MAX-8Q", footprint="MODULE-GPS-SMD-MAX-7Q-0_18P-9.6X10MM_:GPS18P-SMD-1.1-10X9.6MM",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN), Pin(num="5", func=Pin.types.PWRIN), Pin(num="6", func=Pin.types.PWRIN), Pin(num="7", func=Pin.types.PWRIN), Pin(num="8", func=Pin.types.PWRIN), Pin(num="9", func=Pin.types.PWRIN), Pin(num="10", func=Pin.types.PWRIN), Pin(num="11", func=Pin.types.PWRIN), Pin(num="12", func=Pin.types.PWRIN), Pin(num="13", func=Pin.types.PWRIN), Pin(num="14", func=Pin.types.PWRIN), Pin(num="15", func=Pin.types.PWRIN), Pin(num="16", func=Pin.types.PWRIN), Pin(num="17", func=Pin.types.PWRIN), Pin(num="18", func=Pin.types.PWRIN)], dest=TEMPLATE)
U10 = U10_tmpl()
U10.ref = "U10"
U10.value = "u-blox MAX-8Q"

# UART4_NAVC1 - Conn_01x04
UART4_NAVC1_tmpl = Part(tool=SKIDL, name="Conn_01x04", footprint="Connector_Molex:Molex_PicoBlade_53048-0410_1x04_P1.25mm_Horizontal",
    pins=[Pin(num="1", func=Pin.types.PWRIN), Pin(num="2", func=Pin.types.PWRIN), Pin(num="3", func=Pin.types.PWRIN), Pin(num="4", func=Pin.types.PWRIN)], dest=TEMPLATE)
UART4_NAVC1 = UART4_NAVC1_tmpl()
UART4_NAVC1.ref = "UART4_NAVC1"
UART4_NAVC1.value = "Conn_01x04"

# ── Connections ───────────────────────────────────────────────
BAT1["1"] += net_GND
BAT1["2"] += net_VIN

C1["1"] += net_REG_VIN
C1["2"] += net_GND

C2["1"] += net_REG_VIN
C2["2"] += net_GND

C3["1"] += net_Net_REG1_PVDD
C3["2"] += net_GND

C4["1"] += net_Net_D1_A
C4["2"] += net_GND

C5["1"] += net_REG_CS
C5["2"] += net_REG_BST

C6["1"] += net_REG_CS
C6["2"] += net_Net_C6_Pad2

C7["1"] += net_N_5V
C7["2"] += net_REG_FB

C8["1"] += net_N_5V
C8["2"] += net_GND

C9["1"] += net_N_5V
C9["2"] += net_GND

C10["1"] += net_N_3_3V
C10["2"] += net_GND

C11["1"] += net_N_5V
C11["2"] += net_GND

C12["1"] += net_N_3_3V
C12["2"] += net_GND

D1["1"] += net_REG_BST
D1["2"] += net_Net_D1_A

L1["1"] += net_REG_CS
L1["2"] += net_N_5V

LED1["1"] += net_Net_LED1_K
LED1["2"] += net_N_5V

LED2["1"] += net_Net_LED2_K
LED2["2"] += net_N_3_3V

R1["1"] += net_REG_VIN
R1["2"] += net_VIN

R2["1"] += net_REG_VIN
R2["2"] += net_REG_EN

R3["1"] += net_REG_PG
R3["2"] += net_Net_D1_A

R4["1"] += net_Net_C6_Pad2
R4["2"] += net_REG_FB

R5["1"] += net_N_5V
R5["2"] += net_REG_FB

R6["1"] += net_GND
R6["2"] += net_REG_FB

R7["1"] += net_GND
R7["2"] += net_Net_LED1_K

R8["1"] += net_GND
R8["2"] += net_Net_LED2_K

REG1["1"] += net_Net_REG1_PVDD
REG1["2"] += net_GND
REG1["3"] += net_unconnected_REG1_NC_Pad3
REG1["4"] += net_REG_CS
REG1["5"] += net_GND
REG1["6"] += net_GND
REG1["7"] += net_GND
REG1["8"] += net_GND
REG1["9"] += net_REG_CS
REG1["10"] += net_REG_CS
REG1["11"] += net_REG_CS
REG1["12"] += net_REG_CS
REG1["13"] += net_REG_VIN
REG1["14"] += net_REG_VIN
REG1["15"] += net_REG_VIN
REG1["16"] += net_REG_VIN
REG1["17"] += net_REG_VIN
REG1["18"] += net_REG_VIN
REG1["19"] += net_REG_VIN
REG1["20"] += net_REG_BST
REG1["21"] += net_GND
REG1["22"] += net_REG_CS
REG1["23"] += net_GND
REG1["24"] += net_REG_FB
REG1["25"] += net_REG_PG
REG1["26"] += net_REG_EN
REG1["27"] += net_REG_VIN
REG1["28"] += net_Net_D1_A
REG1["29"] += net_REG_CS
REG1["30"] += net_REG_VIN
REG1["31"] += net_GND

REG2["1"] += net_N_3_3V
REG2["2"] += net_N_3_3V
REG2["3"] += net_GND
REG2["4"] += net_unconnected_REG2_PG_Pad4
REG2["5"] += net_N_5V
REG2["6"] += net_N_5V
REG2["7"] += net_GND

U1["1"] += net_VIN
U1["2"] += net_REG_VIN
U1["3"] += net_GND
U1["4"] += net_N_3_3V
U1["5"] += net_I2C2_SCL_FCC
U1["6"] += net_I2C2_SDA_FCC
U1["7"] += net_GND
U1["8"] += net_GND

C13["1"] += net_unconnected_C13_Pad1
C13["2"] += net_GND

C14["1"] += net_Net_FCC1_PH0
C14["2"] += net_GND

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

C26["1"] += net_N_3V3
C26["2"] += net_GND

C28["1"] += net_VDDA_FCC
C28["2"] += net_GND

C30["1"] += net_VREF_FCC
C30["2"] += net_GND

C31["1"] += net_NRST_FCC
C31["2"] += net_GND

C32["1"] += net_HSE_IN_FCC
C32["2"] += net_GND

C33["1"] += net_Net_C33_Pad1
C33["2"] += net_GND

FCC1["1"] += net_unconnected_FCC1_PE2_Pad1
FCC1["2"] += net_unconnected_FCC1_PE3_Pad2
FCC1["3"] += net_unconnected_FCC1_PE4_Pad3
FCC1["4"] += net_unconnected_FCC1_PE5_Pad4
FCC1["5"] += net_HSE_IN_FCC
FCC1["6"] += net_unconnected_FCC1_VBAT_Pad6
FCC1["7"] += net_unconnected_FCC1_PC13_Pad7
FCC1["8"] += net_unconnected_FCC1_PC14_Pad8
FCC1["9"] += net_unconnected_FCC1_PC15_Pad9
FCC1["10"] += net_GND
FCC1["11"] += net_unconnected_FCC1_VDD_Pad11
FCC1["12"] += net_Net_FCC1_PH0
FCC1["13"] += net_VREF_FCC
FCC1["14"] += net_unconnected_FCC1_NRST_Pad14
FCC1["15"] += net_unconnected_FCC1_PC0_Pad15
FCC1["16"] += net_unconnected_FCC1_PC1_Pad16
FCC1["17"] += net_unconnected_FCC1_PC2_C_Pad17
FCC1["18"] += net_ADC3_0_FCC
FCC1["19"] += net_GND
FCC1["20"] += net_unconnected_FCC1_VREF_Pad20
FCC1["21"] += net_unconnected_FCC1_VDDA_Pad21
FCC1["22"] += net_unconnected_FCC1_PA0_Pad22
FCC1["23"] += net_UART4_TX_FCC
FCC1["24"] += net_UART4_RX_FCC
FCC1["25"] += net_UART2_TX_FCC
FCC1["26"] += net_GND
FCC1["27"] += net_unconnected_FCC1_VDD_Pad27
FCC1["28"] += net_UART2_RX_FCC
FCC1["29"] += net_SPI1_CS_FLASH_FCC
FCC1["30"] += net_SPI1_SCK_FCC
FCC1["31"] += net_SPI1_MISO_FCC
FCC1["32"] += net_ADC3_1_FCC
FCC1["33"] += net_unconnected_FCC1_PC5_Pad33
FCC1["34"] += net_unconnected_FCC1_PB0_Pad34
FCC1["35"] += net_LED_A_FCC
FCC1["36"] += net_LED_B_FCC
FCC1["37"] += net_HSE_OUT_FCC
FCC1["38"] += net_unconnected_FCC1_PE8_Pad38
FCC1["39"] += net_unconnected_FCC1_PE9_Pad39
FCC1["40"] += net_unconnected_FCC1_PE10_Pad40
FCC1["41"] += net_unconnected_FCC1_PE11_Pad41
FCC1["42"] += net_unconnected_FCC1_PE12_Pad42
FCC1["43"] += net_unconnected_FCC1_PE13_Pad43
FCC1["44"] += net_unconnected_FCC1_PE14_Pad44
FCC1["45"] += net_unconnected_FCC1_PE15_Pad45
FCC1["46"] += net_unconnected_FCC1_PB10_Pad46
FCC1["47"] += net_I2C2_SCL_FCC
FCC1["48"] += net_UART3_TX_FCC
FCC1["49"] += net_GND
FCC1["50"] += net_unconnected_FCC1_VDD_Pad50
FCC1["51"] += net_I2C2_SDA_FCC
FCC1["52"] += net_UART5_RX_FCC
FCC1["53"] += net_UART5_TX_FCC
FCC1["54"] += net_UART1_TX_FCC
FCC1["55"] += net_unconnected_FCC1_PD8_Pad55
FCC1["56"] += net_GPIO_A_FCC
FCC1["57"] += net_GPIO_B_FCC
FCC1["58"] += net_GPIO_C_FCC
FCC1["59"] += net_GPIO_D_FCC
FCC1["60"] += net_GPIO_E_FCC
FCC1["61"] += net_GPIO_F_FCC
FCC1["62"] += net_GPIO_G_FCC
FCC1["63"] += net_unconnected_FCC1_PC6_Pad63
FCC1["64"] += net_unconnected_FCC1_PC7_Pad64
FCC1["65"] += net_unconnected_FCC1_PC8_Pad65
FCC1["66"] += net_unconnected_FCC1_PC9_Pad66
FCC1["67"] += net_SPI1_MOSI_FCC
FCC1["68"] += net_I2C3_SCL_FCC
FCC1["69"] += net_USB_VBUS_FCC
FCC1["70"] += net_USB_ID_FCC
FCC1["71"] += net_USB_DM_FCC
FCC1["72"] += net_USB_DP_FCC
FCC1["73"] += net_UART3_RX_FCC
FCC1["74"] += net_GND
FCC1["75"] += net_unconnected_FCC1_VDD_Pad75
FCC1["76"] += net_SWDIO_FCC
FCC1["77"] += net_SWCLK_FCC
FCC1["78"] += net_I2C3_SDA_FCC
FCC1["79"] += net_unconnected_FCC1_PC11_Pad79
FCC1["80"] += net_unconnected_FCC1_PC12_Pad80
FCC1["81"] += net_unconnected_FCC1_PD0_Pad81
FCC1["82"] += net_unconnected_FCC1_PD1_Pad82
FCC1["83"] += net_unconnected_FCC1_PD2_Pad83
FCC1["84"] += net_unconnected_FCC1_PD3_Pad84
FCC1["85"] += net_unconnected_FCC1_PD4_Pad85
FCC1["86"] += net_unconnected_FCC1_PD5_Pad86
FCC1["87"] += net_unconnected_FCC1_PD6_Pad87
FCC1["88"] += net_unconnected_FCC1_PD7_Pad88
FCC1["89"] += net_LED_C_FCC
FCC1["90"] += net_LED_D_FCC
FCC1["91"] += net_LED_E_FCC
FCC1["92"] += net_LED_F_FCC
FCC1["93"] += net_I2C1_SCL_FCC
FCC1["94"] += net_unconnected_FCC1_BOOT0_Pad94
FCC1["95"] += net_I2C1_SDA_FCC
FCC1["96"] += net_unconnected_FCC1_PB9_Pad96
FCC1["97"] += net_unconnected_FCC1_PE0_Pad97
FCC1["98"] += net_unconnected_FCC1_PE1_Pad98
FCC1["99"] += net_GND
FCC1["100"] += net_unconnected_FCC1_VDD_Pad100

HSE1["1"] += net_HSE_IN_FCC
HSE1["2"] += net_GND
HSE1["3"] += net_Net_C33_Pad1
HSE1["4"] += net_GND

LED3["1"] += net_Net_LED3_K
LED3["2"] += net_LED_A_FCC

LED4["1"] += net_Net_LED4_K
LED4["2"] += net_LED_B_FCC

LED5["1"] += net_Net_LED5_K
LED5["2"] += net_LED_C_FCC

LED6["1"] += net_Net_LED6_K
LED6["2"] += net_LED_D_FCC

LED7["1"] += net_Net_LED7_K
LED7["2"] += net_LED_E_FCC

LED8["1"] += net_Net_LED8_K
LED8["2"] += net_LED_F_FCC

R9["1"] += net_N_3V3
R9["2"] += net_I2C1_SCL_FCC

R10["1"] += net_N_3V3
R10["2"] += net_I2C1_SDA_FCC

R11["1"] += net_N_3V3
R11["2"] += net_I2C2_SCL_FCC

R12["1"] += net_N_3V3
R12["2"] += net_I2C2_SDA_FCC

R13["1"] += net_N_3V3
R13["2"] += net_I2C3_SCL_FCC

R14["1"] += net_N_3V3
R14["2"] += net_I2C3_SDA_FCC

R15["1"] += net_GND
R15["2"] += net_Net_LED3_K

R16["1"] += net_GND
R16["2"] += net_Net_LED4_K

R17["1"] += net_GND
R17["2"] += net_Net_LED5_K

R18["1"] += net_GND
R18["2"] += net_Net_LED6_K

R19["1"] += net_GND
R19["2"] += net_Net_LED7_K

R20["1"] += net_GND
R20["2"] += net_Net_LED8_K

R21["1"] += net_VREF_FCC
R21["2"] += net_VDDA_FCC

R22["1"] += net_Net_SW2_C
R22["2"] += net_BOOT0_FCC

R23["1"] += net_HSE_OUT_FCC
R23["2"] += net_Net_C33_Pad1

SW1["1"] += net_NRST_FCC
SW1["2"] += net_NRST_FCC
SW1["3"] += net_GND
SW1["4"] += net_GND

SW2["1"] += net_N_3V3
SW2["2"] += net_GND
SW2["3"] += net_Net_SW2_C

TP1["1"] += net_I2C1_SCL_FCC

TP2["1"] += net_I2C1_SDA_FCC

C37["1"] += net_Net_NAVC1_PH0
C37["2"] += net_GND

C38["1"] += net_Net_NAVC1_PH1
C38["2"] += net_GND

C40["1"] += net_N_3V3
C40["2"] += net_GND

C41["1"] += net_N_3V3
C41["2"] += net_GND

C42["1"] += net_N_3V3
C42["2"] += net_GND

C43["1"] += net_N_3V3
C43["2"] += net_GND

C44["1"] += net_N_3V3
C44["2"] += net_GND

C45["1"] += net_N_3V3
C45["2"] += net_GND

C46["1"] += net_N_3V3
C46["2"] += net_GND

C47["1"] += net_N_3V3
C47["2"] += net_GND

C48["1"] += net_N_3V3
C48["2"] += net_GND

C49["1"] += net_NRST_NAVC
C49["2"] += net_GND

C51["1"] += net_VDDA_NAVC
C51["2"] += net_GND

C52["1"] += net_HSE_IN_NAVC
C52["2"] += net_GND

C53["1"] += net_Net_C53_Pad1
C53["2"] += net_GND

HSE2["1"] += net_HSE_IN_NAVC
HSE2["2"] += net_GND
HSE2["3"] += net_Net_C53_Pad1
HSE2["4"] += net_GND

LED9["1"] += net_Net_LED9_K
LED9["2"] += net_LED_A_NAVC

LED10["1"] += net_Net_LED10_K
LED10["2"] += net_LED_B_NAVC

LED11["1"] += net_Net_LED11_K
LED11["2"] += net_LED_C_NAVC

LED12["1"] += net_Net_LED12_K
LED12["2"] += net_LED_D_NAVC

NAVC1["1"] += net_N_3V3
NAVC1["2"] += net_unconnected_NAVC1_PC13_Pad2
NAVC1["3"] += net_unconnected_NAVC1_PC14_Pad3
NAVC1["4"] += net_unconnected_NAVC1_PC15_Pad4
NAVC1["5"] += net_Net_NAVC1_PH0
NAVC1["6"] += net_Net_NAVC1_PH1
NAVC1["7"] += net_unconnected_NAVC1_NRST_Pad7
NAVC1["8"] += net_unconnected_NAVC1_PC0_Pad8
NAVC1["9"] += net_unconnected_NAVC1_PC1_Pad9
NAVC1["10"] += net_unconnected_NAVC1_PC2_Pad10
NAVC1["11"] += net_unconnected_NAVC1_PC3_Pad11
NAVC1["12"] += net_unconnected_NAVC1_VSSA_Pad12
NAVC1["13"] += net_VDDA_NAVC
NAVC1["14"] += net_unconnected_NAVC1_PA0_Pad14
NAVC1["15"] += net_unconnected_NAVC1_PA1_Pad15
NAVC1["16"] += net_unconnected_NAVC1_PA2_Pad16
NAVC1["17"] += net_unconnected_NAVC1_PA3_Pad17
NAVC1["18"] += net_Net_NAVC1_VSS_Pad18
NAVC1["19"] += net_unconnected_NAVC1_VDD_Pad19
NAVC1["20"] += net_unconnected_NAVC1_PA4_Pad20
NAVC1["21"] += net_unconnected_NAVC1_PA5_Pad21
NAVC1["22"] += net_unconnected_NAVC1_PA6_Pad22
NAVC1["23"] += net_unconnected_NAVC1_PA7_Pad23
NAVC1["24"] += net_unconnected_NAVC1_PC4_Pad24
NAVC1["25"] += net_unconnected_NAVC1_PC5_Pad25
NAVC1["26"] += net_unconnected_NAVC1_PB0_Pad26
NAVC1["27"] += net_unconnected_NAVC1_PB1_Pad27
NAVC1["28"] += net_unconnected_NAVC1_PB2_Pad28
NAVC1["29"] += net_unconnected_NAVC1_PB10_Pad29
NAVC1["30"] += net_unconnected_NAVC1_PB11_Pad30
NAVC1["31"] += net_unconnected_NAVC1_VCAP_1_Pad31
NAVC1["32"] += net_unconnected_NAVC1_VDD_Pad32
NAVC1["33"] += net_unconnected_NAVC1_PB12_Pad33
NAVC1["34"] += net_unconnected_NAVC1_PB13_Pad34
NAVC1["35"] += net_unconnected_NAVC1_PB14_Pad35
NAVC1["36"] += net_unconnected_NAVC1_PB15_Pad36
NAVC1["37"] += net_unconnected_NAVC1_PC6_Pad37
NAVC1["38"] += net_unconnected_NAVC1_PC7_Pad38
NAVC1["39"] += net_unconnected_NAVC1_PC8_Pad39
NAVC1["40"] += net_unconnected_NAVC1_PC9_Pad40
NAVC1["41"] += net_unconnected_NAVC1_PA8_Pad41
NAVC1["42"] += net_unconnected_NAVC1_PA9_Pad42
NAVC1["43"] += net_unconnected_NAVC1_PA10_Pad43
NAVC1["44"] += net_unconnected_NAVC1_PA11_Pad44
NAVC1["45"] += net_unconnected_NAVC1_PA12_Pad45
NAVC1["46"] += net_unconnected_NAVC1_PA13_Pad46
NAVC1["47"] += net_unconnected_NAVC1_VCAP_2_Pad47
NAVC1["48"] += net_unconnected_NAVC1_VDD_Pad48
NAVC1["49"] += net_unconnected_NAVC1_PA14_Pad49
NAVC1["50"] += net_unconnected_NAVC1_PA15_Pad50
NAVC1["51"] += net_unconnected_NAVC1_PC10_Pad51
NAVC1["52"] += net_unconnected_NAVC1_PC11_Pad52
NAVC1["53"] += net_unconnected_NAVC1_PC12_Pad53
NAVC1["54"] += net_unconnected_NAVC1_PD2_Pad54
NAVC1["55"] += net_unconnected_NAVC1_PB3_Pad55
NAVC1["56"] += net_unconnected_NAVC1_PB4_Pad56
NAVC1["57"] += net_unconnected_NAVC1_PB5_Pad57
NAVC1["58"] += net_unconnected_NAVC1_PB6_Pad58
NAVC1["59"] += net_unconnected_NAVC1_PB7_Pad59
NAVC1["60"] += net_unconnected_NAVC1_BOOT0_Pad60
NAVC1["61"] += net_unconnected_NAVC1_PB8_Pad61
NAVC1["62"] += net_unconnected_NAVC1_PB9_Pad62
NAVC1["63"] += net_Net_NAVC1_VSS_Pad18
NAVC1["64"] += net_unconnected_NAVC1_VDD_Pad64

R26["1"] += net_Net_SW3_C
R26["2"] += net_BOOT0_NAVC

R27["1"] += net_Net_SW4_C
R27["2"] += net_BOOT1_NAVC

R28["1"] += net_N_3V3
R28["2"] += net_I2C1_SCL_NAVC

R29["1"] += net_N_3V3
R29["2"] += net_I2C1_SDA_NAVC

R30["1"] += net_N_3V3
R30["2"] += net_I2C3_SCL_NAVC

R31["1"] += net_N_3V3
R31["2"] += net_I2C3_SDA_NAVC

R32["1"] += net_HSE_OUT_NAVC
R32["2"] += net_Net_C53_Pad1

R33["1"] += net_GND
R33["2"] += net_Net_LED9_K

R34["1"] += net_GND
R34["2"] += net_Net_LED10_K

R35["1"] += net_GND
R35["2"] += net_Net_LED11_K

R36["1"] += net_GND
R36["2"] += net_Net_LED12_K

SW3["1"] += net_N_3V3
SW3["2"] += net_GND
SW3["3"] += net_Net_SW3_C

SW4["1"] += net_N_3V3
SW4["2"] += net_GND
SW4["3"] += net_Net_SW4_C

SW5["1"] += net_NRST_NAVC
SW5["2"] += net_NRST_NAVC
SW5["3"] += net_GND
SW5["4"] += net_GND

TP3["1"] += net_I2C1_SCL_NAVC

TP4["1"] += net_I2C1_SDA_NAVC

C68["1"] += net_GND
C68["2"] += net_Net_D4_A

C69["1"] += net_GND
C69["2"] += net_unconnected_C69_Pad2

C70["1"] += net_GND
C70["2"] += net_Net_D5_A

C71["1"] += net_GND
C71["2"] += net_unconnected_C71_Pad2

D2["1"] += net_unconnected_D2_K_Pad1
D2["2"] += net_Net_D2_A

D3["1"] += net_unconnected_D3_K_Pad1
D3["2"] += net_Net_D3_A

D4["1"] += net_unconnected_D4_K_Pad1
D4["2"] += net_Net_D4_A

D5["1"] += net_unconnected_D5_K_Pad1
D5["2"] += net_Net_D5_A

GPS_BAT1["1"] += net_unconnected_GPS_BAT1_Pin_1_Pad1
GPS_BAT1["2"] += net_GND

JP1["1"] += net_Net_D2_A
JP1["2"] += net_USB_VBUS_FCC

JP2["1"] += net_Net_D3_A
JP2["2"] += net_USB_VBUS_NAVC

JP4["1"] += net_unconnected_JP4_A_Pad1
JP4["2"] += net_GPS_BAT_BACKUP
JP4["3"] += net_unconnected_JP4_B_Pad3

LED13["1"] += net_Net_LED13_K
LED13["2"] += net_Net_D4_A

LED14["1"] += net_Net_LED14_K
LED14["2"] += net_Net_D5_A

R40["1"] += net_GPIO_A_NAVC
R40["2"] += net_GPIO_A_FCC

R41["1"] += net_GPIO_B_NAVC
R41["2"] += net_GPIO_B_FCC

R42["1"] += net_GPIO_C_NAVC
R42["2"] += net_GPIO_C_FCC

R43["1"] += net_GPIO_D_NAVC
R43["2"] += net_GPIO_D_FCC

R44["1"] += net_GPIO_E_NAVC
R44["2"] += net_GPIO_E_FCC

R45["1"] += net_GPIO_F_NAVC
R45["2"] += net_GPIO_F_FCC

R46["1"] += net_GPIO_G_NAVC
R46["2"] += net_GPIO_G_FCC

R47["1"] += net_GPIO_H_NAVC
R47["2"] += net_GPIO_H_FCC

R48["1"] += net_UART2_TX_NAVC
R48["2"] += net_UART2_RX_FCC

R49["1"] += net_UART2_RX_NAVC
R49["2"] += net_UART2_TX_FCC

R50["1"] += net_I2C2_SCL_NAVC
R50["2"] += net_I2C1_SCL_FCC

R51["1"] += net_I2C2_SDA_NAVC
R51["2"] += net_I2C1_SDA_FCC

R52["1"] += net_USB_DP_FCC
R52["2"] += net_Net_USB1_D_POS

R53["1"] += net_USB_DM_FCC
R53["2"] += net_Net_USB1_D_NEG

R54["1"] += net_USB_ID_FCC
R54["2"] += net_Net_USB1_ID

R55["1"] += net_USB_DP_NAVC
R55["2"] += net_Net_USB2_D_POS

R56["1"] += net_USB_DM_NAVC
R56["2"] += net_Net_USB2_D_NEG

R57["1"] += net_USB_ID_NAVC
R57["2"] += net_Net_USB2_ID

R58["1"] += net_GND
R58["2"] += net_Net_LED13_K

R59["1"] += net_GND
R59["2"] += net_Net_LED14_K

SWD1["1"] += net_N_3V3
SWD1["2"] += net_SWDIO_FCC
SWD1["3"] += net_GND
SWD1["4"] += net_SWCLK_FCC
SWD1["5"] += net_GND
SWD1["6"] += net_unconnected_SWD1_Pin_6_Pad6
SWD1["7"] += net_unconnected_SWD1_Pin_7_Pad7
SWD1["8"] += net_unconnected_SWD1_Pin_8_Pad8
SWD1["9"] += net_GND
SWD1["10"] += net_NRST_FCC

SWD2["1"] += net_N_3V3
SWD2["2"] += net_SWDIO_NAVC
SWD2["3"] += net_GND
SWD2["4"] += net_SWCLK_NAVC
SWD2["5"] += net_GND
SWD2["6"] += net_unconnected_SWD2_Pin_6_Pad6
SWD2["7"] += net_unconnected_SWD2_Pin_7_Pad7
SWD2["8"] += net_unconnected_SWD2_Pin_8_Pad8
SWD2["9"] += net_GND
SWD2["10"] += net_NRST_NAVC

USB1["1"] += net_Net_D2_A
USB1["2"] += net_Net_USB1_D_NEG
USB1["3"] += net_Net_USB1_D_POS
USB1["4"] += net_Net_USB1_ID
USB1["5"] += net_GND
USB1["SH"] += net_GND

USB2["1"] += net_Net_D3_A
USB2["2"] += net_Net_USB2_D_NEG
USB2["3"] += net_Net_USB2_D_POS
USB2["4"] += net_Net_USB2_ID
USB2["5"] += net_GND
USB2["SH"] += net_GND

USB3["1"] += net_Net_D4_A
USB3["2"] += net_unconnected_USB3_D_Pad2
USB3["3"] += net_unconnected_USB3_D_Pad3
USB3["4"] += net_unconnected_USB3_ID_Pad4
USB3["5"] += net_GND
USB3["SH"] += net_GND

USB4["1"] += net_Net_D5_A
USB4["2"] += net_unconnected_USB4_D_Pad2
USB4["3"] += net_unconnected_USB4_D_Pad3
USB4["4"] += net_unconnected_USB4_ID_Pad4
USB4["5"] += net_GND
USB4["SH"] += net_GND

ADC_FCC1["1"] += net_N_3V3
ADC_FCC1["2"] += net_GND
ADC_FCC1["3"] += net_ADC3_0_FCC
ADC_FCC1["4"] += net_ADC3_1_FCC

C34["1"] += net_N_3_3V
C34["2"] += net_GND

C35["1"] += net_N_3_3V
C35["2"] += net_GND

C36["1"] += net_GND
C36["2"] += net_N_3_3V

I2C3_FCC1["1"] += net_N_3V3
I2C3_FCC1["2"] += net_GND
I2C3_FCC1["3"] += net_I2C3_SCL_FCC
I2C3_FCC1["4"] += net_I2C3_SDA_FCC

PWM_POW1["1"] += net_N_5V
PWM_POW1["2"] += net_GND
PWM_POW1["3"] += net_N_5V
PWM_POW1["4"] += net_GND
PWM_POW1["5"] += net_N_5V
PWM_POW1["6"] += net_GND
PWM_POW1["7"] += net_N_5V
PWM_POW1["8"] += net_GND
PWM_POW1["9"] += net_N_5V
PWM_POW1["10"] += net_GND
PWM_POW1["11"] += net_N_5V
PWM_POW1["12"] += net_GND
PWM_POW1["13"] += net_N_5V
PWM_POW1["14"] += net_GND
PWM_POW1["15"] += net_N_5V
PWM_POW1["16"] += net_GND

PWM_SIG1["1"] += net_PWM_0
PWM_SIG1["2"] += net_PWM_1
PWM_SIG1["3"] += net_PWM_2
PWM_SIG1["4"] += net_PWM_3
PWM_SIG1["5"] += net_PWM_4
PWM_SIG1["6"] += net_PWM_5
PWM_SIG1["7"] += net_PWM_6
PWM_SIG1["8"] += net_PWM_7

R24["1"] += net_N_3_3V
R24["2"] += net_Net_U4_HOLD_IO3

R25["1"] += net_N_3_3V
R25["2"] += net_Net_U4_WP_IO2

RCIN_FCC1["1"] += net_N_3V3
RCIN_FCC1["2"] += net_GND
RCIN_FCC1["3"] += net_TIM4_CH1_FCC
RCIN_FCC1["4"] += net_TIM4_CH2_FCC
RCIN_FCC1["5"] += net_TIM4_CH3_FCC
RCIN_FCC1["6"] += net_TIM4_CH4_FCC

U2["1"] += net_N_3_3V
U2["2"] += net_GND
U2["3"] += net_GND
U2["4"] += net_GND
U2["5"] += net_GND
U2["6"] += net_PWM_0
U2["7"] += net_PWM_1
U2["8"] += net_PWM_2
U2["9"] += net_PWM_3
U2["10"] += net_PWM_4
U2["11"] += net_PWM_5
U2["12"] += net_PWM_6
U2["13"] += net_PWM_7
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
U2["26"] += net_I2C2_SCL_FCC
U2["27"] += net_I2C2_SDA_FCC
U2["28"] += net_N_3_3V

U3["1"] += net_I2C2_SCL_FCC
U3["2"] += net_GND
U3["3"] += net_I2C2_SDA_FCC
U3["4"] += net_N_3_3V
U3["5"] += net_unconnected_U3_NC_Pad5

U4["1"] += net_SPI1_CS_FLASH_FCC
U4["2"] += net_SPI1_MISO_FCC
U4["3"] += net_Net_U4_WP_IO2
U4["4"] += net_GND
U4["5"] += net_SPI1_MOSI_FCC
U4["6"] += net_SPI1_SCK_FCC
U4["7"] += net_Net_U4_HOLD_IO3
U4["8"] += net_N_3_3V
U4["9"] += net_GND

UART3_FCC1["1"] += net_N_3V3
UART3_FCC1["2"] += net_GND
UART3_FCC1["3"] += net_UART3_TX_FCC
UART3_FCC1["4"] += net_UART3_RX_FCC

UART4_FCC1["1"] += net_N_3V3
UART4_FCC1["2"] += net_GND
UART4_FCC1["3"] += net_UART4_TX_FCC
UART4_FCC1["4"] += net_UART4_RX_FCC

UART5_FCC1["1"] += net_N_3V3
UART5_FCC1["2"] += net_GND
UART5_FCC1["3"] += net_UART5_TX_FCC
UART5_FCC1["4"] += net_UART5_RX_FCC

ANT1["1"] += net_Net_ANT1_Pad1
ANT1["2"] += net_GND
ANT1["3"] += net_GND
ANT1["4"] += net_GND
ANT1["5"] += net_GND

C54["1"] += net_N_3_3V
C54["2"] += net_GND

C55["1"] += net_N_3_3V
C55["2"] += net_GND

C56["1"] += net_N_3_3V
C56["2"] += net_GND

C57["1"] += net_Net_U7_VO_NEG
C57["2"] += net_Net_U7_VO_POS

C58["1"] += net_N_3_3V
C58["2"] += net_GND

C59["1"] += net_Net_U8_C1
C59["2"] += net_GND

C60["1"] += net_N_3_3V
C60["2"] += net_GND

C61["1"] += net_N_3_3V
C61["2"] += net_GND

C62["1"] += net_N_3_3V
C62["2"] += net_GND

C63["1"] += net_N_3_3V
C63["2"] += net_GND

C64["1"] += net_N_3_3V
C64["2"] += net_GND

C65["1"] += net_N_3_3V
C65["2"] += net_GND

C66["1"] += net_Net_ANT1_Pad1
C66["2"] += net_Net_U10_RF_IN

C67["1"] += net_Net_ANT1_Pad1
C67["2"] += net_GND

GPS_NAVC1["1"] += net_N_3V3
GPS_NAVC1["2"] += net_GND
GPS_NAVC1["3"] += net_UART1_TX_NAVC
GPS_NAVC1["4"] += net_UART1_RX_NAVC
GPS_NAVC1["5"] += net_GPS_PPS_NAVC
GPS_NAVC1["6"] += net_GPS_NRST_NAVC
GPS_NAVC1["7"] += net_GPS_LNA_EN_NAVC

I2C3_NAVC1["1"] += net_N_3V3
I2C3_NAVC1["2"] += net_GND
I2C3_NAVC1["3"] += net_I2C3_SCL_NAVC
I2C3_NAVC1["4"] += net_I2C3_SDA_NAVC

JP3["1"] += net_N_3_3V
JP3["2"] += net_Net_JP3_C
JP3["3"] += net_GND

L2["1"] += net_Net_L2_Pad1
L2["2"] += net_Net_ANT1_Pad1

R37["1"] += net_N_3_3V
R37["2"] += net_BAR_NRST_NAVC

R38["1"] += net_N_3_3V
R38["2"] += net_GPS_NRST_NAVC

R39["1"] += net_Net_L2_Pad1
R39["2"] += net_Net_U10_VCC_RF

U5["1"] += net_unconnected_U5_INT2_Pad1
U5["3"] += net_N_3_3V
U5["4"] += net_GND
U5["5"] += net_unconnected_U5_CSB2_Pad5
U5["6"] += net_GND
U5["7"] += net_N_3_3V
U5["8"] += net_I2C1_SCL_NAVC
U5["9"] += net_I2C1_SDA_NAVC
U5["10"] += net_N_3_3V
U5["11"] += net_N_3_3V
U5["12"] += net_INT_GYR_NAVC
U5["13"] += net_unconnected_U5_INT4_Pad13
U5["14"] += net_N_3_3V
U5["15"] += net_N_3_3V
U5["16"] += net_INT_ACC_NAVC

U6["1"] += net_I2C1_SCL_NAVC
U6["2"] += net_GND
U6["3"] += net_N_3_3V
U6["4"] += net_N_3_3V
U6["5"] += net_N_3_3V
U6["6"] += net_I2C1_SDA_NAVC

U7["1"] += net_unconnected_U7_SS_Pad1
U7["2"] += net_I2C1_SDA_NAVC
U7["3"] += net_I2C1_SCL_NAVC
U7["4"] += net_Net_U7_VO_POS
U7["6"] += net_Net_U7_VO_NEG
U7["7"] += net_unconnected_U7_MISO_Pad7
U7["8"] += net_BAR_NRST_NAVC
U7["9"] += net_INT_BAR_NAVC
U7["10"] += net_GND
U7["12"] += net_N_3_3V

U8["1"] += net_I2C1_SCL_NAVC
U8["2"] += net_unconnected_U8_NC_1_Pad2
U8["3"] += net_N_3_3V
U8["4"] += net_I2C1_SDA_NAVC
U8["5"] += net_Net_U8_C1
U8["6"] += net_GND
U8["7"] += net_INT_MAG_NAVC
U8["8"] += net_GND
U8["9"] += net_N_3_3V
U8["10"] += net_N_3_3V
U8["11"] += net_unconnected_U8_NC_2_Pad11
U8["12"] += net_unconnected_U8_NC_3_Pad12

U9["1"] += net_I2C1_SCL_NAVC
U9["2"] += net_GND
U9["3"] += net_I2C1_SDA_NAVC
U9["4"] += net_N_3_3V
U9["5"] += net_unconnected_U9_NC_Pad5

U10["1"] += net_GND
U10["2"] += net_UART1_RX_NAVC
U10["3"] += net_UART1_TX_NAVC
U10["4"] += net_GPS_PPS_NAVC
U10["5"] += net_unconnected_U10_EXTINT_Pad5
U10["6"] += net_GPS_BAT_BACKUP
U10["7"] += net_N_3_3V
U10["8"] += net_N_3_3V
U10["9"] += net_GPS_NRST_NAVC
U10["10"] += net_GND
U10["11"] += net_Net_U10_RF_IN
U10["12"] += net_GND
U10["13"] += net_GPS_LNA_EN_NAVC
U10["14"] += net_Net_U10_VCC_RF
U10["15"] += net_unconnected_U10_RES_Pad15
U10["16"] += net_unconnected_U10_SDA_Pad16
U10["17"] += net_unconnected_U10_SCL_Pad17
U10["18"] += net_Net_JP3_C

UART4_NAVC1["1"] += net_N_3V3
UART4_NAVC1["2"] += net_GND
UART4_NAVC1["3"] += net_UART4_TX_NAVC
UART4_NAVC1["4"] += net_UART4_RX_NAVC


generate_netlist()