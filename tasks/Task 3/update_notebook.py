import json

# Read the notebook
with open('Task_3.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find and update markdown cells with interpretations
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        
        # Add interpretation after ADF test section
        if 'Augmented Dickey-Fuller' in source or 'ADF' in source:
            pass  # Will add new cells instead
        
        # Add interpretation after Task 2 header
        if 'Task 2: Time Series Decomposition' in source:
            # Add interpretation note
            cell['source'] = [source + '\n\n### Key Findings:\n\n',
                              '- **Selected ETF:** BOTZ (Global X Robotics & AI ETF)\n',
                              '- **Decomposition:** The time series shows a clear **upward trend** over the 3-year period\n',
                              '- **Seasonality:** Minimal seasonal patterns observed (typical for equity ETFs)\n',
                              '- **Residuals:** Random fluctuations around the trend component\n']

# Add new markdown cells with detailed interpretations after key code cells
new_cells = []

# Find the index after ADF test for level
adf_level_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        if 'ADF Statistic: -1.823574' in str(cell.get('outputs', [])):
            adf_level_idx = i
            break

if adf_level_idx > 0:
    interpretation_cell = {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '#### Interpretation of ADF Test (Level Prices):\n',
            '\n',
            'The Augmented Dickey-Fuller test results show:\n',
            '\n',
            '| Statistic | Value |\n',
            '|-----------|-------|\n',
            '| **ADF Statistic** | -1.82 |\n',
            '| **p-value** | 0.369 |\n',
            '| **5% Critical Value** | -2.86 |\n',
            '\n',
            '**Conclusion:** Since the p-value (0.369) is greater than 0.05 and the ADF statistic (-1.82) is greater than the 5% critical value (-2.86), we **fail to reject the null hypothesis**. This means the BOTZ price series contains a **unit root** and is **non-stationary**.\n',
            '\n',
            '**Economic Interpretation:** This is expected for asset prices - they follow a random walk pattern where past prices do not predict future prices. The non-stationarity implies that statistical properties (mean, variance) change over time, making direct forecasting unreliable.\n'
        ]
    }
    new_cells.append((adf_level_idx + 1, interpretation_cell))

# Find the index after ADF test for differenced series
adf_diff_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
        if 'ADF Statistic: -14.450409' in str(cell.get('outputs', [])):
            adf_diff_idx = i
            break

if adf_diff_idx > 0:
    interpretation_cell = {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '#### Interpretation of ADF Test (First Differences/Returns):\n',
            '\n',
            'After taking first differences (calculating daily returns), the ADF test shows:\n',
            '\n',
            '| Statistic | Value |\n',
            '|-----------|-------|\n',
            '| **ADF Statistic** | -14.45 |\n',
            '| **p-value** | < 0.001 |\n',
            '| **5% Critical Value** | -2.86 |\n',
            '\n',
            '**Conclusion:** The p-value is essentially zero (< 0.001) and the ADF statistic (-14.45) is far below all critical values. We **strongly reject the null hypothesis** - the differenced series is **stationary**.\n',
            '\n',
            '**Economic Interpretation:** This confirms that while price levels are unpredictable, **returns are stationary** - they fluctuate around a constant mean with constant variance. This is a fundamental assumption for most financial models including CAPM, portfolio theory, and time series forecasting.\n',
            '\n',
            '**Next Steps:** With stationary returns, we can now:\n',
            '1. Model the return process using ARMA/ARIMA models\n',
            '2. Calculate meaningful statistics (mean, variance, correlations)\n',
            '3. Perform reliable hypothesis testing\n',
            '4. Build forecasting models\n'
        ]
    }
    new_cells.append((adf_diff_idx + 1, interpretation_cell))

# Find the index after Sharpe ratio calculation
sharpe_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        if 'Best risk-adjusted performer: AIQ' in str(cell.get('outputs', [])):
            sharpe_idx = i
            break

if sharpe_idx > 0:
    interpretation_cell = {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '#### Interpretation of Sharpe Ratio Analysis:\n',
            '\n',
            '**Key Finding:** AIQ (Global X Artificial Intelligence & Technology ETF) demonstrates the **best risk-adjusted performance** with a Sharpe ratio of 1.54.\n',
            '\n',
            '**What This Means:**\n',
            '- A Sharpe ratio of 1.54 indicates that for each unit of risk (volatility), AIQ generated 1.54 units of excess return\n',
            '- This is considered an **excellent** risk-adjusted return (Sharpe > 1.0 is generally considered good)\n',
            '- AIQ\'s outperformance may be attributed to its broader technology exposure beyond pure robotics/AI\n',
            '\n',
            '**Investment Implication:** For investors seeking exposure to the AI theme with optimal risk-adjusted returns, AIQ appears to be the preferred choice among the five ETFs analyzed. However, past performance does not guarantee future results.\n'
        ]
    }
    new_cells.append((sharpe_idx + 1, interpretation_cell))

# Find the index after portfolio comparison
portfolio_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        if 'Annualized Return: 25.70%' in str(cell.get('outputs', [])):
            portfolio_idx = i
            break

