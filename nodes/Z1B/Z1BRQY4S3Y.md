---
tag: Z1BRQY4S3Y
kind: definition
name: Racah polynomials
msc: [33C45, 33C80]
defines: P6JYNDX5DR
uses: [YZHM3HSM0F, VDBAW9PN88]
sources:
  - url: https://en.wikipedia.org/wiki/Racah_polynomials
---

## Definition

Let $N \ge 0$ be an integer, let $\alpha, \beta, \gamma, \delta$ be real numbers, and assume that one of $\alpha + 1$, $\beta + \delta + 1$, $\gamma + 1$ equals $-N$.
Write $(a)_k$ for the [[Pochhammer symbol|YZHM3HSM0F]] and set $\lambda(x) = x(x + \gamma + \delta + 1)$.
For $0 \le n \le N$, the *Racah polynomial* of degree $n$ is
$$R_n(\lambda(x); \alpha, \beta, \gamma, \delta) = \sum_{k=0}^{n} \frac{(-n)_k \, (n + \alpha + \beta + 1)_k \, (-x)_k \, (x + \gamma + \delta + 1)_k}{(\alpha + 1)_k \, (\beta + \delta + 1)_k \, (\gamma + 1)_k \, k!},$$
that is, the terminating [[generalized hypergeometric series|VDBAW9PN88]] ${}_4F_3\left( -n, n + \alpha + \beta + 1, -x, x + \gamma + \delta + 1; \alpha + 1, \beta + \delta + 1, \gamma + 1; 1 \right)$, assuming the denominators do not vanish.

## Remarks

Since $(-x)_k (x + \gamma + \delta + 1)_k = \prod_{j=0}^{k-1} \left( j(j + \gamma + \delta + 1) - \lambda(x) \right)$, each $R_n$ is a polynomial of degree $n$ in $\lambda(x)$.
Example: $R_1 = 1 + \frac{(\alpha + \beta + 2) \, \lambda(x)}{(\alpha + 1)(\beta + \delta + 1)(\gamma + 1)}$.
They are orthogonal on $x = 0, 1, \dots, N$ for the weight
$$w(x) = \frac{(\alpha + 1)_x (\beta + \delta + 1)_x (\gamma + 1)_x (\gamma + \delta + 1)_x \left( \frac{\gamma + \delta + 3}{2} \right)_x}{(-\alpha + \gamma + \delta + 1)_x (-\beta + \gamma + 1)_x \left( \frac{\gamma + \delta + 1}{2} \right)_x (\delta + 1)_x \, x!},$$
that is, $\sum_{x=0}^{N} w(x) R_m(\lambda(x)) R_n(\lambda(x)) = 0$ for $m \ne n$; the weight is positive for suitable ranges of the parameters.
The balanced condition holds: the sum of the lower parameters exceeds the sum of the upper ones by $1$.
Non-example: with $\alpha + 1 = -N$, the degree $n = N + 1$ is not allowed, since the term $k = N + 1$ has the factor $(\alpha + 1)_{N+1} = (-N)_{N+1} = 0$ in its denominator.
