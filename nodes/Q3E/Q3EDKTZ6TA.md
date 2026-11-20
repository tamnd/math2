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

Let $F$ be a field, and let $V$ and $W$ be vector spaces over $F$ with bases $B = (b_1, \dots, b_n)$ and $C = (c_1, \dots, c_m)$.
Then the map
$$\Phi \colon \Hom_F(V, W) \to M_{m \times n}(F), \qquad T \mapsto [T]_{C,B},$$
from the [[space of linear maps|0VPCJWGMP9]] to the space of $m \times n$ matrices is a [[linear isomorphism|0B8T10CE7N]].
Its inverse sends a matrix $A$ to the [[linear map of $A$|009892PZ30]] in the bases $B$ and $C$.

## Remarks

### Why each hypothesis is needed

- The bases must be finite, so that the matrices have finitely many rows and columns.
- The isomorphism depends on the bases. A different choice of bases gives a different isomorphism, related by the [[change-of-basis formula|0MQXVZEBMT]].

### Consequences

- $\dim \Hom_F(V, W) = mn = \dim V \cdot \dim W$, as in the theorem on the [[dimension of $\Hom(V, W)$|0Z9N1ER0W0]].
- The linear maps $E_{ij}$ with $E_{ij}(b_j) = c_i$ and $E_{ij}(b_k) = 0$ for $k \ne j$ form a basis of $\Hom_F(V, W)$. They correspond to the matrix units.
- For $V = W$ and $B = C$, the map $\Phi$ also respects products, by the theorem on the [[matrix of a composition|05Q1B7MH0M]]. So it is an isomorphism of algebras $\End(V) \cong M_n(F)$, as in the theorem on the [[algebra of endomorphisms|7BDGQ1Q46E]].

### Converse

Not every linear isomorphism $\Hom_F(V, W) \to M_{m \times n}(F)$ is of the form $\Phi$ for some bases.
Take $V = W = \R$.
Each $T$ is $x \mapsto tx$, and $[T]_{B,B} = (t)$ for every basis $B = (b)$, since $T(b) = tb$.
So the isomorphism $T \mapsto (2t)$ is not $\Phi$ for any choice of bases.

### Generalizations

For free modules of finite rank over a commutative ring, the same map is an isomorphism of modules, with the same proof.
In Mathlib, this is the linear equivalence `LinearMap.toMatrix`, and its inverse is `Matrix.toLin`.

## Explanations

### L1 human

Once bases are fixed, linear maps and matrices of the right size are the same thing.
Adding maps or scaling a map corresponds to adding or scaling its matrix.

### L2 human

The map $T \mapsto [T]_{C,B}$ is linear, because the coordinates of $(S + \lambda T)(b_j)$ are those of $S(b_j)$ plus $\lambda$ times those of $T(b_j)$.
It is injective, because a linear map is determined by the images of the basis vectors.
It is surjective, because each choice of images of the basis vectors defines a linear map.

### L3 human

The isomorphism is natural only after the bases are chosen.
Without bases, $\Hom(V, W)$ is naturally isomorphic to $V^* \otimes W$ in finite dimension, and a choice of bases identifies $V^* \otimes W$ with $F^n \otimes F^m \cong M_{m \times n}(F)$.
