# CAT 15: Capstone Project – Smart Campus Weather Station and Real-Time Cricket Match Decision Engine

**Course:** Foundations of IoT (FIoT) Lab (Week 15)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 27/10/2026  

---

## Overview
CAT 15 represents the capstone integration project of the Foundations of IoT curriculum. It brings together multi-variable environmental physical sensing (I2C Bosch BME280), high-performance ARM Cortex-M4 microcontroller firmware (STM32 NUCLEO-F401RE @ 84 MHz), embedded wireless networking (ESP8266 Wemos D1 Mini), standardized cloud pub/sub messaging (MQTT over TCP port 1883 on `college/weather/bme280`), and an automated analytics and decision engine executed within Node-RED (`weather_flow_dashboard2.json`).

The complete system ingests live campus ground microclimate parameters (temperature, humidity, barometric pressure), correlates them in real time against regional meteorological API observations fetched from OpenWeatherMap (Chennai City), evaluates athletic safety and sports playability rules, and generates actionable cricket match recommendations alongside an interactive dark-theme web dashboard (`/dashboard/weather`).

## Task Directory Index
| Task Directory | Experiment Title | Source Files | Protocols | Primary Function |
|---|---|---|---|---|
| [TASK15](./TASK15/README.md) | Smart Campus Weather Station & Cricket Decision Engine | `main.c`, `bme280.c`, `ESPLib.c`, `weather_flow_dashboard2.json`, `Dashboard.jpeg`, `node-red.jpeg` | I2C (100kHz), UART AT (115200), MQTT (1883), HTTP REST | End-to-end edge-to-cloud IoT environmental monitoring, campus vs. regional city differential meteorology analysis, and real-time cricket match playability decision engine. |

## End-to-End System Pipeline
```text
[Bosch BME280 Sensor]
       │ (I2C1: PB6 SCL, PB7 SDA @ 100 kHz)
       ▼
[STM32 NUCLEO-F401RE Host Core] (84 MHz Cortex-M4)
       │ Formats JSON telemetry: {"temperature":T, "pressure":P, "humidity":H}
       │ (USART1: PA9 TX, PA10 RX @ 115200 Baud via AT commands)
       ▼
[ESP8266 Wemos D1 Mini Wi-Fi Coprocessor]
       │ (WLAN 802.11 b/g/n -> TCP Port 1883 Socket)
       ▼
[Public Cloud MQTT Broker (broker.emqx.io)]
       │ (Topic: "college/weather/bme280")
       ▼
[Node-RED Stream Analytics Engine] <───> [OpenWeatherMap API (Chennai)]
       │
       ├─► [Smart Decisions: Playability Band, Drizzle Advisory, Cool Alert]
       └─► [Interactive Web Dashboard: Dual Weather Gauges, Comparison Cards]
```
