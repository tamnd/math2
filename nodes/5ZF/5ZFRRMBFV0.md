---
tag: 5ZFRRMBFV0
kind: statement
role: theorem
name: Levinson's theorem on asymptotic integration
msc: ["34E10", 34D05, 34A30]
uses: [037ZNY7NAG, 0H1GN6P9R5, 044JNC7ZAA, X7GTF3D98F]
about: [037ZNY7NAG, 0H1GN6P9R5]
sources:
  - book: isbn:9780898715101
---

## Statement

Let $t_0 \in \R$ and let $n \ge 1$.
Let $\Lambda(t) = \operatorname{diag}(\lambda_1(t), \dots, \lambda_n(t))$ be a continuous [[diagonal matrix|044JNC7ZAA]] function on $[t_0, \infty)$ with complex entries.
Let $R(t)$ be a continuous complex $n \times n$ matrix function on $[t_0, \infty)$ with
$$\int_{t_0}^{\infty} \norm{R(t)} \, dt < \infty.$$
Assume the dichotomy condition: there is a constant $K$ such that for each pair $i \ne j$ one of the following holds, where $D_{ij}(s, t) = \int_s^t \operatorname{Re}\bigl(\lambda_i(u) - \lambda_j(u)\bigr) \, du$:

1. $D_{ij}(t_0, t) \to \infty$ as $t \to \infty$, and $D_{ij}(s, t) \ge -K$ for all $t \ge s \ge t_0$;
2. $D_{ij}(s, t) \le K$ for all $t \ge s \ge t_0$.

Then the [[linear system|037ZNY7NAG]]
$$x' = \bigl(\Lambda(t) + R(t)\bigr) x$$
has a [[fundamental matrix|0H1GN6P9R5]] of the form
$$X(t) = \bigl(I + E(t)\bigr) \exp\Bigl(\int_{t_0}^{t} \Lambda(s) \, ds\Bigr), \qquad E(t) \to 0 \text{ as } t \to \infty.$$
Equivalently, for each $k$ there is a solution $x_k(t) = \bigl(e_k + o(1)\bigr) \exp\bigl(\int_{t_0}^t \lambda_k(s) \, ds\bigr)$, where $e_k$ is the $k$-th standard basis vector.

## Remarks

The proof writes the $k$-th solution as $x_k = \exp\bigl(\int \lambda_k\bigr) z$ and turns the equation for $z$ into an integral equation.
The dichotomy condition splits the indices into those whose integrals are taken from $t_0$ to $t$ and those taken from $t$ to $\infty$.
With this split the integral operator is a contraction on a far half-line $[T, \infty)$, because $\int_T^\infty \norm{R}$ is small.
Its fixed point gives $z(t) \to e_k$.

Example: if $\Lambda$ is a constant diagonal matrix, then each $D_{ij}(s, t)$ is $(t - s)$ times a constant, so the dichotomy condition holds automatically.
Hence for a constant diagonal $\Lambda$ with distinct or equal eigenvalues and an integrable perturbation $R$, each solution of $x' = (\Lambda + R) x$ behaves like $e^{\lambda_k t}$ times a vector close to $e_k$.

The integrability of $R$ cannot be dropped.
For $n = 1$, $\Lambda = 0$ and $R(t) = 1/t$ on $[1, \infty)$, the solutions are $c t$, which do not tend to a constant multiple of $e^0 = 1$.

## Explanations

### L1 human

Many linear systems look like a simple diagonal system plus a small disturbance.
For a diagonal system the solutions are explicit exponentials, one for each coordinate.
Levinson's theorem says that if the disturbance is small in total, measured by the integral of its size, then the true solutions still look like these exponentials for large times.
A mild condition on the growth rates is needed, so that the exponentials can be told apart.

### L2 human

The theorem is the basic tool of asymptotic integration of linear systems.
One first brings a system into the form diagonal part plus integrable part, often by a change of variables that diagonalises the leading term.
Then the theorem gives the leading behaviour of a fundamental matrix.
The WKB, or Liouville–Green, approximation for $y'' = Q(t) y$ can be justified in this way after a suitable substitution.
Hartman and Wintner proved a related result in which $R$ is only square integrable, at the cost of a stronger dichotomy condition and a correction term in the exponent.
