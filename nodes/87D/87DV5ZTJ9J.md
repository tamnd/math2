---
tag: 87DV5ZTJ9J
kind: statement
role: theorem
name: Landweber iteration
msc: [65J20, 65F22, 47A52]
uses: [HM2HHE3J51, 0YY8VX28JR, 06EKW1AKXF, WTY54BFC46]
about: [WTY54BFC46]
sources:
  - url: https://en.wikipedia.org/wiki/Landweber_iteration
same_as:
  wikidata: Q6485285
  wikipedia: Landweber iteration
---

## Statement

Let $X, Y$ be [[Hilbert spaces|HM2HHE3J51]], let $A \colon X \to Y$ be a bounded linear operator with adjoint $A^*$, and let $A^\dagger$ be its [[Moore–Penrose generalized inverse|0YY8VX28JR]].
Let $0 < \omega < 2/\norm{A}^2$.
For $z \in Y$, the *Landweber iteration* is $x_0(z) = 0$ and
$$x_{k+1}(z) = x_k(z) + \omega A^* \bigl( z - A x_k(z) \bigr), \qquad k \ge 0.$$

1. If $y \in \mathcal{R}(A) + \mathcal{R}(A)^\perp$, then $x_k(y) \to A^\dagger y$ as $k \to \infty$.
2. If moreover $\omega \le 1/\norm{A}^2$, then $\norm{x_k(y^\delta) - x_k(y)} \le \sqrt{\omega k} \, \delta$ for all $y^\delta \in Y$ with $\norm{y^\delta - y} \le \delta$.
3. Consequently, if $k(\delta) \to \infty$ and $\delta \sqrt{k(\delta)} \to 0$ as $\delta \to 0$, then $x_{k(\delta)}(y^\delta) \to A^\dagger y$ uniformly over all $y^\delta$ with $\norm{y^\delta - y} \le \delta$.

## Remarks

Write $x^\dagger = A^\dagger y$; then $A^* y = A^* A x^\dagger$.
The error satisfies $x_k(y) - x^\dagger = -(I - \omega A^* A)^k x^\dagger$.
The self-adjoint operator $A^* A$ has spectrum in $[0, \norm{A}^2]$, and $\abs{1 - \omega t} < 1$ for $0 < t \le \norm{A}^2$.
Since $x^\dagger$ is orthogonal to $\ker A$, the spectral theorem gives $(I - \omega A^* A)^k x^\dagger \to 0$, which is part 1.
For part 2, $x_k(z) = \sum_{j < k} (I - \omega A^* A)^j \omega A^* z$, and a spectral bound on $\sqrt{\omega t} \sum_{j<k} (1 - \omega t)^j$ gives the factor $\sqrt{\omega k}$.

The iteration is gradient descent with fixed step $\omega$ for $\tfrac12 \norm{A x - z}^2$.
When $\mathcal{R}(A)$ is not closed, $x_k(y^\delta)$ first approaches $x^\dagger$ and then diverges, a behavior called semi-convergence.
So the iteration index plays the role of the [[regularization|WTY54BFC46]] parameter, and one must stop early, for example by the discrepancy principle.
Without the condition $\omega < 2/\norm{A}^2$, components along large singular values are amplified and the iteration diverges.

## Explanations

### L1 human

Landweber iteration solves $A x = y$ by repeatedly correcting the guess in the direction that reduces the misfit $\norm{A x - y}$.
With exact data it converges to the best solution.
With noisy data it first improves and later starts to fit the noise, so one stops it at the right moment.

### L2 human

Landweber iteration is the simplest iterative regularization method, and it is the model for others such as conjugate gradients on the normal equations.
Stopping after $k$ steps acts like a filter on the singular values: components with $\omega \sigma^2 k \gg 1$ are recovered and the others are damped.
It converges slowly, but it extends directly to nonlinear operators and to constraints by adding a projection.
It was introduced by Louis Landweber in 1951.
