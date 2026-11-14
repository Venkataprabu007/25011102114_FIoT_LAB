# CAT 8: STM32 Cortex-M3 GPIO Interfacing (LED & Switch)

**Course:** Foundations of IoT (FIoT) Lab (Week 8)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 18/09/2026  

---

## Overview
CAT 8 marks the transition from the legacy 8-bit 8051 architecture to the 32-bit ARM Cortex-M3 platform using the STM32F103C8T6 microcontroller ("Blue Pill"). Experiments cover basic digital input polling, software debounce filtering, and advanced event-driven state machine gesture detection (short-press vs. long-press) paired with autonomous non-blocking LED control using the STM32Cube HAL framework.

## Task Directory Index
| Task Directory | Experiment Title | Primary Source | Hardware Pins | Key Mechanism |
|---|---|---|---|---|
| [TASK8A](./TASK8A/README.md) | Direct Switch Polling | `Core/Src/main.c` | PA9 (Btn), PC13 (LED) | Direct combinational mapping: button hold = LED ON. |
| [TASK8B](./TASK8B/README.md) | Debounce Filter & Toggle | `Core/Src/main.c` | PA9 (Btn), PC13 (LED) | 20 ms non-blocking SysTick filter; falling-edge LED toggle. |
| [TASK8C](./TASK8C/README.md) | Multi-Function State Machine | `Core/Src/main.c` | PA9 (Btn), PC13 (LED) | Short-press toggle vs. Long-press (>= 1s) 500 ms auto-blink. |

## Hardware Architecture
- **Microcontroller:** STM32F103C8T6 (ARM Cortex-M3 core, 72 MHz SYSCLK via 8 MHz HSE crystal and PLL).
- **Digital Input:** Tactile push-button on PA9 with internal pull-up (`GPIO_PULLUP`). Active-low (0V when pressed).
- **Digital Output:** On-board Green LED on PC13. Active-low (`GPIO_PIN_RESET` drives cathode to 0V, lighting LED).
- **Timebase:** ARM SysTick timer generating 1 ms tick interrupts (`HAL_GetTick()`).
