---
tag: 0JWM6GJNQW
kind: statement
role: proposition
name: An orthonormal family is linearly independent
msc: ["15A63", "46C05"]
topics: [1D4JTZ9VS3]
audience: ug1
about: [0RW9TNNT87, 0CRMGPAH83]
uses: [09VYHEF2VT, 0TS7VZJBWD, 0EVHJFTG9Z, 08ZDRN6H41]
sources:
  - url: https://en.wikipedia.org/wiki/Orthonormality
    locator: Properties
  - book: isbn:9783031410253
    locator: Chapter 6
---

## Statement

Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.

1. Let $(v_i)_{i \in I}$ be a family of nonzero vectors of $V$ that are pairwise [[orthogonal|0TS7VZJBWD]]. Then the family is [[linearly independent|0EVHJFTG9Z]].
2. Each [[orthonormal family|09VYHEF2VT]] in $V$ is linearly independent.
3. If $\dim V = n$ is finite, then each orthonormal family in $V$ has at most $n$ vectors.

## Remarks

### Why each hypothesis is needed

- Part 1 needs nonzero vectors. The family $(0, e_1)$ in $\mathbb{R}^2$ is pairwise orthogonal, since $\ip{0}{e_1} = 0$, but $1 \cdot 0 + 0 \cdot e_1 = 0$ is a nontrivial relation.
- Part 1 needs orthogonality of every pair. The nonzero vectors $(1, 0)$, $(0, 1)$ and $(1, 1)$ of $\mathbb{R}^2$ are dependent; only the pairs with $(1, 1)$ fail the test.
- Part 3 needs finite dimension. In the space of real polynomials with $\int_{-1}^1 pq$, the normalized [[Legendre polynomials|QFYGJVA996]] form an infinite orthonormal family.
- Positivity of the inner product is not used in the proof of part 2. The proof works for any sesquilinear form $\beta$ with $\beta(e_i, e_j) = \delta_{ij}$.

### Consequences

- In a space of dimension $n$, an orthonormal family of $n$ vectors is a basis, by the [[right-size criterion|096V7H13H9]]. It is an [[orthonormal basis|0S9GGTR0EX]].
- If $v = \sum_j a_j e_j$ in an orthonormal family, then the coefficients are unique, and they are $a_j = \ip{v}{e_j}$, by the [[coordinate formula|09DZ8CD1AK]].
- An $n \times k$ matrix with orthonormal columns has rank $k$, so $k \leq n$.

### Converse

The converse is false: a linearly independent family need not be orthogonal.
The vectors $(1, 0)$ and $(1, 1)$ of $\mathbb{R}^2$ are independent, but their dot product is $1$.
The [[Gram-Schmidt process|0VT6P0GNQR]] gives a partial converse: each finite independent family can be replaced by an orthonormal family with the same initial spans.

### Generalizations

- Part 1 holds in every inner product space, also for infinite families and in infinite dimension, with the same proof.
- An orthogonal family of nonzero vectors for a [[nondegenerate symmetric bilinear form|01TXN7ETH2]] can fail to be independent when some vector $v$ has $\beta(v, v) = 0$. For $\beta(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$, the family $((1, 1), (2, 2))$ is orthogonal, since $\beta = 2 - 2 = 0$, and dependent.

## Explanations

### L1 human

Vectors at right angles cannot be built from each other.
In $\mathbb{R}^3$, the three axes point in directions that no combination of the other two can reach.
To find the coefficient of $e_j$ in a combination, take the inner product with $e_j$.
If the combination is zero, then every coefficient is zero.

### L2 human

Worked example: we find coefficients by inner products, without a linear system.

1. In $\mathbb{R}^2$, let $e_1 = (\frac35, \frac45)$ and $e_2 = (-\frac45, \frac35)$. They are orthonormal.
2. Suppose $a_1 e_1 + a_2 e_2 = (1, 7)$. Take the dot product with $e_1$: $a_1 = \frac35 + \frac{28}{5} = \frac{31}{5}$.
3. Take the dot product with $e_2$: $a_2 = -\frac45 + \frac{21}{5} = \frac{17}{5}$.
4. Check: $\frac{31}{5} e_1 + \frac{17}{5} e_2 = (\frac{93 - 68}{25}, \frac{124 + 51}{25}) = (1, 7)$.
5. For $(0, 0)$ in place of $(1, 7)$, the same method gives $a_1 = a_2 = 0$. This is the independence.

The typical use is to prove that a family is a basis without row reduction.
A trap: part 1 needs nonzero vectors, since the zero vector is orthogonal to everything.

### L3 human

The proof uses only the values $\ip{e_i}{e_j} = \delta_{ij}$, so it shows more: the [[Gram matrix|00SPJSDT3Z]] of an orthonormal family is the identity, which is invertible.
The general criterion says that a finite family is independent exactly when its Gram matrix is invertible.
In a [[Hilbert space|HM2HHE3J51]] the statement gives the bound $n$ only in finite dimension.
For infinite orthonormal families, the right notion of size is the Hilbert dimension.
