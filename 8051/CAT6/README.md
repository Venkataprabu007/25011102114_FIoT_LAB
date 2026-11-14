# CAT 6: 8051 UART Driver & Serial Communication

* **Course Code & Title:** 25CS2741 – Fundamentals of Internet of Things Laboratory
* **Assessment Period:** Continuous Assessment 6 (Week 6)
* **Date:** 17/08/2026
* **Student Name:** Venkataprabu V
* **Registration Number:** 25011102114
* **Microcontroller Platform:** Microchip / Atmel AT89S52 (8051 Architecture)
* **Development Environment:** Keil µVision IDE (C51 Compiler v9.60)

---

## 1. Overview
Continuous Assessment 6 focuses on asynchronous serial communication using the on-chip UART of the 8051 microcontroller. By configuring Timer 1 in Mode 2 (8-bit auto-reload) with an 11.0592 MHz crystal, an exact 9600 baud rate (8N1) is established for simplex string transmission and full-duplex interactive character echo.

## 2. Subtasks Summary

| Task Identifier | Subtask Title | Key Peripherals & Pins | Source File | Documentation Link |
|---|---|---|---|---|
| **TASK 6A** | UART Init & String Transmission | Timer 1 Mode 2, `P3.1` (TXD) $\rightarrow$ USB-UART | `uart_tx.c` | [TASK 6A README](TASK6A/README.md) |
| **TASK 6B** | Full-Duplex UART Echo | Timer 1 Mode 2, `P3.0` (RXD), `P3.1` (TXD) | `lab6.c` | [TASK 6B README](TASK6B/README.md) |

---

## 3. Hardware Architecture & Baud Generation
* **Microcontroller:** AT89S52 (DIP-40, 11.0592 MHz Crystal, 8 KB Flash ROM).
* **Baud Formula:**
  $$\text{Baud Rate} = \frac{11,059,200\text{ Hz}}{384 \times (256 - 253)} = \frac{11,059,200}{1,152} = 9600\text{ bps}$$
* **Serial Protocols:** 8 data bits, 1 stop bit, no parity, 9600 baud (8N1).
* **Firmware Binaries:** `TASK6A/Objects/lab-4.hex` and `TASK6B/Objects/lab-6.hex`.
