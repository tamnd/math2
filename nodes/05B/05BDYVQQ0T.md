---
tag: 05BDYVQQ0T
kind: definition
name: Space of solutions of a linear recurrence
msc: [39A06]
defines: 099GXMHV40
uses: [0ZV2YKKZ58]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_recurrence_with_constant_coefficients
    locator: General solution
---

## Definition

Let $R$ be a commutative ring, and let $E$ be a linear recurrence with constant coefficients over $R$ of order $d$.
The space of solutions of $E$ is the set of all [[solutions|0ZV2YKKZ58]] of $E$.
It is a submodule of the $R$-module $R^{\mathbb{N}}$ of all sequences in $R$, with termwise addition and scalar multiplication.

## Remarks

The map $u \mapsto (u_0, \dots, u_{d-1})$ is an isomorphism of $R$-modules from the space of solutions to $R^d$. Over a field, the space of solutions has dimension $d$.
For the Fibonacci recurrence over $\mathbb{R}$, the sequences $\varphi^n$ and $\psi^n$ form a basis, with $\varphi$ and $\psi$ the roots of $X^2 - X - 1$.

## Explanations

### L1 human

If two sequences solve the same linear recurrence, then so does their sum, and so does any multiple of one of them.
So the solutions form a vector space, and the first $d$ terms are coordinates on it.
