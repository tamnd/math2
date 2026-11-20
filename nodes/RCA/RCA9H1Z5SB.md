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

1. Case $\operatorname{rank} A = n$. Then $\det A \neq 0$ by the [[invertibility criterion|FBSAPTP1PR]], and $\operatorname{adj} A = (\det A) A^{-1}$ by the [[inverse via the adjugate|0ENVM493VK]].
2. A nonzero multiple of an invertible matrix is invertible. So $\operatorname{adj} A$ has rank $n$.
3. Case $\operatorname{rank} A \le n - 2$. By the [[rank by minors|HVHQ50TJB1]], every minor of order $n - 1$ of $A$ is $0$.
4. The entries of $\operatorname{adj} A$ are these minors with signs, by the [[definition of the adjugate|0GMPYM0NSR]]. So $\operatorname{adj} A = 0$, of rank $0$.
5. Case $\operatorname{rank} A = n - 1$. By the rank by minors, some minor of order $n - 1$ is nonzero. So $\operatorname{adj} A \neq 0$, and its rank is at least $1$.
6. $A$ is not invertible, so $\det A = 0$ by the invertibility criterion.
7. By the [[adjugate identity|0528HKWZ1Z]], $A \operatorname{adj} A = (\det A) I_n = 0$. So every column of $\operatorname{adj} A$ lies in the kernel of $A$.
8. By [[rank-nullity|0W4FSW1TVB]], the kernel of $A$ has dimension $n - (n - 1) = 1$.
9. So the columns of $\operatorname{adj} A$ span a subspace of a line, and by step 5 they span the whole kernel. Hence $\operatorname{rank} \operatorname{adj} A = 1$.

## Idea

The entries of the adjugate are the minors of order $n - 1$, so the rank of $A$ decides whether they all vanish.
In the middle case $A \operatorname{adj} A = 0$ forces the columns of the adjugate into the kernel of $A$, which is a line.

## Variants

Over a commutative ring the middle case has an analogue: $A \operatorname{adj} A = 0$ still holds when $\det A = 0$, and the columns of $\operatorname{adj} A$ solve $Ax = 0$.
