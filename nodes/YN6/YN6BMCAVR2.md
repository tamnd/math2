---
tag: YN6BMCAVR2
kind: proof
name: Proof that a homogeneous system with more unknowns than equations has a nontrivial solution
proves: JPW6KVS70A
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [FCM29NQ6DN, P3HMRQN5KT, E4GKK727ZM, 0J0BBCMJ5W]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
---

## Proof

Let $R$ be the reduced row echelon form of $A$, which exists by [[the existence theorem|FCM29NQ6DN]].

1. The matrix $[R \mid 0]$ is row equivalent to $[A \mid 0]$, because the operations do not change a zero column.
2. So $Ax = 0$ and $Rx = 0$ have the same solutions, by [[the row equivalence theorem|E4GKK727ZM]].
3. The matrix $[R \mid 0]$ is in reduced row echelon form, and its last column has no leading entry, because it is zero.
4. Each row of $R$ has at most one leading entry, so $R$ has at most $m$ [[pivot|0J0BBCMJ5W]] columns.
5. Second part, first direction: assume that some column $f$ of $R$ has no pivot, so $k \ge 1$ free variables exist.
6. By [[the lemma on systems in RREF|P3HMRQN5KT]], part 3, there is a solution with $x_f = 1$ and every other free variable $0$.
7. This solution has $x_f = 1 \neq 0$, so it is nontrivial.
8. Second part, second direction: assume that every column has a pivot, so $k = 0$.
9. Then part 4 of the lemma gives a bijection from $F^0$, a set with one element, onto the solutions.
10. So $x = 0$ is the only solution.
11. First part: if $n > m$, then $R$ has at most $m < n$ pivot columns, by step 4.
12. So some column has no pivot, and step 7 gives a nontrivial solution.

## Idea

There are more columns than possible pivots, so some variable is free, and we set it to $1$.

## Variants

With the rank-nullity theorem: $\dim \ker A = n - \operatorname{rank} A \ge n - m \ge 1$.
A proof by induction on $m$ eliminates one unknown with the first equation and applies the induction hypothesis to the remaining $m - 1$ equations in $n - 1$ unknowns.
