---
tag: ACDFDABVQK
kind: statement
role: theorem
name: Invertible matrix theorem
msc: ["15A09"]
topics: [P8J6QR66TJ]
audience: ug1
about: [0EB9N0S33C]
uses: [0TWTS88TWN, 0WF5AQYTW6, 0BCMGDHZGR, 0M79HRJCRR, 04KGXJG1A2, 0CRMGPAH83, 0DTY8B9HMS, 0KCQ9Y3QKA, 0NRYHJPQG2, 0ZC9YTXZRY, 0PHDYNR24D, 03AJKXH1AV, 09DXWYRD43, 00KDZRW4C0, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: The invertible matrix theorem
  - book: isbn:9780321982384
    locator: Section 2.3
  - book: isbn:9780134860244
    locator: Section 3.2
---

## Statement

Let $F$ be a field, let $A$ be an $n \times n$ matrix over $F$, and let $T \colon F^n \to F^n$ be the [[linear map|0NRYHJPQG2]] $T(x) = Ax$.
The following conditions are equivalent.

1. $A$ is [[invertible|0TWTS88TWN]].
2. $A$ has a left inverse: $CA = I_n$ for some $n \times n$ matrix $C$.
3. $A$ has a right inverse: $AD = I_n$ for some $n \times n$ matrix $D$.
4. The [[reduced row echelon form|0WF5AQYTW6]] of $A$ is $I_n$.
5. $A$ has $n$ [[pivot positions|0BCMGDHZGR]].
6. $A$ is a product of [[elementary matrices|0M79HRJCRR]].
7. The [[homogeneous system|04KGXJG1A2]] $Ax = 0$ has only the trivial solution.
8. The system $Ax = b$ has at least one solution for each $b \in F^n$.
9. The system $Ax = b$ has exactly one solution for each $b \in F^n$.
10. The columns of $A$ are [[linearly independent|0CRMGPAH83]].
11. The columns of $A$ [[span|0DTY8B9HMS]] $F^n$.
12. The columns of $A$ form a [[basis|0KCQ9Y3QKA]] of $F^n$.
13. $T$ is injective.
14. $T$ is surjective.
15. $T$ is bijective.
16. The [[rank|0ZC9YTXZRY]] of $A$ is $n$.
17. The [[null space|0PHDYNR24D]] of $A$ is $\set{0}$.
18. The [[column space|03AJKXH1AV]] of $A$ is $F^n$.
19. The [[transpose|09DXWYRD43]] $A^{\mathsf{T}}$ is invertible.
20. The rows of $A$ are linearly independent.

Two more conditions are equivalent to these, by theorems of later sub-areas.

21. $\det A \ne 0$, where $\det$ is the [[determinant|00KDZRW4C0]]. The equivalence with condition 1 is the [[determinant criterion|FBSAPTP1PR]] of the sub-area on determinants.
22. The number $0$ is not an [[eigenvalue|0BQAA2BK3Q]] of $A$. By the definition of an eigenvalue, $0$ is an eigenvalue exactly when $Ax = 0$ for some $x \ne 0$, so this condition is condition 7 in other words.

## Remarks

### Why each hypothesis is needed

The matrix must be square.
For the $2 \times 3$ matrix of the [[right inverse example|540E86V3N9]], conditions 3, 8, 11 and 14 hold, but conditions 2, 7, 10 and 13 fail.
The dimension must be finite: the [[shift operators|MRJ5JPW9HN]] give an injective map that is not surjective.
Over a commutative ring that is not a field, conditions 7 and 1 differ.
The $1 \times 1$ matrix $(2)$ over $\mathbb{Z}$ satisfies condition 7 but is not invertible.

### Consequences

- To show that $A$ is invertible, it is enough to check any one condition, for example a zero null space or one one-sided inverse.
- If one condition fails, all fail. For example, a square matrix with dependent columns is not onto.
- A square matrix with a zero row or a zero column is singular.

### Converse

The theorem is a list of equivalences, so each part is the converse of another part.
No such theorem holds for non-square matrices.
There, the conditions split into those about injectivity (2, 7, 10, 13) and those about surjectivity (3, 8, 11, 14).

### Generalizations

For a linear map $T \colon V \to V$ of a finite-dimensional vector space, the conditions "injective", "surjective" and "bijective" are equivalent, by the [[theorem on injective endomorphisms|0912EEEVCT]].
Over a commutative ring, $A$ is invertible exactly when $\det A$ is a unit, by the [[determinant criterion over rings|03Q7RE2HXR]].

## History

The name "invertible matrix theorem" and the long list of conditions are due to modern textbooks.
Lay gives a list of this kind in his Section 2.3.

## Explanations

### L1 human

A square matrix either has an inverse or it does not.
The theorem lists many ways to tell which case we are in.
Each test gives the same answer, so we can use the test that is easiest for the matrix in front of us.

### L2 human

Worked example: let $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$.

1. $R_2 \to R_2 - 3R_1$ gives $\begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}$, an echelon form with $2$ pivots. So condition 5 holds.
2. By the theorem, $A$ is invertible, its columns form a basis of $F^2$, and $Ax = b$ has exactly one solution for each $b$.
3. As a check of condition 21, $\det A = 4 - 6 = -2 \ne 0$.

For $B = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the same operation $R_2 \to R_2 - 2R_1$ gives a zero row, so only $1$ pivot.
So every condition fails for $B$: for example $B(2, -1)^{\mathsf{T}} = 0$, and $(1, 0)^{\mathsf{T}}$ is not in the column space.
A trap: the theorem is only for square matrices.

### L3 human

Conditions 1 to 9 are about the algebra of $A$.
Conditions 10 to 18 are about the linear map $T$ and its subspaces, and conditions 19 and 20 use the transpose.
The heart of the theorem is that, for an endomorphism of a finite-dimensional space, injective and surjective are the same; this is rank-nullity.
In ring language, the matrix ring $M_n(F)$ is Dedekind-finite, and its non-units are exactly the zero divisors.
