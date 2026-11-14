# CAT 2: 8051 GPIO Interfacing & Toolchain Bring-Up

* **Course Code & Title:** 25CS2741 – Fundamentals of Internet of Things Laboratory
* **Assessment Period:** Continuous Assessment 2 (Week 2)
* **Date:** 20/07/2026
* **Student Name:** Venkataprabu V
* **Registration Number:** 25011102114
* **Microcontroller Platform:** Microchip / Atmel AT89S52 (Classical 8051 Core)
* **Development Environment:** Keil µVision IDE (C51 Compiler v9.60)

---

## 1. Overview
Continuous Assessment 2 establishes the embedded software development toolchain for the 8-bit 8051 microcontroller architecture using the AT89S52 target processor. The exercises progress from fundamental development board bring-up to bare-metal GPIO output toggling and multi-channel input/output coordination with software debouncing.

## 2. Subtasks Summary

| Task Identifier | Subtask Title | Key Peripherals & Pins | Source File | Documentation Link |
|---|---|---|---|---|
| **TASK 2A** | Hardware Board Bring-Up | P1.0 (LED Indicator), 11.0592 MHz Clock, RST | `bringup.c` | [TASK 2A README](TASK2A/README.md) |
| **TASK 2B** | Bare-Metal LED Blink | P1.0 (Output LED Driver), Software Delay Loop | `blink.c` | [TASK 2B README](TASK2B/README.md) |
| **TASK 2C** | Multi-Pattern LED Controller | P1.1–P1.4 (4-LED Array), P3.2 (Debounced Button) | `controller.c` | [TASK 2C README](TASK2C/README.md) |

---

## 3. Hardware Architecture & Toolchain Setup
* **Microcontroller:** AT89S52 (DIP-40 Package, 8 KB Flash ROM, 256 Bytes on-chip RAM).
* **Clock System:** 11.0592 MHz Quartz Crystal with dual 33 pF ceramic load capacitors (machine cycle: $1.0851\ \mu\text{s}$).
* **Reset Circuit:** High-pulse Power-On Reset network (10 µF capacitor to VCC + 10 kΩ pull-down resistor to GND on Pin 9).
* **Firmware Compilation:** Keil C51 Toolchain generating Intel HEX output files located under `Objects/` in each task folder.
