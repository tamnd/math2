---
tag: BGRWCAT4SZ
kind: definition
name: Lopatinskii–Shapiro condition
msc: [35J40, 35J25]
defines: 48MEJEMEXM
uses: [XY8GEQSWPR, F31T650DKY]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_boundary_value_problem
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set with smooth boundary $\partial \Omega$, with $n \ge 2$, and let $m \ge 1$.
Let $A$ be a linear differential operator of order $2m$ with smooth coefficients on $\overline{\Omega}$, with [[principal symbol|F31T650DKY]] $a(x, \xi)$.
For $x \in \partial \Omega$, let $\nu(x)$ be the inner unit normal.
Assume that $A$ is properly [[elliptic|XY8GEQSWPR]].
That is, let $x \in \partial \Omega$ and let $\xi' \in \R^n$ be nonzero and tangent to $\partial \Omega$ at $x$.
Then the polynomial $\tau \mapsto a(x, \xi' + \tau \nu(x))$ has exactly $m$ roots with positive imaginary part.
The roots are counted with multiplicity.
Let $B_1, \ldots, B_m$ be linear differential operators on $\partial \Omega$ with smooth coefficients, of orders $m_j < 2m$ and principal symbols $b_j(x, \xi)$.
Write $D_t = -i \, d/dt$.
The operators $B_1, \ldots, B_m$ satisfy the *Lopatinskii–Shapiro condition* with respect to $A$ if the following holds.
Let $x \in \partial \Omega$ and let $\xi'$ be a nonzero tangent vector at $x$.
The only bounded solution $v \colon [0, \infty) \to \C$ of
$$a\big(x, \xi' + \nu(x) D_t\big) v(t) = 0 \quad (t > 0), \qquad b_j\big(x, \xi' + \nu(x) D_t\big) v(0) = 0 \quad (j = 1, \ldots, m)$$
is $v = 0$.

## Remarks

Equivalently, the polynomials $\tau \mapsto b_j(x, \xi' + \tau \nu)$ are linearly independent modulo $\prod_k (\tau - \tau_k^+)$, where $\tau_k^+$ are the $m$ roots of $a(x, \xi' + \tau \nu)$ with positive imaginary part.
Example: $A = -\Delta$ with the Dirichlet condition $B_1 u = u$ on the half-space $\set{x_n > 0}$.
Here $a(\xi) = \abs{\xi}^2$, $\nu = e_n$, and the ordinary differential equation is $-v'' + \abs{\xi'}^2 v = 0$, whose bounded solutions are $v(t) = c \, e^{-\abs{\xi'} t}$; the condition $v(0) = 0$ forces $c = 0$.
The Neumann condition $\partial_\nu u$ also passes: $v'(0) = -c \abs{\xi'} = 0$ forces $c = 0$.
Non-example: in $\R^3$, take $A = -\Delta$ on $\set{x_3 > 0}$ with $B_1 u = \partial_1 u$ on the boundary.
For $\xi' = (0, 1, 0)$, the function $v(t) = e^{-t}$ is a bounded nonzero solution, since the symbol of $B_1$ is $i \xi_1 = 0$, so the condition fails.
