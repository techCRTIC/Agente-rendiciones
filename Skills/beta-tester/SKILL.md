---
name: beta-tester
description: Professional Quality Assurance (QA) and environment optimization specialist. Use this skill when the user requests comprehensive debugging, "user testing" simulations, or a cleanup of the development environment (removing unused files, dependencies, or artifacts).
---

# Beta Tester & Environment Optimizer

This skill provides a structured approach to testing software from a user's perspective and keeping the development environment clean and efficient.

## Capabilities

1.  **User-Centric Debugging**: Simulating user interactions to find edge cases and UX logical errors.
2.  **Environment Cleanup**: Analyzing the codebase to identify and remove unused files, dead code, and obsolete artifacts.
3.  **Performance Auditing**: Verifying software fluidity and responsiveness.

## Workflows

### 1. Comprehensive Debugging (User Testing)

When asked to "test" or "debug" as a user:

1.  **Analyze the UI/UX Flow**:
    *   Map out key user stories (e.g., "User creates a new board," "User exports an image").
    *   Identify potential friction points or logical gaps.

2.  **Simulate Interactions**:
    *   Walk through usage scenarios mentally (or using browser tools if available).
    *   Check for feedback on actions (toasts, loading states, error messages).
    *   Verify critical paths (Sign in -> Create -> Save -> Export).

3.  **Report Findings**:
    *   Classify issues: **Critical** (Crashes/Data Loss), **Major** (Broken Functionality), **Minor** (Visual/Cosmetic).
    *   Propose fixes for each issue.

### 2. Environment & Codebase Cleanup

When asked to "clean" the environment or remove unused files:

1.  **Inventory Analysis**:
    *   List all files in the relevant source directories (e.g., `src/`, `public/`).
    *   Identify entry points (e.g., `index.html`, `main.jsx`, `App.jsx`).

2.  **Dependency Graphing**:
    *   Start from entry points and trace all `import` items.
    *   Mark every imported file as "Used".
    *   Any file NOT marked "Used" is a candidate for removal.

3.  **Visual Asset Verification**:
    *   For images/icons, check string references in code (e.g., `src="logo.png"` or `url('/img.jpg')`).
    *   Be careful with dynamic paths.

4.  **Verification**:
    *   **Config Files**: Ensure configuration files (like `tailwind.config.js`, `vite.config.js`) are not falsely flagged.
    *   **Documentation**: Preserve `docs/`, `README.md`, etc., unless explicitly told to remove.

5.  **Action**:
    *   List candidates for deletion to the user.
    *   Ideally, verify removal doesn't break build (run build test if possible).
    *   Delete files upon confirmation.

### 3. Code Quality Review

*   Check for `console.log` leftovers (except in error handling).
*   Check for commented-out blocks of code that are no longer needed.
*   Identify duplicated logic or components.

## Best Practices

*   **Safety First**: When cleaning, err on the side of caution. If unsure if a file is used (e.g., dynamic import), KEEP IT or ask.
*   **User Persona**: Act as a demanding professional user who expects polish, speed, and intuitive design.
*   **Constructive Feedback**: Don't just list bugs; suggest how to polish the experience to a premium level.
