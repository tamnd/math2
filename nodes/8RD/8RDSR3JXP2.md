---
tag: 8RDSR3JXP2
kind: statement
role: theorem
name: Alternating-direction implicit method
msc: [65M06, 65M12]
uses: [VP2HN86VAG, X7HYEBA5SA, M92S0Y15N1, F1QWA1PEQQ]
about: [VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Alternating-direction_implicit_method
---

## Statement

Consider the [[heat equation|VP2HN86VAG]] $u_t = u_{xx} + u_{yy}$ on the square $(0, 1)^2$, with $u = 0$ on the boundary and a given initial value.
Let $M \ge 1$, $h = 1/(M + 1)$, $\Delta t > 0$, and let $u^n_{jk}$ approximate $u(jh, kh, n \Delta t)$ for $1 \le j, k \le M$, with zero values on the boundary.
Let $\delta_x^2$ and $\delta_y^2$ be the second differences $(\delta_x^2 v)_{jk} = (v_{j+1,k} - 2 v_{jk} + v_{j-1,k}) / h^2$ and $(\delta_y^2 v)_{jk} = (v_{j,k+1} - 2 v_{jk} + v_{j,k-1}) / h^2$.
The Peaceman–Rachford alternating-direction implicit method computes
$$\left(I - \tfrac{\Delta t}{2} \delta_x^2\right) u^{*} = \left(I + \tfrac{\Delta t}{2} \delta_y^2\right) u^n, \qquad \left(I - \tfrac{\Delta t}{2} \delta_y^2\right) u^{n+1} = \left(I + \tfrac{\Delta t}{2} \delta_x^2\right) u^{*}.$$

1. Each half step consists of independent tridiagonal systems, one for each grid line in the $x$ direction or in the $y$ direction.
2. The method is unconditionally stable: $\norm{u^{n+1}}_2 \le \norm{u^n}_2$ for all $\Delta t > 0$ and $h$, where $\norm{v}_2^2 = h^2 \sum_{j,k} v_{jk}^2$.
3. For smooth solutions, the method is second-order accurate: its local truncation error is $O(\Delta t^2 + h^2)$.

## Remarks

The matrices $\delta_x^2$ and $\delta_y^2$ are symmetric, negative definite and commute, with common eigenvectors $\sin(p \pi j h) \sin(q \pi k h)$.
On such an eigenvector, with eigenvalues $-\alpha$ and $-\beta$ ($\alpha, \beta > 0$), one step multiplies by
$$g = \frac{1 - \frac{\Delta t}{2} \alpha}{1 + \frac{\Delta t}{2} \alpha} \cdot \frac{1 - \frac{\Delta t}{2} \beta}{1 + \frac{\Delta t}{2} \beta},$$
and each factor has absolute value less than $1$; this gives clause 2.
Eliminating $u^*$ shows that the method equals the two-dimensional [[Crank–Nicolson method|M92S0Y15N1]] plus the term $\frac{\Delta t^2}{4} \delta_x^2 \delta_y^2 (u^{n+1} - u^n)$, which is $O(\Delta t^3)$ for smooth solutions; this gives clause 3.
Each tridiagonal system is solved in linear time by the [[tridiagonal matrix algorithm|F1QWA1PEQQ]], so a step costs $O(M^2)$ operations, against a sparse system with $M^2$ unknowns for Crank–Nicolson.

## Explanations

### L1 human

Implicit methods for the heat equation in two dimensions lead to a large linear system at every step.
The alternating-direction implicit method splits each step in two halves.
In the first half it is implicit only along the rows of the grid, in the second only along the columns.
So it solves many small tridiagonal systems instead of one large one, and it keeps the stability and the second-order accuracy of Crank–Nicolson.

### L2 human

The method is an operator splitting of $\delta_x^2 + \delta_y^2$, and its analysis uses that the two pieces commute; for variable coefficients or non-rectangular domains this fails and the analysis is harder.
The same iteration, used with varying parameters, is an iterative solver for the discrete Poisson equation and for Lyapunov and Sylvester matrix equations.
In three dimensions one usually uses the Douglas form of the method instead.
