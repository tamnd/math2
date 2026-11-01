---
tag: MGSX6V5Y5Y
kind: definition
name: Selberg sieve
msc: [11N35, 11N36]
defines: 5252P3NHT7
uses: [4G65M0ZWAZ, M4G4RXASTY]
sources:
  - url: https://en.wikipedia.org/wiki/Selberg_sieve
---

## Definition

Let $\mathcal{A}$ be a finite set of integers, $\mathcal{P}$ a set of primes, $z \ge 2$, and $P(z)$, $\mathcal{A}_d$ and $S(\mathcal{A}, \mathcal{P}, z)$ as for the [[Brun sieve|M4G4RXASTY]].
Let $D \ge 1$.
Let $(\lambda_d)$ be real numbers indexed by the divisors $d$ of $P(z)$ such that:

1. $\lambda_1 = 1$;
2. $\lambda_d = 0$ for $d > D$.

The *Selberg sieve* is the upper bound
$$S(\mathcal{A}, \mathcal{P}, z) \le \sum_{a \in \mathcal{A}} \Big( \sum_{d \mid \gcd(a, P(z))} \lambda_d \Big)^{2} = \sum_{d_1, d_2 \mid P(z)} \lambda_{d_1} \lambda_{d_2}\, \#\mathcal{A}_{\lcm(d_1, d_2)},$$
together with the choice of the weights $\lambda_d$ that minimises the main term of the right side.
That main term is a quadratic form in the $\lambda_d$ once $\#\mathcal{A}_d$ is written as $X g(d) + r_d$ with a multiplicative function $g$ and remainders $r_d$.

## Remarks

The inequality holds termwise: if $\gcd(a, P(z)) = 1$, the inner sum is $\lambda_1 = 1$; otherwise the square is $\ge 0$.
Example: take $\mathcal{A} = \set{1, \ldots, 10}$, $P(z) = 6$, $D = 3$, $\lambda_1 = 1$, $\lambda_2 = \lambda_3 = -1/2$ and $\lambda_6 = 0$.
The inner sum is $1$ for the three $a$ coprime to $6$, and $1/2$ for the six $a$ divisible by exactly one of $2$ and $3$.
It is $0$ for $a = 6$.
So the bound is $3 + 6 \cdot \tfrac14 = 4.5$, and indeed $S(\mathcal{A}, \mathcal{P}, z) = 3 \le 4.5$.
Non-example: weights with $\lambda_1 = 0$ fail clause 1, and then $a = 1$ contributes $0$ instead of $1$, so the inequality can fail.
With $0 < g(p) < 1$ for $p \mid P(z)$, the optimal weights give the main term $X / G$ with
$$G = \sum_{\substack{d \mid P(z) \\ d \le D}} \prod_{p \mid d} \frac{g(p)}{1 - g(p)},$$
and they satisfy $\abs{\lambda_d} \le 1$.
