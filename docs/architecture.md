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
