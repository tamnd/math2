---
tag: 8Q7P2WA8ZT
kind: definition
name: Volterra equation of the first kind
msc: [45D05]
defines: H6ZGEDM4VV
uses: [DND8CBEVXT, GSMBXT7FPK, 0W29TBTY12]
sources:
  - url: https://en.wikipedia.org/wiki/Volterra_integral_equation
---

## Definition

Let $a < b$, let $\Delta = \set{(t, s) : a \le s \le t \le b}$, let $K \colon \Delta \to \C$ be a [[kernel|GSMBXT7FPK]], and let $f \colon [a, b] \to \C$ be a given function.
A *linear Volterra equation of the first kind* is the equation
$$\int_a^t K(t, s) \, x(s) \, ds = f(t), \quad t \in [a, b],$$
for an unknown function $x$ on $[a, b]$.
The unknown appears only inside the [[integral|0W29TBTY12]], and the upper limit of integration is the variable $t$.

## Remarks

Example: $\int_0^t (t - s) \, x(s) \, ds = t^3$ on $[0, 1]$ is of the first kind with $K(t, s) = t - s$.
Differentiating twice gives $x(t) = 6t$, and indeed $\int_0^t (t - s) \, 6s \, ds = 3t^3 - 2t^3 = t^3$.
Non-example: $x(t) - \int_0^t x(s) \, ds = 1$ is not of the first kind, since $x$ also appears outside the integral; it is a [[Volterra equation of the second kind|ATPSAHYG7C]].
A necessary condition for a continuous solution when $K$ is continuous is $f(a) = 0$, since the integral vanishes at $t = a$.
Often $K$ is required to be continuous on $\Delta$, but weakly singular kernels such as $(t - s)^{-1/2}$ are also allowed, as in [[Abel's integral equation|G4GWBYTW7B]].
