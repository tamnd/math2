---
tag: Q3EDKTZ6TA
kind: statement
role: theorem
name: Linear maps between finite-dimensional spaces correspond to matrices
msc: ["15A04"]
topics: [S6559D61BP]
audience: ug1
about: [06HMCTAQH3, 0YQSGNYE3K, 0X9MBPP2Z3]
uses: [0YYMY95FWS, 009892PZ30, 0VPCJWGMP9, 0B8T10CE7N]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Matrices
  - book: isbn:9783031410253
    locator: Chapter 3
  - book: isbn:9780134860244
    locator: Section 2.4
---

## Statement

Once bases are fixed, the linear maps from $V$ to $W$ and the matrices of the matching size are the same thing, and adding or scaling maps is adding or scaling matrices.
Let $F$ be a field, and let $V$ and $W$ be vector spaces over $F$ with finite ordered bases $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$.
Then the map
$$\Phi \colon \Hom_F(V, W) \to M_{m \times n}(F), \qquad T \mapsto [T]_{C,B},$$
from the [[space of linear maps|0VPCJWGMP9]] to the space of $m \times n$ matrices, which sends $T$ to its [[matrix|0YYMY95FWS]], is a [[linear isomorphism|0B8T10CE7N]].
Its inverse sends a matrix $A$ to the [[linear map of A|009892PZ30]] in the bases $B$ and $C$.
The [[proof|V6R98FKC2K]] checks linearity, injectivity and surjectivity.

## Remarks

### Why each hypothesis is needed

The bases must be finite, so that the matrices have finitely many rows and columns.
For an infinite-dimensional space such as the polynomial ring $\mathbb{R}[x]$ with the basis $1, x, x^2, \dots$, the same recipe still gives each map an array, but the array is infinite, with finitely many nonzero entries in each column.
So the statement with $M_{m \times n}(F)$, and the count of dimensions below, needs finite bases.

The isomorphism depends on the bases.
A different choice of bases gives a different isomorphism, and the [[change of basis formula|0MQXVZEBMT]] relates the two.
For example, the identity of $\mathbb{R}^2$ has the matrix $I_2$ when $B = C$, but the matrix $\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$ when $B = ((1, 1), (1, -1))$ and $C$ is the standard basis.

### What it gives you

The dimension follows at once: $\dim \Hom_F(V, W) = mn = \dim V \cdot \dim W$, as in the theorem on the [[dimension of Hom(V, W)|0Z9N1ER0W0]].
A basis comes with it.
The maps $E_{ij}$ with $E_{ij}(b_j) = c_i$ and $E_{ij}(b_k) = 0$ for $k \ne j$ correspond to the matrix units, so they form a basis of $\Hom_F(V, W)$, as the [[example on matrix units|XQB25QZHAH]] checks for $\Hom(\mathbb{R}^3, \mathbb{R}^2)$.
For $V = W$ and $B = C$, the map $\Phi$ also respects products, by the theorem on the [[matrix of a composition|05Q1B7MH0M]].
So it is an isomorphism of algebras $\End(V) \cong M_n(F)$, as in the theorem on the [[algebra of endomorphisms|7BDGQ1Q46E]].

### The converse

Is every linear isomorphism $\Hom_F(V, W) \to M_{m \times n}(F)$ of the form $\Phi$ for some bases?
No.
Take $V = W = \mathbb{R}^2$, and let $\psi(T)$ be the standard matrix of $T$ with the two entries of its first row swapped.
Then $\psi$ is linear and bijective, and $\psi(\id) = \begin{pmatrix} 0 & 1 \\ 0 & 1 \end{pmatrix}$ has rank $1$.
But for any bases, the columns of $[\id]_{C,B}$ are the coordinate vectors $[b_1]_C$ and $[b_2]_C$, which are independent, so $[\id]_{C,B}$ has rank $2$.
So $\psi$ is not $\Phi$ for any choice of $B$ and $C$.

### Generalizations

For free modules of finite rank over a commutative ring, the same map is an isomorphism of modules, with the same proof.
In Mathlib this is the linear equivalence `LinearMap.toMatrix`, and its inverse is `Matrix.toLin`.

## Explanations

### L1 human

Once bases are fixed, linear maps and tables of numbers of the right size are the same thing.
Every map has exactly one table, and every table comes from exactly one map.
Adding two maps adds their tables, and doubling a map doubles its table.
So the linear maps from a space of dimension $3$ to a space of dimension $2$ form a space of dimension $6$, one for each entry of a $2 \times 3$ table.

### L2 human

The map $T \mapsto [T]_{C,B}$ is linear, because the coordinates of $(S + \lambda T)(b_j)$ are those of $S(b_j)$ plus $\lambda$ times those of $T(b_j)$.
It is injective, because a linear map is determined by the images of the basis vectors.
It is surjective, because each choice of images of the basis vectors defines a linear map.
For a typical use, take the derivative $D$ and the identity on $P_2$ with the basis $(1, x, x^2)$: the matrix of $D + 3\,\id$ is
$$\begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 2 \\ 0 & 0 & 0 \end{pmatrix} + 3 I_3 = \begin{pmatrix} 3 & 1 & 0 \\ 0 & 3 & 2 \\ 0 & 0 & 3 \end{pmatrix}.$$
Check: $(D + 3\,\id)(x^2) = 2x + 3x^2$, whose coordinates $(0, 2, 3)$ are the third column.

### L3 human

The isomorphism is natural only after the bases are chosen.
Without bases, $\Hom(V, W)$ is naturally isomorphic to $V^* \otimes W$ in finite dimension, and a choice of bases identifies $V^* \otimes W$ with $F^n \otimes F^m \cong M_{m \times n}(F)$.
The sub-area on [[duality|9K7FFF26QR]] studies $V^*$, and there the transpose of a matrix gets its meaning as the matrix of the dual map.
