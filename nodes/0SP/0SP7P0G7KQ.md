---
tag: 0SP7P0G7KQ
kind: statement
role: theorem
name: Orthogonal decomposition
msc: [46C05, 15A63]
topics: [8GQVME4SZZ]
audience: ug1
about: [0XJXTBCB2T]
uses: [079D68S3AW, 041JTZCK9Q, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Properties
  - book: isbn:9783031410253
    locator: Section 6C
  - book: isbn:9780321982384
    locator: Section 6.3
---

## Statement

Every vector splits in exactly one way into a part inside a finite-dimensional subspace and a part orthogonal to it.
Let $V$ be an inner product space over $\R$ or $\C$, and let $U$ be a finite-dimensional subspace of $V$.
Let $U^\perp$ be the [[orthogonal complement|079D68S3AW]] of $U$.
Then:

1. $V = U \oplus U^\perp$, a [[direct sum|041JTZCK9Q]]. So each $v \in V$ is $v = u + u'$ for exactly one pair with $u \in U$ and $u' \in U^\perp$.
2. If $e_1, \dots, e_k$ is an orthonormal basis of $U$, then $u = \sum_{i=1}^{k} \ip{v}{e_i} e_i$ and $u' = v - u$.
3. If $V$ is also finite-dimensional, then $\dim U^\perp = \dim V - \dim U$, where $\dim$ is the [[dimension|05G2G0P224]].

The [[proof|T8GV9PYHDQ]] builds $u$ from an orthonormal basis of $U$.
The map $v \mapsto u$ is the [[orthogonal projection|0B8KZRT28M]] onto $U$.

## Remarks

### A first decomposition

Take $V = \R^3$ and let $U$ be the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$.
By [[the plane example|38S0WYCSA3]], $U^\perp$ is the line through $n = (1, -1, 1)$.
To split $v = (1, 2, 3)$, write $v = u + t n$ with $u \in U$ and take the dot product with $n$.
Since $u \cdot n = 0$, this gives $v \cdot n = t \, (n \cdot n)$:
$$1 - 2 + 3 = 3t, \qquad t = \tfrac{2}{3}.$$
So $u' = \tfrac{2}{3}(1, -1, 1) = (\tfrac{2}{3}, -\tfrac{2}{3}, \tfrac{2}{3})$ and $u = v - u' = (\tfrac{1}{3}, \tfrac{8}{3}, \tfrac{7}{3})$.
Check: $u \cdot n = \tfrac{1}{3} - \tfrac{8}{3} + \tfrac{7}{3} = 0$, so $u$ lies in $U$.

### Why each hypothesis is needed

The subspace $U$ must be finite-dimensional, or at least closed.
In the Hilbert space $\ell^2$ of square-summable sequences, the subspace $c_{00}$ of finitely supported sequences has $c_{00}^\perp = \{0\}$.
So $c_{00} + c_{00}^\perp = c_{00}$, which is not all of $\ell^2$, as [[the counterexample in l2|DNZF0R4VMZ]] shows.

The form must be positive.
For $\langle x, y \rangle = x_1 y_1 - x_2 y_2$ on $\R^2$ and $U = \R(1, 1)$, the condition $x_1 - x_2 = 0$ gives $U^\perp = U$, so $U + U^\perp = U \ne \R^2$.

The space $V$ must be finite-dimensional only for part 3, because $\dim V - \dim U$ has no meaning otherwise.

### What it gives you

Part 3, stated on its own, is the [[dimension of the orthogonal complement|0E2NYPVSP9]].
It leads at once to the [[double orthogonal complement|0PXN9G4MX1]], $(U^\perp)^\perp = U$ in finite dimension.
The [[best approximation theorem|0MCDDSCB9Z]] adds that $u$ is the point of $U$ closest to $v$.
For a matrix, every vector of $\R^n$ splits into a row space part and a null space part, by the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]].

### The converse

Suppose that $V = U \oplus W$ and that $W \subseteq U^\perp$.
Then $W = U^\perp$.
To see this, let $x \in U^\perp$ and write $x = u + w$ with $u \in U$ and $w \in W$.
Then $u = x - w$ lies in $U^\perp$ as well as in $U$, so $u = 0$ and $x = w \in W$.
So $U^\perp$ is the only complement of $U$ whose vectors are all orthogonal to $U$.

### Generalizations

In a [[Hilbert space|HM2HHE3J51]], the same decomposition holds for every closed subspace $U$, by the [[Hilbert projection theorem|J5YNTHQMFX]].
In a general inner product space, it holds for every complete subspace, and finite-dimensional subspaces are always complete.
The subspace $c_{00}$ is not closed in $\ell^2$, which is why it fails there.

## Explanations

### L1 human

Every vector splits in exactly one way into a part inside $U$ and a part at a right angle to $U$.
In a room, with $U$ the floor, the first part is the shadow of an arrow on the floor, and the second part is the vertical part.
A line and a plane at a right angle to each other fill space, and the dimensions add up: $1 + 2 = 3$.

### L2 human

The formula of part 2 needs an orthonormal basis, and the typical mistake is to use it with any basis.
For $v = (1, 2, 3)$ and the basis $(1, 1, 0), (0, 1, 1)$ of the plane above, the inner products are $3$ and $5$, and the formula would give
$$3(1, 1, 0) + 5(0, 1, 1) = (3, 8, 5).$$
The vector $(3, 8, 5)$ does lie in $U$, but it is the wrong point of $U$.
The difference $v - (3, 8, 5) = (-2, -6, -2)$ has dot product $-8$ with $(1, 1, 0)$, so it is not orthogonal to $U$.
With the orthonormal basis $e_1 = \tfrac{1}{\sqrt 2}(1, 1, 0)$ and $e_2 = \tfrac{1}{\sqrt 6}(-1, 1, 2)$ the formula works:
$$\ip{v}{e_1} e_1 + \ip{v}{e_2} e_2 = \tfrac{3}{2}(1, 1, 0) + \tfrac{7}{6}(-1, 1, 2) = (\tfrac{1}{3}, \tfrac{8}{3}, \tfrac{7}{3}).$$
For a basis that is not orthonormal, the [[projection formulas|AK3JJ5HHG2]] give the correct matrix form.

### L3 human

The theorem says that the subspaces of a finite-dimensional inner product space have a canonical complement, $U \mapsto U^\perp$.
In functional analysis the closed subspaces of a Hilbert space keep this property, and Fourier series use it to split a function into orthogonal pieces.
The decomposition is the start of the theory of orthogonal projections, the [[adjoint|0R9NMSM1ZP]] and the [[spectral theorem|06J4PXRG22]], where a space splits into orthogonal eigenspaces.
