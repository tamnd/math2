---
tag: 7M6MQ2HB1X
kind: definition
name: Method of lines
msc: [65M20]
defines: FNGWJR2FPK
uses: [0FXDW992DS, X7HYEBA5SA, VP2HN86VAG, 0JARTXX4XP, 558XADG64M]
sources:
  - url: https://en.wikipedia.org/wiki/Method_of_lines
---

## Definition

Consider an evolution equation $u_t = \mathcal{A}(u)$ for an unknown $u(x, t)$, $x \in \Omega \subseteq \R^m$, $t \ge 0$.
Here $\mathcal{A}$ is a differential operator in the space variable $x$.
Boundary conditions and an initial value $u(\cdot, 0) = u_0$ are given.
The *method of lines* computes an approximate solution in two steps.

1. Semi-discretisation: choose a spatial discretisation with $N$ unknowns, such as [[finite differences|X7HYEBA5SA]] on a grid. Choose an operator $A_N \colon \R^N \to \R^N$ that approximates $\mathcal{A}$ with the boundary conditions built in. This gives the system of ordinary differential equations $U'(t) = A_N(U(t))$, with $U(0)$ an approximation of $u_0$.
2. Time integration: solve this [[initial value problem|0FXDW992DS]] with a [[numerical method for ordinary differential equations|558XADG64M]].

## Remarks

Example: for the [[heat equation|VP2HN86VAG]] $u_t = u_{xx}$ on $(0, 1)$ with zero boundary values and grid $x_j = j \Delta x$, $\Delta x = 1/(N + 1)$, step 1 gives $U_j' = (U_{j+1} - 2U_j + U_{j-1}) / \Delta x^2$ for $1 \le j \le N$, with $U_0 = U_{N+1} = 0$.
Step 2 with the [[Euler method|0JARTXX4XP]] and step size $\Delta t$ gives the explicit scheme $U_j^{n+1} = U_j^n + r (U_{j+1}^n - 2U_j^n + U_{j-1}^n)$ with $r = \Delta t / \Delta x^2$.
The eigenvalues of the semi-discrete matrix lie in $(-4/\Delta x^2, 0)$, and the Euler method is stable for $\Delta t \lambda \in [-2, 0]$, so the scheme is stable when $r \le 1/2$.
Non-example: Rothe's method discretises time first, which gives a sequence of elliptic boundary value problems in $x$; it fails clause 1, since no system of ODEs is formed.
The semi-discrete systems are often stiff, because their eigenvalues grow like $\Delta x^{-2}$ for diffusion, so implicit or stabilised time integrators are used.

## Explanations

### L1 human

Discretise space, keep time continuous, and hand the resulting ODE system to an ODE solver.
The two choices, in space and in time, can then be made and analysed separately.
