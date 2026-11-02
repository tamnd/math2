---
tag: GF40N88TVM
kind: definition
name: Homogeneous integral equation
msc: [45A05, 45C05]
defines: W6CYS54QXS
uses: [AYZCKG34QK, 8KJCN49V64, GSMBXT7FPK, 04KGXJG1A2]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$, let $a_0, f \colon [a, b] \to \C$ and a [[kernel|GSMBXT7FPK]] $K \colon [a, b] \times [a, b] \to \C$ be given, and let $\lambda \in \C$.
For each $x \in [a, b]$, let $I_x$ be either $[a, b]$ or $[a, x]$.
A [[linear integral equation|AYZCKG34QK]]
$$a_0(x) \varphi(x) = f(x) + \lambda \int_{I_x} K(x, s) \varphi(s) \, ds \quad \text{for all } x \in [a, b]$$
is *homogeneous* if $f(x) = 0$ for all $x \in [a, b]$, and *inhomogeneous* otherwise.
For an equation of the [[second kind|8KJCN49V64]], the homogeneous equation is
$$\varphi(x) = \lambda \int_{I_x} K(x, s) \varphi(s) \, ds \quad \text{for all } x \in [a, b].$$

## Remarks

Example: $\varphi(x) = \lambda \int_0^1 x s \, \varphi(s) \, ds$ on $[0, 1]$ is homogeneous.
Every solution has the form $\varphi(x) = c x$ with $c = \lambda c / 3$, so there is a nonzero solution exactly when $\lambda = 3$.

Non-example: $\varphi(x) = x + \lambda \int_0^1 x s \, \varphi(s) \, ds$ is inhomogeneous, since its free term $f(x) = x$ is not zero.

The solutions of a homogeneous equation form a vector space, like the solutions of a [[homogeneous system of linear equations|04KGXJG1A2]].
The difference of two solutions of an inhomogeneous equation solves the homogeneous one.
