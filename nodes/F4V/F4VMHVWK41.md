---
tag: F4VMHVWK41
kind: statement
role: theorem
name: Cauchy–Kovalevskaya theorem for ODEs
msc: [34A12, 34M04, 35A10]
uses: [0FXDW992DS, 0NAHXR1FRH, 0MZB06ST2B, 081WKEDK6C]
about: [0FXDW992DS]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%E2%80%93Kovalevskaya_theorem
---

## Statement

Let $z_0 \in \C$, $w_0 \in \C^n$, and let $F$ be a function from a neighbourhood of $(z_0, w_0)$ in $\C \times \C^n$ to $\C^n$ that is [[holomorphic|0NAHXR1FRH]] in all its variables.
Then there is $r > 0$ such that the [[initial value problem|0FXDW992DS]]
$$w'(z) = F(z, w(z)), \qquad w(z_0) = w_0$$
has a holomorphic solution $w$ on the disc $\abs{z - z_0} < r$.
Any two holomorphic solutions on a disc around $z_0$ agree on the smaller disc.

## Remarks

Writing $w(z) = \sum_{k \ge 0} a_k (z - z_0)^k$ and differentiating the equation repeatedly, each $a_k$ is a polynomial with nonnegative coefficients in $a_0 = w_0$ and the Taylor coefficients of $F$.
So the Taylor series of any holomorphic solution is determined by the equation, which gives uniqueness.
Cauchy's method of majorants proves convergence.
One replaces $F$ by a function with larger Taylor coefficients in absolute value, for which the equation can be solved explicitly.
The solution of this new equation dominates the formal [[power series|0MZB06ST2B]].
The real version holds as well: if $F$ is real [[analytic|081WKEDK6C]], the solution is real analytic.

Example: $w' = w^2$, $w(0) = 1$ has the holomorphic solution $w(z) = \frac{1}{1 - z} = \sum_{k \ge 0} z^k$ on $\abs{z} < 1$.
The radius $r$ cannot be taken arbitrarily large, since this solution has a pole at $z = 1$.

Analyticity of $F$ is needed for an analytic solution: for a smooth but not analytic function $g$ on $\R$, the solution $w(x) = \int_0^x g$ of $w' = g(x)$, $w(0) = 0$, is not analytic.

## Explanations

### L1 human

If the right side of a differential equation is given by convergent power series, then so is the solution.
One can compute the Taylor coefficients of the solution one by one from the equation.
The theorem says that the resulting series really converges near the starting point.

### L2 human

This is the case of ordinary differential equations in the general Cauchy–Kovalevskaya theorem for partial differential equations.
It is the starting point of the theory of differential equations in the complex domain.
Unlike the Picard–Lindelöf theorem, it gives analyticity of the solution, but it needs analytic data.
For linear equations, the solution even extends along every path in the domain where the coefficients are holomorphic, which leads to [[monodromy|C8HD62AB6Q]].
