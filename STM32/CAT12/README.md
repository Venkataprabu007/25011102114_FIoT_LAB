# CAT 12: STM32 Cortex-M4 GPIO and User Interface

**Course:** Foundations of IoT (FIoT) Lab (Week 12)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 19/10/2026  

---

## Overview
CAT 12 introduces General Purpose Input/Output programming and advanced human-machine interface (HMI) gesture detection on the 32-bit ARM Cortex-M4 architecture (STM32F401RE / STM32F411CE). Exercises progress from basic periodic square-wave LED toggling to non-blocking debounce filtering and complex multi-gesture recognition (short-press toggle vs. long-press continuous blinking).

## Task Directory Index
| Task Directory | Experiment Title | Source File | Pins Used | Primary Function |
|---|---|---|---|---|
| [TASK12A](./TASK12A/README.md) | On-Board LED Bring-Up | `Core/Src/main.c` | PA5 (LED LD2) | 1.0 Hz periodic square-wave blinking with 500 ms delay intervals. |
| [TASK12B](./TASK12B/README.md) | Switch Debounce & Latch | `Core/Src/main.c` | PC13 (Btn), PA5 (LED) | 30 ms non-blocking SysTick debounce filter with state remembrance. |
| [TASK12C](./TASK12C/README.md) | Multi-Gesture Detection | `Core/Src/main.c` | PC13 (Btn), PA5 (LED) | Short-press (<1s) static toggle vs. Long-press (>=1s) 500 ms auto-blink mode. |

## Hardware Architecture
- **Target Platform:** STM32 Cortex-M4 Development Board.
- **Output Actuator:** Green User LED LD2 on pin PA5 (Active-High push-pull).
- **Input Sensor:** Blue User Push-Button B1 on pin PC13.
- **Timebase:** ARM SysTick timer generating 1 ms tick interrupts accessible via `HAL_GetTick()`.
