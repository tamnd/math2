---
tag: 59CF2D7BRB
kind: definition
name: Continuous kernel
msc: [45P05, 45B05]
defines: ZM5G144PZG
uses: [GSMBXT7FPK, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$.
A *continuous kernel* on $[a, b]$ is a [[kernel|GSMBXT7FPK]] $K \colon [a, b] \times [a, b] \to \C$ that is a [[continuous function|0X3WGX95FE]] of the pair $(x, s)$ on the square $[a, b] \times [a, b]$.

## Remarks

Example: $K(x, s) = \min(x, s)$ on $[0, 1]$.
On the closed triangle $s \le x$ it equals $s$, and on the closed triangle $x \le s$ it equals $x$.
Both formulas are continuous and agree on the diagonal, so $K$ is continuous on the square.

Non-example: $K(x, s) = \abs{x - s}^{-1/2}$ for $x \ne s$, with any value on the diagonal, is not continuous on $[0, 1]^2$, since it is unbounded near the diagonal.
It is a weakly singular kernel.

A continuous kernel is bounded, $\abs{K(x, s)} \le M$, and uniformly continuous on the compact square.
So $x \mapsto \int_a^b K(x, s) \varphi(s) \, ds$ is continuous for every continuous $\varphi$, and it is bounded by $M (b - a) \max \abs{\varphi}$.
The same definition is used with $[a, b]$ replaced by a compact subset of $\R^m$.
