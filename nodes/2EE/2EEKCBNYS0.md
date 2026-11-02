---
tag: 2EEKCBNYS0
kind: definition
name: Integral equation of the second kind
msc: [45A05, 45B05]
defines: 8KJCN49V64
uses: [AYZCKG34QK, GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[kernel|GSMBXT7FPK]], let $f \colon [a, b] \to \C$ be given, and let $\lambda \in \C$.
For each $x \in [a, b]$, let $I_x$ be either $[a, b]$ or $[a, x]$.
An *integral equation of the second kind* is a [[linear integral equation|AYZCKG34QK]] of the form
$$\varphi(x) = f(x) + \lambda \int_{I_x} K(x, s) \varphi(s) \, ds \quad \text{for all } x \in [a, b],$$
for the unknown function $\varphi \colon [a, b] \to \C$.

## Remarks

Example: $\varphi(x) = 1 + \lambda \int_0^1 \varphi(s) \, ds$ on $[0, 1]$, with $K = 1$.
Any solution is a constant $c$ with $c = 1 + \lambda c$, so for $\lambda \ne 1$ the unique solution is $\varphi = 1/(1 - \lambda)$.
For $\lambda = 1$ there is no solution.

Non-example: $\int_0^1 \varphi(s) \, ds = 1$ is not of the second kind, since $\varphi$ does not appear outside the integral; it is of the first kind.

In operator notation, $(I - \lambda K) \varphi = f$, where $I$ is the identity and $K$ is the integral operator.
Some authors write $\varphi(x) - \lambda \int K \varphi = f(x)$ or put $\lambda$ into the kernel.
