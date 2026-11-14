# CAT 10: STM32 Cortex-M3 + ESP8266 (Wemos) Wi-Fi Experiments

**Course:** Foundations of IoT (FIoT) Lab (Week 10)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 05/10/2026  

---

## Overview
CAT 10 implements wireless networking capabilities on the STM32F103C8T6 ARM Cortex-M3 platform by bridging it to an external ESP8266 Wi-Fi coprocessor (Wemos D1 mini). The STM32 orchestrates high-level AT command sequences over USART2, parsing telemetry, and establishing 802.11 network association, while tunneling diagnostic logs to a host computer over USART1.

## Task Directory Index
| Task Directory | Experiment Title | Source File | Pins Used | Primary Function |
|---|---|---|---|---|
| [TASK10A](./TASK10A/README.md) | Basic AT Probe & Echo | `Core/Src/main.c` | USART1 (PA9/10), USART2 (PA2/3) | Dispatches attention ping `"AT\r\n"` and streams response to PC terminal. |
| [TASK10B](./TASK10B/README.md) | Multi-Command Sequence | `Core/Src/main.c` | USART1 (PA9/10), USART2 (PA2/3) | Automated 5-stage setup: Mode 1, CIFSR, Multi-mux, and Port 80 TCP server. |
| [TASK10C](./TASK10C/README.md) | Wi-Fi AP Association & IP | `Core/Src/main.c` | USART1 (PA9/10), USART2 (PA2/3) | WPA2 wireless join (`"SNUC"` / `"snu12345"`), DHCP leasing, and IP reporting. |

## Hardware Architecture
- **Host Controller:** STM32F103C8T6 (72 MHz core clock, APB1 at 36 MHz, APB2 at 72 MHz).
- **Wi-Fi Coprocessor:** Wemos D1 mini / ESP8266 running Espressif AT firmware.
- **Console Interface (USART1):** PA9 (TX) and PA10 (RX) at 115200 baud connected to PC via USB-to-UART bridge.
- **Modem Interface (USART2):** PA2 (TX) connected to ESP8266 RX, and PA3 (RX) connected to ESP8266 TX at 115200 baud.
