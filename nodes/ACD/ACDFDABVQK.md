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

For a square matrix over a field, many conditions from different parts of linear algebra are all equivalent to invertibility, so checking any one of them settles all the others.
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
17. The [[null space|0PHDYNR24D]] of $A$ is $\{0\}$.
18. The [[column space|03AJKXH1AV]] of $A$ is $F^n$.
19. The [[transpose|09DXWYRD43]] $A^{\mathsf{T}}$ is invertible.
20. The rows of $A$ are linearly independent.
21. $\det A \ne 0$, where $\det$ is the [[determinant|00KDZRW4C0]].
22. The number $0$ is not an [[eigenvalue|0BQAA2BK3Q]] of $A$.

The equivalence of condition 21 with condition 1 is the [[determinant criterion|FBSAPTP1PR]] of the sub-area on determinants, and condition 22 is condition 7 in the language of eigenvalues.

## Remarks

### The theorem at work

Take $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ and do one row operation:
$$\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \xrightarrow{R_2 \to R_2 - 3R_1} \begin{pmatrix} 1 & 2 \\ 0 & -2 \end{pmatrix}.$$
There are two pivots, so condition 5 holds.
The theorem now gives everything else for free: $A$ is invertible, its columns form a basis of $F^2$, and $Ax = b$ has exactly one solution for each $b$.
Check with condition 21: $\det A = 4 - 6 = -2 \ne 0$.

For $B = \begin{pmatrix} 1 & 2 \\ 2 & 4 \end{pmatrix}$, the operation $R_2 \to R_2 - 2R_1$ gives a zero row and only one pivot, so every condition fails.
Two of the failures are visible at once:
$$B \begin{pmatrix} 2 \\ -1 \end{pmatrix} = \begin{pmatrix} 2 - 2 \\ 4 - 4 \end{pmatrix} = 0,$$
and $(1, 0)^{\mathsf{T}}$ is not in the column space, since every column of $B$ has second entry twice its first.

### How the conditions are organized

The list looks long, but it has a simple shape.
Conditions 2, 7, 10, 13 and 17 say that $A$ loses no information: different inputs give different outputs.
Conditions 3, 8, 11, 14 and 18 say that $A$ reaches every output.
Conditions 4, 5, 6 and 16 are about elimination, and 19 and 20 are about the transpose.
The content of the theorem is that, for a square matrix, the first group and the second group are equivalent, so that losing nothing and reaching everything go together.
The [[proof|WBJGQNKA4A]] runs through the list as two cycles of implications that meet in the pivot count.

### Watch out: the matrix must be square

For a non-square matrix the two groups split apart, and a right inverse is not a left inverse.
The $2 \times 3$ matrix $A = \begin{pmatrix} 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$ of the [[right inverse example|540E86V3N9]] has
$$AB = I_2 \quad \text{for} \quad B = \begin{pmatrix} 1 & -1 \\ 0 & 1 \\ 0 & 0 \end{pmatrix}, \qquad \text{but} \quad BA = \begin{pmatrix} 1 & 0 & -1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix} \ne I_3.$$
Here conditions 3, 8, 11 and 14 hold, while 2, 7, 10 and 13 fail, since $A(1, -1, 1)^{\mathsf{T}} = 0$.
In fact no $2 \times 3$ matrix has a left inverse, because it always has a nonzero vector in its null space.

### Why the other hypotheses are needed

Finite dimension matters.
On the space of infinite sequences, the [[shift operators|MRJ5JPW9HN]] give a linear map that is injective but not surjective, so conditions 13 and 14 come apart.
The field matters too.
Over the ring $\mathbb{Z}$, the $1 \times 1$ matrix $(2)$ satisfies condition 7, since $2x = 0$ forces $x = 0$, but it is not invertible, because $\tfrac{1}{2} \notin \mathbb{Z}$.

### What it gives you

To prove that a square matrix is invertible, check whichever condition is easiest, for example a trivial null space or a single one-sided inverse.
To prove that it is singular, exhibit one failure, such as a nonzero solution of $Ax = 0$.
Some quick consequences: a square matrix with a zero row or a zero column is singular, and a square matrix with dependent columns cannot be onto.

### Generalizations

For a linear map $T \colon V \to V$ of a finite-dimensional vector space, the conditions injective, surjective and bijective are equivalent, by the [[theorem on injective endomorphisms|0912EEEVCT]].
Over a commutative ring, $A$ is invertible exactly when $\det A$ is a unit, by the [[determinant criterion over rings|03Q7RE2HXR]], and condition 7 is then weaker than invertibility.

## Explanations

### L1 human

A square matrix either has an inverse or it does not.
The theorem lists many ways to tell which case we are in.
Each test gives the same answer, so we can use the test that is easiest for the matrix in front of us.
For a $2 \times 2$ matrix, the quickest test is often $ad - bc \ne 0$.

### L2 human

In practice, row reduce and count pivots: $n$ pivots means every condition holds, and fewer means every condition fails.
The reduction also hands you a witness of failure, a free variable that gives a nonzero solution of $Ax = 0$.
Use the theorem in proofs to trade a hard condition for an easy one.
For example, to show that $AB = I_n$ forces $BA = I_n$, note that $B$ satisfies condition 7, since $Bx = 0$ gives $x = A(Bx) = 0$, so $B$ is invertible.
A trap: everything here is for square matrices only.

### L3 human

The heart of the theorem is that, for an endomorphism of a finite-dimensional space, injective and surjective are the same, which is a form of rank-nullity.
In ring language, the matrix ring $M_n(F)$ is Dedekind-finite, meaning that $AB = I_n$ implies $BA = I_n$.
Its non-units are exactly its zero divisors: a singular $A$ has a nonzero $x$ with $Ax = 0$, and then $A$ times the matrix with first column $x$ and other columns $0$ is the zero matrix.
