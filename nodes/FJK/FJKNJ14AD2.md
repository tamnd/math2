---
tag: FJKNJ14AD2
kind: statement
role: proposition
name: Approximation of a kernel by degenerate kernels
msc: [45B05, 45P05]
uses: [ZM5G144PZG, WWMWX7AD4V, 6Y1RY5767R, 1P8D3MK79H, 0S9GGTR0EX]
about: [6Y1RY5767R]
sources:
  - url: https://en.wikipedia.org/wiki/Fredholm_integral_equation
---

## Statement

Let $a < b$.

1. Let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]], and let $\varepsilon > 0$. Then there is a [[degenerate kernel|6Y1RY5767R]] $K_\varepsilon(x, y) = \sum_{i=1}^{m} a_i(x) b_i(y)$, with polynomials $a_i$ and $b_i$, such that $\abs{K - K_\varepsilon} < \varepsilon$ on $[a, b]^2$.
2. If $K \in L^2([a, b] \times [a, b])$ is a [[square-integrable kernel|WWMWX7AD4V]], then for every $\varepsilon > 0$ there is a degenerate kernel $K_\varepsilon$ with $a_i, b_i \in L^2[a, b]$ such that $\norm{K - K_\varepsilon}_{L^2([a, b]^2)} < \varepsilon$.

## Remarks

Part 1 follows from the [[Stone–Weierstrass theorem|1P8D3MK79H]]: polynomials in $x$ and $y$ are dense in the continuous functions on the square.
Each monomial $x^p y^q$ is a product of a function of $x$ and a function of $y$.
For part 2, let $(e_i)$ be an [[orthonormal basis|0S9GGTR0EX]] of $L^2[a, b]$.
The products $e_i(x) \overline{e_j(y)}$ form an orthonormal basis of $L^2([a, b]^2)$.
The partial sums of the expansion of $K$ in this basis are degenerate kernels converging to $K$.

Example: $K(x, y) = e^{xy}$ on $[0, 1]^2$ is approximated by $\sum_{k=0}^{N} x^k y^k / k!$, with error at most $\sum_{k > N} 1/k!$.

The norm of an integral operator is at most the $L^2$ norm of its kernel, and at most $b - a$ times its sup norm.
So the result says that the integral operator of $K$ is a norm limit of finite-rank operators.
This is the main step in the proof that such operators are compact, and in the reduction of [[Fredholm's theorem|XQ8DYKW4SH]] to linear algebra.

## Explanations

### L1 human

A general kernel mixes the variables $x$ and $y$ in a complicated way.
A degenerate kernel separates them into finitely many products, and equations with such kernels reduce to finite linear systems.
This result says that every reasonable kernel is as close as one wants to a degenerate one.

### L2 human

The approximation is used together with a perturbation argument.
Write $K = K_\varepsilon + (K - K_\varepsilon)$; the small part is inverted by a Neumann series, and the degenerate part leads to a finite linear system.
This yields the Fredholm alternative for square-integrable kernels, and the compactness of their integral operators.
