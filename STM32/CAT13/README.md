# CAT 13: Sensor Interfacing (BME280, I2C)

**Course:** Foundations of IoT (FIoT) Lab (Week 13)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 23/10/2026  

---

## Overview
CAT 13 focuses on digital sensor integration using the Inter-Integrated Circuit (I2C) bus on the STM32F410RB ARM Cortex-M4 microcontroller. The exercises interface a Bosch Sensortec BME280 multi-parameter environmental sensor, applying polynomial calibration formulas for Temperature, Pressure, and Humidity, and deploying an embedded JSON RESTful API over wireless HTTP using an ESP8266 coprocessor.

## Task Directory Index
| Task Directory | Experiment Title | Source File | Pins Used | Primary Function |
|---|---|---|---|---|
| [TASK13A](./TASK13A/README.md) | Sensor Bring-Up & ID Check | `Core/Src/main.c` | I2C1 (PB6/PB7), USART1 (PA9/10) | Probes I2C address 0x76, verifies Chip ID (0x60), initializes calibration tables. |
| [TASK13B](./TASK13B/README.md) | Environmental Data Logging | `Core/Src/main.c` | I2C1 (PB6/PB7), USART1 (PA9/10) | 1 Hz continuous telemetry sampling (Temp °C, Press hPa, Humidity %RH) via printf. |
| [TASK13C](./TASK13C/README.md) | JSON REST Telemetry Server | `Core/Src/main.c` | I2C1 (PB6/PB7), USART1 (PA9/10) | Port 80 HTTP server returning structured JSON environmental metrics to browser clients. |

## Hardware Architecture
- **Host Controller:** STM32F410RBT6 (ARM Cortex-M4 @ 100 MHz SYSCLK).
- **Environmental Sensor:** Bosch BME280 connected to I2C1 (PB6 SCL, PB7 SDA) in Standard Mode (100 kHz).
- **Wireless Coprocessor (Task 13C):** ESP8266 Wemos D1 mini on USART1 (PA9/PA10) at 115200 baud.
