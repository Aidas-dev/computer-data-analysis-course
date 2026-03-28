# Product Guidelines

## Documentation Style
- **Tutorial-style:** Notebooks should include step-by-step explanations with code comments and learning notes
- Write for a self-learner audience—explain not just what the code does, but why
- Include brief summaries at the end of each major section

## Code Quality
- Follow general PEP 8 guidelines without strict tooling enforcement
- Prioritize readable, working code that clearly demonstrates the analysis
- Use meaningful variable names that reflect the economic/statistical context
- Keep cells focused on a single logical operation

## Notebook Organization
- **Sectioned structure:** Use clear markdown headers to separate:
  1. Data Loading
  2. Data Processing/Cleaning
  3. Exploratory Analysis
  4. Modeling/Regression
  5. Visualization
  6. Conclusions
- Include a table of contents for longer notebooks
- Number major sections for easy reference

## Visualization Style
- **Exploratory focus:** Create visualizations primarily for understanding data patterns
- Include axis labels, titles, and brief interpretations of what each plot shows
- Use seaborn for consistent, clean styling
- Prioritize clarity over aesthetic complexity

## Reproducibility
- All notebooks should be executable from top to bottom without errors
- Document any manual steps or external data preparation required
- Use relative paths for data files within the repository
- Pin dependency versions in requirements.txt for consistent results
