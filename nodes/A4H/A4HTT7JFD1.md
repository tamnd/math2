---
tag: A4HTT7JFD1
kind: concept
name: Matrix unit
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
uses: [0N1MY1T0W9, 032Q9FB8MT]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Matrix_unit
    locator: Properties
same_as:
  wikipedia: Matrix unit
---

## Summary

A matrix unit is a matrix of zeros with a single entry $1$, and every matrix is built from matrix units by scaling and adding.
Exactly, $E_{ij}$ is the [[matrix|0N1MY1T0W9]] with entry $1$ in row $i$ and column $j$ and $0$ in every other place; the [[formal definition|4H93XF4RVH]] states it.
Matrix units multiply by the [[rule|E66YRYVWQ3]]
$$E_{ij} E_{kl} = \delta_{jk} E_{il},$$
and the $mn$ matrix units of size $m \times n$ form the [[standard basis|0V7ZD6P7RK]] of the space of $m \times n$ matrices.

## Motivation

A matrix unit is the simplest nonzero matrix, and the product rule tells us every product of two of them at once.
Since every matrix is a sum of multiples of matrix units, many identities about matrices reduce to a check on matrix units, followed by linearity.
This is the standard way to find the [[center of the matrix ring|DVZ1V4A884]] and its [[two-sided ideals|Z46WD9W1ZS]].
Matrix units also give the simplest examples of [[idempotent|0KCE8CG86P]] and [[nilpotent|07BSPZPSMF]] matrices, and of pairs that do not commute.

## Notation

Other notations are $e_{ij}$ and $E^{(ij)}$, and some books write $e_i e_j^{\mathsf{T}}$, the product of a column and a row of the identity matrix.
The size is not part of the symbol; it comes from the context.
In Mathlib, `Matrix.stdBasisMatrix i j a` is the matrix with entry `a` at `(i, j)` and `0` elsewhere, and recent versions call it `Matrix.single i j a`.
Do not confuse $E_{ij}$ with the [[identity matrix|6NHZRCKJNW]], which some books write $E$.

## Remarks

### The four 2 × 2 matrix units

In size $2$ there are four matrix units:
$$E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, \quad E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, \quad E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.$$
Every $2 \times 2$ matrix is a combination of them, for example $\begin{pmatrix} 3 & -1 \\ 4 & 7 \end{pmatrix} = 3E_{11} - E_{12} + 4E_{21} + 7E_{22}$, as [[a 2 × 2 matrix written in the basis of matrix units|HXYXR42RA1]] works out.
[[The products of the 2 × 2 matrix units|CGP5S9CXT0]] checks the rule by direct computation, for instance $E_{12} E_{21} = E_{11}$ and $E_{12} E_{12} = 0$.

### What it is not

[[The identity matrix is a sum of matrix units, not a matrix unit|V9MKVNQ207]]: $I_2 = E_{11} + E_{22}$ has two entries equal to $1$.
The zero matrix and $2E_{11}$ are not matrix units either, since a matrix unit has exactly one nonzero entry, and it equals $1$.
A matrix unit is also not the [[elementary matrix|01REXW3WWE]] $I + cE_{ij}$, which adds $c$ times row $j$ to row $i$.

### The rules you can use

Let $R$ be a ring with identity and let $E_{ij}$ be the $n \times n$ matrix units over $R$.
Each matrix is $A = \sum_{i, j} a_{ij} E_{ij}$, since only the term $(i, j) = (p, q)$ contributes to the entry at $(p, q)$.
From the product rule, $E_{ii}$ is idempotent, $E_{ij}$ squares to $0$ for $i \ne j$, and $E_{11} + \dots + E_{nn} = I_n$.
Multiplying by a matrix unit moves one row or one column: $E_{ij} A$ has row $j$ of $A$ in row $i$ and zeros elsewhere, and $A E_{ij}$ has column $i$ of $A$ in column $j$ and zeros elsewhere.
Combining the two, $E_{ij} A E_{kl} = a_{jk} E_{il}$ picks out one entry of $A$ and moves it to the place $(i, l)$.
Also $\operatorname{tr} E_{ij} = \delta_{ij}$ and $E_{ij}^{\mathsf{T}} = E_{ji}$.

### Use in proofs

For $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, the rules give
$$E_{12} A = \begin{pmatrix} c & d \\ 0 & 0 \end{pmatrix}, \qquad A E_{12} = \begin{pmatrix} 0 & a \\ 0 & c \end{pmatrix}.$$
So $A$ commutes with $E_{12}$ exactly when $c = 0$ and $d = a$.
The same test with $E_{21}$ gives $b = 0$, so a matrix that commutes with every matrix unit is [[scalar|TX4J5JR205]], which is the key step for the [[center|DVZ1V4A884]].
For [[ideals|Z46WD9W1ZS]] of $M_n(F)$, the identity $E_{ij} A E_{kl} = a_{jk} E_{il}$ moves one nonzero entry of $A$ to every place.
The [[cyclic property of the trace|0Y4NF1DRKD]] and [[associativity|073E4XC016]] can also be checked on matrix units and extended by linearity.

### Watch out

The product rule has a condition: $E_{ij} E_{kl} = E_{il}$ only when the inner indices agree, $j = k$, and the product is $0$ otherwise.
So $E_{12} E_{12} = 0$, although each factor is nonzero.
The order matters too: $E_{12} E_{21} = E_{11}$ but $E_{21} E_{12} = E_{22}$.

### History

Wedderburn proved in 1908 that every finite-dimensional simple algebra is a matrix algebra over a division algebra, and the standard proofs of this build a system of matrix units inside the algebra.

### Try it

First, compute $E_{23} E_{31} E_{12}$ for $3 \times 3$ matrices.
The rule gives $E_{23} E_{31} = E_{21}$, and then $E_{21} E_{12} = E_{22}$.

Second, what is $E_{12} A E_{21}$ for $A = \begin{pmatrix} 3 & -1 \\ 4 & 7 \end{pmatrix}$?
By the rule $E_{ij} A E_{kl} = a_{jk} E_{il}$ it is $a_{22} E_{11} = 7 E_{11}$.

## Explanations

### L1 human

A matrix unit is a grid of zeros with a single $1$, and the two indices say where the $1$ is: $E_{21}$ has it in row $2$, column $1$.
Every matrix is built from these by scaling and adding, just as every vector in the plane is built from $(1, 0)$ and $(0, 1)$.

### L2 human

As a linear map, $E_{ij}$ sends the basis vector $e_j$ to $e_i$ and every other basis vector to $0$.
Then $E_{ij} E_{kl}$ first sends $e_l$ to $e_k$.
If $k = j$, the second factor sends $e_k$ on to $e_i$, so the product sends $e_l$ to $e_i$ and is $E_{il}$.
If $k \ne j$, the second factor kills $e_k$, and the product is $0$.
This is the multiplication rule, read as following arrows.

### L3 human

In a ring $S$, a family $e_{ij}$, for $1 \le i, j \le n$, with $e_{ij} e_{kl} = \delta_{jk} e_{il}$ and $\sum_i e_{ii} = 1$ is a *system of matrix units*.
Such a system forces $S \cong M_n(e_{11} S e_{11})$.
This is a main step in the structure theory of simple rings, which belongs to [[ring theory|0B1261B5ED]].
