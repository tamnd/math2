---
tag: RCA9H1Z5SB
kind: proof
name: Proof of the rank of the adjugate
msc: ["15A09"]
topics: [DTBK11SR77]
audience: ug2
proves: 9CJME5W96T
methods: [0WCP0PVET6]
uses: [HVHQ50TJB1, 0528HKWZ1Z, 0ENVM493VK, FBSAPTP1PR, 0W4FSW1TVB, 0GMPYM0NSR]
sources:
  - url: https://en.wikipedia.org/wiki/Adjugate_matrix
    locator: Properties
---

## Proof

We treat the three cases one by one: the inverse formula settles full rank, the rank by minors settles low rank, and the adjugate identity settles rank $n - 1$.
Let $A$ be an $n \times n$ matrix over a field $F$ with $n \ge 2$.

*Case $\operatorname{rank} A = n$.*

1. Then $A$ is invertible, so $\det A \neq 0$ by the [[invertibility criterion|FBSAPTP1PR]].
2. By the [[inverse via the adjugate|0ENVM493VK]], $\operatorname{adj} A = (\det A) A^{-1}$.
3. A nonzero scalar times an invertible matrix is invertible, with inverse $(\det A)^{-1} A$.
   So $\operatorname{adj} A$ is invertible and has rank $n$.

*Case $\operatorname{rank} A \le n - 2$.*

4. By the [[rank by minors|HVHQ50TJB1]], every minor of $A$ of size $n - 1$ is $0$, since a nonzero one would give rank at least $n - 1$.
5. By the [[definition of the adjugate|0GMPYM0NSR]], the entries of $\operatorname{adj} A$ are these minors with signs.
   So $\operatorname{adj} A = 0$, and its rank is $0$.

*Case $\operatorname{rank} A = n - 1$.*

6. By the rank by minors, some minor of size $n - 1$ is nonzero.
   So $\operatorname{adj} A$ has a nonzero entry, and its rank is at least $1$.
7. The matrix $A$ is not invertible, so $\det A = 0$ by the invertibility criterion.
8. By the [[adjugate identity|0528HKWZ1Z]], $A \operatorname{adj} A = (\det A) I_n = 0$.
   So every column of $\operatorname{adj} A$ lies in the kernel of $A$.
9. By the [[rank-nullity theorem|0W4FSW1TVB]], the kernel of $A$ has dimension $n - (n - 1) = 1$.
10. So the columns of $\operatorname{adj} A$ span a subspace of a line, and by step 6 this subspace is not zero.
    Hence the columns span the whole kernel, and $\operatorname{rank} \operatorname{adj} A = 1$.

## Idea

The entries of the adjugate are the minors of size $n - 1$, so the rank of $A$ decides at once whether they all vanish.
In the middle case the identity $A \operatorname{adj} A = 0$ pushes every column of the adjugate into the kernel of $A$.
That kernel is a line, so the adjugate can have rank at most $1$, and it has a nonzero entry, so its rank is exactly $1$.

## Variants

The middle case can also be done with rows: $\operatorname{adj} A \cdot A = 0$ puts every row of $\operatorname{adj} A$ in the left kernel of $A$, which is also a line.
Over a commutative ring that is not a field, the rank is not available, but the key step survives: when $\det A = 0$, the identity still gives $A \operatorname{adj} A = 0$, so the columns of $\operatorname{adj} A$ solve $Ax = 0$.
