# TASK 5B: Hardware Timer Waveform Generation Suite

* **Course Code & Title:** 25CS2741 – Fundamentals of Internet of Things Laboratory
* **Assessment Period:** Continuous Assessment 5 (Week 5)
* **Date:** 10/08/2026
* **Student Name:** Venkataprabu V
* **Registration Number:** 25011102114
* **Microcontroller Platform:** Microchip / Atmel AT89S52 (8051 Architecture)
* **Development Environment:** Keil µVision IDE (C51 Compiler v9.60)

---

## 1. Overview
TASK 5B evaluates waveform synthesis techniques using Timer 0 in 16-bit Mode 1. Across three subtasks, the 1 ms hardware interrupt tick is leveraged to synthesize variable-frequency square waves, asymmetrical duty-cycle waveforms, and periodic impulse pulse trains.

## 2. Subtasks Summary

| Subtask | Title | Key Mechanism | Output Signal on P1.0 | Documentation Link |
|---|---|---|---|---|
| **TASK 5B.1** | Variable-Frequency Square Wave | Switch-selected threshold (`mode0`, `mode1`) | 10 Hz, 50 Hz, 250 Hz (50% Duty) | [TASK 5B.1 README](TASK5B.1/README.md) |
| **TASK 5B.2** | Variable Duty-Cycle Waveform | Threshold comparison `pulse = (tick < 7)` | 100 Hz, 70% Duty Cycle | [TASK 5B.2 README](TASK5B.2/README.md) |
| **TASK 5B.3** | Periodic Pulse Train | Single-tick comparison `pulse = (tick == 0)` | 100 Hz, 10% Duty Impulse Train | [TASK 5B.3 README](TASK5B.3/README.md) |

---

## 3. Hardware Architecture
* **Target Processor:** AT89S52 (DIP-40, 11.0592 MHz Crystal).
* **Timer Mode:** 16-Bit Timer Mode 1 (`TMOD = 0x01`), Auto-reloaded with `TH0 = 0xFC; TL0 = 0x66` (1.0 ms tick).
* **Output Pin:** `P1.0` (Physical Pin 1).
