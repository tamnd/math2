---
tag: TH54SPVN1N
kind: statement
role: proposition
name: Levenberg–Marquardt algorithm
msc: [65K10, 90C30, 62J02]
uses: [047NDTEPCV, 0BYTQ4X1HC, 0KX66CZMBB, CYV4T43FQJ]
about: [C7E69V030F]
sources:
  - url: https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm
same_as:
  wikidata: Q1426494
  wikipedia: Levenberg–Marquardt algorithm
---

## Statement

Let $D \subseteq \R^n$ be open, let $r \colon D \to \R^m$ be continuously differentiable with [[Jacobian matrix|047NDTEPCV]] $J(x)$, and let $S(x) = \tfrac12 \norm{r(x)}_2^2$.
For $x \in D$ and a damping parameter $\lambda > 0$, the *Levenberg–Marquardt step* $\delta = \delta(\lambda)$ is the solution of
$$\bigl( J(x)^T J(x) + \lambda I \bigr) \delta = -J(x)^T r(x).$$
Write $J = J(x)$, $r = r(x)$ and $g = \nabla S(x) = J^T r$.
Then:

1. $J^T J + \lambda I$ is [[positive definite|0KX66CZMBB]], so $\delta(\lambda)$ exists and is unique;
2. if $g \ne 0$, then $g^T \delta(\lambda) < 0$, so $\delta(\lambda)$ is a descent direction for $S$;
3. $\delta(\lambda)$ minimizes $\norm{r + J p}_2$ over all $p$ with $\norm{p}_2 \le \norm{\delta(\lambda)}_2$;
4. if $J$ has full column rank, then $\delta(\lambda)$ tends to the [[Gauss–Newton|CYV4T43FQJ]] step as $\lambda \to 0$;
5. $\lambda \, \delta(\lambda) \to -g$ as $\lambda \to \infty$.

## Remarks

Part 1 holds because $p^T (J^T J + \lambda I) p = \norm{J p}^2 + \lambda \norm{p}^2 > 0$ for $p \ne 0$.
Part 2 follows: $g^T \delta = -g^T (J^T J + \lambda I)^{-1} g < 0$.
For part 3, $\delta$ satisfies the optimality conditions of the ball-constrained problem with multiplier $\lambda \ge 0$, and the problem is convex.
So the method is a [[trust region method|5DCSNQ8CXZ]] for the Gauss–Newton model, with $\lambda$ controlling the radius.
Parts 4 and 5 show that it interpolates between Gauss–Newton steps (small $\lambda$) and short steepest descent steps (large $\lambda$).

The algorithm updates $\lambda$ at each step.
If the step reduces $S$ enough, it is accepted and $\lambda$ is decreased; otherwise it is rejected and $\lambda$ is increased.
Marquardt proposed replacing $\lambda I$ by $\lambda \, \mathrm{diag}(J^T J)$, which makes the step invariant under rescaling of the variables.
Example: with $m = n = 1$, $r(x) = x - 1$ and $x = 3$, one has $J = 1$, $g = 2$ and $\delta(\lambda) = -2/(1 + \lambda)$, which is the full Gauss–Newton step $-2$ at $\lambda = 0$ and shrinks as $\lambda$ grows.

## Explanations

### L1 human

Gauss–Newton is fast near a solution but can jump too far when the guess is poor.
Levenberg–Marquardt adds a damping term that shortens the step and turns it toward the downhill direction.
When things go well the damping is reduced and the method becomes Gauss–Newton; when they go badly it is increased.

### L2 human

The method is due to Kenneth Levenberg (1944) and Donald Marquardt (1963).
It is the standard algorithm for small and medium nonlinear least squares problems, such as curve fitting and camera calibration.
Its damped normal equations are the same equations as in Tikhonov regularization of the linearized problem.
