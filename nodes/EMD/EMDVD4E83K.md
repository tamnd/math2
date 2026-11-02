---
tag: EMDVD4E83K
kind: statement
role: theorem
name: Parabolic maximum principle
msc: [35B50, 35K05]
uses: [VP2HN86VAG]
about: [VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_principle
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded open set and let $T > 0$.
Let $\Omega_T = \Omega \times (0, T]$, and let $\Gamma_T = \overline{\Omega_T} \setminus \Omega_T$ be its parabolic boundary, which is the bottom $\overline{\Omega} \times \set{0}$ together with the sides $\partial \Omega \times [0, T]$.
Let $u \colon \overline{\Omega_T} \to \R$ be continuous, with $\partial_t u$ and the second partial derivatives in $x$ continuous on $\Omega_T$, and assume that
$$\partial_t u - \Delta u \le 0 \quad \text{in } \Omega_T.$$
Then
$$\max_{\overline{\Omega_T}} u = \max_{\Gamma_T} u.$$

## Remarks

First assume the strict inequality $\partial_t u - \Delta u < 0$.
At a maximum point $(x_0, t_0)$ in $\Omega_T$ one would have $\Delta u(x_0, t_0) \le 0$ and $\partial_t u(x_0, t_0) \ge 0$, the latter also when $t_0 = T$, which is a contradiction.
In general apply this to $v = u + \varepsilon \abs{x}^2$, for which $\partial_t v - \Delta v \le -2n\varepsilon < 0$, and let $\varepsilon \to 0$.
Applied to $u$ and $-u$, it shows that a solution of the [[heat equation|VP2HN86VAG]] on $\Omega_T$ is bounded by its values on the parabolic boundary.
So the initial-boundary value problem has at most one solution.
The strong form says more: if $\Omega$ is connected and the maximum is reached at a point $(x_0, t_0)$ of $\Omega_T$, then $u$ is constant on $\overline{\Omega} \times [0, t_0]$.
Boundedness of $\Omega$ is needed.
On $\R \times (0, T]$, Tychonoff's example is a nonzero solution of the heat equation with zero initial values, so its maximum is not controlled by the initial values.
Without the side boundary, uniqueness only holds under growth conditions, such as $\abs{u(x, t)} \le A e^{a \abs{x}^2}$.

## Explanations

### L1 human

In a body with no heat sources, the hottest moment and place must lie at the start or on the edge.
Heat cannot pile up in the interior by itself; it can only spread out and even out.
This gives a simple way to compare and bound temperatures without solving the equation.

### L2 human

The principle is the main tool for uniqueness and comparison results for parabolic equations.
It extends to operators $\partial_t u - \sum_{i,j} a_{ij} \partial_i \partial_j u - \sum_i b_i \partial_i u$ with $(a_{ij})$ positive definite.
It is the time-dependent analogue of the maximum principle for harmonic and subharmonic functions.
Its strong form follows from a mean value property on heat balls or from a parabolic Harnack inequality.
