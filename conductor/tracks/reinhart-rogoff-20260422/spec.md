# Track Specification: Task 4 - Reinhart Rogoff Analysis

## Overview
This track replicates and critiques Reinhart and Rogoff (2010) "Growth in a Time of Debt" paper, following the course task instructions. It analyzes the original findings, the Herndon et al. (2014) critique, provides correct replication results, and reflects on policy implications.

## Task Requirements (from CDA_2026_Task4.md)

### Part 1: Original Paper Summary
- Read RR 2010 paper
- Write short paragraph summarizing findings and main policy implications
- Reference "Age of Austerity" context and related articles

### Part 2: Critique Paper Explanation  
- Read Herndon et al. (2014) critique
- Write short paragraph explaining why original results may not hold
- Discuss implications of Herndon et al. findings for replication

### Part 3: Replication Analysis
- Use Steven V. Miller's GitHub repo (svmiller/reinhart-rogoff)
- Show "true" results without exclusions and data manipulations
- Document steps required to reproduce RR original results
- Alternatively use vincentarelbundock/Reinhart-Rogoff Python package

### Part 4: Reflection
- Read blog post on "The Reinhart-Rogoff Excel Error Debate"
- Write paragraph on growth-debt nexus and policy use today

## Functional Requirements

### FR1: Data Retrieval
- Load data from replication sources:
  - svmiller/reinhart-rogoff GitHub (R format)
  - vincentarelbundock/Reinhart-Rogoff Python package
- Document data source and version

### FR2: RR Original Results
- Calculate mean GDP growth by debt category (as RR did):
  - 0-30% debt/GDP
  - 30-60% debt/GDP  
  - 60-90% debt/GDP
  - 90%+ debt/GDP
- Show RR's reported results: 4.1%, 2.8%, 2.8%, -0.1%

### FR3: Herndon et al. Corrections
- Apply corrections:
  1. Fix excel errors (formula errors in original)
  2. Include all available data (no selective exclusions)
  3. Use standard weighting (not unconventional)
- Show corrected results: ~2.2% for 90%+ category

### FR4: Additional Analysis
- Examine variation by time period
- Examine variation by country
- Compare median vs mean results

### FR5: Visualization
- Bar chart: GDP growth by debt category (RR vs corrected)
- Time series plot showing debt and growth over time
- Country-specific analysis

## Acceptance Criteria
1. Task 4 notebook executes from top to bottom without errors
2. All four parts answered with clear paragraphs
3. Data visualizations with proper labels
4. Code comments explain the analysis
5. Conclusions answer the specific questions posed
6. All sources documented

## Technical Requirements
- Python 3.14+
- Use pandas for data manipulation
- Use matplotlib for visualizations
- Use statsmodels or scipy for basic statistics

## Deliverables
- Jupyter notebook: `tasks/Task 4/Task_4.ipynb`
- Code that reproduces both RR and corrected results
- Clear markdown explanations for each part