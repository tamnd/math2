---
tag: TSPTN464CM
kind: concept
name: Pick matrix
msc: ["30E05", 47A57]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna–Pick_interpolation
---

## Summary

The Pick matrix of interpolation data $z_1, \ldots, z_n$ in the [[unit disc|8G5ABXRK85]] and target values $w_1, \ldots, w_n$ is the Hermitian matrix with entries $\frac{1 - w_i \overline{w_j}}{1 - z_i \overline{z_j}}$.
By [[Nevanlinna–Pick interpolation|4VMSSYB5DN]], a holomorphic self-map of the disc with $f(z_i) = w_i$ exists exactly when this matrix is positive semidefinite.
It turns an analytic existence problem into a finite check of linear algebra.

## Explanations

### L1 human

Suppose you want a holomorphic map of the disc into itself that sends some given points to some given values inside the disc.
You write down a square table of numbers built from the points and the values.
If that table is a [[positive semidefinite matrix|0880F9EQCP]], such a map exists; otherwise it does not.
With one point, the table is the single positive number $\frac{1 - \abs{w_1}^2}{1 - \abs{z_1}^2}$, and indeed a [[Möbius transformation|0B346DDAM5]] of the disc sends $z_1$ to $w_1$.
