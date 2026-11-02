---
tag: CRZH89G0J1
kind: definition
name: Hahn polynomials
msc: [33C45, 42C05]
defines: Y1M82VZYS2
uses: [YZHM3HSM0F, VDBAW9PN88, 0GBZM0MT0F]
sources:
  - url: https://en.wikipedia.org/wiki/Hahn_polynomials
---

## Definition

Let $N \ge 0$ be an integer, let $\alpha, \beta > -1$ be real numbers, and let $n$ be an integer with $0 \le n \le N$.
Write $(a)_k$ for the [[Pochhammer symbol|YZHM3HSM0F]].
The *Hahn polynomial* of degree $n$ is
$$Q_n(x; \alpha, \beta, N) = \sum_{k=0}^{n} \frac{(-n)_k \, (n + \alpha + \beta + 1)_k \, (-x)_k}{(\alpha + 1)_k \, (-N)_k \, k!},$$
that is, the terminating [[generalized hypergeometric series|VDBAW9PN88]] ${}_3F_2\left( -n, n + \alpha + \beta + 1, -x; \alpha + 1, -N; 1 \right)$.

## Remarks

They are orthogonal on $\set{0, 1, \dots, N}$:
$$\sum_{x=0}^{N} \binom{\alpha + x}{x} \binom{\beta + N - x}{N - x} Q_m(x) Q_n(x) = 0 \quad (m \ne n),$$
where the [[binomial coefficients|0GBZM0MT0F]] are $\binom{a + j}{j} = \frac{(a + 1)_j}{j!}$.
Example: $Q_1(x) = 1 - \frac{(\alpha + \beta + 2) x}{(\alpha + 1) N}$.
Check: the weight is proportional to a beta-binomial distribution with mean $\frac{N(\alpha + 1)}{\alpha + \beta + 2}$, so $Q_1$ has weighted mean $0$.
Non-example: $n = N + 1$ is not allowed, since $(-N)_k = 0$ for $k = N + 1$ and the defining sum has a zero denominator.
The value at $0$ is $Q_n(0) = 1$.
