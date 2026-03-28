# Project Workflow

## Guiding Principles

1. **The Plan is the Source of Truth:** All work must be tracked in `plan.md`
2. **The Tech Stack is Deliberate:** Changes to the tech stack must be documented in `tech-stack.md` *before* implementation
3. **Data Analysis Focused:** This is a data analysis project - prioritize reproducible, well-documented analysis over traditional software testing
4. **Code Coverage:** No formal test coverage requirement (data analysis project)
5. **User Experience First:** Every decision should prioritize user experience
6. **Non-Interactive & CI-Aware:** Prefer non-interactive commands. Use `CI=true` for watch-mode tools (tests, linters) to ensure single execution.

## Task Workflow

All tasks follow a strict lifecycle:

### Standard Task Workflow

1. **Select Task:** Choose the next available task from `plan.md` in sequential order

2. **Mark In Progress:** Before beginning work, edit `plan.md` and change the task from `[ ]` to `[~]`

3. **Implement the Analysis:**
   - Write clear, well-documented code that follows the product guidelines
   - For data analysis tasks: ensure reproducibility and clear explanations
   - Include markdown cells explaining the purpose and findings of each analysis step

4. **Verify the Analysis:**
   - Ensure the notebook executes from top to bottom without errors
   - Verify that all visualizations are properly labeled and interpreted
   - Check that conclusions are supported by the data

5. **Refactor (Optional but Recommended):**
   - Improve code clarity and remove duplication
   - Ensure variable names are meaningful and reflect the economic/statistical context
   - Verify that documentation is clear and complete

6. **Document Deviations:** If implementation differs from tech stack:
   - **STOP** implementation
   - Update `tech-stack.md` with new design
   - Add dated note explaining the change
   - Resume implementation

7. **Commit Code Changes:**
   - Stage all code changes related to the task.
   - Propose a clear, concise commit message e.g, `feat(analysis): Add IRS data preprocessing and summary statistics`.
   - Perform the commit.

8. **Commit Frequency:** Changes are committed per phase (not per task) - multiple tasks within a phase can be batched into a single commit.

9. **Record Task Summary in Commit Messages:**
   - Include task summary in the commit message body
   - Format: First line is the conventional commit header, body contains task description and key findings

10. **Get and Record Task Commit SHA:**
    - **Step 10.1: Update Plan:** Read `plan.md`, find the line for the completed task, update its status from `[~]` to `[x]`, and append the first 7 characters of the *just-completed commit's* commit hash.
    - **Step 10.2: Write Plan:** Write the updated content back to `plan.md`.

11. **Commit Plan Update:**
    - **Action:** Stage the modified `plan.md` file.
    - **Action:** Commit this change with a descriptive message (e.g., `conductor(plan): Mark task 'IRS Data Analysis' as complete`).

### Phase Completion Verification and Checkpointing Protocol

**Trigger:** This protocol is executed immediately after a task is completed that also concludes a phase in `plan.md`.

1.  **Announce Protocol Start:** Inform the user that the phase is complete and the verification and checkpointing protocol has begun.

2.  **Verify Notebook Execution:**
    -   **Step 2.1: Determine Phase Scope:** To identify the files changed in this phase, you must first find the starting point. Read `plan.md` to find the Git commit SHA of the *previous* phase's checkpoint. If no previous checkpoint exists, the scope is all changes since the first commit.
    -   **Step 2.2: List Changed Files:** Execute `git diff --name-only <previous_checkpoint_sha> HEAD` to get a precise list of all files modified during this phase.
    -   **Step 2.3: Verify Notebook Execution:** For each Jupyter notebook (`.ipynb`) file in the list:
        -   Ensure the notebook executes from top to bottom without errors
        -   Verify that all outputs are current (not stale)
        -   Check that markdown cells provide clear explanations

3.  **Manual Verification Plan:**
    -   **CRITICAL:** To generate the plan, first analyze `product.md`, `product-guidelines.md`, and `plan.md` to determine the user-facing goals of the completed phase.
    -   You **must** generate a step-by-step plan that walks the user through the verification process, including specific expected outcomes.
    -   The plan you present to the user **must** follow this format:

        **For a Data Analysis Task:**
        ```
        For manual verification of the phase, please follow these steps:

        **Manual Verification Steps:**
        1.  **Open the notebook:** `tasks/Task X/Task_X.ipynb` in Jupyter or VS Code
        2.  **Run all cells:** Execute "Run All" to verify the notebook runs without errors
        3.  **Confirm the outputs:** Check that all visualizations display correctly and conclusions match the expected analysis results
        ```

4.  **Await Explicit User Feedback:**
    -   After presenting the detailed plan, ask the user for confirmation: "**Does this meet your expectations? Please confirm with yes or provide feedback on what needs to be changed.**"
    -   **PAUSE** and await the user's response. Do not proceed without an explicit yes or confirmation.

5.  **Create Checkpoint Commit:**
    -   Stage all changes. If no changes occurred in this step, proceed with an empty commit.
    -   Perform the commit with a clear and concise message (e.g., `conductor(checkpoint): Checkpoint end of Phase X`).

6.  **Record Verification in Commit Message:**
    -   Include the verification steps and user confirmation in the commit message body

