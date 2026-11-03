---
tag: 2WMYTJD33F
kind: concept
name: Additive character
msc: [11T24, 43A40]
sources:
  - url: https://en.wikipedia.org/wiki/Character_(mathematics)
---

## Summary

An additive character of a ring or field $R$ is a [[character|H1WNVN5V7F]] of the additive group $(R, +)$.
It is a map $\psi$ to the nonzero complex numbers with $\psi(x + y) = \psi(x)\psi(y)$.
The name contrasts it with a multiplicative character, which is a character of the group of units $R^\times$.
Additive characters of finite fields are the building blocks of exponential sums, Gauss sums and the discrete Fourier transform on $\F_q$.
In Mathlib, an additive character of an additive monoid $A$ with values in a monoid $M$ is a map $\psi \colon A \to M$ with $\psi(0) = 1$ and $\psi(a + b) = \psi(a)\psi(b)$.

## Explanations

### L1 human

An additive character turns adding into multiplying.
On the integers modulo a prime $p$, the map $x \mapsto e^{2\pi i x / p}$ wraps the $p$ residues evenly around the unit circle, and adding residues corresponds to adding angles.
Every additive character of $\Z/p\Z$ has the form $x \mapsto e^{2\pi i a x / p}$ for one residue $a$.
Sums of an additive character against other functions, such as $\sum_x e^{2\pi i x^2 / p}$, are central in number theory.
