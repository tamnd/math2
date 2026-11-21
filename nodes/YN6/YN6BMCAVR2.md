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

We reduce $A$ to reduced row echelon form, prove the criterion with free variables, and then count pivots to get the case $n > m$.

1. Let $R$ be the reduced row echelon form of $A$, which exists by the [[existence theorem for echelon forms|FCM29NQ6DN]]. The row operations that take $A$ to $R$ take $[A \mid 0]$ to $[R \mid 0]$, because each operation keeps a zero column zero.
2. So $Ax = 0$ and $Rx = 0$ have the same solutions, by the theorem that [[row equivalence keeps the solutions|E4GKK727ZM]].
3. The matrix $[R \mid 0]$ is in reduced row echelon form, and its last column has no leading entry, because it is zero. So we may apply the [[lemma on systems in reduced row echelon form|P3HMRQN5KT]] to it.
4. Each row of $R$ has at most one leading entry. So $R$ has at most $m$ [[pivot|0J0BBCMJ5W]] columns.
5. Suppose that some column $f$ of $R$ has no pivot, so $x_f$ is a free variable. By part 3 of the lemma, there is a solution with $x_f = 1$ and every other free variable equal to $0$. This solution is not zero, because its entry $x_f$ is $1$.
6. Suppose instead that every column of $R$ has a pivot. Then there are no free variables, and part 4 of the lemma gives a bijection from $F^0$, a set with one element, onto the solution set. Since $x = 0$ is a solution, it is the only one.
7. Steps 5 and 6 prove the criterion: $Ax = 0$ has a nonzero solution if and only if some column has no pivot.
8. Now let $n > m$. By step 4, $R$ has at most $m < n$ pivot columns, so some column has no pivot. By step 5, $Ax = 0$ has a solution $x \ne 0$.

## Idea

There are more columns than places for pivots, because each row can hold only one pivot.
So some variable is free, and we set it to $1$.
The other free variables are set to $0$, and the pivot rows then fix the basic variables.
The result is a solution with a $1$ in it, so it is not zero.

## Variants

With the rank-nullity theorem the proof is one line: $\dim \ker A = n - \rank A \ge n - m \ge 1$.
That proof uses dimension theory, which in turn is usually built on the present theorem, so it is not a first proof.

A proof by induction on $m$ avoids echelon forms.
If every coefficient of $x_1$ is zero, then $x = (1, 0, \dots, 0)$ is a nonzero solution.
Otherwise use an equation with a nonzero coefficient of $x_1$ to express $x_1$ by the other unknowns, and put this into the other $m - 1$ equations.
They become a homogeneous system in $n - 1 > m - 1$ unknowns, which has a nonzero solution by the induction hypothesis, and that solution extends to one of the original system.
