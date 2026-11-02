---
tag: RK8B7KEA3M
kind: definition
name: Adjoint integral equation
msc: [45A05, 45B05]
defines: XEZXGBT42J
uses: [8KJCN49V64, GSMBXT7FPK, 0FTH2E9TAS]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_equation
---

## Definition

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[kernel|GSMBXT7FPK]], and let $\lambda \in \C$.
Consider the [[integral equation of the second kind|8KJCN49V64]]
$$\varphi(x) - \lambda \int_a^b K(x, s) \varphi(s) \, ds = f(x), \quad x \in [a, b].$$
Its *adjoint kernel* is $K^*(x, s) = \overline{K(s, x)}$, where the bar is the [[complex conjugate|0FTH2E9TAS]].
For a given function $g \colon [a, b] \to \C$, the *adjoint integral equation* is
$$\psi(x) - \bar\lambda \int_a^b \overline{K(s, x)} \, \psi(s) \, ds = g(x), \quad x \in [a, b],$$
for the unknown function $\psi \colon [a, b] \to \C$.

## Remarks

Example: for $K(x, s) = i x$ on $[0, 1]$, the adjoint kernel is $K^*(x, s) = \overline{i s} = -i s$.
The check: put $x$ and $s$ in reverse order and conjugate.

Non-example: the equation with kernel $K(s, x)$ and parameter $\lambda$, without conjugation, is the adjoint only when $K$ is real and $\lambda$ is real.
For $K(x, s) = i x$ it gives the kernel $i s$, not $-i s$.

With the inner product $\ip{u}{v} = \int_a^b u(x) \overline{v(x)} \, dx$, the integral operators satisfy $\ip{K u}{v} = \ip{u}{K^* v}$ when $K$ is continuous or square-integrable.
For real kernels and real $\lambda$, the adjoint equation is often called the *transposed* or *associated* equation.
A kernel equal to its adjoint kernel is called Hermitian.
