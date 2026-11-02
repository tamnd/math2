---
tag: RABJ6X1BXC
kind: statement
role: theorem
name: Toeplitz index theorem
msc: [47B35, 47A53, 19K56]
uses: [GQ0X3R3WM2, 8HWGKWD6ZM, 2V9Q4KHY1T, 0NQSV2EWDR]
about: [GQ0X3R3WM2, 2V9Q4KHY1T]
sources:
  - url: https://en.wikipedia.org/wiki/Toeplitz_operator
---

## Statement

Let $\mathbb{T}$ be the unit circle, let $H^2 \subseteq L^2(\mathbb{T})$ be the Hardy space, and let $\varphi \colon \mathbb{T} \to \C$ be a continuous function with no zeros.
Then the [[Toeplitz operator|GQ0X3R3WM2]] $T_\varphi$ on $H^2$ is a [[Fredholm operator|8HWGKWD6ZM]].
Its [[index|2V9Q4KHY1T]] is
$$\operatorname{ind} T_\varphi = -\operatorname{wind}(\varphi, 0).$$
Here $\operatorname{wind}(\varphi, 0)$ is the [[winding number|0NQSV2EWDR]] of the closed curve $\varphi$ around $0$.

## Remarks

Idea of the proof: for continuous $\varphi$ and $\psi$, the operator $T_\varphi T_\psi - T_{\varphi\psi}$ is compact.
So $T_{1/\varphi}$ is an inverse of $T_\varphi$ modulo compact operators, and $T_\varphi$ is Fredholm by Atkinson's theorem.
The index is constant along homotopies of nonvanishing symbols, and $\varphi$ is homotopic to $z^n$ with $n = \operatorname{wind}(\varphi, 0)$.
For $n \ge 0$, $T_{z^n}$ is the $n$-th power of the shift, which is injective with cokernel of dimension $n$, so its index is $-n$; for $n < 0$ one takes adjoints.
The hypothesis that $\varphi$ has no zeros is necessary: for continuous $\varphi$, the operator $T_\varphi$ is Fredholm if and only if $\varphi$ has no zeros on $\mathbb{T}$.

## Explanations

### L1 human

A Toeplitz operator multiplies by a function on the circle and then discards negative frequencies.
When the function never vanishes, the operator is nearly invertible, and the failure is measured by an integer.
That integer is minus the number of times the function winds around the origin.
For the simplest case, multiplication by $z$ shifts the coefficients of a power series one step and loses exactly one dimension.

### L2 human

The theorem is the one-dimensional model of the Atiyah–Singer index theorem: an analytic index equals a topological invariant of the symbol.
It is also a basic example of index theory for $C^*$-algebras, through the Toeplitz extension $0 \to \mathcal{K} \to \mathcal{T} \to C(\mathbb{T}) \to 0$, whose index map $K_1(C(\mathbb{T})) \to K_0(\mathcal{K}) = \Z$ is the winding number up to a sign convention.
Higher-dimensional versions for Toeplitz operators on strictly pseudoconvex domains are due to Boutet de Monvel.
