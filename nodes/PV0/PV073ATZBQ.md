---
tag: PV073ATZBQ
kind: proof
name: Proof of term-by-term integration
msc: [40A30, 26A42]
proves: 0YBY3VYX0K
uses: [0MRE6XRE5V, 080RWVVSB6, 0BWGW68B66, 0K0H5E3Z5N]
sources:
  - url: https://www.jirka.org/ra/html/sec_liminter.html
    locator: Theorem 6.2.4
---

## Proof

We apply the theorem on uniform limits and integration to the partial sums.

1. Let $a < b$, and let each $f_n \colon [a, b] \to \R$ be Riemann integrable. Let $s_N = \sum_{n=0}^{N} f_n$ be the partial sums of the [[series|0MRE6XRE5V]], and let $s$ be its sum.
2. By [[linearity of the integral|080RWVVSB6]] and induction on $N$, each $s_N$ is Riemann integrable, and $\int_a^b s_N = \sum_{n=0}^{N} \int_a^b f_n$.
3. By hypothesis, the series converges uniformly on $[a, b]$. That is, $s_N \to s$ uniformly on $[a, b]$.
4. By steps 2 and 3, the theorem that [[uniform limits commute with integration|0BWGW68B66]] applies to $(s_N)$.
5. It gives that $s$ is Riemann integrable, and $\int_a^b s_N \to \int_a^b s$ as $N \to \infty$.
6. By step 2, $\int_a^b s_N$ is the $N$-th partial sum of the series $\sum_n \int_a^b f_n$. By step 5 and the definition of the [[sum of a series|0K0H5E3Z5N]], this series converges, and
$$\sum_{n=0}^{\infty} \int_a^b f_n(x) \, dx = \lim_{N \to \infty} \int_a^b s_N(x) \, dx = \int_a^b \sum_{n=0}^{\infty} f_n(x) \, dx.$$

## Idea

Finite sums can be integrated term by term, by linearity. Uniform convergence lets the limit of the partial sums pass through the integral. So the integral of the sum is the sum of the integrals.
