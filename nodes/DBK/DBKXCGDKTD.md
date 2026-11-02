---
tag: DBKXCGDKTD
kind: concept
name: Chaos theory
msc: [37D45, 37N99, 34C28]
sources:
  - url: https://en.wikipedia.org/wiki/Chaos_theory
same_as:
  wikidata: Q166314
  wikipedia: Chaos theory
---

## Summary

Chaos theory studies deterministic [[dynamical systems|BBZP1R872N]] whose long-time behaviour looks random and cannot be predicted in practice.
The key feature is sensitive dependence on initial conditions, the [[butterfly effect|G0ZT1SDQGS]]: tiny differences in the starting state grow until they dominate.
Typical tools are [[Lyapunov exponents|NJ1FJSNK6A]], [[strange attractors|9WKCZGG906]], symbolic dynamics and invariant measures, and a standard mathematical definition of a chaotic map is [[Devaney chaos|21B8AHPD4P]].
Classical examples are the [[Lorenz system|WYRC41CQN9]] in meteorology and the [[logistic map|QN9X9BNKTX]] in population dynamics.

## Explanations

### L1 human

A chaotic system follows exact rules, with no chance involved, and yet its future is practically unpredictable.
The reason is that any small error in the present, such as rounding a measurement, is magnified again and again.
The doubling map $x \mapsto 2x \bmod 1$ shows this well: it shifts the binary digits of $x$ one place to the left.
Two starting values that agree in their first $50$ binary digits give orbits that look unrelated after about $50$ steps.
Weather is the most famous example, which is why forecasts become unreliable after a week or two.
