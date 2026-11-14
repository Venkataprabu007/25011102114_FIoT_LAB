# CAT 15: Capstone Project – Smart Environmental Monitoring and Industrial Recommendation Engine

**Course:** Foundations of IoT (FIoT) Lab (Week 15)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 27/10/2026  

---

## Overview
CAT 15 represents the capstone integration project of the Foundations of IoT curriculum. It brings together multi-variable environmental physical sensing (I2C Bosch BME280), high-performance ARM Cortex-M4 microcontroller firmware (STM32 NUCLEO-F401RE), embedded wireless TCP/IP networking (ESP8266 Wemos coprocessor), standardized cloud pub/sub messaging (MQTT over TCP port 1883), and an automated analytics and recommendation engine executed within Node-RED. 

The complete system ingests live environmental parameters (temperature, humidity, atmospheric barometric pressure), correlates them in real time against external local meteorological observations fetched via OpenWeatherMap REST APIs, evaluates occupational health and thermal comfort models, and automatically issues actionable industrial ventilation and HVAC recommendations alongside an interactive user dashboard.

## Task Directory Index
| Task Directory | Experiment Title | Source Files | Protocols | Primary Function |
|---|---|---|---|---|
| [TASK15](./TASK15/README.md) | Capstone IoT Environmental Analytics Engine | `main.c`, `bme280.c`, `ESPLib.c`, `flows-recengine.json` | I2C (100kHz), UART AT (115200), MQTT (1883), HTTP REST | End-to-end edge-to-cloud IoT environmental monitoring, differential meteorology analysis, and industrial recommendation engine. |

## End-to-End System Pipeline
```text
[BME280 Environmental Sensor]
       │ (I2C1: PB6 SCL, PB7 SDA @ 100 kHz)
       ▼
[STM32 NUCLEO-F401RE Host Core] (84 MHz Cortex-M4)
       │ Formats JSON telemetry: {"temperature":T, "pressure":P, "humidity":H}
       │ (USART1: PA9 TX, PA10 RX @ 115200 Baud via AT frames)
       ▼
[ESP8266 Wi-Fi Coprocessor]
       │ (WLAN 802.11 b/g/n -> TCP Port 1883 Socket)
       ▼
[Cloud MQTT Broker (broker.emqx.io)]
       │ (Topic: "snu/iot/bme280")
       ▼
[Node-RED Stream Analytics Engine] <───> [OpenWeatherMap API]
       │
       ├─► [Smart Recommendations: Heat Index, HVAC Throttling, Free Cooling]
       └─► [Interactive Web Dashboard: Gauges, Time-Series Charts, Deltas]
```
