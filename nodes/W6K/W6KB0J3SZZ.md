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

Let $F$ be a field and let $m, n \ge 1$ be integers.

1. For each $m \times n$ matrix $A$ over $F$, the map $T_A \colon F^n \to F^m$, $T_A(x) = Ax$, is a [[linear map|0RJF668P1T]].
2. Conversely, let $T \colon F^n \to F^m$ be a linear map. Then there is exactly one $m \times n$ matrix $A$ with $T(x) = Ax$ for all $x \in F^n$.
3. This matrix is $A = \begin{pmatrix} T(e_1) & T(e_2) & \cdots & T(e_n) \end{pmatrix}$, so its $j$-th column is $T(e_j)$. Here $e_1, \dots, e_n$ is the [[standard basis|0V7ZD6P7RK]] of $F^n$.

The map $T_A$ is called the *matrix transformation* of $A$, and $A$ is called the *standard matrix* of $T$.

## Remarks

### Why each hypothesis is needed

- The source and target must be $F^n$ and $F^m$ with the same field $F$. For an abstract space $V$, a matrix needs a choice of basis, which is the subject of the [[matrix of a linear map|0YQSGNYE3K]].
- Part 2 needs linearity. The map $x \mapsto x^2$ on $F = \R$ is not of the form $x \mapsto ax$, since it is [[not linear|~1498930f]].

### Consequences

- The linear maps $F \to F$ are exactly the maps $x \mapsto ax$ with $a \in F$.
- To find the matrix of a linear map, compute the images of $e_1, \dots, e_n$. For the rotation of $\R^2$ by a right angle, $e_1 \mapsto e_2$ and $e_2 \mapsto -e_1$, so $A = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
- The map $A \mapsto T_A$ is a bijection from $M_{m \times n}(F)$ to the [[space of linear maps|0X9MBPP2Z3]] from $F^n$ to $F^m$. Under it, the matrix product corresponds to the [[composite|~ed2e194c]].
- The [[image of $T_A$|~b1674adb]] is the column space of $A$, and the kernel is the null space of $A$.

### Converse

Part 1 and part 2 are converses of each other.
Together they say that a map $F^n \to F^m$ is linear if and only if it is a matrix transformation.

### Generalizations

For finite-dimensional spaces $V$ and $W$ with bases, each linear map $V \to W$ has a [[matrix|0YQSGNYE3K]], and the [[linear map of a matrix|06HMCTAQH3]] goes the other way.
In infinite dimension, a linear map is still fixed by the images of a basis, by the [[theorem on bases|0R8X9XA83A]], but the "matrix" has infinitely many columns.

## History

Cayley introduced matrices in 1858 as a short notation for linear substitutions of variables.
The product of matrices was defined so that it matches the composite of two substitutions.

## Explanations

### L1 human

A linear map from $F^n$ to $F^m$ is the same thing as multiplication by a matrix.
The columns of the matrix are the images of the standard basis vectors.
So a linear map of the plane is known as soon as the images of $(1, 0)$ and $(0, 1)$ are known.

### L2 human

Let $T \colon \R^2 \to \R^3$ be linear with $T(1, 0) = (1, 2, 0)$ and $T(0, 1) = (3, 0, -1)$.

1. The standard matrix is $A = \begin{pmatrix} 1 & 3 \\ 2 & 0 \\ 0 & -1 \end{pmatrix}$.
2. Then $T(2, 1) = A \begin{pmatrix} 2 \\ 1 \end{pmatrix} = (2 + 3,\ 4 + 0,\ 0 - 1) = (5, 4, -1)$.
3. Linearity gives the same answer: $2(1, 2, 0) + (3, 0, -1) = (5, 4, -1)$.

The trap is to put the images in the rows instead of the columns, which gives the transpose.

### L3 human

The theorem says that $F^n$ is the free vector space on $n$ generators $e_1, \dots, e_n$.
In the language of categories, the full subcategory of the spaces $F^n$ is equivalent to the category of matrices over $F$, with matrix product as composition.
Mathlib states this as a linear equivalence between `Matrix (Fin m) (Fin n) F` and the linear maps, called `Matrix.toLin'`.
