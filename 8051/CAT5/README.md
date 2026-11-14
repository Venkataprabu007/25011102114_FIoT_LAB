# CAT 5: 8051 Hardware Timer, PWM, & Stepper Motor Control

* **Course Code & Title:** 25CS2741 – Fundamentals of Internet of Things Laboratory
* **Assessment Period:** Continuous Assessment 5 (Week 5)
* **Date:** 10/08/2026
* **Student Name:** Venkataprabu V
* **Registration Number:** 25011102114
* **Microcontroller Platform:** Microchip / Atmel AT89S52 (8051 Architecture)
* **Development Environment:** Keil µVision IDE (C51 Compiler v9.60)

---

## 1. Overview
Continuous Assessment 5 explores internal hardware timers and interrupt-driven firmware architectures. Using Timer 0 configured in 16-bit Mode 1 (`TMOD = 0x01`) with an auto-reloaded 1.0 ms interrupt interval (`TH0 = 0xFC; TL0 = 0x66`), the laboratory investigates three domains of time-critical embedded control: software pulse-width modulation for LED breathing, multi-mode waveform and pulse train generation, and precise phase commutation for stepper motor actuation.

## 2. Subtasks Summary

| Task Identifier | Subtask Title | Key Peripherals & Pins | Source File | Documentation Link |
|---|---|---|---|---|
| **TASK 5A** | LED Fading using Software PWM | Timer 0 Mode 1, `P1.0` (Breathing LED) | `fade.c` | [TASK 5A README](TASK5A/README.md) |
| **TASK 5B.1** | Variable-Frequency Square Wave | Timer 0, `P1.0` (Pulse Out), `P3.0`/`P3.1` (Mode Select) | `square_wave.c` | [TASK 5B.1 README](TASK5B/TASK5B.1/README.md) |
| **TASK 5B.2** | Variable Duty-Cycle Waveform | Timer 0, `P1.0` (70% Duty Cycle Waveform) | `square_wave.c` | [TASK 5B.2 README](TASK5B/TASK5B.2/README.md) |
| **TASK 5B.3** | Periodic Pulse Train | Timer 0, `P1.0` (10% Duty Impulse Train) | `square_wave.c` | [TASK 5B.3 README](TASK5B/TASK5B.3/README.md) |
| **TASK 5C** | Stepper Motor Speed & Commutation Control | Timer 0, `P1.0`–`P1.3` $\rightarrow$ ULN2003 $\rightarrow$ 28BYJ-48 Stepper | `stepper.c` | [TASK 5C README](TASK5C/README.md) |

---

## 3. Hardware Architecture & Timing Mechanics
* **Target Processor:** AT89S52 (DIP-40, 8 KB Flash ROM, 256 B RAM, 11.0592 MHz Crystal).
* **Timer Frequency Calculation:**
  $$\text{Machine Cycle} = \frac{12}{11.0592\text{ MHz}} \approx 1.0851\ \mu\text{s}$$
  $$\text{Count Register Difference} = 65536 - 64614 (\text{0xFC66}) = 922\text{ counts}$$
  $$\text{Interrupt Period} = 922 \times 1.0851\ \mu\text{s} \approx 1.000\text{ ms}$$
* **Firmware Binaries:** Intel HEX files located under `Objects/lab-4.hex` in each respective subtask directory.
