# RouteForge BDD Studio v1.0 Enterprise 🚀

> **Multi-Format Data Modeling & Behavioral Requirement Engineering Studio**  
> Architected & Developed by **Pratyush Ranjan Mishra**  
> 🔗 **LinkedIn**: [linkedin.com/in/leadtherightway](https://www.linkedin.com/in/leadtherightway/) | 🐙 **GitHub**: [github.com/geekpratyush](https://github.com/geekpratyush)

---

## 🌟 Overview

**RouteForge BDD Studio v1.0 Enterprise** is a high-performance, zero-dependency browser application designed by **Pratyush Ranjan Mishra** for Business Analysts (BAs), Solution Architects, and QA Engineering teams.

Unlike conventional BDD tools that enforce rigid JSON structures, **RouteForge BDD Studio** grants BAs total freedom to model **any data format** (ISO 20022 XML, SWIFT MT blocks, NACHA ACH fixed-width flat files, JSON, and YAML) directly inside Gherkin feature files.

---

## ✨ Key Features

- **🌐 Multi-Format Payload Editor**:
  - **ISO 20022 XML**: Model `pacs.008`, `camt.053`, SOAP messages with full XML tag structures.
  - **SWIFT MT & FlatFiles**: SWIFT MT103/MT202 message blocks, NACHA ACH fixed-width line records, ISO 8583 card settlement lines, pipe/comma CSV.
  - **JSON & YAML**: Microservices payloads, credit facility trees, and risk policy maps.
  - **⚡ 1-Click Payload Presets**: Built-in sample templates for immediate BA productivity.

- **📂 Local Project Directory Integration**:
  - Native browser File System Access API scanning (`📂 Open Project Folder`).
  - Automatically loads and groups multi-folder project trees with a top workspace tab bar.

- **🏦 Enterprise Banking & Payment Templates**:
  - **Clearing Line Utilization & Intraday Queueing**: Intraday exposure limit validation.
  - **Excess Approval & Hierarchy Escalation**: Dual sign-off threshold matrices.
  - **Daily Overdraft & Limit/Sublimit Engine**: Earmarking holds and settlement releases.
  - **ISO 20022 MX Pacs.008 XML to SWIFT Transformation**: Message translation modeling.
  - **Sanctions Screening & Message Quarantine**: OFAC and UN fuzzy list matching logic.

- **⚡ Interactive 1-Click Permutation Simulation**:
  - Execute test scenario runs step-by-step.
  - Real-time substitution of `<placeholder>` variables in XML, SWIFT, and JSON payloads using row data from Examples tables.

- **📊 Visual Flow & Gherkin Export**:
  - Instant visual node diagram rendering of scenario steps.
  - Export standard, fully compliant `.feature` Gherkin files with language-tagged DocStrings (`"""xml`, `"""swift`, `"""flatfile`).

---

## 🚀 Live Demo & GitHub Pages Setup

### Option 1: Direct Web Access
Host this zero-dependency static studio directly on GitHub Pages!

1. Go to your GitHub repository settings: `https://github.com/geekpratyush/BDDModeler/settings/pages`
2. Under **Build and deployment** > **Source**, select **`Deploy from a branch`**.
3. Choose branch: **`main`** / Folder: **`/ (root)`**.
4. Click **Save**.
5. Your live app will be published at:  
   👉 **`https://geekpratyush.github.io/BDDModeler/`**

---

## 🛠️ Local Development & Quick Start

Since **RouteForge BDD Studio** is a pure HTML5/JavaScript application with zero node_modules or build dependencies:

```bash
# 1. Clone the repository
git clone https://github.com/geekpratyush/BDDModeler.git

# 2. Navigate to directory
cd BDDModeler

# 3. Open index.html in any modern browser (Chrome, Edge, Opera, Safari)
open index.html   # macOS
# OR
xdg-open index.html   # Linux
```

---

## 📦 How to Push to GitHub

Run the following commands in your terminal to initialize and push this project to your GitHub repository (`geekpratyush/BDDModeler`):

```bash
# Initialize git repository
git init

# Configure user identity
git config user.name "Pratyush Ranjan Mishra"
git config user.email "leadtherightway@gmail.com" # (or your GitHub email)

# Add files and commit
git add .
git commit -m "feat: initial release of RouteForge BDD Studio v1.0 Enterprise by Pratyush Ranjan Mishra"

# Set main branch and remote
git branch -M main
git remote add origin https://github.com/geekpratyush/BDDModeler.git

# Push to GitHub
git push -u origin main
```

---

## 📄 License & Attribution

Architected & Developed by **Pratyush Ranjan Mishra**.  
Connect on [LinkedIn](https://www.linkedin.com/in/leadtherightway/) or check out more projects on [GitHub](https://github.com/geekpratyush).
