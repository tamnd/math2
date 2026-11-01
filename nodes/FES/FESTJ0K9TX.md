---
tag: FESTJ0K9TX
kind: statement
role: theorem
name: Sylow theorems
msc: [20D20]
uses: [G5S1M9, 01826KMG2H, 0053CQE9Y2, 06QYRTX9KQ, 0H11ZPX4ND, 0YGN3VAA0D, 0DTXBQPA2S, 0V98WY94B8, 09GCQ5STVJ, 0Q8DGAZSJ4, 0M3PYJ3TSE, 09ZJ6CAK7S, 3C53TD, 0PDBVPP233, 0CB0DX5BVV, 0QTZDKJEDV, KPWW9X14V2, H1BSG0J5G1]
about: [0053CQE9Y2]
sources:
  - url: https://en.wikipedia.org/wiki/Sylow_theorems
    locator: Statement
same_as:
  wikidata: Q1057919
  wikipedia: Sylow theorems
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $p$ be a [[prime number|01826KMG2H]], and write $\abs{G} = p^n m$ with $n \ge 0$ and $p \nmid m$.
A [[Sylow $p$-subgroup|0053CQE9Y2]] of $G$ is a subgroup of order $p^n$, and $n_p$ denotes the number of them.

1. $G$ has a Sylow $p$-subgroup.
2. Any two Sylow $p$-subgroups of $G$ are [[conjugate|0H11ZPX4ND]] in $G$, and every [[$p$-subgroup|06QYRTX9KQ]] of $G$ is contained in some Sylow $p$-subgroup.
3. $n_p \equiv 1 \pmod p$, $n_p$ divides $m$, and $n_p = [G : N_G(P)]$ for any Sylow $p$-subgroup $P$, where $N_G(P)$ is the [[normaliser|0YGN3VAA0D]] of $P$.

## Remarks

Each part has its own node: the [[first Sylow theorem|0V98WY94B8]], the [[second Sylow theorem|09GCQ5STVJ]] and the [[third Sylow theorem|0Q8DGAZSJ4]].
The rest of part 3 is in the nodes [[$n_p$ divides the index|0M3PYJ3TSE]] and [[$n_p$ is the index of the normaliser|09ZJ6CAK7S]].
The usual proofs let a group act on a set and count orbits or fixed points.
Part 1 uses the action on subsets of size $p^n$, or induction on $\abs{G}$.
Parts 2 and 3 let a $p$-group act on conjugates or cosets, and count its fixed points modulo $p$.

Example: every group $G$ of order $15 = 3 \cdot 5$ is cyclic.
By part 3, $n_3$ divides $5$ and $n_3 \equiv 1 \pmod 3$, so $n_3 = 1$; and $n_5$ divides $3$ and $n_5 \equiv 1 \pmod 5$, so $n_5 = 1$.
So $G$ has a [[normal|0CB0DX5BVV]] subgroup of order $3$ and one of order $5$.
Their intersection is $\set{e}$, since its order divides both $3$ and $5$.
Hence $G \cong \Z/3\Z \times \Z/5\Z \cong \Z/15\Z$.

The prime power in part 1 matters: the converse of [[Lagrange's theorem|3C53TD]] fails for other divisors, since [[$A_4$ has no subgroup of order $6$|0PDBVPP233]].

## Explanations

### L1 human

Lagrange's theorem says that the order of a subgroup divides the order of the group, but a group need not have a subgroup of each such order.
The Sylow theorems say that this does hold for the largest prime power dividing the order.
Moreover, these largest prime-power subgroups are all alike, and their number obeys strict rules.

### L2 human

The Sylow theorems are the first main tool to study finite groups through their order alone.
A typical use: the counting rules in part 3 force $n_p = 1$, so the Sylow subgroup is normal and the group is not simple.
In this way one shows, for example, that no group of order $20$ and no group of order $pq$, with primes $p < q$, is simple.
The theorems lead to the [[Frattini argument|0QTZDKJEDV]], to [[Hall subgroups|KPWW9X14V2]] in solvable groups, and to the study of how $p$-elements are conjugate, as in the [[focal subgroup theorem|H1BSG0J5G1]].
