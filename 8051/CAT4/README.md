# CAT 4: 8051 Keypad Matrix & HMI Display Interfacing

* **Course Code & Title:** 25CS2741 – Fundamentals of Internet of Things Laboratory
* **Assessment Period:** Continuous Assessment 4 (Week 4)
* **Date:** 03/08/2026
* **Student Name:** Venkataprabu V
* **Registration Number:** 25011102114
* **Microcontroller Platform:** Microchip / Atmel AT89S52 (8051 Architecture)
* **Development Environment:** Keil µVision IDE (C51 Compiler v9.60)

---

## 1. Overview
Continuous Assessment 4 explores the development of an integrated embedded Human-Machine Interface (HMI). It combines a matrix keypad input scanning algorithm with concurrent output driving on both a single-digit 7-segment display (Port 0) and a 4-channel LED array (Port 1).

## 2. Subtasks Summary

| Task Identifier | Subtask Title | Key Peripherals & Pins | Source File | Documentation Link |
|---|---|---|---|---|
| **TASK 4A** | HMI with Matrix Keypad, LEDs, and Seven-Segment Display | Port 2 (3×4 Keypad), Port 0 (7-Seg + 10k Pull-Ups), Port 1 (4 LEDs) | `lab4.c` | [TASK 4A README](TASK4A/README.md) |

---

## 3. Hardware Architecture & Pin Interconnects
* **Target Microcontroller:** AT89S52 (DIP-40, 8 KB Flash, 256 B RAM, 11.0592 MHz Crystal).
* **Matrix Keypad Interface:** 3 rows (`P2.7`, `P2.6`, `P2.5`) and 4 columns (`P2.3`, `P2.2`, `P2.1`, `P2.0`).
* **7-Segment Display:** Common cathode 7-segment unit driven via Port 0 (`P0.0`–`P0.7`) with an external 10 kΩ pull-up resistor pack.
* **LED Indicators:** Port 1 Pins `P1.1` to `P1.4` driving four colored LEDs through 330 Ω current-limiting resistors.
* **Firmware Binary:** `TASK4A/Objects/lab-4.hex`.
