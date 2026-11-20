---
tag: 02FDWY55AS
kind: statement
role: proposition
name: Rank of a product of matrices
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
about: [0ZC9YTXZRY]
uses: [0EWQEYRVA8, 076JGP6R3T]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.rank_mul_le
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 3.2
---

## Statement

Let $F$ be a field, let $A$ be an $m \times n$ matrix and $B$ an $n \times p$ matrix over $F$.
Then
$$\rank(AB) \le \min(\rank A, \rank B),$$
where $\rank$ is the [[rank of a matrix|0ZC9YTXZRY]].

## Remarks

### Why each hypothesis is needed

- The product must be defined, so the number of columns of $A$ must equal the number of rows of $B$.
- The inequality can be strict. For $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$, $\rank A = \rank B = 1$ but $AB = 0$.

### Consequences

- If $A$ is invertible, then $\rank(AB) = \rank B$. If $B$ is invertible, then $\rank(AB) = \rank A$.
- So [[similar matrices|0E89HQATM8]] and [[equivalent matrices|0CMHSGTWXB]] have the same rank.
- A product of $n \times n$ matrices is invertible only if each factor has rank $n$.

### Converse

There are lower bounds as well.
[[Sylvester's rank inequality|GS8WE1ZYV9]] gives $\rank A + \rank B - n \le \rank(AB)$.
The Frobenius inequality in the same node bounds the rank of a product of three matrices.
For a sum, [[subadditivity|5M6SX7JN01]] gives $\rank(A + B) \le \rank A + \rank B$.
Over $\R$, [[the rank of the Gram matrix|FGPT52R1ZE]] gives the equality $\rank(A^\top A) = \rank A$.

### Generalizations

For linear maps $S \colon U \to V$ and $T \colon V \to W$ between finite-dimensional spaces, $\rank(TS) \le \min(\rank T, \rank S)$.
The proof is the same: $\im(TS) \subseteq \im T$, and $\im(TS)$ is the image of $\im S$ under $T$.

## History

The inequality is classical, and it appears in the standard textbooks on matrix theory.

## Explanations

### L1 human

Multiplying by a matrix can never create new independent directions.
So the rank of a product is at most the rank of each factor.
Multiplying by an invertible matrix keeps the rank.

### L2 human

Each column of $AB$ is $A$ times a column of $B$, so it lies in the column space of $A$.
Each row of $AB$ is a row of $A$ times $B$, so it lies in the row space of $B$.
These two inclusions give the two bounds.

### L3 human

For linear maps, the image of a composite lies in the image of the last map, and its dimension is at most the dimension of the image of the first map.
In Mathlib the statement is `Matrix.rank_mul_le`.
