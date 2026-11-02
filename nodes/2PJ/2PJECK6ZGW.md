---
tag: 2PJECK6ZGW
kind: statement
role: theorem
name: Bulirsch–Stoer algorithm
msc: [65L06, 65L05]
uses: [0FXDW992DS, WMTZG71K2Y]
about: [WMTZG71K2Y]
sources:
  - url: https://en.wikipedia.org/wiki/Bulirsch%E2%80%93Stoer_algorithm
---

## Statement

Let $f \colon \R \times \R^d \to \R^d$ be infinitely differentiable, and consider the [[initial value problem|0FXDW992DS]] $y' = f(t, y)$, $y(t_0) = y_0$.
Fix a step $H > 0$, an even integer $n$, and put $h = H / n$.
Gragg's modified midpoint rule computes
$$z_0 = y_0, \qquad z_1 = z_0 + h f(t_0, z_0), \qquad z_{m+1} = z_{m-1} + 2 h f(t_0 + m h, z_m) \quad (1 \le m \le n - 1),$$
and sets $S(h) = z_n$.
Then $S(h)$ has an asymptotic expansion in even powers of $h$:
$$y(t_0 + H) - S(h) = e_1 h^2 + e_2 h^4 + \cdots + e_k h^{2k} + O(h^{2k+2})$$
for each $k \ge 1$, where the vectors $e_j$ do not depend on $h$.

The Bulirsch–Stoer algorithm computes $S(h_i)$ for $h_i = H / n_i$ with increasing even integers $n_1 < n_2 < \cdots$.
It extrapolates the values $T_{i,1} = S(h_i)$ to $h = 0$ by polynomial (or rational) extrapolation in $h^2$.
With polynomial extrapolation, the entry $T_{j,k}$ of the extrapolation table is a one-step method of order $2k$ in $H$.

## Remarks

The expansion in $h^2$ is due to Gragg, and it comes from the symmetry of the two-step midpoint rule.
For general $n$ the expansion of $z_n$ also contains terms with the factor $(-1)^n$.
Taking $n$ even makes these factors equal to $1$, so the coefficients $e_j$ are the same for all the $h_i$.
[[Richardson extrapolation|WMTZG71K2Y]] in the variable $h^2$ then removes one even power of $h$ in each column of the table.
For example, with $n_1 = 2$ and $n_2 = 4$, the value $T_{2,2} = S(h_2) + \frac{S(h_2) - S(h_1)}{(n_2/n_1)^2 - 1} = \frac{4 S(h_2) - S(h_1)}{3}$ has local error $O(H^5)$, so it is a method of order $4$.
Bulirsch and Stoer used rational extrapolation, and Gragg also proposed a final smoothing step; the order statement is the same.

## Explanations

### L1 human

The method takes one big step several times, each time cut into a different number of small midpoint steps.
The answers get better as the small steps shrink, and the way they improve is very regular.
One fits a curve through the answers and reads off its value at step size zero.
This gives very accurate results for smooth problems at a modest cost.

### L2 human

The algorithm is an extrapolation method: the order is raised by adding rows to the table, not by changing the base method.
The difference between the last two diagonal entries of the table estimates the error.
This estimate drives the choice of $H$ and of the number of rows, as in [[adaptive step size|6MREWBZR7R]] control.
It works best for smooth, non-stiff problems with tight tolerances; for stiff problems one uses an extrapolated linearly implicit method instead.
