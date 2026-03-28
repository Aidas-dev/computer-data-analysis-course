# Task 3 – AI ETFs Analysis

**Due:** April 12 at 12:00 (noon)

**Submission:** Email to nora.laurinaityte@ilte.lt or submit via TEAMS

---

## Overview

I would like you to have a closer look at **Artificial Intelligence ETFs**. Artificial Intelligence ETFs are funds that meet at least one of the following three criteria:

1. They are funds that specifically invest in companies involved in the development of new products or services, technological improvements in scientific research related to artificial intelligence, **or**

2. They are funds that have at least **25% of portfolio exposure** to companies that spend large amounts on artificial intelligence research and development (R&D) expenses. Examples of such companies are Amazon, Tesla Motors, Apple and Alphabet, **or**

3. They are funds that use **artificial intelligence methodologies** to select individual securities for inclusion into the fund.

### Main Aim

The main aim of your analysis is to explore time series properties of these ETFs and how (a portfolio constructed from) these ETFs performs in terms of risk/return and produce forecasts for future performance.

### ETFs to Analyze

| Ticker | Fund Name |
|--------|-----------|
| **BOTZ** | Global X Robotics & Artificial Intelligence ETF |
| **WTAI** | WisdomTree Artificial Intelligence and Innovation Fund |
| **IGPT** | Invesco AI and Next Gen Software ETF |
| **ROBO** | ROBO Global Robotics & Automation Index ETF |
| **AIQ** | Global X Artificial Intelligence & Technology ETF |

---

## Data Requirements

Obtain price information for **2023, 2024 and 2025** (three full years of daily data) for these AI ETFs.

> **Note:** ETFs data is available from Yahoo Finance (and I showed you the code example of how to get the data in Tutorials).

---

## Tasks

### 1. Price Series Plot

Plot the five series in one plot for **one of the price points** (open, close, high, low).

> **Hint:** You may need to ensure your dates are read by R as dates.

**Requirements:**
- Clearly indicate your chosen price point
- Make sure axes, legend, etc. is tidy
- Comment briefly what you observe

---

### 2. Time Series Decomposition

Pick **one ETF series** and **one price point** (open/close/high/low) and make it a time series.

> **Note:** For simplicity, if you struggle, you can just say the time series are daily, ignoring that the values are observed only on working days.

**Requirements:**
- Decompose the time series of your choice using `decompose` function
- Is this time series stationary? Why?
- Perform **Augmented Dickey-Fuller test** for unit root
- Interpret the test
- If your series is not stationary, can you make your time series stationary? Try some transformation
- Did you get to stationarity?

---

### 3. Stationary Process Analysis

If/once your series is stationary, what is your stationary process? (White noise? AR(p)? MA(q)?)

**Requirements:**
- Plot **ACF** and **PACF**
- Interpret what you see
- Calculate **returns** (at your choice of data frequency and your choice of method to calculate the returns) for all assets (5 AI ETFs)

---

### 4. Return Series Analysis

**Requirements:**
- Plot return series in one graph
- Report main summary statistics for each of the return series
- Clearly indicate what parameters you chose to calculate returns
- Make sure axes, legend, etc. is tidy
- Comment briefly what you observe
- **What would be an ETF of your choice to invest in? Why?**

---

### 5. Equally Weighted Portfolio

Construct an **equally weighted portfolio** from AI ETFs (so each ETF has a portfolio weight of 1/5).

**Requirements:**
- Report portfolio volatility and returns
- Plot and report main characteristics

---

### 6. Custom Weighted Portfolio

Construct an **alternative portfolio** (feel free to use weights of your choice) from the AI ETFs.

**Requirements:**
- Again, report portfolio characteristics

---

### 7. CAPM Beta Analysis

For each of the two portfolios (equal weighted and with weights of your choice) calculate their **CAPM betas**.

> **Note:** Feel free to use **S&P 500 (^GSPC)** as your benchmark for the market.

**Requirements:**
- What do you see?
- Interpret your findings briefly (2-3 sentences)

---

### 8. Monte Carlo Simulation – Single ETF

Run a **Monte Carlo (MC) simulation** for the performance (in terms of daily return) of **one of the AI ETFs** for the next **30 days**.

**Requirements:**
- Clearly state assumptions employed in your simulation
- Interpret simulation results (plot!)

---

### 9. Monte Carlo Simulation – Portfolio

Run a **Monte Carlo (MC) simulation** for the performance (in terms of daily return) of **any of the portfolios** analyzed above for the next **30 days**.

**Requirements:**
- Clearly state assumptions employed in your simulation
- Interpret simulation results (plot!)

---

### 10. Sensitivity Analysis

Perform a **sensitivity analysis** to your MC simulation done in part 9:

**Requirements:**
- Perform more simulations under different simulation assumptions (hint: change seed a couple of times!)
- Simulate for different forecasting periods (hint: try simulating for 60 days and compare the result to the one from 30 day simulation)
- Discuss your findings

---

## Grading

**All parts carry equal weight.**

---

## Submission Requirements

Please include **all the commands used in your work** in addition to the plots etc. that have been requested, i.e.:

- Submit a **code** (ideally copied into MS Word file) to produce all the results
- **Comment to answer questions** in the Task directly in your code that produces calculations and graphs from raw data
- Otherwise submit an **answer sheet** where you include your code as well as the results themselves
