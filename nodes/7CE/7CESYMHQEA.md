---
tag: 7CESYMHQEA
kind: statement
role: theorem
name: Modified Richardson iteration
msc: [65F10]
uses: [0GT4WWGWH2, 0KX66CZMBB, 0BQAA2BK3Q, 9V7YQA85PC, AB3S6MHJ8X, 2RPE77ACER, KE98SW3SBD]
about: [2RPE77ACER]
sources:
  - url: https://en.wikipedia.org/wiki/Modified_Richardson_iteration
same_as:
  wikidata: Q1375161
  wikipedia: Modified Richardson iteration
---

## Statement

Let $A$ be a real symmetric [[positive definite|0KX66CZMBB]] $n \times n$ matrix, let $b \in \R^n$, and let $\omega > 0$.
The *modified Richardson iteration* for the [[linear system|0GT4WWGWH2]] $A x = b$ starts from any $x^{(0)} \in \R^n$ and sets
$$x^{(k+1)} = x^{(k)} + \omega \left( b - A x^{(k)} \right).$$
Let $\lambda_{\min}$ and $\lambda_{\max}$ be the least and greatest [[eigenvalues|0BQAA2BK3Q]] of $A$.

1. The iterates converge to $A^{-1} b$ for every $b$ and every $x^{(0)}$ if and only if $0 < \omega < 2 / \lambda_{\max}$.
2. The [[spectral radius|9V7YQA85PC]] of the iteration matrix $I - \omega A$ is least for $\omega = 2 / (\lambda_{\min} + \lambda_{\max})$. Its value there is $(\kappa - 1) / (\kappa + 1)$, where $\kappa = \lambda_{\max} / \lambda_{\min}$.

## Remarks

The error satisfies $e_{k+1} = (I - \omega A) e_k$, and $I - \omega A$ has the eigenvalues $1 - \omega \lambda$ for the eigenvalues $\lambda$ of $A$.
All of them lie in $(-1, 1)$ exactly when $0 < \omega \lambda_{\max} < 2$, which gives clause 1.
The largest of $\abs{1 - \omega \lambda_{\min}}$ and $\abs{1 - \omega \lambda_{\max}}$ is least when the two are equal, which gives clause 2.
Example: if $A$ has eigenvalues $1$ and $3$, the best choice is $\omega = 1/2$, and the error shrinks by the factor $1/2$ at each step.
The number $\kappa$ is the [[condition number|AB3S6MHJ8X]] of $A$, so the method is slow when $A$ is ill-conditioned.

## Explanations

### L1 human

The residual $b - A x$ tells how far the current guess is from solving the system.
Richardson's method moves the guess a fixed fraction $\omega$ of the residual and repeats.
The step must not be too large, or the guess overshoots and the error grows.

### L2 human

Richardson iteration is the simplest stationary [[iterative method|2RPE77ACER]], and the Jacobi method is Richardson iteration applied to the system scaled by the diagonal.
With a [[preconditioner|KE98SW3SBD]] $P$ it becomes $x^{(k+1)} = x^{(k)} + \omega P^{-1} (b - A x^{(k)})$, and the same analysis applies to $P^{-1} A$.
For a symmetric positive definite $A$ it is gradient descent with a fixed step on $\frac12 x^T A x - b^T x$.
Letting $\omega$ vary with $k$ and choosing the steps as reciprocal Chebyshev nodes leads to Chebyshev iteration.
