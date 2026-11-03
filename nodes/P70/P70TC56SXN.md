---
tag: P70TC56SXN
kind: definition
name: Phase diagram
msc: [80A22, 82B26, 80A10]
defines: R6XCQYXKRP
uses: [6WJ0NADBT4, WVH4PVW64P, 5EKTEE00FZ, H9F9CNPBSN]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_diagram
---

## Definition

Consider a pure substance that can exist in phases $\alpha_1, \dots, \alpha_k$ (in the sense of [[phase transition|6WJ0NADBT4]]).
For each phase $\alpha_i$, let $\mu_i(T, p)$ be its [[chemical potential|WVH4PVW64P]] as a function of the temperature $T$ and the pressure $p$.
The *phase diagram* of the substance is the $(T, p)$ plane with each point labelled by certain phases.
The labels of $(T, p)$ are the phases $\alpha_i$ for which $\mu_i(T, p)$ is the smallest of $\mu_1(T, p), \dots, \mu_k(T, p)$.
These are the phases present in [[thermodynamic equilibrium|5EKTEE00FZ]] at $(T, p)$.

## Remarks

A point labelled by one phase lies in a region of that phase.
A point labelled by two phases lies on a *coexistence curve*, where the two chemical potentials are equal.
A point labelled by three phases is a triple point.
For water, the point $T = 298.15\,\mathrm{K}$, $p = 101.325\,\mathrm{kPa}$ is labelled liquid, because liquid water has the smallest chemical potential there.
A non-example: labelling each point by the phase of largest molar volume does not give the phase diagram.
At room conditions that rule would pick vapour, while the phase of least chemical potential of water there is liquid.
For mixtures one also uses compositions as axes, together with other [[intensive variables|H9F9CNPBSN]] such as the mole fractions.
