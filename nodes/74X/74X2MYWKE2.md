---
tag: 74X2MYWKE2
kind: statement
name: Eigenvalues of a regular Sturm–Liouville problem
role: theorem
msc:
  - 34B24
  - 34L10
about:
  - 7WV6B2502K
uses:
  - 0BQAA2BK3Q
  - TM8VQJWGHZ
  - 7WV6B2502K
sources:
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ch-eigenvalue-probs.tex#L134
    locator: ch-eigenvalue-probs.tex:134
---

## Statement

Consider the [[Sturm–Liouville|7WV6B2502K]] [[boundary value problem|TM8VQJWGHZ]] on an interval $[a,b]$. It has the equation $(p y')' + q y + \lambda r y = 0$ with one separated boundary condition at each end, of the form $\alpha_1 y(a) - \alpha_2 y'(a) = 0$ and $\beta_1 y(b) + \beta_2 y'(b) = 0$.

Assume that the functions $p$, $p'$, $q$ and $r$ are continuous on $[a,b]$. Assume also that $p > 0$ and $r > 0$ at every point of $[a,b]$.

Then the problem has [[eigenvalues|0BQAA2BK3Q]] that form a strictly increasing sequence $\lambda_1 < \lambda_2 < \lambda_3 < \cdots$ with $\lambda_n \to +\infty$. For each $\lambda_n$, the eigenfunctions are exactly the multiples of one function $y_n$. So each eigenspace has dimension one.

If in addition $q \geq 0$ on $[a,b]$ and $\alpha_1, \alpha_2, \beta_1, \beta_2 \geq 0$, then every $\lambda_n$ is nonnegative.
