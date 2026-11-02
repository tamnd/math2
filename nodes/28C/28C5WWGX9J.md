---
tag: 28C5WWGX9J
kind: statement
role: theorem
name: Minimal curvature property of natural cubic splines
msc: [41A15, 65D07, 41A05]
uses: [V42H0R3EKX, D59HBKKRP9, 0W29TBTY12, 08Y1BBQTK9]
about: [V42H0R3EKX]
sources:
  - url: https://en.wikipedia.org/wiki/Spline_interpolation
---

## Statement

Let $k \ge 1$, let $a = x_0 < x_1 < \cdots < x_k = b$, and let $y_0, \dots, y_k \in \R$.
Let $s$ be the natural [[cubic spline|V42H0R3EKX]] with knots $x_0, \dots, x_k$ such that $s(x_i) = y_i$ for all $i$.
Let $g \colon [a, b] \to \R$ be twice continuously differentiable with $g(x_i) = y_i$ for all $i$.
Then
$$\int_a^b s''(x)^2 \, dx \le \int_a^b g''(x)^2 \, dx,$$
with equality only if $g = s$.

## Remarks

Let $h = g - s$, which vanishes at every knot.
[[Integration by parts|08Y1BBQTK9]] gives $\int_a^b s'' h'' \, dx = \bigl[s'' h'\bigr]_a^b - \int_a^b s''' h' \, dx$.
The boundary term is $0$ because $s''(a) = s''(b) = 0$.
On each $[x_{i-1}, x_i]$ the function $s'''$ is a constant $c_i$, so the last integral is $\sum_i c_i \bigl(h(x_i) - h(x_{i-1})\bigr) = 0$.
Hence $\int g''^2 = \int s''^2 + \int h''^2$, and equality forces $h'' = 0$, so $h$ is linear with two zeros and $h = 0$.

Example: for two data points ($k = 1$) the natural cubic spline is the straight line through them.
The statement says that every other $C^2$ curve through the two points has $\int g''^2 > 0$.

The end conditions matter.
For other cubic spline interpolants, such as the clamped one, the inequality holds only among functions $g$ that satisfy the same end conditions.

## Explanations

### L1 human

The integral of the squared second derivative measures how much a curve bends overall; for a thin elastic strip it is roughly its bending energy.
The theorem says that among all smooth curves through given points, the natural cubic spline bends the least.
This is why it imitates the draftsman's spline, a flexible strip held by pegs at the data points.

### L2 human

The theorem gives a variational characterisation of the natural cubic spline interpolant.
It minimises $\int_a^b g''^2$ among the $C^2$ functions $g$ that satisfy the interpolation conditions.
The same holds in the larger Sobolev space $H^2$.
The proof shows an orthogonality: $s''$ is orthogonal to $h''$ for every $h$ vanishing at the knots, and this orthogonality is what makes $s$ the minimiser.
Replacing the interpolation conditions by a penalised fit leads to [[smoothing splines|BNEXZF75QC]], and the same idea in two variables leads to [[thin plate splines|P9ZPH7EC8K]].
