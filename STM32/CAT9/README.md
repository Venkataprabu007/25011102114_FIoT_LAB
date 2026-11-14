# CAT 9: STM32 Cortex-M3 UART Controlled Communication

**Course:** Foundations of IoT (FIoT) Lab (Week 9)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 28/09/2026  

---

## Overview
CAT 9 focuses on serial communication over the Universal Synchronous Asynchronous Receiver Transmitter (USART1) interface of the STM32F103C8T6 ARM Cortex-M3 microcontroller. Tasks implement full-duplex asynchronous serial communication, autonomous periodic heartbeat beacons, terminal character echo with line-ending formatting, and text-based command decoding to actuate embedded peripherals.

## Task Directory Index
| Task Directory | Experiment Title | Source Files | Pins Used | Primary Function |
|---|---|---|---|---|
| [TASK9A](./TASK9A/README.md) | Basic UART Echo & Heartbeat | `Core/Src/main.c` | PA9 (TX), PA10 (RX) | 1 Hz `'A'` heartbeat transmission; real-time character echo with `\r` -> `\r\n` translation. |
| [TASK9B](./TASK9B/README.md) | Command Controlled LED | `Core/Src/main.c` | PA9 (TX), PA10 (RX), PC13 (LED) | ASCII command interpreter parsing `"LED ON"`, `"LED OFF"`, `"LED TOGGLE"` to control PC13 LED. |

## Hardware & Interface Architecture
- **Microcontroller:** STM32F103C8T6 (72 MHz core clock, APB2 running at 72 MHz).
- **Serial Interface:** USART1 configured in asynchronous mode at 115200 baud, 8 data bits, 1 stop bit, no parity (8N1).
  - Transmit Line: PA9 (USART1_TX) connected to USB-to-UART Adapter RXD.
  - Receive Line: PA10 (USART1_RX) connected to USB-to-UART Adapter TXD.
- **On-Board Actuator:** Active-low user LED on pin PC13 (illuminates when driven LOW / RESET).
