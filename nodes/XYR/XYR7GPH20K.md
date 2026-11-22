---
tag: XYR7GPH20K
kind: statement
role: theorem
name: Characteristic and minimal polynomial of a companion matrix
aliases: [polynomials-of-a-companion-matrix]
msc: ["15A21", "15A18"]
topics: [GEBYZKYV3D]
audience: ug2
about: [0ZCWPNZTQ3]
uses: [0VH1TC1PWF, 039HF58KQ5, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Companion_matrix
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cyclic_subspace
    locator: Companion matrix
---

## Statement

The companion matrix of a monic polynomial has that polynomial as its characteristic polynomial, and no shorter polynomial kills it.
Let $F$ be a field, let $n \ge 1$, and let $p = x^n + c_{n-1} x^{n-1} + \cdots + c_0 \in F[x]$ be monic.
Let $C = C(p)$ be its [[companion matrix|0VH1TC1PWF]] in the column version.
Then:

1. $C^{i-1} e_1 = e_i$ for $1 \le i \le n$, so $e_1$ is a cyclic vector of $C$;
2. the [[minimal polynomial|03NDVCSHSB]] of $C$ is $p$;
3. the [[characteristic polynomial|039HF58KQ5]] $\det(xI - C)$ of $C$ is $p$.

The same holds for the row version $C^{\mathsf T}$.

## Remarks

### A worked case

Let $p = x^3 - 1$ over $\mathbb{Q}$, so $C = C(p)$ has columns $e_2$, $e_3$, $e_1$.
Part 1 is the chain $e_1 \mapsto e_2 \mapsto e_3$, and one more step gives $C^3 e_1 = C e_3 = e_1$.
So $(C^3 - I) e_1 = 0$, and then $(C^3 - I) e_i = C^{i-1} (C^3 - I) e_1 = 0$ for each $i$, which means $C^3 = I$.
No shorter polynomial works, because for $f = a_0 + a_1 x + a_2 x^2$ we get
$$f(C) e_1 = a_0 e_1 + a_1 e_2 + a_2 e_3,$$
which is zero only when $f = 0$.
So $m_C = x^3 - 1 = p$, as part 2 says.

### Why each hypothesis is needed

The polynomial must be monic, because minimal and characteristic polynomials are monic by definition.
For $a p$ with $a \ne 0, 1$, the theorem applies to $p$ after you divide by $a$.
The field is used only in part 2, where the minimal polynomial needs division with remainder; part 3 holds over every commutative ring.

### What it gives you

Every monic polynomial of degree $n \ge 1$ is the characteristic polynomial of some $n \times n$ matrix, namely $C(p)$.
The roots of $p$ in $F$ are exactly the eigenvalues of $C(p)$ in $F$.
Since a matrix is diagonalizable exactly when its minimal polynomial splits into distinct linear factors, $C(p)$ is diagonalizable over $F$ if and only if $p$ has $n$ distinct roots in $F$.
If $p = (x - \lambda)^n$, then $C(p)$ is [[similar|027KDW2K72]] to the [[Jordan block|07PH4RX0X5]] $J_n(\lambda)$, since both are cyclic with the same characteristic polynomial.

### The converse

A matrix whose minimal and characteristic polynomials are both $p$ need not equal $C(p)$.
For example, $J_2(1)$ has both polynomials equal to $(x - 1)^2$, and it is not a companion matrix.
But such a matrix is always similar to $C(p)$, by the [[criterion for cyclic maps|RK1QVMYW7H]].

### Generalizations

Over a commutative ring $R$, the identity $\det(xI - C(p)) = p$ still holds, by the same cofactor expansion.
For a monic matrix polynomial $x^k I + A_{k-1} x^{k-1} + \cdots + A_0$ with square blocks $A_i$, the block companion matrix has characteristic polynomial $\det(x^k I + A_{k-1} x^{k-1} + \cdots + A_0)$.

## Explanations

### L1 human

The companion matrix of a polynomial is built so that its characteristic polynomial is that polynomial.
The theorem also says that no shorter polynomial kills the matrix.
For example, the matrix with columns $(0, 1)$ and $(-1, 0)$ is a quarter turn of the plane.
Turning twice gives minus the identity, so $x^2 + 1$ kills it, and no polynomial of degree $1$ does, since a quarter turn is not a multiple of the identity.

### L2 human

Here is a typical use: build a rational matrix with characteristic polynomial $x^3 - 2$.
The coefficients are $c_0 = -2$ and $c_1 = c_2 = 0$, so
$$C = \begin{pmatrix} 0 & 0 & 2 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{pmatrix}.$$
Check: $C e_1 = e_2$, $C e_2 = e_3$ and $C e_3 = 2 e_1$, so $C^3 e_1 = 2 e_1$, and in the same way $C^3 = 2I$.
By the theorem, $C$ has minimal polynomial $x^3 - 2$, which has no rational root.
So $C$ has no rational eigenvalue and no invariant line in $\mathbb{Q}^3$, although it is a matrix with integer entries.
Watch out: $x^3 - 1$ has three distinct complex roots, but $C(x^3 - 1)$ is not diagonalizable over $\mathbb{Q}$, because the factor $x^2 + x + 1$ has no rational root.

### L3 human

The matrix $C(p)$ is the matrix of multiplication by $x$ on the $F[x]$-module $F[x]/(p)$ in the basis $1, x, \dots, x^{n-1}$.
The annihilator of this module is the ideal $(p)$, which gives part 2 at once, and its dimension is $n = \deg p$, which then gives part 3.
The [[rational canonical form|042JWAR3Q0]] writes every matrix as a block diagonal matrix of companion matrices, so the theorem is the basic case of all of similarity theory.