if portfolio_idx > 0:
    interpretation_cell = {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '#### Interpretation of Portfolio Analysis:\n',
            '\n',
            '**Equal Weight Portfolio (20% each):**\n',
            '| Metric | Value |\n',
            '|--------|-------|\n',
            '| Annualized Return | 25.70% |\n',
            '| Annualized Volatility | 22.95% |\n',
            '| Sharpe Ratio | 1.12 |\n',
            '| CAPM Beta | 1.39 |\n',
            '\n',
            '**Custom Weight Portfolio (Sharpe-based):**\n',
            '| Metric | Value |\n',
            '|--------|-------|\n',
            '| Annualized Return | 27.04% |\n',
            '| Annualized Volatility | 23.01% |\n',
            '| Sharpe Ratio | 1.17 |\n',
            '| CAPM Beta | 1.39 |\n',
            '\n',
            '**Key Observations:**\n',
            '\n',
            '1. **Return Enhancement:** The custom portfolio achieved 1.34% higher annualized return (27.04% vs 25.70%) by tilting towards higher-Sharpe ETFs\n',
            '\n',
            '2. **Similar Risk:** Both portfolios have nearly identical volatility (~23%), indicating the custom weighting did not significantly increase risk\n',
            '\n',
            '3. **Market Sensitivity:** Both portfolios have beta > 1 (approximately 1.39), meaning they are **40% more volatile than the S&P 500**. This is expected for sector-specific technology/AI ETFs.\n',
            '\n',
            '4. **Diversification Benefit:** The portfolio volatility (23%) is lower than the average individual ETF volatility, demonstrating the benefit of diversification across multiple AI ETFs.\n',
            '\n',
            '**Investment Recommendation:** The custom Sharpe-weighted portfolio offers superior risk-adjusted returns. However, investors should be aware of the higher market sensitivity (beta > 1) and expect larger swings compared to the broader market.\n'
        ]
    }
    new_cells.append((portfolio_idx + 1, interpretation_cell))

# Find the index after Monte Carlo simulation
mc_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        if 'Monte Carlo Simulation Parameters' in str(cell.get('outputs', [])):
            mc_idx = i
            break

if mc_idx > 0:
    # Find the cell with simulation results
    for i in range(mc_idx, min(mc_idx + 5, len(nb['cells']))):
        if 'Mean Price:' in str(nb['cells'][i].get('outputs', [])):
            mc_idx = i
            break

if mc_idx > 0:
    interpretation_cell = {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '#### Interpretation of Monte Carlo Simulation:\n',
            '\n',
            '**Simulation Setup:**\n',
            '- **Method:** Geometric Brownian Motion (GBM)\n',
            '- **Assumptions:** Returns are normally distributed with constant drift (μ) and volatility (σ)\n',
            '- **Paths:** 1,000 simulated price trajectories\n',
            '- **Horizon:** 30 trading days (approximately 6 weeks)\n',
            '\n',
            '**Results Interpretation:**\n',
            '\n',
            '1. **Mean Path:** The red line shows the expected price trajectory based on historical average returns\n',
            '\n',
            '2. **Confidence Interval:** The shaded gray area represents the 95% confidence interval - we expect 95% of possible price paths to fall within this band\n',
            '\n',
            '3. **Uncertainty Growth:** Notice how the confidence interval widens over time, reflecting increasing uncertainty in longer-term forecasts\n',
            '\n',
            '4. **Risk Assessment:** The spread between the 5th and 95th percentiles quantifies the potential range of outcomes, useful for risk management\n',
            '\n',
            '**Limitations:**\n',
            '- Assumes constant volatility (in reality, volatility clusters)\n',
            '- Does not account for extreme events (fat tails)\n',
            '- Based on historical parameters that may not persist\n',
            '\n',
            '**Practical Use:** Monte Carlo simulations are valuable for:\n',
            '- Setting realistic return expectations\n',
            '- Assessing downside risk (Value at Risk)\n',
            '- Stress testing portfolio allocations\n',
            '- Planning investment horizons\n'
        ]
    }
    new_cells.append((mc_idx + 1, interpretation_cell))

# Find the index after sensitivity analysis
sens_idx = -1
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        if 'Sensitivity Analysis Results' in str(cell.get('outputs', [])):
            sens_idx = i
            break

if sens_idx > 0:
    interpretation_cell = {
        'cell_type': 'markdown',
        'metadata': {},
        'source': [
            '#### Interpretation of Sensitivity Analysis:\n',
            '\n',
            '**Analysis Design:**\n',
            '- Tested 3 different random seeds (42, 123, 456) to assess simulation stability\n',
            '- Compared 30-day vs 60-day forecast horizons\n',
            '- Initial portfolio value: $1,000\n',
            '\n',
            '**Key Findings:**\n',
            '\n',
            '| Horizon | Avg Return | Avg Std Dev |\n',
            '|---------|------------|-------------|\n',
            '| 30 days | ~3.4% | ~$83 |\n',
            '| 60 days | ~7.1% | ~$122 |\n',
            '\n',
            '**Observations:**\n',
            '\n',
            '1. **Return Scaling:** 60-day returns (~7.1%) are approximately double 30-day returns (~3.4%), as expected when doubling the time horizon\n',
            '\n',
            '2. **Uncertainty Growth:** Standard deviation increases from ~$83 to ~$122 (47% increase) when doubling the horizon - uncertainty grows **faster than returns** (√2 ≈ 1.41)\n',
            '\n',
            '3. **Seed Stability:** Different random seeds produce similar average results, confirming the simulation is stable and not overly sensitive to random number generation\n',
            '\n',
            '**Investment Implication:** While longer investment horizons offer higher expected returns, they also come with disproportionately higher uncertainty. This quantifies the fundamental risk-return tradeoff in investing.\n'
        ]
    }
    new_cells.append((sens_idx + 1, interpretation_cell))

# Insert new cells in reverse order to maintain correct indices
new_cells.sort(key=lambda x: x[0], reverse=True)
for idx, cell in new_cells:
    nb['cells'].insert(idx, cell)

# Write the updated notebook
with open('Task_3.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print('Notebook updated with detailed interpretations!')
