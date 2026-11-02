---
tag: CHESR1W1CY
kind: concept
name: Inverse Mellin transform
msc: [44A15]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_inversion_theorem
---

## Summary

The inverse Mellin transform turns a function $\varphi$ on a vertical line $\operatorname{Re} s = c$ into the function $x \mapsto \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} x^{-s} \varphi(s) \, ds$ on $(0, \infty)$.
By the [[Mellin inversion theorem|XJWC13NY9E]], it undoes the [[Mellin transform|N5PVGRJE1T]] under suitable hypotheses.
In logarithmic variables it is an [[inverse Fourier transform|JB8QMT8DCH]], and when $\varphi$ is meromorphic it can often be computed with the [[residue theorem|032HKYS329]].

## Explanations

### L1 human

The Mellin transform breaks a function on $(0, \infty)$ into the powers $x^{-s}$, with $s$ on a vertical line.
The inverse Mellin transform adds these powers back together, with the weights $\varphi(s)$.
For example, with $\varphi = \Gamma$ and any $c > 0$, the inverse transform gives back $e^{-x}$.
Moving the line of integration to the left and collecting residues of $\Gamma$ at $0, -1, -2, \dots$ then gives the power series of $e^{-x}$.
