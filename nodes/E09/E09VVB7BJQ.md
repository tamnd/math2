---
tag: E09VVB7BJQ
kind: definition
name: Hall subgroup
msc: [20D20]
defines: KPWW9X14V2
uses: [G5S1M9, 0X1JXT47GA, 0B85S2V2DR, 0DTXBQPA2S, 0VZ48N083F, 01826KMG2H, 0053CQE9Y2, 8Z8PE69SJS, 64K1A69C80]
sources:
  - url: https://en.wikipedia.org/wiki/Hall_subgroup
---

## Definition

Let $G$ be a finite [[group|G5S1M9]].
A *Hall subgroup* of $G$ is a [[subgroup|0X1JXT47GA]] $H$ whose [[order|0B85S2V2DR]] and [[index|0DTXBQPA2S]] are [[coprime|0VZ48N083F]]: $\gcd(\abs{H}, [G : H]) = 1$.

Let $\pi$ be a set of [[prime numbers|01826KMG2H]].
A *$\pi$-number* is a positive integer whose prime factors all lie in $\pi$.
A *Hall $\pi$-subgroup* of $G$ is a subgroup $H$ such that $\abs{H}$ is a $\pi$-number and $[G : H]$ has no prime factor in $\pi$.

## Remarks

A Hall subgroup $H$ is a Hall $\pi$-subgroup for $\pi$ the set of primes dividing $\abs{H}$.
For $\pi = \set{p}$, the Hall $\pi$-subgroups are the [[Sylow $p$-subgroups|0053CQE9Y2]].

Example: $A_4 \le A_5$.
Here $\abs{A_4} = 12$ and $[A_5 : A_4] = 5$, and $\gcd(12, 5) = 1$, so $A_4$ is a Hall $\set{2, 3}$-subgroup of $A_5$.

Non-example: the subgroup $\set{0, 2}$ of $\Z/4\Z$.
Its order is $2$ and its index is $2$, and $\gcd(2, 2) = 2 \ne 1$.

Hall $\pi$-subgroups need not exist: $A_5$ has no subgroup of order $15$ or $20$, so it has no Hall $\set{3, 5}$-subgroup and no Hall $\set{2, 5}$-subgroup.
In solvable groups they always exist, by [[Hall's theorem|8Z8PE69SJS]].
A normal Hall subgroup always has a complement, by the [[Schur–Zassenhaus theorem|64K1A69C80]].
