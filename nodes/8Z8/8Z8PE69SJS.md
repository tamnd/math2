---
tag: 8Z8PE69SJS
kind: statement
role: theorem
name: Hall's theorem on solvable groups
msc: [20D20, 20D10]
uses: [0FXJ7YFMMX, KPWW9X14V2, 01826KMG2H, 0H11ZPX4ND, FESTJ0K9TX, 64K1A69C80, 0YMYMNQ0QZ]
about: [KPWW9X14V2, 0FXJ7YFMMX]
sources:
  - url: https://en.wikipedia.org/wiki/Hall_subgroup
---

## Statement

Let $G$ be a finite [[solvable group|0FXJ7YFMMX]], and let $\pi$ be a set of [[prime numbers|01826KMG2H]].
A $\pi$-subgroup is a subgroup whose order has all its prime factors in $\pi$.

1. $G$ has a [[Hall $\pi$-subgroup|KPWW9X14V2]].
2. Any two Hall $\pi$-subgroups of $G$ are [[conjugate|0H11ZPX4ND]] in $G$.
3. Every $\pi$-subgroup of $G$ is contained in some Hall $\pi$-subgroup of $G$.

## Remarks

The proof is by induction on $\abs{G}$.
A minimal normal subgroup $N$ of a solvable group is an elementary abelian $p$-group.
One applies induction to $G/N$ and takes the preimage $K$ of a Hall $\pi$-subgroup of $G/N$.
If $p \in \pi$, then $K$ is a Hall $\pi$-subgroup of $G$.
If $p \notin \pi$, then a complement of $N$ in $K$, given by the [[Schur–Zassenhaus theorem|64K1A69C80]], is one.

Example: $G = S_3 \times \Z/5\Z$ of order $30$ is solvable, and $S_3 \times \set{0}$ is a Hall $\set{2, 3}$-subgroup, of order $6$ and index $5$.

Solvability is necessary.
The [[simple group|0YMYMNQ0QZ]] $A_5$ of order $60$ has no subgroup of order $15$, so it has no Hall $\set{3, 5}$-subgroup.
In the simple group $\mathrm{PSL}_2(\F_7)$ of order $168$ there are two conjugacy classes of subgroups isomorphic to $S_4$; these are Hall $\set{2, 3}$-subgroups, of index $7$, that are not conjugate.

Philip Hall also proved a converse.
Let $p'$ denote the set of all primes other than $p$.
If a finite group has a Hall $p'$-subgroup for every prime $p$, then it is solvable.

## Explanations

### L1 human

In any finite group, the Sylow theorems give subgroups that collect all factors of one prime in the order.
Hall's theorem says that in a solvable group one can do the same for any set of primes at once.
For example, a solvable group of order $60$ has a subgroup of order $12$, one of order $15$, and one of order $20$.
Such subgroups exist for every choice of primes, and they are unique up to conjugation.

### L2 human

The theorem extends the [[Sylow theorems|FESTJ0K9TX]] from one prime to sets of primes, but only for solvable groups.
Together with the converse, it characterises solvable groups by the existence of Hall subgroups.
Hall $p'$-subgroups are also called Sylow complements, since a Hall $p'$-subgroup and a Sylow $p$-subgroup together make up the whole order of the group.
