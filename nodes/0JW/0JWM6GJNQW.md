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

Vectors at right angles to each other are independent, so an orthonormal family is independent and is never larger than the dimension.
Let $V$ be an [[inner product space|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.

1. Let $(v_i)_{i \in I}$ be a family of nonzero vectors of $V$ that are pairwise [[orthogonal|0TS7VZJBWD]].
   Then the family is [[linearly independent|0EVHJFTG9Z]].
2. Each [[orthonormal family|09VYHEF2VT]] in $V$ is linearly independent.
3. If $\dim V = n$ is finite, then each orthonormal family in $V$ has at most $n$ members.

## Remarks

### Why each hypothesis is needed

Part 1 needs nonzero vectors.
The zero vector is orthogonal to everything, so the family $(0, e_1)$ in $\mathbb{R}^2$ is pairwise orthogonal, and yet $1 \cdot 0 + 0 \cdot e_1 = 0$ is a relation with a nonzero coefficient.

Part 1 needs every pair to be orthogonal, not just most pairs.
The nonzero vectors $(1, 0)$, $(0, 1)$ and $(1, 1)$ of $\mathbb{R}^2$ are dependent, since the third is the sum of the first two.
The pair $(1, 0)$, $(0, 1)$ passes the test, but the two pairs that contain $(1, 1)$ have dot product $1$.

Part 3 needs finite dimension.
On the space of all real polynomials with $\ip{p}{q} = \int_{-1}^{1} p(x) q(x) \, dx$, the normalized [[Legendre polynomials|QFYGJVA996]] form an orthonormal family with infinitely many members.

The positivity of the inner product is used only to know that $\ip{v_i}{v_i} \neq 0$.
For part 2 that is given, since $\ip{e_i}{e_i} = 1$, so the same proof works for any sesquilinear form $\beta$ with $\beta(e_i, e_j) = \delta_{ij}$.

### What it gives you

In a space of dimension $n$, an orthonormal family of $n$ vectors is a basis by the [[right-size criterion|096V7H13H9]], so it is an [[orthonormal basis|0S9GGTR0EX]].
This saves work: to show that $n$ vectors form a basis, you only check $\ip{e_i}{e_j} = \delta_{ij}$, with no row reduction.
The proof also finds the coefficients.
If $v = \sum_j a_j e_j$ for an orthonormal family, then $a_j = \ip{v}{e_j}$, as in the [[coordinate formula|09DZ8CD1AK]].
For example, with $e_1 = (\tfrac35, \tfrac45)$ and $e_2 = (-\tfrac45, \tfrac35)$ and $v = (1, 7)$,
$$a_1 = \tfrac35 + \tfrac{28}{5} = \tfrac{31}{5}, \qquad a_2 = -\tfrac45 + \tfrac{21}{5} = \tfrac{17}{5}.$$
Check: $\tfrac{31}{5} e_1 + \tfrac{17}{5} e_2 = \left(\tfrac{93 - 68}{25}, \tfrac{124 + 51}{25}\right) = (1, 7)$.
In matrix form, an $n \times k$ matrix with orthonormal columns has rank $k$, so $k \le n$.

### The converse

The converse is false: an independent family need not be orthogonal.
The vectors $(1, 0)$ and $(1, 1)$ of $\mathbb{R}^2$ are independent, but their dot product is $1$.
The [[Gram-Schmidt process|0VT6P0GNQR]] gives a partial converse.
Each finite independent family can be replaced by an orthonormal family with the same initial spans.

### Generalizations

Part 1 holds in every inner product space, for infinite families and in infinite dimension, with the same proof, because independence is a condition on finite subfamilies.
It fails for forms that are not positive definite, as in the setting of [[orthogonality for a bilinear form|01TXN7ETH2]].
For $\beta(x, y) = x_1 y_1 - x_2 y_2$ on $\mathbb{R}^2$, the vectors $(1, 1)$ and $(2, 2)$ are nonzero and $\beta((1, 1), (2, 2)) = 2 - 2 = 0$, yet they are dependent.
The reason is that $\beta((1, 1), (1, 1)) = 0$, so the step that cancels the factor $\beta(v, v)$ breaks down.

## Explanations

### L1 human

Arrows at right angles cannot be built from each other.
In space, the three axes point in directions that no mix of the other two can reach.
To find how much of one axis a mix contains, take the inner product of the mix with that axis.
If the mix is the zero vector, every such amount is zero, so the mix used nothing at all.

### L2 human

Here is the argument on a small case.
Suppose $a_1 e_1 + a_2 e_2 = 0$ for $e_1 = (\tfrac35, \tfrac45)$ and $e_2 = (-\tfrac45, \tfrac35)$.
Take the dot product of both sides with $e_1$:
$$a_1 (e_1 \cdot e_1) + a_2 (e_2 \cdot e_1) = a_1 \cdot 1 + a_2 \cdot 0 = 0,$$
so $a_1 = 0$.
The dot product with $e_2$ gives $a_2 = 0$ in the same way.
So only the trivial combination gives $0$, and the family is independent.
This is the typical use: independence comes from a table of inner products, not from row reduction.
Watch out: the zero vector is orthogonal to everything, so part 1 really needs nonzero vectors.

### L3 human

The proof uses only the values $\ip{e_i}{e_j} = \delta_{ij}$, so it shows that the [[Gram matrix|00SPJSDT3Z]] of an orthonormal family is the identity, which is invertible.
The general criterion says that a finite family is independent exactly when its Gram matrix is invertible.
In a [[Hilbert space|HM2HHE3J51]] the bound $n$ applies only in finite dimension.
For infinite orthonormal families, the right measure of size is the Hilbert dimension, the cardinality of a maximal orthonormal family.
