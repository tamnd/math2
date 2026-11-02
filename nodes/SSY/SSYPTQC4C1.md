---
tag: SSYPTQC4C1
kind: definition
name: Elliptic boundary value problem
msc: [35J25, 35J40]
defines: C1F7T523G0
uses: [TM8VQJWGHZ, XY8GEQSWPR, 48MEJEMEXM]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_boundary_value_problem
---

## Definition

Let $\Omega \subseteq \R^n$ be a bounded open set with smooth boundary, with $n \ge 2$, and let $m \ge 1$.
Let $A$ be a linear differential operator of order $2m$ with smooth coefficients on $\overline{\Omega}$.
Let $B_1, \ldots, B_m$ be linear differential operators with smooth coefficients on $\partial \Omega$, of orders $m_1, \ldots, m_m$ less than $2m$.
Consider the [[boundary value problem|TM8VQJWGHZ]]
$$A u = f \ \text{in } \Omega, \qquad B_j u = g_j \ \text{on } \partial \Omega \quad (j = 1, \ldots, m).$$
It is *elliptic* if:

1. $A$ is properly [[elliptic|XY8GEQSWPR]] on $\overline{\Omega}$;
2. $B_1, \ldots, B_m$ satisfy the [[Lopatinskii–Shapiro condition|48MEJEMEXM]] with respect to $A$ at every point of $\partial \Omega$.

## Remarks

Example: the Dirichlet problem $-\Delta u = f$ in $\Omega$, $u = g$ on $\partial \Omega$ has $m = 1$, the Laplacian is properly elliptic, and the Dirichlet condition satisfies the Lopatinskii–Shapiro condition.
Non-example: $-\Delta u = f$ with the two conditions $u = 0$ and $\partial_\nu u = 0$ on $\partial \Omega$ is not elliptic, since an operator of order $2$ takes exactly one boundary condition.
Agmon, Douglis and Nirenberg proved an a priori estimate for elliptic problems.
For each integer $s \ge 0$ there is $C > 0$ with
$$\norm{u}_{H^{2m+s}(\Omega)} \le C \Big( \norm{Au}_{H^s(\Omega)} + \sum_{j=1}^m \norm{B_j u}_{H^{2m+s-m_j-1/2}(\partial \Omega)} + \norm{u}_{L^2(\Omega)} \Big),$$
where $H^k$ denotes Sobolev spaces.
For a properly elliptic operator of order $2$, the Dirichlet condition always satisfies the Lopatinskii–Shapiro condition.
Indeed, the bounded solutions of the ordinary differential equation form a line spanned by a function that does not vanish at $0$.
