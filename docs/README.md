
# 🌍 El-Mahrosa.Teos-Sovereign-System
![License: PolyForm NC + TESL](https://img.shields.io/badge/License-PolyFormNC%20%2B%20TESL-gold)
![CI](https://github.com/Elmahrosa/El-Mahrosa.Teos-Sovereign-System/actions/workflows/ci.yml/badge.svg)
[![License](https://img.shields.io/github/license/Elmahrosa/El-Mahrosa.Teos-Sovereign-System)](LICENSE)
![GitHub issues](https://img.shields.io/github/issues/Elmahrosa/El-Mahrosa.Teos-Sovereign-System)
![License: PolyForm NC + TESL](https://img.shields.io/badge/License-PolyFormNC%20%2B%20TESL-gold)

**Sovereign Blockchain Infrastructure for TEOS Egypt**  
Compliance-first, audit-ready, and aligned with UN SDGs and Egypt’s Vision 2030.

---

## 📌 Table of contents
1. [Overview](#-overview)
2. [Repository structure](#-repository-structure)
3. [Features](#-features)
4. [Tech stack](#-tech-stack)
5. [Getting started](#-getting-started)
6. [Architecture](#-architecture)
7. [Contributing](#-contributing)
8. [Security policy](#-security-policy)
9. [License](#-license)
10. [Author](#-author)

---

## 🏛 Overview
El-Mahrosa.Teos-Sovereign-System is the sovereign backbone of TEOS Egypt — enforcing governance, compliance, and civic-first infrastructure. It provides modules for treasury, SDG mapping, and compliance automation, with audit transparency baked in.
## 🔗 Ecosystem
- Developer docs: `README.DEV.md`
- Presale portal: `teospump-presale.vercel.app`
- Holder verification: `Solscan snapshot integration (runtime)`
- Founder wallet: `Akvm3CbND...ZhbF (admin treasury)`

---

## 📁 Repository structure
```El-Mahrosa.Teos-Sovereign-System/
├─ README.md                    # Investor-facing overview (with links to Dev README)
├─ README.DEV.md                # Developer-facing quickstart and docs
├─ LICENSE                      # Dual-license notice (PolyForm NC + TESL)
├─ CODE_OF_CONDUCT.md           # Adapted for sovereign mission alignment
├─ CONTRIBUTING.md              # Verified contributors, DCO, SDG mapping
├─ SECURITY.md                  # Vulnerability reporting and disclosure
├─ .gitignore                   # Hygiene and secrets
├─ .env                         # Local environment
├─ package.json                 # Node project manifest
├─ config/
│  ├─ example.settings.yml      # Copyable example
│  └─ settings.yml              # Operational config (gitignored)
├─ src/
│  ├─ sovereignCore.js          # App entry with module mounting
│  ├─ modules/
│  │  ├─ compliance.js          # Compliance gates (DCO, verified, audit)
│  │  ├─ treasury.js            # Treasury endpoints (status, stake intent)
│  │  └─ sdgMapping.js          # SDG registry utilities and endpoints
│  └─ utils/
│     └─ auditLogger.js         # File-based audit log (logs/audit.log)
├─ logs/
│  └─ audit.log                 # Created at runtime
├─ tests/
│  ├─ compliance.test.js        # Middleware tests
│  ├─ treasury.test.js          # Treasury tests
│  └─ sdg.test.js               # SDG mapping tests
├─ docs/
│  ├─ architecture.md           # Diagrams and flow
│  └─ whitepaper.md             # Sovereign governance whitepaper section
└─ .github/
   └─ workflows/
      └─ ci.yml                 # CI: install, lint, test

```

---
# 🇪🇬 El-Mahrosa Sovereign System

## The Core Infrastructure for TEOS Egypt

---

## 📜 Condensed Strategic Summary

The El-Mahrosa Sovereign System is the final consolidated project and operational backbone of the TEOS Egypt ecosystem. It represents a strategic pivot from a foundational blockchain project into a **Compliance-First, Civic-Centered Ecosystem** aligned with **Egypt’s Vision 2030**.

### Executive Vision
- **Mission:** To build a sovereign, secure, and sustainable digital infrastructure for Egypt’s financial and civic future.
- **Anchor:** The Elmahrosa Reserve Token ($ERT), the reserve utility token backed by ecosystem reserves and real-world assets.

---

### 🏛 Foundation: Compliance & Governance
- **Compliance-First Philosophy:** Full alignment with the Central Bank of Egypt (CBE) and national regulators.
- **Digital Sovereignty:** Ownership of infrastructure, identity, and financial systems. This repository houses the modular **Compliance Kit**, featuring audit-ready workflows, badge logic, and Mermaid diagrams for SDG tracking.
- **Sovereign Authority:** Secured by a dual-layer licensing model (**PolyForm Noncommercial + TESL**), ensuring the founder retains commercial rights and sovereign control.

### The Elmahrosa Statement: The Authority
> "He who owns the sovereign infrastructure is the one who sets the rules, not the one who waits for permission. Because we own the sovereign system, we are the licensing authority, not the applicant."

---

## 🌐 TEOS Egypt Ecosystem — Official Link Index

This index serves as the official navigation hub for all projects and components within the TEOS Egypt ecosystem.

### 📜 Core Documentation
- [Whitepaper](https://whitepaper.teosegypt.com )
- [Main Website](https://teosegypt.com )
- [Ecosystem Map of Pi](https://emapofpi6390.pinet.com )

### 🏦 Financial & Banking Layer
- [Bank Portal](https://bank.teosegypt.com )
- BankChain Gateway
- [FPBE (First Pi‑Misr Bank Elmahrosa)](https://firstpimisrbanke1502.pinet.com )
- $ERT Token
- [DEX Exchange](https://niledex7283.pinet.com )
- [Wallet v1](https://teoswallet6613.pinet.com )
- Nilex Exchange

### 🎨 Civic & NFT Layer
- [NFT Platform](https://teosnft9637.pinet.com )
- Studio AI
- [TEOS Pi Taxi dApp](https://teospitaxi.teosegypt.com )
- Earn Portal
- [Pump](https://teospumpeabbdc3939.pinet.com )
- Purchas

### 🌆 Smart‑City & Civic Governance
- [Smart City Portal](https://teospismartcitye8281.pinet.com )
- Fact Portal
- Holders Dashboard
- Hub
- Live Dashboard
- [Mine Portal](https://elmahrosamininga1462.pinet.com )

### 🎁 Campaigns & Community
- Pioneers Portal
- Airdrop
- Pool Tutteos
- Bot

### 🧪 Experimental / Hosting Mirrors
- Hostinger Site 1
- Hostinger Site 2

### 💻 Development Backbone
- [Elmahrosa GitHub Organization](https://github.com/Elmahrosa )

---

## El-Mahrosa.Teos-Sovereign-System 🇪🇬🦀

### 📖 Vision & Sovereign Design
El-Mahrosa Sovereign System is Egypt’s unified Digital Public Infrastructure (DPI) framework by TEOS Egypt, delivering:
- Education modules
- Solana Anchor smart contracts
- API services
- Integration SDKs

All as one deploy-ready package.

Built with **Rust 🦀 + Solana**, the system blends Egyptian heritage with compliant, non-custodial Web3 innovation for regulated finance, governance, and civic learning.

---

### 🗂 Repository Structure
## ✨ Features
- **Compliance enforcement:** DCO, immutable releases, governance labeling  
- **SDG alignment:** Map modules to UN SDGs for civic transparency  
- **Treasury module:** Non-custodial rules for staking and reserves  
- **Audit layer:** Logs, dashboards, and verification workflows  

---

## ⚙ Tech stack
- **Backend:** Node.js (Express) or Rust/Solana for smart contracts  
- **APIs:** GitHub REST + GraphQL (integration layer)  
- **Automation:** GitHub App webhooks and rulesets  
- **Testing:** Jest or Mocha for Node; Anchor tests for Solana modules  

---

## 🚀 Getting started
1. **Clone**:
   ```bash
   git clone https://github.com/Elmahrosa/El-Mahrosa.Teos-Sovereign-System.git
   cd El-Mahrosa.Teos-Sovereign-System
   ```
2. **Copy config**:
   ```bash
   cp config/example.settings.yml config/settings.yml
   ```
3. **Install dependencies** (Node option):
   ```bash
   npm install
   ```
4. **Run tests**:
   ```bash
   npm test
   ```
5. **Start (if Node-based)**:
   ```bash
   node src/sovereignCore.js
   ```

---

## 📊 Architecture
See `docs/architecture.md` for the system flow diagram (sovereign core ↔ modules ↔ audit/dashboard).

---

## 🤝 Contributing
Please read `CONTRIBUTING.md` for verified contributor policy, code quality requirements, and licensing terms.

---

## 🛡 Security policy
Report issues privately as described in `SECURITY.md`. Do not open public issues for vulnerabilities.

---

## 📜 License
Dual-license governance model:
- PolyForm Noncommercial 1.0.0 — open civic use  
- TESL (TEOS Egypt Sovereign License) — commercial rights reserved by the Founder  

Commercial/government use requires written permission from Ayman Seif / Elmahrosa International.

---

## 👤 Author
**Ayman Seif**  
Founder — TEOS Egypt  
Sovereign blockchain infrastructure for compliance, governance & DPI
```

---

### `LICENSE`

```
This project is licensed under a dual-licensing model:

1. PolyForm Noncommercial 1.0.0: For open civic use.
2. TEOS Egypt Sovereign License (TESL): Commercial rights are reserved exclusively for the Founder.

For full license terms, please refer to the respective license documents.

Commercial/Government Use: Requires explicit written permission from Ayman Seif / Elmahrosa International.
```

---

### `CONTRIBUTING.md`

```markdown
# 🏛 Contributing to El-Mahrosa.Teos-Sovereign-System

We welcome contributions that strengthen Digital Public Infrastructure (DPI), compliance, and security — aligned with Egypt’s Vision 2030.

## 🏅 Verified contributor policy
- **Verification required:** Contributors must be verified within the TEOS Egypt ecosystem.
- **Mission alignment:** Changes must serve compliance, governance, SDG integration, or audit transparency.

## ✅ Submission process
1. **Open an issue** describing the change and civic impact.
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/short-title
   ```
3. **Write tests** and ensure CI passes.
4. **Commit with sign-off (DCO)**:
   ```bash
   git commit -s -m "feat: add compliance rule"
   ```
5. **Open a PR** with a clear title, description, and labels (`compliance`, `SDG-mapping`, `treasury` where relevant).

## 🧪 Code quality
- Follow Node.js best practices (or Anchor/Rust for contracts).
- Include unit/integration tests for new logic.
- Keep modules small, documented, and auditable.

## ⚖️ Licensing agreement
By contributing, you agree to license your contributions under the project’s dual-license (PolyForm NC + TESL).
```

---

### `SECURITY.md`

```markdown
# 🛡 Security Policy — El-Mahrosa.Teos-Sovereign-System

## Reporting a vulnerability
Do not open public issues for security vulnerabilities.

Report privately to:
- **Email:** security@elmahrosa.eg
- **Encrypted channel:** [PGP key or secure form link]

We acknowledge within 48 hours and aim to respond fully within 7 days.

## Compliance and audits
Part of the TEOS Egypt Compliance Kit: audit-ready workflows and logs. Regular external audits are performed on core modules.
```

---

### `CODE_OF_CONDUCT.md`

```markdown
# 🌐 Code of Conduct — El-Mahrosa.Teos-Sovereign-System

## Our pledge
We commit to a respectful, inclusive community focused on civic-first outcomes and compliance.

## Standards
- Use welcoming language; respect diverse perspectives
- Accept constructive feedback gracefully
- Focus on mission integrity and audit transparency

## Unacceptable behavior
- Harassment, trolling, or personal attacks
- Publishing private information without consent
- Non-compliant or disruptive contributions

## Enforcement
Report violations to:
- **Email:** conduct@elmahrosa.eg

Complaints will be reviewed promptly and fairly.

## Attribution
Adapted from Contributor Covenant v2.1.
```

---

### `.gitignore`

```gitignore
# Node
node_modules/
npm-debug.log*
yarn.lock

# Env
.env
config/settings.yml

# Logs
logs/
*.log

# Coverage
coverage/

# OS/Editor
.DS_Store
.vscode/
```

---

### `.github/workflows/ci.yml`

```yaml
name: CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '18'
      - name: Install
        run: npm install
      - name: Test
        run: npm test
```

---

### `docs/architecture.md`

```markdown
# Architecture — El-Mahrosa.Teos-Sovereign-System

```mermaid
flowchart TD
    A[Sovereign Core] --> B[Compliance Module]
    A --> C[Treasury Module]
    A --> D[SDG Mapping Module]
    B --> E[Audit Logger]
    C --> E[Audit Logger]
    D --> E[Audit Logger]
    E --> F[Dashboard & Reports]

    A:::core
    B:::mod
    C:::mod
    D:::mod
    E:::audit
    F:::ui

classDef core fill=#0e8a16,fontColor=#ffffff,stroke=#333;
classDef mod fill=#0366d6,fontColor=#ffffff,stroke=#333;
classDef audit fill=#f1c40f,fontColor=#000000,stroke=#333;
classDef ui fill=#6f42c1,fontColor
