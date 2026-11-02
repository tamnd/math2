---
tag: 5JQG4S5JVH
kind: definition
name: Glimm scheme
msc: [35L65, 65M06, 35L45]
defines: Y70AC2X30T
uses: [8RA7AMWSAF, GJWKX22VVE, XN081NCPF5]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_problem
---

## Definition

Let $u_t + F(u)_x = 0$ be a strictly [[hyperbolic system of conservation laws|XN081NCPF5]], with $F \colon \Omega \to \R^m$ smooth on an open set $\Omega \subseteq \R^m$.
Assume that every [[Riemann problem|GJWKX22VVE]] with states in $\Omega$ close enough to each other has an entropy solution.
Let $\Lambda$ be an upper bound for the absolute values of the eigenvalues of $DF(u)$ on $\Omega$.
Fix a space step $\Delta x > 0$ and a time step $\Delta t > 0$ with $\Lambda \Delta t \le \Delta x / 2$.
Set $x_j = j \Delta x$ for $j \in \Z$ and $t_n = n \Delta t$ for $n \ge 0$.
Fix a sequence $(\theta_n)_{n \ge 1}$ in $(0, 1)$.

The *Glimm scheme* defines an approximate solution $u^\Delta$ of the initial value problem with data $u_0$ as follows.

1. At $t = 0$, set $u^\Delta(x, 0) = u_0(x_j)$ for $x_{j-1} < x \le x_j$.
2. If $u^\Delta(\cdot, t_n)$ is constant on each cell $(x_{j-1}, x_j]$, then on $t_n \le t < t_{n+1}$ let $u^\Delta$ be the exact solution of the Riemann problems at the points $x_j$.
3. At $t = t_{n+1}$, set $u^\Delta(x, t_{n+1}) = u^\Delta(x_{j-1} + \theta_{n+1} \Delta x,\, t_{n+1} - 0)$ for $x_{j-1} < x \le x_j$.

When the $\theta_n$ are chosen independently and uniformly at random, it is also called the *random choice method*.

## Remarks

The bound $\Lambda \Delta t \le \Delta x/2$ is a [[Courant–Friedrichs–Lewy condition|FQVVNYV6N8]].
It ensures that waves from neighbouring points $x_j$ do not meet before time $t_{n+1}$.
So in step 2 the solution on the strip is exactly the union of the local Riemann solutions.

Glimm proved that, if the total variation of $u_0$ is small enough, the total variation of $u^\Delta(\cdot, t)$ stays bounded uniformly in $\Delta x$ and $t$.
For almost every random sequence $(\theta_n)$, as $\Delta x \to 0$ with $\Delta t / \Delta x$ fixed, a subsequence of the approximations converges to a weak solution.
T.-P. Liu later showed that any equidistributed sequence $(\theta_n)$ gives convergence.

Example: for the linear equation $u_t + a u_x = 0$ with $0 < a$ and $a \Delta t \le \Delta x/2$, the Riemann solution at $x_j$ moves the jump to $x_j + a(t - t_n)$.
At $t_{n+1}$, a cell takes its old value if $\theta_{n+1} \Delta x > a \Delta t$, and the value of its left neighbour otherwise.

Non-example: step 3 with the cell average instead of a sampled value is not the Glimm scheme.
It is [[Godunov's scheme|43HZJ7DRT0]], which smears shocks over several cells, while sampling keeps them sharp.

## Explanations

### L1 human

The scheme replaces the data by steps, solves each jump exactly, and then resamples.
Sampling at random points means that a jump moves by a whole cell or not at all in each step.
On average it moves at the right speed, so shocks stay sharp and travel correctly.
