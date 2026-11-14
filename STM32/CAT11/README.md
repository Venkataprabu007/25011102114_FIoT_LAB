# CAT 11: STM32 Cortex-M3/M4 + ESP8266 HTTP Server

**Course:** Foundations of IoT (FIoT) Lab (Week 11)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 12/10/2026  

---

## Overview
CAT 11 extends the Wi-Fi networking foundations developed in CAT 10 by deploying an embedded Hypertext Transfer Protocol (HTTP) server daemon on an ARM Cortex-M4 microcontroller (STM32F410RB) coupled with an ESP8266 Wi-Fi transceiver over USART6. The system serves dynamic HTML web pages directly to web browser clients operating on the local network.

## Task Directory Index
| Task Directory | Experiment Title | Source File | Pins Used | Primary Function |
|---|---|---|---|---|
| [TASK11A](./TASK11A/README.md) | Embedded HTTP Web Server | `Core/Src/main.c` | USART6 (PC6/PC7) | Port 80 HTTP server handling inbound GET requests and returning web pages. |

## Hardware & Architecture Highlights
- **Microcontroller Platform:** STM32F410RBT6 (ARM Cortex-M4 @ 100 MHz SYSCLK).
- **Wi-Fi Coprocessor:** Wemos D1 mini ESP8266 executing AT firmware.
- **Interconnect:** USART6 operating at 115200 baud, 8N1 (PC6 TX -> ESP8266 RX, PC7 RX <- ESP8266 TX).
- **Network Stack:** TCP Port 80 multi-connection daemon serving compliant HTTP/1.1 response frames (`Content-Type: text/html`).
