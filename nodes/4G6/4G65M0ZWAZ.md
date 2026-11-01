---
tag: 4G65M0ZWAZ
kind: definition
name: Brun sieve
msc: [11N35, 11N36]
defines: M4G4RXASTY
uses: [0FANE7P0DY, 08RQ62VAVA, 0XM8ZA9RNM]
sources:
  - url: https://en.wikipedia.org/wiki/Brun_sieve
---

## Definition

Let $\mathcal{A}$ be a finite set of integers, let $\mathcal{P}$ be a set of primes and let $z \ge 2$ be real.
Let $P(z)$ be the product of the primes $p \in \mathcal{P}$ with $p < z$.
For $d \ge 1$ let $\mathcal{A}_d = \set{a \in \mathcal{A} : d \mid a}$.
The sifting function is
$$S(\mathcal{A}, \mathcal{P}, z) = \#\set{a \in \mathcal{A} : \gcd(a, P(z)) = 1}.$$
Let $\mu$ be the [[Möbius function|0FANE7P0DY]] and $\omega(d)$ the [[number of distinct prime factors|08RQ62VAVA]] of $d$.
The *Brun sieve* in its simplest form, Brun's pure sieve, uses the truncated sums
$$S_r = \sum_{\substack{d \mid P(z) \\ \omega(d) \le r}} \mu(d)\, \#\mathcal{A}_d,$$
together with the inequalities, valid for every integer $r \ge 0$,
$$S_{2r+1} \le S(\mathcal{A}, \mathcal{P}, z) \le S_{2r}.$$

## Remarks

Example: let $\mathcal{A} = \set{1, \ldots, 10}$, let $\mathcal{P}$ be all primes and $z = 4$, so $P(z) = 6$.
Then $S(\mathcal{A}, \mathcal{P}, 4) = \#\set{1, 5, 7} = 3$.
Here $S_0 = 10$ and $S_1 = 10 - 5 - 3 = 2$, so $S_1 \le 3 \le S_0$; and $S_2 = 2 + \#\mathcal{A}_6 = 3$.
The inequalities are the Bonferroni inequalities: for $m \ge 1$, the partial sums $\sum_{j \le k} (-1)^j \binom{m}{j}$ are $\ge 0$ for even $k$ and $\le 0$ for odd $k$.
Non-example: the full Legendre sum $S_r$ with $r \ge \omega(P(z))$ is exact, but it is not a truncation.
It has $2^{\omega(P(z))}$ terms, and the errors in approximating each $\#\mathcal{A}_d$ add up.
Brun's later, more refined sieve replaces the condition $\omega(d) \le r$ by conditions on the sizes of the prime factors of $d$.
