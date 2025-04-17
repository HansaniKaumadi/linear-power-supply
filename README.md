# Transistorized Voltage Regulator with Current-Limiting Circuit

This repository contains the lab report, circuit analysis, and relevant materials for the **Transistorized Voltage Regulator with Current-Limiting Circuit** experiment conducted as part of the **EN2111 Electronic Circuit Design** module for semester 4.

## 📋 Experiment Overview

This experiment focuses on designing and implementing a transistorized voltage regulator equipped with a current-limiting circuit using two diodes. The main objectives of the experiment were:

- To maintain a **stable output voltage** under varying load conditions.
- To **protect circuit components** from excessive current by incorporating a current-limiting mechanism.
- To evaluate **voltage stability** and **current-limiting effectiveness** under conditions such as short circuits and varying resistive loads.

<p align="center">
  <img src="https://github.com/user-attachments/assets/737d10dc-edfb-4286-8091-e9816a8b1fce" 
       alt="breadboard" 
       width="300" 
       style="transform: rotate(90deg);">
</p>



## ⚙️ Design Specifications

- **Group A and B values**: A = 4, B = 0
- **Input Voltage Range**: 17 V ± 1.5 V
- **Output Voltage Range**: 6 V ± 2.5 V
- **Maximum Current Limit**: 50 mA (to prevent circuit damage)

The regulator circuit includes two diodes as part of the current-limiting mechanism, ensuring that the current drawn by the load does not exceed the specified limit.

## 🔩 Component Selection

All components used in the design were carefully chosen to meet the above specifications. The details of component selection, including part numbers and justification for each choice, are included in the [Lab Report](./lab_report.pdf).

## 📈 Observations and Results

- Performance was analyzed across different load conditions.
- Voltage regulation and current-limiting behavior were observed using both simulated and real measurements.
- Short circuit tests were conducted to verify the circuit’s response under fault conditions.

All observations, results, and graphs are documented in the lab report.

## 💻 Code and Simulations

Python codes used to plot the graphs are included in the `/codes` directory of this repository.

## 📄 Files Included

- `lab report.pdf`: Complete documentation of the experiment
- `/codes/`: python codes used
- `/graphs/`: Voltage vs. current plots and other analysis visuals


---

Feel free to clone or fork this repository if you're working on a similar voltage regulation project.

