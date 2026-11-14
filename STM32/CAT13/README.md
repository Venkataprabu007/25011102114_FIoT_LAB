# CAT 13: Sensor Interfacing (BME280, I2C)

**Course:** Foundations of IoT (FIoT) Lab (Week 13)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 23/10/2026  

---

## Overview
CAT 13 focuses on digital sensor integration using the Inter-Integrated Circuit (I2C) bus on the STM32F410RB ARM Cortex-M4 microcontroller. The experiment interfaces a Bosch Sensortec BME280 precision multi-parameter environmental sensor, applies polynomial calibration compensation formulas for temperature, barometric pressure, and relative humidity using the official Bosch Sensortec API, and deploys an embedded HTTP JSON telemetry micro-webserver over Wi-Fi using an ESP8266 coprocessor.

## Task Directory Index
| Task Directory | Experiment Title | Source File | Pins Used | Primary Function |
|---|---|---|---|---|
| [TASK13C](./TASK13C/README.md) | BME280 I2C Sensor Interfacing & HTTP JSON Webserver | `Core/Src/main.c`, `bme280.c` | I2C1 (PB6/PB7), USART1 (PA9/10) | Probes I2C address 0x76, verifies Chip ID (0x60), initializes calibration tables, samples temperature/pressure/humidity, and serves JSON environmental metrics over HTTP port 80. |

## Hardware Architecture
- **Host Controller:** STM32 NUCLEO-F410RB (ARM Cortex-M4 @ 100 MHz SYSCLK).
- **Environmental Sensor:** Bosch BME280 connected to I2C1 (PB6 SCL, PB7 SDA) in Standard Mode (100 kHz).
- **Wireless Coprocessor:** ESP8266 Wemos D1 mini on USART1 (PA9/PA10) at 115200 baud.
