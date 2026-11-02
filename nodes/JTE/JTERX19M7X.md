---
tag: JTERX19M7X
kind: statement
role: theorem
name: Linearized stability theorem for maps
msc: [39A30, 37C75]
uses: [R6QVS6P21N, 047NDTEPCV, 0BQAA2BK3Q, 9V7YQA85PC, CHEQ235HW9]
about: [R6QVS6P21N, CHEQ235HW9]
sources:
  - url: https://en.wikipedia.org/wiki/Hartman%E2%80%93Grobman_theorem
---

## Statement

Let $U \subseteq \R^k$ be open, let $f \colon U \to \R^k$ be continuously differentiable, and let $x^* \in U$ be a [[fixed point|R6QVS6P21N]] of $f$.
Let $J = Df(x^*)$ be the [[Jacobian matrix|047NDTEPCV]] of $f$ at $x^*$, and consider the difference equation $x_{n+1} = f(x_n)$.

1. If every [[eigenvalue|0BQAA2BK3Q]] $\lambda$ of $J$ satisfies $\abs{\lambda} < 1$, then $x^*$ is locally asymptotically [[stable|CHEQ235HW9]].
   Equivalently, the hypothesis is that the [[spectral radius|9V7YQA85PC]] of $J$ is less than $1$.
2. If some eigenvalue $\lambda$ of $J$ satisfies $\abs{\lambda} > 1$, then $x^*$ is unstable.

## Remarks

For part 1, choose a norm on $\R^k$ in which $\norm{J} < 1$; such a norm exists because the spectral radius is below $1$.
By continuity of $Df$, the map $f$ is a contraction with ratio $q < 1$ on a small closed ball around $x^*$ in this norm.
So iterates stay in the ball and $\norm{x_n - x^*} \le q^n \norm{x_0 - x^*}$.
Part 2 needs a finer argument along the direction of the expanding eigenvalues.
For the logistic map $f(x) = r x (1 - x)$ with $1 < r < 3$, the fixed point $x^* = 1 - 1/r$ has $f'(x^*) = 2 - r$, of modulus less than $1$, so it is asymptotically stable.
When some eigenvalue has modulus exactly $1$ and none has modulus greater than $1$, the theorem says nothing.
For example, $x \mapsto x - x^3$ and $x \mapsto x + x^3$ both have derivative $1$ at $0$, but $0$ is asymptotically stable for the first and unstable for the second.

## Explanations

### L1 human

To know whether a fixed point of a map attracts nearby points, replace the map by its best linear approximation there.
If the linear part shrinks every direction, the fixed point attracts.
If it stretches some direction, nearby points are pushed away.
This reduces a nonlinear question to computing eigenvalues of one matrix.

### L2 human

This is the main tool for the local stability of equilibria of nonlinear difference equations.
For a scalar equation it reduces to $\abs{f'(x^*)} < 1$ for stability and $\abs{f'(x^*)} > 1$ for instability.
For higher-order scalar equations one writes the system in vector form and applies the theorem to the companion-type Jacobian, whose characteristic polynomial can be tested by the Jury criterion.
When no eigenvalue has modulus $1$, the fixed point is hyperbolic.
Then the [[Hartman–Grobman theorem|0S8WX8A4V9]] gives the stronger conclusion that $f$ is locally topologically conjugate to $J$ when $f$ is a local diffeomorphism.
