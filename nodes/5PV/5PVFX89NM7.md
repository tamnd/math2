---
tag: 5PVFX89NM7
kind: statement
role: theorem
name: Similarity does not depend on the field
aliases: [similarity-is-invariant-under-field-extension, similarity-over-a-field-extension]
msc: ["15A21"]
topics: [GEBYZKYV3D]
audience: grad
about: [0E89HQATM8, 0EQWVHF3W5]
uses: [0EQWVHF3W5, 027KDW2K72, F7GJPMVBXA, 03NDVCSHSB]
sources:
  - url: https://en.wikipedia.org/wiki/Frobenius_normal_form
    locator: General case and theory
  - url: https://en.wikipedia.org/wiki/Transpose
    locator: Properties
  - book: isbn:9780135367971
    locator: Section 7.2
---

## Statement

Enlarging the field never makes two matrices similar that were not similar before: a change of basis with entries in a bigger field can always be replaced by one with entries in the field of the matrices.

Let $K \subseteq L$ be a [[field extension|0EQWVHF3W5]] and let $A, B \in M_n(K)$.

1. The [[invariant factors|F7GJPMVBXA]] of $A$ over $K$ are also the invariant factors of $A$ over $L$.
2. If $A$ and $B$ are [[similar|027KDW2K72]] over $L$, that is, $B = Q^{-1} A Q$ for some $Q \in GL_n(L)$, then $B = P^{-1} A P$ for some $P \in GL_n(K)$.
3. In particular, the [[minimal polynomial|03NDVCSHSB]] of $A$ is the same over $K$ and over $L$.

## Remarks

### A real similarity found through the complex numbers

Take the two real rotations by a quarter turn in opposite directions,
$$A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}, \qquad B = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.$$
Both have characteristic polynomial $x^2 + 1$, with the distinct eigenvalues $i$ and $-i$.
So over $\mathbb{C}$ both are similar to $\operatorname{diag}(i, -i)$, and hence to each other.
The theorem promises a real similarity as well, and one is easy to find: the reflection $P = \operatorname{diag}(1, -1)$ gives
$$P^{-1} A P = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} = B.$$
In words, a rotation turns into the opposite rotation when we look at it in a mirror.

### Why each hypothesis is needed

Both matrices must have their entries in $K$.
The real matrix $A$ above is similar over $\mathbb{C}$ to $\operatorname{diag}(i, -i)$, but the second matrix is not in $M_2(\mathbb{R})$, so no real similarity can exist.
No hypothesis on $L$ is needed.
The extension can be finite or infinite, algebraic or transcendental, because the proof only uses the uniqueness of the rational canonical form over $L$.

### What it gives you

To decide whether two rational matrices are similar, we may compute over $\mathbb{C}$, for example with Jordan forms, and the answer holds over $\mathbb{Q}$.
If two real matrices have the same complex Jordan form, they are similar over $\mathbb{R}$, even when that Jordan form has nonreal entries, as in the example above.
The invariant factors and the rational canonical form of $A$ can be computed in the smallest field that contains the entries of $A$.
The minimal polynomial of $A$ does not change when $K$ grows, which is part 3.

### The converse

The converse holds and is immediate.
A similarity over $K$ is a similarity over $L$, since $GL_n(K) \subseteq GL_n(L)$.

### Generalizations

The same result holds for finite-dimensional modules over a finite-dimensional algebra over $K$: if two modules become isomorphic after the extension of scalars to $L$, they are isomorphic over $K$.
This is the Noether-Deuring theorem.
For a pair of matrices with the same characteristic polynomial $\chi$, the algebra is $K[x]/(\chi)$, and $x$ acts through $A$ on one module and through $B$ on the other.

## Explanations

### L1 human

Suppose two matrices have only rational numbers as entries.
If some change of basis with complex entries turns one into the other, then there is also a change of basis with rational entries that does the same.
So the extra numbers of a bigger field never make two matrices similar.
For example, the two quarter-turn rotations of the plane are related by a mirror, which has entries $1$ and $-1$ only.

### L2 human

Here is a typical problem: are $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & -2 \\ 1 & -1 \end{pmatrix}$ similar over $\mathbb{R}$, and by which matrix?
Both have trace $0$ and determinant $1$, so both have characteristic polynomial $x^2 + 1$.
Over $\mathbb{C}$ both are similar to $\operatorname{diag}(i, -i)$, since the eigenvalues are distinct.
The theorem then gives a real $P$ with $B = P^{-1} A P$.
To find one, solve $AP = PB$; the matrix $P = \begin{pmatrix} 1 & -1 \\ 0 & 1 \end{pmatrix}$ works, since
$$AP = \begin{pmatrix} 0 & -1 \\ 1 & -1 \end{pmatrix} = PB.$$
Check: $\det P = 1 \ne 0$, so $P$ is invertible.
The trap is to look for $P$ among the complex eigenvector matrices: those give a complex similarity, and the real one has to be found separately.

### L3 human

The rational canonical form of $A$ over $K$ has entries in $K$, and it is also a rational canonical form over $L$, so the uniqueness over $L$ forces the two forms to agree.
In the same way, the [[Smith normal form of $xI - A$|92VZF0QRM8]] uses only gcds, and the gcd of polynomials in $K[x]$ does not change in $L[x]$.
For infinite $K$ there is also a direct argument, since the solutions of $AX = XB$ form a $K$-space whose $L$-span is the solution space over $L$, and $\det$ restricted to it is a nonzero polynomial.
So the map from similarity classes over $K$ to similarity classes over $L$ is injective, and the [[proof by the rational canonical form|K8ZFWFS2BG]] gives the first argument in full and the second in outline.
