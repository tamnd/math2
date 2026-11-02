---
tag: XY7H05ANPD
kind: definition
name: Symmetric kernel
msc: [45C05, 45P05]
defines: ADTYF8FG6C
uses: [GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_integral_operator
---

## Definition

Let $a < b$.
A *symmetric kernel* on $[a, b]$ is a real-valued [[kernel|GSMBXT7FPK]] $K \colon [a, b] \times [a, b] \to \R$ such that
$$K(x, s) = K(s, x) \quad \text{for all } x, s \in [a, b].$$

## Remarks

Example: $K(x, s) = \min(x, s)$ on $[0, 1]$.
The check: the minimum of two numbers does not depend on their order.

Non-example: $K(x, s) = x - s$.
Here $K(1, 0) = 1$ and $K(0, 1) = -1$.

A symmetric kernel is a Hermitian kernel that takes real values.
For square-integrable kernels the condition is often required only for almost all $(x, s)$.
Some authors call a complex kernel with $K(x, s) = K(s, x)$ symmetric as well; that condition is different from the Hermitian one.
