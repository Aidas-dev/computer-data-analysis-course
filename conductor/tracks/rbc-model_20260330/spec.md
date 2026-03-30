# Track Specification: Economics RBC Model Task

## Overview
This track implements a Real Business Cycle (RBC) style business cycle analysis using the Hodrick-Prescott (HP) filter for the United States, Argentina, and Lithuania. The analysis follows the exercise instructions from `rbc_hp_exercise.pdf` and uses World Bank API data retrieved via the `wbgapi` Python package.

## Functional Requirements

### FR1: Data Retrieval
- Download annual World Bank data for three countries (US, Argentina, Lithuania)
- Required indicators:
  - Real GDP: `NY.GDP.MKTP.KN`
  - Real household consumption: `NE.CON.PRVT.KN`
  - Real gross capital formation (investment): `NE.GDI.TOTL.KN`
  - Labor force: `SL.TLF.TOTL.IN`
  - Employment ratio: `SL.EMP.TOTL.SP.ZS`
- Data period: Maximum available range from World Bank API

### FR2: Cyclical Volatility Analysis (Section 1)
- **1.1 Plot Raw Series**: Create log plots of GDP, consumption, and investment for each country
- **1.2 Apply HP Filter**: Extract cyclical components using HP filter with λ=100 (annual data)
- **1.3 Compute RBC-style Moments**: Calculate for each country:
  - Standard deviations of GDP, consumption, and investment cycles
  - Relative volatilities: sd(consumption)/sd(output), sd(investment)/sd(output)
  - Correlations with output

### FR3: Total Factor Productivity Analysis (Section 2) - US Only
- **2.1 Construct TFP**: 
  - Compute employment: N_t = labor force × (employment ratio / 100)
  - Construct capital stock using perpetual inventory method with δ=0.06
  - Compute TFP from Cobb-Douglas: ln(A_t) = ln(Y_t) - α·ln(K_t) - (1-α)·ln(N_t), with α=1/3
- **2.2 TFP Cyclicality**:
  - Apply HP filter to ln(Y) and ln(A)
  - Plot cyclical components of GDP and TFP together
  - Compute sd(GDP cycle), sd(TFP cycle), correlation(GDP cycle, TFP cycle)

### FR4: Visualization & Documentation
- All plots must have descriptive titles and labeled axes
- Comparative visualizations across three countries
- Markdown cells must summarize and interpret all results
- Conclusions must answer the questions posed in the PDF exercise

## Non-Functional Requirements
- **Reproducibility**: All code must execute from top to bottom without errors
- **Documentation**: Markdown cells must explain each analysis step and interpret results
- **Data Handling**: Use relative paths for any local data files
- **Code Style**: Follow project code style guidelines

## Acceptance Criteria
1. Notebook successfully retrieves data from World Bank API using `wbgapi`
2. All raw series plots are generated with proper labels
3. HP filter correctly applied with λ=100 for annual data
4. RBC-style moments table computed for all three countries
5. TFP constructed for US using perpetual inventory method
6. TFP cyclicality analysis completed with correlation analysis
7. All visualizations display correctly
8. Conclusions provided for each analysis section answering the PDF questions
9. Task-specific requirements.txt created with wbgapi dependency

## Out of Scope
- Extending analysis to additional countries beyond the three specified
- Using local data files as primary data source (World Bank API is primary)
- Building full RBC DSGE model (this is empirical analysis only)

## Technical Notes
- HP filter smoothing parameter: λ = 100 (for annual data)
- Capital depreciation rate: δ = 0.06
- Capital share parameter: α = 1/3
- Package: `wbgapi>=1.0` for World Bank API access
- Package: `statsmodels>=0.14` for HP filter
