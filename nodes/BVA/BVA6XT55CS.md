---
tag: BVA6XT55CS
kind: statement
role: theorem
name: Euler product for multiplicative functions
msc: [11A25, 11M06, 40A20]
uses: [0AP80TT660, 0SN0MAEKYX, 0W3K3QPEWT, 084HH1NDCB, RZ0Z2BTMT4]
about: [JYV1Y8XX16]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_product
same_as:
  wikidata: Q1194667
  wikipedia: Euler product
---

## Statement

Let $f$ be a [[multiplicative function|0AP80TT660]] from the positive integers to $\C$ such that $\sum_{n=1}^{\infty} f(n)$ converges [[absolutely|0W3K3QPEWT]].
Then for each [[prime|0SN0MAEKYX]] $p$ the series $\sum_{k=0}^{\infty} f(p^k)$ converges absolutely, and
$$\sum_{n=1}^{\infty} f(n) = \lim_{x \to \infty} \prod_{p \le x} \sum_{k=0}^{\infty} f(p^k),$$
where the [[product|RZ0Z2BTMT4]] runs over the primes $p \le x$.
If $f$ is completely multiplicative, then $\abs{f(p)} < 1$ for each prime $p$, and the factor for $p$ equals $1/(1 - f(p))$.

## Remarks

For finite $x$, multiplying out the finitely many absolutely convergent factors gives $\sum f(n)$ over all $n$ whose prime factors are at most $x$.
Here one uses that $f$ is multiplicative and the [[fundamental theorem of arithmetic|084HH1NDCB]].
Every missing $n$ is larger than $x$, so the difference from the full sum is at most $\sum_{n > x} \abs{f(n)}$, which tends to $0$.
With $f(n) = n^{-s}$ and $\operatorname{Re}(s) > 1$ this is the [[Euler product formula|0C3PN4075R]] for the zeta function.
With $f(n) = \mu(n) n^{-s}$, where $\mu$ is the [[Möbius function|0C8QENHYZW]], it gives $\sum \mu(n) n^{-s} = \prod_p (1 - p^{-s})$.

## Explanations

### L1 human

An Euler product writes a sum over all positive integers as a product over the primes.
It works because each integer is built from primes in exactly one way, and a multiplicative function respects this building.
It is the basic bridge between sums over integers and the primes.

### L2 human

Euler products are the starting point of analytic number theory.
The zeta function, Dirichlet $L$-functions and many other Dirichlet series have them in their half-plane of absolute convergence.
From the product one reads off facts about primes and zeros.
For example, the zeta function has no zeros where its Euler product converges, since a convergent product of nonzero factors is nonzero.