7.  **Get and Record Phase Checkpoint SHA:**
    -   **Step 7.1: Get Commit Hash:** Obtain the hash of the *just-created checkpoint commit* (`git log -1 --format="%H"`).
    -   **Step 7.2: Update Plan:** Read `plan.md`, find the heading for the completed phase, and append the first 7 characters of the commit hash in the format `[checkpoint: <sha>]`.
    -   **Step 7.3: Write Plan:** Write the updated content back to `plan.md`.

8.  **Commit Plan Update:**
    -   **Action:** Stage the modified `plan.md` file.
    -   **Action:** Commit this change with a descriptive message following the format `conductor(plan): Mark phase '<PHASE NAME>' as complete`.

9.  **Announce Completion:** Inform the user that the phase is complete and the checkpoint has been created.
    - **Action:** Stage the modified `plan.md` file.
    - **Action:** Commit this change with a descriptive message following the format `conductor(plan): Mark phase '<PHASE NAME>' as complete`.

10.  **Announce Completion:** Inform the user that the phase is complete and the checkpoint has been created, with the detailed verification report attached as a git note.

### Quality Gates

Before marking any task complete, verify:

- [ ] Notebook executes from top to bottom without errors
- [ ] All visualizations are properly labeled and interpreted
- [ ] Code follows project's code style guidelines (as defined in `code_styleguides/`)
- [ ] All code cells are documented with clear markdown explanations
- [ ] Data processing steps are reproducible
- [ ] Conclusions are supported by the analysis
- [ ] No hardcoded absolute paths (use relative paths for data files)
- [ ] Documentation updated if needed
- [ ] No sensitive data committed (API keys, credentials)

## Development Commands

### Setup
```bash
# Install Python dependencies
pip install -r requirements.txt

# Verify Python version (3.14+ recommended)
python --version
```

### Daily Development
```bash
# Run a Jupyter notebook (non-interactive execution)
jupyter execute tasks/Task_X/Task_X.ipynb

# Or open notebook in Jupyter Lab
jupyter lab

# List installed packages
pip list

# Check for package updates
pip list --outdated
```

### Before Committing
```bash
# Verify notebook can be executed without errors
jupyter execute tasks/Task_X/Task_X.ipynb

# Check git status
git status

# Review changes
git diff
```

## Analysis Verification

### Notebook Execution
- All notebooks must execute from top to bottom without errors
- Outputs should be current and match the code
- Markdown cells should explain the analysis steps

### Data Verification
- Verify data sources are correctly loaded
- Check for missing values and document handling
- Validate data types and ranges

### Visualization Quality
- All plots have descriptive titles
- Axes are properly labeled with units where applicable
- Color choices are accessible and clear
- Key insights are highlighted in markdown

## Code Review Process

### Self-Review Checklist
Before marking a task as complete:

1. **Analysis Correctness**
   - Analysis follows the task requirements
   - Statistical methods are appropriate
   - Conclusions are supported by the data

2. **Code Quality**
   - Follows Python style guide
   - DRY principle applied
   - Clear variable/function names
   - Markdown cells explain the analysis

3. **Notebook Execution**
   - Notebook runs from top to bottom without errors
   - All outputs are current
   - Visualizations display correctly

4. **Data Handling**
   - No hardcoded absolute paths
   - Data files referenced with relative paths
   - Missing values handled appropriately

5. **Documentation**
   - Each section has explanatory markdown
   - Visualizations have titles and axis labels
   - Key findings are summarized

## Commit Guidelines

### Message Format
```
<type>(<scope>): <description>

[optional body with task summary]
```

### Types
- `feat`: New analysis or feature
- `fix`: Bug fix or correction
- `docs`: Documentation only (markdown updates)
- `style`: Formatting, code style improvements
- `refactor`: Code restructuring without changing results
- `chore`: Maintenance tasks (dependency updates, etc.)

### Examples
```bash
git commit -m "feat(task1): Add Sala-i-Martin regression analysis"
git commit -m "fix(data): Correct CSV parsing for semicolon separator"
git commit -m "docs(task2): Add interpretation for marginal effects plots"
```

## Definition of Done

A task is complete when:

1. Analysis implemented to specification
2. Notebook executes without errors
3. Visualizations are properly labeled
4. Markdown documentation is complete
5. Code follows project style guidelines
6. Task summary added to commit message
7. `plan.md` updated with commit SHA

## Emergency Procedures

### Critical Bug in Production
1. Create hotfix branch from main
2. Write failing test for bug
3. Implement minimal fix
4. Test thoroughly including mobile
5. Deploy immediately
6. Document in plan.md

### Data Loss
1. Stop all write operations
2. Restore from latest backup
3. Verify data integrity
4. Document incident
5. Update backup procedures

### Security Breach
1. Rotate all secrets immediately
2. Review access logs
3. Patch vulnerability
4. Notify affected users (if any)
5. Document and update security procedures

## Deployment Workflow

### Pre-Deployment Checklist
- [ ] All tests passing
- [ ] Coverage >80%
- [ ] No linting errors
- [ ] Mobile testing complete
- [ ] Environment variables configured
- [ ] Database migrations ready
- [ ] Backup created

### Deployment Steps
1. Merge feature branch to main
2. Tag release with version
3. Push to deployment service
4. Run database migrations
5. Verify deployment
6. Test critical paths
7. Monitor for errors

### Post-Deployment
1. Monitor analytics
2. Check error logs
3. Gather user feedback
4. Plan next iteration

## Continuous Improvement

- Review workflow weekly
- Update based on pain points
- Document lessons learned
- Optimize for user happiness
- Keep things simple and maintainable
