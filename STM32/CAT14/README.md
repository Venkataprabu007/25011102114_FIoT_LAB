# CAT 14: Sensor MQTT with Node-RED

**Course:** Foundations of IoT (FIoT) Lab (Week 14)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 27/10/2026  

---

## Overview
CAT 14 demonstrates an end-to-end cloud IoT architecture combining multi-variable environmental sensing, binary protocol framing, wireless network transport, and cloud visualization. The STM32F410RB microcontroller reads a Bosch BME280 sensor over I2C1, serializes telemetry into JSON, and dispatches MQTT packets across an ESP8266 Wi-Fi modem using the custom `ESPLib` API to an MQTT broker. Incoming telemetry is ingested by Node-RED flows to drive interactive dashboard widgets.

## Task Directory Index
| Task Directory | Experiment Title | Source Files | Protocols | Primary Function |
|---|---|---|---|---|
| [TASK14](./TASK14/README.md) | BME280 Sensor MQTT Telemetry | `main.c`, `bme280.c`, `ESPLib.c` | I2C (100kHz), MQTT (1883) | 1 Hz JSON telemetry broadcast to topic `"snu/iot/bme280"` visualized on Node-RED. |

## System Architecture Pipeline
```text
[BME280 Sensor]
       │ (I2C1: PB6 SCL, PB7 SDA @ 100 kHz)
       ▼
[STM32F410RB Host Controller]
       │ (USART1: PA9 TX, PA10 RX @ 115200 Baud via ESPLib)
       ▼
[ESP8266 Wemos D1 Mini]
       │ (Wi-Fi 802.11 b/g/n -> TCP Port 1883)
       ▼
[MQTT Broker (Mosquitto)]
       │ (Topic: "snu/iot/bme280")
       ▼
[Node-RED Dashboard (/ui)]
 (Live Temperature, Pressure, and Humidity Gauges & Line Trends)
```
