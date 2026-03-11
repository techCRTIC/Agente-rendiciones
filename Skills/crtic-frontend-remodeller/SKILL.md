---
name: crtic-frontend-remodeller
description: Automated workflow to review a project's frontend files and README, restyle them using the CRTIC brand guidelines (Esencia CRTIC), and generate a stylish HTML documentation page. Use this when asked to rebrand, restyle, or document a project for CRTIC.
license: Complete terms in LICENSE.txt
---

# CRTIC Frontend Remodeller Workflow

This skill provides an automated workflow to take any existing project instance, analyze its frontend components and `README.md`, re-style the entire UI to match the official CRTIC brand essence, and finally generate a stunning, standalone HTML documentation page.

## The Workflow

When triggered to rebrand or restyle a project, you MUST follow these exact steps sequentially:

### Step 1: Project Discovery & Analysis
1. Scan the project directory to identify all relevant visual and frontend files.
   - Look for `README.md`, `index.html`, CSS files (`index.css`, `App.css`), and UI components (React/Vue/Svelte or plain JS/TS).
   - Read the `README.md` to deeply understand what the project does, its purpose, and its audience. 
   - Identify the current styling approach (Tailwind, vanilla CSS, etc.).

### Step 2: Absorb the CRTIC Essence & Design Principles
1. Read `references/esencia-crtic.md` to understand the exact brand colors (Manrope font, white/light theme, orange and teal accents), and the **CRTIC tone of voice** (Accessible, Professional, Inspiring, and Clear).
2. Read `references/frontend-design.md` to understand the principles of creating bold, non-generic, high-end interfaces.
   - **Crucial Rule**: You must combine the strict CRTIC brand guidelines with the bold, maximalist/refined design principles to create something truly unforgettable. Do not create "AI slop". 

### Step 3: Rewrite and Enhance the README
1. Evaluate the `README.md` file found in the project.
2. If the `README.md` is missing, incomplete, or lacks a professional structure:
   - **Rewrite it completely from scratch** to thoroughly document everything the project does in its current state.
   - Use the **CRTIC Brand Voice** (Professional, forward-looking, emphasizing innovation, creativity, and the "Ecosistema Tecnocreativo").
   - Ensure the README includes: a strong visionary header, project overview, technical architecture, and visual aesthetics notes (referencing the CRTIC styling applied).
3. If it exists but lacks the brand tone, refactor the copy so it reads with the voice of CRTIC.

### Step 4: Frontend Code Restyling
1. Rewrite the CSS/Tailwind configurations to inject the CRTIC color palette and typography (Manrope).
2. Update the structural frontend files (HTML/JSX/TSX). 
   - Change border-radiuses to 0px (sharp corners).
   - Use the high-contrast light theme.
   - Apply the energetic orange (`#ff4613`) and teal (`#3bd4ae`) for primary CTAs and highlights.
   - Ensure the layout is bold, readable, and breathes with ample whitespace.

### Step 5: Project Hygiene & Cleanup
1. **Review and Remove Junk:** Scan the project for unused files, redundant placeholder images, `console.log` statements in production files, dead code, or temporary generated files (like `.tmp` artifacts that shouldn't be versioned).
2. **Refactor:** Ensure the directory structure is clean, logical, and removes any irrelevant files that do not serve the application's final vision. The cleaner the repo, the more professional it looks.

### Step 6: Generate the Showcase Documentation
1. Create a breathtaking, standalone HTML page named `Documentacion-del-proyecto.html` and place it strictly in the **project root** directory. **Never** name it `index.html` and avoid creating a separate `docs/` folder to prevent routing and naming conflicts.
2. This page MUST be a single HTML file containing its own CSS (for portability) that explains the project's features, architecture, and usage as found in the `README.md`.
3. Apply the `frontend-design.md` principles heavily here: use staggered animations, bold typography scales, and a unique spatial composition. It should look like an award-winning landing page for the project.

### Step 7: Repo Professionalization (CRTIC Standard)
To ensure the project repository is world-class, production-ready, and aligns with the Red Tecnocreativa standards, execute the following:
1. **Repository Setup Check:** Check if the root directory is already a git repository. If it is NOT, **explicitly ask the user**: *"El código actual no es un repositorio git. ¿Te gustaría que ejecute `git init` en la raíz para respaldar todo el ecosistema y la aplicación visual juntos?"*. Do not proceed with `git init` until they confirm.
2. **Governance & Collaboration:** Generate `CONTRIBUTING.md` (how to PR/report bugs in CRTIC style), `CODE_OF_CONDUCT.md` (CRTIC ethical standards), and a `LICENSE` file (e.g., MIT) if missing.
3. **README Enrichment (Landing Page):** Inject dynamic GitHub badges at the top of the README (Node version, Build status, License, CRTIC Ecosystem tag). Add a Mermaid diagram (````mermaid`) visualizing the project's technical architecture. Always include a link to [Mermaid Live Editor](https://mermaid.ai/web/) directly below the diagram so non-technical users can easily visualize and edit the architecture.
4. **README Enrichment (Non-Technical Guide):** Ensure the README includes a 'Guía de Archivos para No Programadores' (Guide for Non-Programmers). This section should explain, in simple terms, the purpose of all repository management files (e.g., `.gitignore`, `.github/workflows`, `LICENSE`, `CONTRIBUTING.md`, etc.) so non-technical ecosystem members can understand the repository structure without confusion.
5. **Integrated Automation:** Create a `.github/workflows/ci.yml` file to enable basic GitHub Actions CI (build/test checks) to display a solid green checkmark. Add basic issue templates in `.github/ISSUE_TEMPLATE/`.
6. **Code Aesthetics & Hygiene:** Inject strict `.prettierrc` and `.eslintrc.js` files if missing so future collaborators maintain pristine code. Ensure a robust `.gitignore` is present (excluding `node_modules`, `.tmp`, testing environments, etc.).
7. **Brand Identity (Logo):** You MUST prominently include the official CRTIC logo (`references/Logo naranjo MR.png`) at the top of the generated `README.md` and the `Documentacion-del-proyecto.html` files. The logo must be sized appropriately and centered to serve as the visual anchor for the project.

---

## References

**For exact colors, fonts, and brand voice:**
See [references/esencia-crtic.md](references/esencia-crtic.md)

**For aesthetic execution, animations, and bold styling rules:**
See [references/frontend-design.md](references/frontend-design.md)
