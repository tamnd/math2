---
tag: Q1MD7W6CT3
kind: concept
name: Piola–Kirchhoff stress tensors
msc: [74A10, 74B20]
sources:
  - url: https://en.wikipedia.org/wiki/Piola%E2%80%93Kirchhoff_stress_tensors
same_as:
  wikidata: Q9291589
  wikipedia: Piola–Kirchhoff stress tensors
---

## Summary

The Piola–Kirchhoff stress tensors express [[stress|HXGCGHS070]] in terms of the undeformed reference configuration of a body.
The first one, $P = J \sigma F^{-T}$, gives the actual force per unit undeformed area; the second one, $S = F^{-1} P$, is symmetric and fully referred to the reference configuration.
Here $\sigma$ is the [[Cauchy stress tensor|KG2XWEMJ30]] and $F$ the [[deformation gradient|HTYRR2WDQ6]], with $J = \det F$; these tensors are the natural stress measures in large-deformation problems.

## Explanations

### L1 human

When a rubber sample is stretched, its cross-section shrinks.
Engineers often divide the force by the original area, which they know, rather than by the current area, which changes.
The first Piola–Kirchhoff stress is exactly this force per original area.
The second Piola–Kirchhoff stress goes one step further and also pulls the force back to the original shape, which makes formulas symmetric and convenient.
