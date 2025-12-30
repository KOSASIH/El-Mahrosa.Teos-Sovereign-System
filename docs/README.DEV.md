# 🛠 Developer Setup Guide: El-Mahrosa Sovereign System

This guide provides detailed instructions for setting up your development environment for the **El-Mahrosa Sovereign System**, which supports both **Node.js** (for APIs/UI) and **Rust/Solana** (for smart contracts).

---

## 📁 Repository Structure

```
El-Mahrosa.Teos-Sovereign-System/
├─ README.md                    # Investor-facing overview
├─ README.DEV.md                # This file
├─ LICENSE                      # Dual-license notice
├─ CONTRIBUTING.md              # Verified contributors, DCO, SDG mapping
├─ SECURITY.md                  # Vulnerability reporting and disclosure
├─ AUDIT.md                     # Audit log format and retention policy
├─ ROADMAP.md                   # Future milestones and civic goals
├─ config/
│  ├─ example.settings.yml      # Example configuration file
├─ src/                         # Core source code
│  ├─ modules/                  # Compliance, Treasury, SDG Mapping modules
├─ contracts/                   # Solana Anchor smart contracts (Rust)
├─ tests/                       # Unit and integration tests
├─ docs/                        # Architecture, Whitepaper sections
```

---

## ⚙ Tech Stack

- **Backend/API:** Node.js (Express)
- **Smart Contracts:** Rust (Solana Anchor Framework)
- **Testing:** Jest (Node.js), Anchor Test Framework (Rust)
- **Code Style:** ESLint (Node.js), Clippy (Rust)

---

## 🚀 Getting Started: Node.js Environment

### Prerequisites
- Node.js (v18+)
- npm

### Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/Elmahrosa/El-Mahrosa.Teos-Sovereign-System.git
   cd El-Mahrosa.Teos-Sovereign-System
   ```

2. **Copy and edit the config file:**
   ```bash
   cp config/example.settings.yml config/settings.yml
   # Edit `config/settings.yml` with your local environment variables
   ```

3. **Install dependencies (deterministic build):**
   ```bash
   npm ci
   ```

4. **Run tests:**
   ```bash
   npm test
   ```

5. **Start the API:**
   ```bash
   node src/sovereignCore.js
   ```

---

## 🦀 Getting Started: Rust/Solana Environment

### Prerequisites
- [Install Rust](https://www.rust-lang.org/tools/install)
- [Install Solana Tool Suite](https://docs.solana.com/cli/install)
- [Install Anchor](https://www.anchor-lang.com/docs/installation)

### Steps
1. **Set the Rust toolchain:**
   ```bash
   rustup default stable
   ```

2. **Build contracts:**
   ```bash
   anchor build
   ```

3. **Run contract tests:**
   ```bash
   anchor test
   ```

---

## 🧪 Testing and Quality

- **Unit Tests:** Run with `npm test` (Node) or `anchor test` (Rust).
- **Code Style:** Enforced via **ESLint** (Node) and **Clippy** (Rust).
- **Test Coverage:** Aim for **90%+ coverage**. See the badge in the main `README.md`.
