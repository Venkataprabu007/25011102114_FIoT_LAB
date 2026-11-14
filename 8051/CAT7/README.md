# CAT 7: 8051 LCD Driver and Display Interfacing

**Course:** Foundations of IoT (FIoT) Lab (Week 7)  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 25/08/2026  

---

## Overview
CAT 7 explores character display interfacing using an industry-standard HD44780-compatible 16x2 alphanumeric LCD driven by the AT89S52 8051 microcontroller. The exercises implement a 4-bit parallel bus interface, cutting pin count down to 6 microcontroller I/O lines (4 data lines + 2 control lines).

## Task Summary
| Task Directory | Experiment Title | Source File | Description | Output Artifact |
|---|---|---|---|---|
| [TASK7A](./TASK7A/README.md) | Dual-Row Static LCD Display | `lcd_both_rows.c` | 4-bit bus initialization and static string rendering ("IoT" / "LCD") across both display rows. | `Objects/lab-4.hex` |
| [TASK7B](./TASK7B/README.md) | Dynamic Numeric Counter Refresh | `lcd_update.c` | Continuous counting from 000 to 999 with dynamic ASCII extraction and in-place row refresh. | `Objects/lab-4.hex` |
| [TASK7C](./TASK7C/README.md) | Interactive Cursor Navigation | `lcd_move.c` | Real-time 2D matrix character repositioning on LCD via 4 directional push-buttons on Port 2. | `Objects/lab-4.hex` |

## Hardware Interface Architecture
- **Data Bus:** High nibble of Port 1 (`P1.4`..`P1.7`) mapped to LCD data inputs `D4`..`D7`.
- **Control Lines:** Register Select on `P1.3` (RS) and Enable latch strobe on `P1.2` (EN).
- **Read/Write Control:** LCD `RW` pin hardwired to GND for write-only bus timing.
- **Contrast Bias:** 10 kΩ trimmer potentiometer between +5V and GND with wiper connected to LCD `V0`.
- **User Navigation (Task 7C):** 4 active-low tactile push-buttons connected to `P2.4` (Up), `P2.5` (Down), `P2.6` (Left), and `P2.7` (Right).
