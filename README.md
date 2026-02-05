# Sovereign Quantum Architecture Primitives (SQAP)

> **Status:** SEALED (Cycle 3 Complete)
> **Owner:** System Direction

## Overview
This repository contains the foundational "physics" for a Sovereign Quantum Architecture. [cite_start]It implements a state evolution engine that mimics quantum mechanical constraints: no hidden global state, observation-only inputs, and irreversible collapse[cite: 4].

## Directory Structure
* `src/primitives`: Immutable data structures (`Observation`, `QuantumState`).
* `src/engine`: Pure logic cores (`Evolution`, `Collapse`, `Causality`).
* `tests/`: Abuse testing and invariant validation.
* `docs/`: Formal specifications and proofs.

## Quick Start
To validate the system integrity and invariants:

```bash
# Run the Cycle 1 Abuse Test (Time Paradox & Cloning)
python -m tests.test_invariants

# Run the Cycle 2 Measurement Test (Entropy & Collapse)
python -m tests.test_collapse

# Run the Cycle 3 Final Seal (Integration & Compensation)
python -m tests.test_integration