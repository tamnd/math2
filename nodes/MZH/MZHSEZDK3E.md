---
tag: MZHSEZDK3E
kind: definition
name: Integral equation of the third kind
msc: [45A05, 45H05]
defines: DZ47JVKEF5
uses: [AYZCKG34QK, GSMBXT7FPK, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[kernel|GSMBXT7FPK]], let $f \colon [a, b] \to \C$ be given, and let $\lambda \in \C$.
Let $a_0 \colon [a, b] \to \C$ be a [[continuous function|0X3WGX95FE]] that has at least one zero in $[a, b]$ and is not identically zero.
An *integral equation of the third kind* is a [[linear integral equation|AYZCKG34QK]] of the form
$$a_0(x) \varphi(x) = f(x) + \lambda \int_a^b K(x, s) \varphi(s) \, ds \quad \text{for all } x \in [a, b],$$
for the unknown function $\varphi \colon [a, b] \to \C$.

## Remarks

Example: $x \varphi(x) = x + \int_{-1}^{1} s \, \varphi(s) \, ds$ on $[-1, 1]$, with $a_0(x) = x$, $f(x) = x$, $K(x, s) = s$ and $\lambda = 1$.
The coefficient $a_0$ is continuous, vanishes at $0$, and is not identically zero.
The function $\varphi = 1$ is a solution, since $\int_{-1}^{1} s \, ds = 0$.

Non-example: $(2 + x) \varphi(x) = f(x) + \int_{-1}^{1} \varphi(s) \, ds$ on $[-1, 1]$ is not of the third kind, since $2 + x$ has no zero there.
Dividing by $2 + x$ turns it into an equation of the second kind.

Some authors also allow the upper limit $x$ in place of $b$.
