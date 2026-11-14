# Foundations of IoT – Lab Submission

**Name:** Venkataprabu V
**Registration Number:** 25011102114
**Course:** Foundations of IoT (FIoT) Lab

## About this repository

This repository holds my lab experiments for the Foundations of IoT course. Each experiment has its own folder with the source code, project files, a circuit diagram and a README. The folders are numbered by CAT, which matches the week number in the course's Hands-on Exercises list.

The experiments cover two platforms:

- **8051:** Atmel AT89S52 microcontroller. GPIO, switch polling, keypad, timers and PWM, UART and LCD.
- **STM32:** STM32F103C8T6 (Cortex-M3) and STM32 Nucleo (Cortex-M4). GPIO, UART, ESP8266 Wi-Fi, HTTP server, BME280 sensor, MQTT with Node-RED, and a final project.

Tools used: Keil µVision, STM32CubeMX, Proteus, Node-RED.

*Note: CAT 1 (teardown of a commercial IoT device) is not included because its task sheet was not available.*

## Experiment Index

### 8051 (AT89S52)

| CAT | Experiment | Tasks |
|-----|-----------|-------|
| [CAT 2](8051/CAT2) | GPIO Interfacing | [2A](8051/CAT2/TASK2A), [2B](8051/CAT2/TASK2B), [2C](8051/CAT2/TASK2C) |
| [CAT 3](8051/CAT3) | Switch Polling | [3A](8051/CAT3/TASK3A) |
| [CAT 4](8051/CAT4) | Keypad Matrix | [4A](8051/CAT4/TASK4A) |
| [CAT 5](8051/CAT5) | Hardware Timer / PWM | [5A](8051/CAT5/TASK5A), [5B](8051/CAT5/TASK5B), [5C](8051/CAT5/TASK5C) |
| [CAT 6](8051/CAT6) | UART Driver and Serial | [6A](8051/CAT6/TASK6A), [6B](8051/CAT6/TASK6B) |
| [CAT 7](8051/CAT7) | LCD Driver | [7A](8051/CAT7/TASK7A), [7B](8051/CAT7/TASK7B), [7C](8051/CAT7/TASK7C) |

### STM32

| CAT | Experiment | Tasks |
|-----|-----------|-------|
| [CAT 8](STM32/CAT8) | GPIO (Cortex-M3) | [8A](STM32/CAT8/TASK8A), [8B](STM32/CAT8/TASK8B), [8C](STM32/CAT8/TASK8C) |
| [CAT 9](STM32/CAT9) | UART (Cortex-M3) | [9A](STM32/CAT9/TASK9A), [9B](STM32/CAT9/TASK9B) |
| [CAT 10](STM32/CAT10) | ESP8266 Wi-Fi | [10A](STM32/CAT10/TASK10A), [10B](STM32/CAT10/TASK10B), [10C](STM32/CAT10/TASK10C) |
| [CAT 11](STM32/CAT11) | ESP8266 HTTP Server | [11A](STM32/CAT11/TASK11A) |
| [CAT 12](STM32/CAT12) | GPIO and User Interface (Cortex-M4) | [12A](STM32/CAT12/TASK12A), [12B](STM32/CAT12/TASK12B), [12C](STM32/CAT12/TASK12C) |
| [CAT 13](STM32/CAT13) | Sensor Interfacing (BME280, I2C) | [13C](STM32/CAT13/TASK13C) |
| [CAT 14](STM32/CAT14) | Sensor MQTT with Node-RED | [14](STM32/CAT14/TASK14) |
| [CAT 15](STM32/CAT15) | Final Project | [15](STM32/CAT15/TASK15) |

## Folder Structure

```
25011102114_FIoT_LAB/
├── README.md
├── .gitignore
├── 8051/
│   └── CAT2 ... CAT7/
│       └── TASKxx/   (code, Keil project, Objects/*.hex, circuit.png, README.md)
└── STM32/
    └── CAT8 ... CAT15/
        └── TASKxx/   (CubeMX project, Core/, Drivers/, MDK-ARM/, circuit.png, README.md)
```

Every task folder has its own README with the aim, hardware setup, circuit diagram, code logic and inference.
