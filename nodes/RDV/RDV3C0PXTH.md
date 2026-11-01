---
tag: RDV3C0PXTH
kind: definition
name: Local field
msc: [11S99, 12J25]
defines: J85FZEQG38
uses: [04C5ZBG1WT, 0FFXKTKKQC, 0FE2SB8WVJ, BT6T702C28, MGM3CNJW9V, NJ3APQ8BHH]
sources:
  - url: https://en.wikipedia.org/wiki/Local_field
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] with an [[absolute value|0FFXKTKKQC]] $\abs{\cdot}$ that is nontrivial, that is, $\abs{x} \neq 1$ for some $x \neq 0$.
Give $K$ the topology of the metric $d(x, y) = \abs{x - y}$.
Then $K$ is a *local field* if $K$ is a [[locally compact space|0FE2SB8WVJ]] for this topology.

## Remarks

A local field is Archimedean when it is $\R$ or $\C$, and non-Archimedean otherwise.
Many authors use "local field" only for the non-Archimedean case.
A non-Archimedean field is a local field exactly when it is complete for a discrete valuation and its [[residue field|NJ3APQ8BHH]] is finite.
The non-Archimedean local fields of characteristic $0$ are the finite extensions of the fields $\Q_p$.
Those of characteristic $p$ are the fields $\F_q((t))$ with $q$ a power of $p$.
Example: $\Q_p$ is a local field, because the ball $\Z_p$ is a compact neighbourhood of $0$.
Non-example: $\Q$ with $\abs{\cdot}_p$ is not a local field, because it is not complete, and a field with such an absolute value is locally compact only when complete.
Non-example: $\C((t))$ is complete for a discrete valuation, but its residue field $\C$ is infinite, so it is not locally compact.
