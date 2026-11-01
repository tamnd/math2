---
tag: 8KK1BQSPJT
kind: definition
name: Krull domain
msc: [13F05]
defines: CB9WJCN9BM
uses: [09S3PFBEPM, 0VF11ZTTMD, MGM3CNJW9V]
sources:
  - url: https://en.wikipedia.org/wiki/Krull_ring
---

## Definition

Let $A$ be an [[integral domain|09S3PFBEPM]] with [[field of fractions|0VF11ZTTMD]] $K$.
A *discrete valuation* of $K$ is a surjective map $v \colon K^\times \to \Z$ with $v(xy) = v(x) + v(y)$ and $v(x + y) \ge \min(v(x), v(y))$ whenever $x, y, x + y \in K^\times$; its ring is $R_v = \set{0} \cup \set{x \in K^\times : v(x) \ge 0}$, a [[discrete valuation ring|MGM3CNJW9V]].
$A$ is a *Krull domain* if there is a family $(v_i)_{i \in I}$ of discrete valuations of $K$ such that:

1. $A = \bigcap_{i \in I} R_{v_i}$;
2. for every $x \in K^\times$, $v_i(x) \ne 0$ for only finitely many $i \in I$.

## Remarks

Example: $\Z$ is a Krull domain, with the $p$-adic valuations $v_p$ of $\Q$ for all primes $p$.
A rational number $x$ lies in $\Z$ exactly when $v_p(x) \ge 0$ for all $p$, and a nonzero rational number involves only finitely many primes.
More generally every [[unique factorisation domain|06YMXJMXYS]] and every Noetherian [[integrally closed domain|H20P600HQS]] is a Krull domain.
Non-example: $\Z[\sqrt{-3}]$ is not a Krull domain.
An intersection of valuation rings is integrally closed, but $(1 + \sqrt{-3})/2$ is a root of $x^2 - x + 1$ and does not lie in $\Z[\sqrt{-3}]$.
So clause 1 fails for every family.
The family can be chosen as the valuations of the localizations $A_P$ at the height-one primes $P$ of $A$.
By the [[Mori–Nagata theorem|J8YYYP5CDN]], the integral closure of a Noetherian domain is a Krull domain.
