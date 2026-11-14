# Foundations of IoT – Laboratory Submission Repository

## 1. Student & Course Information

- **Student Name:** Venkataprabu V
- **Registration Number:** 25011102114
- **Course Code & Title:** Foundations of IoT (FIoT) Lab
- **Repository Organization:** Platform-based folder structure with standardized CAT (Week) numbering.

---

## 2. Project Overview

This repository contains the complete laboratory submissions, hardware interfacing firmware, original schematic diagrams, and technical documentation for the Foundations of IoT (FIoT) course. The experiments encompass low-level bare-metal firmware engineering, embedded communications protocols, sensor acquisition, and cloud IoT connectivity spanning two major microcontroller architectures:

1. **8051 Microcontroller Architecture (Nuvoton W78E052DDG / AT89C51):** Bare-metal register manipulation, port I/O, push-button switch polling, 4x4 matrix keypad scanning, hardware Timer 0/1 interrupt-driven PWM signal generation, full-duplex UART serial drivers, and parallel HD44780 alphanumeric LCD interfacing.
2. **ARM Cortex Microcontroller Architecture (STM32F103C8T6 Cortex-M3 & STM32 NUCLEO-F401RE / F410RB Cortex-M4):** HAL-driven peripheral control, interrupt-based tactile input, USART serial command parsers, dual-UART AT command pipelines, ESP8266 Wi-Fi station association, embedded HTTP micro-webservers, Bosch BME280 I2C sensor drivers, and end-to-end MQTT telemetry dispatch into Node-RED analytical dashboards.

> **Note regarding CAT 1:** Week 1 (CAT 1: Teardown of a commercial IoT device) exercise task sheets were not distributed/assigned; no teardown experiment is included in this repository.

---

## 3. Supported Platforms and Toolchains

| Subsystem | Microcontroller / Platform | Clock Frequency | Toolchains & Development Environments |
| :--- | :--- | :--- | :--- |
| **8051 Subsystem** | Nuvoton W78E052DDG / AT89C51 | 11.0592 MHz / 12.0 MHz Crystal | Keil µVision4 / µVision5 (C51 Compiler v9.x), Proteus VSM Simulator |
| **STM32 Cortex-M3** | STM32F103C8T6 (Blue Pill) | 8.0 MHz HSI / 72.0 MHz HSE PLL | STM32CubeMX (v6.x), Keil MDK-ARM µVision5 (ARM Compiler), ST-LINK/V2 |
| **STM32 Cortex-M4** | STM32F401RE / STM32F410RB | 84.0 MHz / 100.0 MHz PLL | STM32CubeMX (v6.x), Keil MDK-ARM µVision5, On-board ST-LINK/V2-1 |
| **Wireless & Networking** | ESP8266 (Wemos D1 Mini / ESP-01) | 80 MHz / 160 MHz | Espressif AT Command Firmware (v1.7+ / v2.x) |
| **IoT Application & Cloud** | Node-RED Runtime & EMQX MQTT Broker | N/A | Node.js, Node-RED Dashboard, OpenWeatherMap REST API |

---

## 4. Complete Experiment Index & Relative Directory Links

The laboratory exercises follow the university's official Hands-on Exercises syllabus numbering (where CAT number corresponds directly to the academic course Week number):

### Part A: 8051 Microcontroller Architecture

