# CAT 3: 8051 Switch Polling & LED Pattern Generation

* **Course Code & Title:** 25CS2741 – Fundamentals of Internet of Things Laboratory
* **Assessment Period:** Continuous Assessment 3 (Week 3)
* **Date:** 27/07/2026
* **Student Name:** Venkataprabu V
* **Registration Number:** 25011102114
* **Microcontroller Platform:** Microchip / Atmel AT89S52 (8051 Core)
* **Development Environment:** Keil µVision IDE (C51 Compiler v9.60)

---

## 1. Overview
Continuous Assessment 3 expands upon GPIO interfacing by implementing switch polling through matrix row/column scanning and real-time user interrupt emulation. The lab demonstrates how to poll input keys inside timing delay loops so that pattern transitions respond instantly to user interaction without hardware timer interrupts.

## 2. Subtasks Summary

| Task Identifier | Subtask Title | Key Peripherals & Pins | Source File | Documentation Link |
|---|---|---|---|---|
| **TASK 3A** | Timer-Based LED Pattern Generator and Button Interrupt Controller | P1.1–P1.4 (4-LED Array), P2.7 (Row 1), P2.1 (Col 1), P2.2 (Col 2) | `lab3.c` | [TASK 3A README](TASK3A/README.md) |

---

## 3. Hardware Architecture & Pin Configuration
* **Microcontroller:** AT89S52 (40-pin DIP, 8 KB Flash ROM, 256 Bytes on-chip RAM, 11.0592 MHz Crystal).
* **Input Switches:** Dual tactile matrix switches connected across active-LOW scan line `P2.7` and sensing column lines `P2.1` (SW1 - Mode Decrement) and `P2.2` (SW2 - Mode Increment).
* **Output Display:** 4 LEDs (Red, Green, Yellow, Blue) connected to Port 1 Pins `P1.1` through `P1.4` via 330 Ω current-limiting resistors.
* **Firmware Binary:** Compiled Intel HEX output `Objects/lab-4.hex` located inside `TASK3A/Objects/`.
