---
tag: XW8YWJ9TNS
kind: concept
name: Stability radius
msc: [93D09, 15A18, 93B35]
sources:
  - url: https://en.wikipedia.org/wiki/Stability_radius
same_as:
  wikidata: Q7595729
  wikipedia: Stability radius
---

## Summary

The stability radius of a stable system is the size of the smallest perturbation that makes it unstable.
For a [[Hurwitz-stable matrix|9A3TBBHRFA]] $A$, consider matrices $\Delta$, possibly of a prescribed structure.
The radius is the smallest norm of such a $\Delta$ for which $A + \Delta$ has an eigenvalue with real part $\ge 0$.
It measures robustness better than the distance of the eigenvalues to the imaginary axis, which can be large while a small perturbation already destroys stability.
For complex perturbations it has an explicit formula in terms of the [[operator norm|06EKW1AKXF]] of $(i\omega I - A)^{-1}$ on the imaginary axis.

## Explanations

### L1 human

A stable system sits in a valley, and the stability radius says how far it can be pushed before it rolls out.
Here the push is a change of the matrix that describes the system, measured by its size.
For the number $A = -a$ with $a > 0$, the radius is $a$: adding anything of size less than $a$ keeps it negative, and adding $a$ reaches $0$.
For matrices the eigenvalues alone can mislead, and the radius gives the honest answer.
