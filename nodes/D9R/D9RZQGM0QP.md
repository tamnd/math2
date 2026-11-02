---
tag: D9RZQGM0QP
kind: definition
name: Jackson kernel
msc: [42A10, 41A25, 41A35]
defines: 9MZFTX77CD
uses: [DCCA2T9GKH, J3NJQ5FZJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson%27s_inequality
---

## Definition

Let $n \ge 1$ be an integer.
The *Jackson kernel* of order $n$ is the function
$$J_n(t) = \lambda_n \left(\frac{\sin(nt/2)}{\sin(t/2)}\right)^4, \qquad t \in \R,$$
with the value $\lambda_n n^4$ at the multiples of $2\pi$.
The constant $\lambda_n > 0$ is chosen so that $\frac{1}{2\pi} \int_{-\pi}^{\pi} J_n(t) \, dt = 1$.

## Remarks

Since $\left(\frac{\sin(nt/2)}{\sin(t/2)}\right)^2 = n F_{n-1}(t)$, where $F_{n-1}$ is the [[Fejér kernel|DCCA2T9GKH]], $J_n$ is a constant times $F_{n-1}^2$.
So $J_n$ is an even, nonnegative [[trigonometric polynomial|J3NJQ5FZJ5]] of degree $2n - 2$.
Its key property is $\frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{t}^k J_n(t) \, dt \le \frac{C}{n^k}$ for $k = 1, 2$, with $C$ independent of $n$.

Example: for $n = 1$, the quotient is $1$, so $J_1 = 1$ and $\lambda_1 = 1$.

Non-example: the Fejér kernel $F_n$ is nonnegative with mean $1$, but it fails the key property for $k = 1$.
Its first moment $\frac{1}{2\pi} \int \abs{t} F_n(t) \, dt$ is of order $\frac{\log n}{n}$, not $\frac{1}{n}$.

Texts differ in the indexing; some call $J_m$ with $m \approx n/2$ the kernel of degree $n$.
The convolution $f \mapsto f * J_n$ is the Jackson operator.