| Official CAT Identifier | Academic Week & Experiment Domain | Subtasks & Working Links | Hardware & Peripheral Focus |
| :--- | :--- | :--- | :--- |
| **CAT 2** | **Week 2: 8051 GPIO Interfacing** | • [CAT 2 Summary](./8051/CAT2/README.md)<br>• [TASK 2A: Hardware Bringup & DC Logic](./8051/CAT2/TASK2A/README.md)<br>• [TASK 2B: Software Delay LED Flashing](./8051/CAT2/TASK2B/README.md)<br>• [TASK 2C: Alternating LED Flash Controller](./8051/CAT2/TASK2C/README.md) | Port 1 & Port 2 GPIOs, LED sourcing/sinking, loop delays |
| **CAT 3** | **Week 3: 8051 Switch Polling** | • [CAT 3 Summary](./8051/CAT3/README.md)<br>• [TASK 3A: Active-Low Switch Polling](./8051/CAT3/TASK3A/README.md) | Tactile push button on P2.0, pull-up logic, LED indicator on P1.0 |
| **CAT 4** | **Week 4: 8051 Keypad Matrix** | • [CAT 4 Summary](./8051/CAT4/README.md)<br>• [TASK 4A: 4x4 Matrix Keypad Scanning](./8051/CAT4/TASK4A/README.md) | Port 2 row drive & column read, nibble masking, lookup decoding |
| **CAT 5** | **Week 5: 8051 Hardware Timers & PWM** | • [CAT 5 Summary](./8051/CAT5/README.md)<br>• [TASK 5A: Software PWM LED Fader](./8051/CAT5/TASK5A/README.md)<br>• [TASK 5B: Hardware Timer Square Waveforms](./8051/CAT5/TASK5B/README.md)<br>• [TASK 5C: 4-Phase Stepper Motor Sequencer](./8051/CAT5/TASK5C/README.md) | Timer 0/1 Mode 1 & 2, precise interval generation, ULN2003 stepper |
| **CAT 6** | **Week 6: 8051 UART Driver & Serial** | • [CAT 6 Summary](./8051/CAT6/README.md)<br>• [TASK 6A: Polled UART Transmitter](./8051/CAT6/TASK6A/README.md)<br>• [TASK 6B: Interactive Serial Terminal Echo](./8051/CAT6/TASK6B/README.md) | Timer 1 Mode 2 auto-reload (9600 baud), SCON, SBUF, polled serial |
| **CAT 7** | **Week 7: 8051 LCD Driver** | • [CAT 7 Summary](./8051/CAT7/README.md)<br>• [TASK 7A: Static Dual-Line Text](./8051/CAT7/TASK7A/README.md)<br>• [TASK 7B: In-Place Numeric Counter Display](./8051/CAT7/TASK7B/README.md)<br>• [TASK 7C: Dynamic Marquee Text Banner](./8051/CAT7/TASK7C/README.md) | 16x2 HD44780 LCD, 8-bit parallel bus (P1), RS/RW/EN strobing |

---

### Part B: ARM Cortex Microcontroller Architecture (STM32)

| Official CAT Identifier | Academic Week & Experiment Domain | Subtasks & Working Links | Hardware & Peripheral Focus |
| :--- | :--- | :--- | :--- |
| **CAT 8** | **Week 8: STM32 Cortex-M3 GPIO** | • [CAT 8 Summary](./STM32/CAT8/README.md)<br>• [TASK 8A: GPIO Toggle (LED Blink)](./STM32/CAT8/TASK8A/README.md)<br>• [TASK 8B: Direct Push-Button Polling](./STM32/CAT8/TASK8B/README.md)<br>• [TASK 8C: Interrupt-Driven EXTI Input](./STM32/CAT8/TASK8C/README.md) | STM32F103C8T6, PC13 User LED, PA0 Button, EXTI0 interrupt |
| **CAT 9** | **Week 9: STM32 Cortex-M3 UART** | • [CAT 9 Summary](./STM32/CAT9/README.md)<br>• [TASK 9A: Polled UART String Transmission](./STM32/CAT9/TASK9A/README.md)<br>• [TASK 9B: Interactive Remote LED Controller](./STM32/CAT9/TASK9B/README.md) | USART1 (PA9/PA10 @ 115200 baud), ASCII command parsing |
| **CAT 10** | **Week 10: STM32 Cortex-M3 + ESP8266 Wi-Fi** | • [CAT 10 Summary](./STM32/CAT10/README.md)<br>• [TASK 10A: Dual-UART Bridge & Modem Bringup](./STM32/CAT10/TASK10A/README.md)<br>• [TASK 10B: Wi-Fi Access Point Scan](./STM32/CAT10/TASK10B/README.md)<br>• [TASK 10C: Wi-Fi Station Association](./STM32/CAT10/TASK10C/README.md) | USART1 (PC) to USART2 (ESP8266), AT command pipeline |
| **CAT 11** | **Week 11: STM32 Cortex-M3 + ESP8266 HTTP** | • [CAT 11 Summary](./STM32/CAT11/README.md)<br>• [TASK 11A: Standalone Embedded HTTP Server](./STM32/CAT11/TASK11A/README.md) | Multi-connection TCP server (`AT+CIPSERVER`), HTTP parsing |
| **CAT 12** | **Week 12: STM32 Cortex-M4 GPIO & UI** | • [CAT 12 Summary](./STM32/CAT12/README.md)<br>• [TASK 12A: Nucleo Onboard LED Flasher](./STM32/CAT12/TASK12A/README.md)<br>• [TASK 12B: B1 User Push-Button Polling](./STM32/CAT12/TASK12B/README.md)<br>• [TASK 12C: Multi-Pattern State-Machine LED Controller](./STM32/CAT12/TASK12C/README.md) | STM32F410RB, PA5 User LED, PC13 Blue Push Button, state machine |
| **CAT 13** | **Week 13: Sensor Interfacing (BME280 I2C)** | • [CAT 13 Summary](./STM32/CAT13/README.md)<br>• [TASK 13C: BME280 I2C Sensor & HTTP Server](./STM32/CAT13/TASK13C/README.md) | I2C1 (PB6/PB7 @ 100 kHz), Bosch BME280 API, 64-bit integer compensation, HTTP JSON |
| **CAT 14** | **Week 14: Sensor MQTT with Node-RED** | • [CAT 14 Summary](./STM32/CAT14/README.md)<br>• [TASK 14: Live Sensor Cloud Telemetry](./STM32/CAT14/TASK14/README.md) | I2C1 + USART1 (ESPLib), MQTT broker (`snu/iot/bme280`), Node-RED |
| **CAT 15** | **Week 15: Capstone Project Submission** | • [CAT 15 Summary](./STM32/CAT15/README.md)<br>• [TASK 15: Environmental Recommendation Engine](./STM32/CAT15/TASK15/README.md) | STM32F401RE, BME280, ESP8266, Node-RED Industrial HVAC Advisory |

