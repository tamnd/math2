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

Let $V$ be an inner product space over $\R$ or $\C$, and let $U$ be a finite-dimensional subspace of $V$.
Let $U^\perp$ be the [[orthogonal complement|079D68S3AW]] of $U$.
Then:

1. $V = U \oplus U^\perp$, a [[direct sum|041JTZCK9Q]]. So each $v \in V$ is $v = u + u'$ for exactly one pair with $u \in U$ and $u' \in U^\perp$.
2. If $e_1, \dots, e_k$ is an orthonormal basis of $U$, then $u = \sum_{i=1}^{k} \ip{v}{e_i} e_i$ and $u' = v - u$.
3. If $V$ is also finite-dimensional, then $\dim U^\perp = \dim V - \dim U$, where $\dim$ is the [[dimension|05G2G0P224]].

The [[proof|T8GV9PYHDQ]] builds $u$ from an orthonormal basis of $U$.
The map $v \mapsto u$ is the [[orthogonal projection|0B8KZRT28M]] onto $U$.

## Remarks

### Why each hypothesis is needed

- Finite dimension of $U$: in the Hilbert space $\ell^2$ of square-summable sequences, the subspace $c_{00}$ of finitely supported sequences has $c_{00}^\perp = \set{0}$. So $c_{00} + c_{00}^\perp = c_{00} \ne \ell^2$, as [[the counterexample in l2|DNZF0R4VMZ]] shows.
- Positivity of the inner product: for the form $\langle x, y \rangle = x_1 y_1 - x_2 y_2$ on $\R^2$ and $U = \R(1, 1)$, we get $U^\perp = U$. So $U + U^\perp = U \ne \R^2$.
- Finite dimension of $V$ is needed only for part 3, because $\dim V - \dim U$ has no meaning otherwise.

### Consequences

- The [[dimension of the orthogonal complement|0E2NYPVSP9]] is part 3, stated alone.
- The [[double orthogonal complement|0PXN9G4MX1]] satisfies $(U^\perp)^\perp = U$ in finite dimension.
- The [[best approximation theorem|0MCDDSCB9Z]]: the part $u$ is the point of $U$ closest to $v$.
- Every vector of $\R^n$ splits into a row space part and a null space part, by the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]].

### Converse

If $V = U \oplus W$ and $W \subseteq U^\perp$, then $W = U^\perp$.
Indeed, let $x \in U^\perp$ and write $x = u + w$; then $u = x - w$ lies in $U \cap U^\perp = \set{0}$, so $x = w \in W$.
So $U^\perp$ is the only complement of $U$ that is orthogonal to $U$.

### Generalizations

In a Hilbert space, the same decomposition holds for every closed subspace $U$, by the [[Hilbert projection theorem|J5YNTHQMFX]].
In a general inner product space, it holds for complete subspaces, and finite-dimensional subspaces are complete.
The subspace $c_{00}$ is not closed in $\ell^2$, and this is why it fails there.

## Explanations

### L1 human

Each vector splits in exactly one way into a part inside $U$ and a part at right angles to $U$.
In space, with $U$ the floor, the first part is the shadow of the vector on the floor, and the second part is its vertical part.
A line and a plane at right angles together fill space, and $1 + 2 = 3$.

### L2 human

We split $v = (1, 2, 3)$ in $\R^3$ with $U$ the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$.

1. By [[the plane example|38S0WYCSA3]], $U^\perp = \R(1, -1, 1)$.
2. Write $v = u + t(1, -1, 1)$ with $u \in U$; the dot product with $n = (1, -1, 1)$ gives $v \cdot n = 3t$, since $u \cdot n = 0$.
3. Here $v \cdot n = 1 - 2 + 3 = 2$, so $t = 2/3$ and $u' = (2/3, -2/3, 2/3)$.
4. Then $u = v - u' = (1/3, 8/3, 7/3)$, and $u \cdot n = 1/3 - 8/3 + 7/3 = 0$, so $u \in U$.

The typical use is to split a problem into a part that lies in $U$ and an error part orthogonal to $U$.
The trap is to use a basis of $U$ that is not orthonormal in the formula of part 2.
For the basis $(1, 1, 0), (0, 1, 1)$ the formula gives $3(1, 1, 0) + 5(0, 1, 1) = (3, 8, 5)$, which is wrong; the [[projection formulas|AK3JJ5HHG2]] give the correct matrix form.

### L3 human

The theorem says that the lattice of subspaces of a finite-dimensional inner product space has a canonical complement operation, $U \mapsto U^\perp$.
In functional analysis the closed subspaces of a [[Hilbert space|HM2HHE3J51]] keep this property.
The decomposition is the start of the theory of orthogonal projections, the [[adjoint|0R9NMSM1ZP]] and the [[spectral theorem|06J4PXRG22]], where a space splits into orthogonal eigenspaces.
