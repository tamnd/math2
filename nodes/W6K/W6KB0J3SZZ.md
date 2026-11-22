---
tag: W6KB0J3SZZ
kind: statement
role: theorem
name: Matrix transformations of Fⁿ
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0NRYHJPQG2]
uses: [0NRYHJPQG2, 0RJF668P1T, 0CCQV3884B, 0V7ZD6P7RK]
sources:
  - locator: src/section2-6.xml:465
    url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-6.xml#L465
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Matrices
  - book: isbn:9780321982384
    locator: Section 1.9
  - book: isbn:9780134860244
    locator: Section 2.2
---

## Statement

The theorem says that the linear maps from $F^n$ to $F^m$ are exactly the multiplications by $m \times n$ matrices, and it tells you which matrix to use.
Let $F$ be a field and let $m, n \ge 1$ be integers.

1. For each $m \times n$ matrix $A$ over $F$, the map $T_A \colon F^n \to F^m$, $T_A(x) = Ax$, is a [[linear map|0RJF668P1T]].
2. Conversely, for each linear map $T \colon F^n \to F^m$ there is exactly one $m \times n$ matrix $A$ with $T(x) = Ax$ for all $x \in F^n$.
3. This matrix is $A = \begin{pmatrix} T(e_1) & T(e_2) & \cdots & T(e_n) \end{pmatrix}$, so its column $j$ is $T(e_j)$, where $e_1, \dots, e_n$ is the [[standard basis|0V7ZD6P7RK]] of $F^n$.

The map $T_A$ is called the *matrix transformation* of $A$, and $A$ is called the *standard matrix* of $T$.

## Remarks

### A worked use

Let $T \colon \R^2 \to \R^3$ be linear with $T(1, 0) = (1, 2, 0)$ and $T(0, 1) = (3, 0, -1)$.
Part 3 puts the two images side by side as columns:
$$A = \begin{pmatrix} 1 & 3 \\ 2 & 0 \\ 0 & -1 \end{pmatrix}.$$
Then part 2 computes any value, for example
$$T(2, 1) = A \begin{pmatrix} 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 2 + 3 \\ 4 + 0 \\ 0 - 1 \end{pmatrix} = \begin{pmatrix} 5 \\ 4 \\ -1 \end{pmatrix}.$$
Check: linearity alone gives $T(2, 1) = 2(1, 2, 0) + (3, 0, -1) = (5, 4, -1)$, the same vector.
In the same way, the rotation of $\R^2$ by a right angle sends $e_1 \mapsto e_2$ and $e_2 \mapsto -e_1$, so its matrix is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.

### Why the hypotheses are needed

The source and the target must be the coordinate spaces $F^n$ and $F^m$ over one field.
An abstract space $V$ has no standard basis, so a matrix needs a choice of basis first, and that is the subject of the [[matrix of a linear map|0YQSGNYE3K]].
Part 2 needs linearity: the map $x \mapsto x^2$ on $\R$ is not of the form $x \mapsto ax$, because it is [[not linear|RMC0D67M01]].

### What it gives you

For $n = m = 1$, the linear maps $F \to F$ are exactly the maps $x \mapsto ax$ with $a \in F$.
The map $A \mapsto T_A$ is a bijection from $M_{m \times n}(F)$ to the [[space of linear maps|0X9MBPP2Z3]] from $F^n$ to $F^m$, and under it the matrix product matches the [[composite|FSXBBV9C76]].
The [[image of T_A|B6KFVB1H5F]] is the column space of $A$, and the kernel of $T_A$ is the null space of $A$.
The [[plane transformations|5BXHREC8C8]] use part 3 to find the matrices of rotations, reflections and shears.

### The converse and generalizations

Parts 1 and 2 are converses of each other, so a map $F^n \to F^m$ is linear if and only if it is a matrix transformation.
For finite-dimensional spaces $V$ and $W$ with chosen bases, each linear map $V \to W$ has a [[matrix|0YQSGNYE3K]], and the [[linear map of a matrix|06HMCTAQH3]] goes the other way.
In infinite dimension a linear map is still fixed by the images of a basis, by the [[theorem on bases|0R8X9XA83A]], but the "matrix" then has infinitely many columns.

## History

Cayley introduced matrices in his memoir of 1858 as a short notation for linear substitutions of variables.
In that memoir the product of two matrices is defined so that it matches the composite of the two substitutions.

## Explanations

### L1 human

A linear map from $F^n$ to $F^m$ is the same thing as multiplication by a matrix.
The columns of the matrix are the images of the standard basis vectors.
So a linear map of the plane is known as soon as the images of $(1, 0)$ and $(0, 1)$ are known.
For example, if $(1, 0)$ goes to $(2, 0)$ and $(0, 1)$ goes to $(0, 3)$, the matrix is $\begin{pmatrix} 2 & 0 \\ 0 & 3 \end{pmatrix}$.

### L2 human

Here is a typical problem: find the matrix of the projection $P \colon \R^3 \to \R^3$ onto the $xy$-plane.
The projection keeps the first two coordinates and sets the third to $0$, so $P(e_1) = e_1$, $P(e_2) = e_2$ and $P(e_3) = 0$.
These are the columns of the matrix:
$$A = \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 0 \end{pmatrix}.$$
Check: $A (4, 5, 6)^{\mathsf T} = (4, 5, 0)^{\mathsf T}$, which is the projection of $(4, 5, 6)$.
The method needs no formula for $P$, only its effect on three vectors.
Watch out: the images go into the columns, not the rows, and putting them in the rows gives the transpose.

### L3 human

The theorem says that $F^n$ is the free vector space on the $n$ generators $e_1, \dots, e_n$: a linear map out of it is the same as a free choice of $n$ vectors.
In the language of categories, the spaces $F^n$ with the linear maps between them form a category isomorphic to the category whose objects are the integers $n \ge 0$ and whose morphisms are matrices, with the matrix product as composition.
Mathlib states this as a linear equivalence between `Matrix (Fin m) (Fin n) F` and the linear maps, called `Matrix.toLin'`.
The sub-area on matrices of linear maps extends the dictionary to all finite-dimensional spaces.