---

## 5. Repository Directory Structure

```text
25011102114_FIoT_LAB/
├── .gitignore
├── README.md
├── validate.py
│
├── 8051/
│   ├── CAT2/
│   │   ├── README.md
│   │   ├── TASK2A/  (circuit.png, README.md, bringup.c, Keil project, Objects/bringup.hex)
│   │   ├── TASK2B/  (circuit.png, README.md, blink.c, Keil project, Objects/blink.hex)
│   │   └── TASK2C/  (circuit.png, README.md, controller.c, Keil project, Objects/controller.hex)
│   ├── CAT3/
│   │   ├── README.md
│   │   └── TASK3A/  (circuit.png, README.md, lab3.c, Keil project, Objects/lab3.hex)
│   ├── CAT4/
│   │   ├── README.md
│   │   └── TASK4A/  (circuit.png, README.md, lab4.c, Keil project, Objects/lab4.hex)
│   ├── CAT5/
│   │   ├── README.md
│   │   ├── TASK5A/  (circuit.png, README.md, fade.c, Keil project, Objects/fade.hex)
│   │   ├── TASK5B/  (circuit.png, README.md, TASK5B.1/, TASK5B.2/, TASK5B.3/, hex files)
│   │   └── TASK5C/  (circuit.png, README.md, stepper.c, Keil project, Objects/stepper.hex)
│   ├── CAT6/
│   │   ├── README.md
│   │   ├── TASK6A/  (circuit.png, README.md, uart_tx.c, Keil project, Objects/uart_tx.hex)
│   │   └── TASK6B/  (circuit.png, README.md, lab6.c, Keil project, Objects/lab6.hex)
│   └── CAT7/
│       ├── README.md
│       ├── TASK7A/  (circuit.png, README.md, lcd_both_rows.c, Keil project, Objects/lcd_both_rows.hex)
│       ├── TASK7B/  (circuit.png, README.md, lcd_update.c, Keil project, Objects/lcd_update.hex)
│       └── TASK7C/  (circuit.png, README.md, lcd_move.c, Keil project, Objects/lcd_move.hex)
│
└── STM32/
    ├── CAT8/
    │   ├── README.md
    │   ├── TASK8A/  (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, Button.ioc)
    │   ├── TASK8B/  (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, Button.ioc)
    │   └── TASK8C/  (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, Button.ioc)
    ├── CAT9/
    │   ├── README.md
    │   ├── TASK9A/  (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, plswork.ioc)
    │   └── TASK9B/  (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, plswork.ioc)
    ├── CAT10/
    │   ├── README.md
    │   ├── TASK10A/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, plswork2.ioc)
    │   ├── TASK10B/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, plswork2.ioc)
    │   └── TASK10C/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, plswork2.ioc)
    ├── CAT11/
    │   ├── README.md
    │   └── TASK11A/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, http_f410rb.ioc)
    ├── CAT12/
    │   ├── README.md
    │   ├── TASK12A/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, TEST1.ioc)
    │   ├── TASK12B/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, TEST1.ioc)
    │   └── TASK12C/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, TEST1.ioc)
    ├── CAT13/
    │   ├── README.md
    │   └── TASK13C/ (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, i2c.ioc, bme280 API)
    ├── CAT14/
    │   ├── README.md
    │   └── TASK14/  (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, i2c.ioc, ESPLib, bme280)
    └── CAT15/
        ├── README.md
        └── TASK15/  (circuit.png, README.md, Core/, Drivers/, MDK-ARM/, FINAL_PROJECT_1.ioc, flows-recengine.json)
```

---

## 6. Verification and Validation

The integrity and completeness of all required project files, documentation files, embedded schematics, relative documentation hyperlinks, and identifier scrubbing can be evaluated using the automated validation test script:

```bash
python validate.py
```
