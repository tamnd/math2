---
tag: 0S4WTRE9GG
kind: statement
role: proposition
name: Inverse of a product
msc: [15A09]
topics: [P8J6QR66TJ]
audience: ug1
about: [0EB9N0S33C]
uses: [0TWTS88TWN, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Invertible_matrix
    locator: Properties
  - book: isbn:9780321982384
    locator: Section 2.2
  - book: isbn:9780135367971
    locator: Section 1.6
---

## Statement

A product of invertible matrices is invertible, its inverse is the product of the inverses in the reverse order, and over a field a product of square matrices is invertible only when every factor is.

1. Let $R$ be a commutative ring and let $A$ and $B$ be [[invertible|0TWTS88TWN]] $n \times n$ matrices over $R$. Then the [[product|076JGP6R3T]] $AB$ is invertible, and $(AB)^{-1} = B^{-1} A^{-1}$.
2. More generally, if $A_1, \dots, A_k$ are invertible $n \times n$ matrices over $R$, then $A_1 A_2 \cdots A_k$ is invertible, and $(A_1 A_2 \cdots A_k)^{-1} = A_k^{-1} \cdots A_2^{-1} A_1^{-1}$.
3. Let $F$ be a field and let $A_1, \dots, A_k$ be $n \times n$ matrices over $F$. Then the product $A_1 A_2 \cdots A_k$ is invertible if and only if each factor $A_i$ is invertible.

## Remarks

### Why the order reverses

The matrix $AB$ acts on a vector by applying $B$ first and $A$ second, since $(AB)x = A(Bx)$.
To get back, we must undo the last step first, so $A^{-1}$ acts first and $B^{-1}$ second, and that is the matrix $B^{-1}A^{-1}$.
In the product $(AB)(B^{-1}A^{-1})$ the two inner factors meet and cancel, $BB^{-1} = I_n$, and then the outer ones cancel too.

### A check with numbers

Take $A = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$, with inverses $A^{-1} = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ and $B^{-1} = \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix}$.
Then
$$AB = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}, \qquad B^{-1}A^{-1} = \begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix},$$
and their product is
$$\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 1 & -1 \\ -1 & 2 \end{pmatrix} = \begin{pmatrix} 2 - 1 & -2 + 2 \\ 1 - 1 & -1 + 2 \end{pmatrix} = I_2.$$

### Watch out

The same order, $A^{-1}B^{-1}$, is wrong in general.
For the matrices above, $A^{-1}B^{-1} = \begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}$, and
$$(AB)(A^{-1}B^{-1}) = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}\begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix} = \begin{pmatrix} 3 & -1 \\ 1 & 0 \end{pmatrix} \ne I_2.$$
The two orders agree only when $A^{-1}$ and $B^{-1}$ commute, for example when $A$ and $B$ are diagonal.

### Why the factors must be square

Part 3 fails for factors that are not square.
For the $2 \times 3$ matrix $A$ and the $3 \times 2$ matrix $B$ of the [[right inverse example|540E86V3N9]], the product $AB = I_2$ is invertible, but neither factor is invertible, because neither is square.
The proof of part 3 needs the theorem that a [[one-sided inverse of a square matrix is two-sided|0753Y2X5K6]], and that theorem is where squareness enters.

### What it gives you

Parts 1 and 2 show that the invertible $n \times n$ matrices over $R$ are closed under products, so they form a group, the [[general linear group|0FCHE902D7]].
A product of [[elementary matrices|01REXW3WWE]] is invertible, and its inverse is the product of the inverse elementary matrices in the reverse order.
Part 3 is a test for singularity: if $AB$ is singular, then $A$ or $B$ is singular.

### The converse and generalizations

Part 3 is the converse of part 2 over a field.
It also holds over any commutative ring, by the [[determinant criterion|03Q7RE2HXR]], because $\det(A_1 \cdots A_k)$ is a unit exactly when each $\det A_i$ is a unit.
Parts 1 and 2 hold in any monoid, where the units form a group with the same rule for inverses of products.

## Explanations

### L1 human

To undo two steps, we undo the last step first.
If we first apply $B$ and then $A$, then we must first undo $A$ and then undo $B$.
Think of socks and shoes: we put on the socks first, but we take off the shoes first.

### L2 human

The typical use of part 2 is to invert a matrix that comes as a product of simple pieces.
If $A = E_3 E_2 E_1$ with elementary matrices $E_i$, then $A^{-1} = E_1^{-1} E_2^{-1} E_3^{-1}$, and each $E_i^{-1}$ is read off at sight.
The typical use of part 3 is the other direction: to prove that a factor is invertible because a product is.
For example, if $A^2 = 3I_n$ over $\mathbb{Q}$, then $A^2$ is invertible, so $A$ is invertible, with $A^{-1} = \tfrac{1}{3}A$.

### L3 human

Parts 1 and 2 hold in every monoid, so the invertible $n \times n$ matrices form the group of units $\mathrm{GL}_n(R)$ of the matrix ring.
Part 3 is special to square matrices of finite size.
In the monoid of linear maps of the space of sequences, the [[shift operators|MRJ5JPW9HN]] give $ST = 1$ while neither $S$ nor $T$ is invertible.
