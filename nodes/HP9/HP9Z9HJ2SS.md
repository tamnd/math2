---
tag: HP9Z9HJ2SS
kind: definition
name: Generalized hypergeometric function
msc: ["33C20"]
defines: VDBAW9PN88
uses: [YZHM3HSM0F, 0MZB06ST2B, 0N288P2TB5]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_hypergeometric_function
---

## Definition

Let $p, q \ge 0$ be integers, let $a_1, \ldots, a_p \in \C$, and let $b_1, \ldots, b_q \in \C \setminus \set{0, -1, -2, \ldots}$.
Let $(x)_n$ be the [[Pochhammer symbol|YZHM3HSM0F]].
The *generalized hypergeometric series* is the [[power series|0MZB06ST2B]]
$${}_pF_q(a_1, \ldots, a_p; b_1, \ldots, b_q; z) = \sum_{n=0}^{\infty} \frac{(a_1)_n \cdots (a_p)_n}{(b_1)_n \cdots (b_q)_n} \, \frac{z^n}{n!}.$$
The *generalized hypergeometric function* is its sum where it converges, together with its analytic continuation.

## Remarks

Assume that no $a_i$ is a non-positive integer, so that the series does not terminate.
By the ratio test, its [[radius of convergence|0N288P2TB5]] is:

1. infinite when $p \le q$, so the function is entire;
2. equal to $1$ when $p = q + 1$, and then the function continues analytically to $\C \setminus [1, \infty)$;
3. equal to $0$ when $p > q + 1$.

Examples: ${}_0F_0(;;z) = e^z$ and ${}_1F_0(a;;z) = (1 - z)^{-a}$ for $\abs{z} < 1$.
Also $J_\nu(x) = \frac{(x/2)^\nu}{\Gamma(\nu + 1)} \, {}_0F_1(;\nu + 1; -x^2/4)$ for the Bessel function of the first kind.

Non-example: ${}_2F_0(1, 1;; z) = \sum_n n! \, z^n$ is a formal series with radius of convergence $0$; it is only an asymptotic series and defines no function near $0$.

A lower parameter equal to an upper one cancels: ${}_{p+1}F_{q+1}(a, c; b, c; z) = {}_pF_q(a; b; z)$, with $a$ and $b$ standing for the lists of parameters.
