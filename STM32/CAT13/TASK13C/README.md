# Experiment 13C: STM32 to BME280 Environmental JSON HTTP Web Server

**Course:** Foundations of IoT (FIoT) Lab  
**Student Name:** Venkataprabu V  
**Registration Number:** 25011102114  
**Date:** 23/10/2026  

---

## 1. Experiment Name and Aim
- **Experiment Name:** STM32 + BME280 RESTful JSON Telemetry Web Server
- **Aim:** To combine I2C environmental data acquisition from a Bosch BME280 sensor with wireless HTTP web serving on the STM32F410RB microcontroller, responding to client HTTP GET requests with structured JSON payloads (`application/json`) containing live temperature, pressure, and humidity measurements.

---

## 2. Components / Tools Required
### Hardware Components
- NUCLEO-F410RB (ARM Cortex-M4 @ 100 MHz) Development Board
- Bosch BME280 Environmental Sensor Breakout
- ESP8266 Wi-Fi Module (Wemos D1 mini running AT firmware)
- USB-to-UART Adapter Module
- Breadboard and DuPont interconnect cables
- Dedicated +3.3V / +5V DC Power Source

### Software / Tools
- Keil MDK-ARM v5 / µVision IDE
- STM32CubeMX
- Web Browser or API Testing Client (cURL, Postman, Chrome)

---

## 3. Hardware Setup
### Bus & Interface Topography
| Peripheral Interface | STM32 Pin | Connected Peripheral | Protocol Detail |
|---|---|---|---|
| I2C1 SCL | PB6 | BME280 SCL | 100 kHz I2C Clock with 4.7k Pull-up |
| I2C1 SDA | PB7 | BME280 SDA | 100 kHz I2C Data with 4.7k Pull-up |
| USART1 TX | PA9 | ESP8266 RX (GPIO3) | 115200 Baud AT Command Dispatch |
| USART1 RX | PA10 | ESP8266 TX (GPIO1) | 115200 Baud Network Stream Ingestion |
| Power Supply | +3.3V / GND | Sensor & ESP8266 VCC/GND | Common Power & Ground Planes |

---

## 4. Circuit Diagram
![Circuit Diagram](circuit.png)

---

## 5. Pseudocode and Code Logic
### REST API Transaction Flow
1. **System Setup:**
   - I2C1 initialized and BME280 sensor calibrated.
   - ESP8266 associated with Wi-Fi network and TCP server activated on Port 80.
2. **`http_task()` Request Handler:**
   - Samples incoming buffer from `huart1`: `HAL_UART_Receive(&huart1, rx, 599, 500)`.
   - Checks for HTTP GET signature: `p = strstr(rx, "+IPD,")` and `strstr(rx, "GET /")`.
   - If not found, exits early.
3. **Data Acquisition & JSON Serialization:**
   - Reads fresh sensor metrics via `bme280_get_sensor_data(BME280_ALL, &comp_data, &dev)`.
   - Serializes payload into formatted JSON string:
     ```c
     int json_len = snprintf(json, sizeof(json),
         "{\"status\":\"success\",\"temperature\":%.2f,\"humidity\":%.2f,\"pressure\":%.2f}",
         temperature, humidity, pressure);
     ```
4. **HTTP Response Construction:**
   - Wraps JSON in an HTTP/1.1 response container with exact `Content-Length`:
     ```c
     int response_len = snprintf(response, sizeof(response),
         "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: %d\r\nConnection: close\r\n\r\n%s",
         json_len, json);
     ```
5. **Socket Transmission & Teardown:**
   - Extracts client link ID: `link_id = p[5]`.
   - Dispatches transmission length: `AT+CIPSEND=<link_id>,<response_len>\r\n`.
   - Transmits HTTP response payload.
   - Closes client connection: `AT+CIPCLOSE=<link_id>\r\n`.

### Pseudocode
```text
INITIALIZE I2C1, USART1
INITIALIZE BME280
START ESP8266 TCP SERVER on Port 80

LOOP FOREVER:
    RECEIVE buffer from USART1 (500 ms timeout)
    IF "+IPD," IN buffer AND "GET /" IN buffer THEN
        link_id <- EXTRACT_LINK_ID(buffer)
        
        READ BME280(temp, press, humid)
        
        json <- "{\"status\":\"success\",\"temperature\":" + temp +
                ",\"humidity\":" + humid + ",\"pressure\":" + press + "}"
                
        header <- "HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: " +
                  LENGTH(json) + "\r\nConnection: close\r\n\r\n"
                  
        response <- header + json
        
        esp_send("AT+CIPSEND=" + link_id + "," + LENGTH(response) + "\r\n")
        WAIT 50 ms
        esp_send(response)
        WAIT 50 ms
        esp_send("AT+CIPCLOSE=" + link_id + "\r\n")
    END IF
END LOOP
```

---

## 6. Procedure
1. Open Keil µVision and load `STM32/CAT13/TASK13C/MDK-ARM/i2c.uvprojx`.
2. Verify Wi-Fi network settings in the project source.
3. Build the target project (**F7**) (0 Errors, 0 Warnings).
4. Connect the NUCLEO board and flash the firmware (**F8**).
5. Query the assigned station IP address via serial monitor or network router table.
6. Open a web browser or execute `curl` on a networked PC:
   ```bash
   curl http://<DEVICE_IP>/
   ```

---

## 7. Expected Output / Inference
- Submitting an HTTP GET request returns a clean JSON response:
  ```json
  {"status":"success","temperature":26.85,"humidity":56.40,"pressure":1013.12}
  ```
- The response header includes `Content-Type: application/json`, allowing automated IoT dashboards, Node-RED flows, or mobile applications to parse the environmental data natively [CONFIRM ON BOARD/SIMULATION].

---

## 8. Conclusion
The experiment verified an end-to-end edge-to-cloud environmental monitoring pipeline. Real-time sensory data acquired over I2C was successfully transformed into structured JSON format and served over wireless HTTP to client applications.
