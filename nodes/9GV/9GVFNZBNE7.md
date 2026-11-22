---
tag: 9GVFNZBNE7
kind: example
name: Invariant subspaces of a diagonal matrix with distinct entries
msc: ["15A04"]
topics: [Z6S6PWMJPH]
audience: ug1
instance_of: [0ACX5QT8TE]
uses: [0EP59ESQ94, 0Q9PGXD9E4, 0BNEXSKNRV]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
  - book: isbn:9780135367971
    locator: Section 6.4
---

## Example

Let $D = \operatorname{diag}(1, 2, 3)$ act on $\R^3$, with the standard basis $e_1, e_2, e_3$.
We show that the $D$-[[invariant subspaces|0ACX5QT8TE]] are exactly the $8$ subspaces
$$U_I = \operatorname{span}\{ e_i : i \in I \}, \qquad I \subseteq \{ 1, 2, 3 \}.$$
The plan is to build, for each $i$, a polynomial in $D$ that picks out the $e_i$ part of a vector.

1. Each $U_I$ is invariant, because $D e_i = i\, e_i$ lies in $U_I$ for each $i \in I$, and testing a spanning set is enough.
2. Now let $U$ be any invariant subspace.
   By induction on $k$, $D^k(U) \subseteq U$ for every $k \ge 0$.
   Since $U$ is closed under linear combinations, $p(D)(U) \subseteq U$ for every [[polynomial|0E3MV6E6MG]] $p$.
3. Let $q_1(x) = \tfrac{1}{2}(x - 2)(x - 3)$.
   Then $q_1(1) = \tfrac{1}{2}(-1)(-2) = 1$ and $q_1(2) = q_1(3) = 0$.
   A polynomial acts on a diagonal matrix entry by entry, so $q_1(D) = \operatorname{diag}(1, 0, 0)$.
4. In the same way, $q_2(x) = -(x - 1)(x - 3)$ has $q_2(2) = -(1)(-1) = 1$ and $q_2(1) = q_2(3) = 0$, so $q_2(D) = \operatorname{diag}(0, 1, 0)$.
   Also $q_3(x) = \tfrac{1}{2}(x - 1)(x - 2)$ has $q_3(3) = 1$ and $q_3(1) = q_3(2) = 0$, so $q_3(D) = \operatorname{diag}(0, 0, 1)$.
5. Let $u = c_1 e_1 + c_2 e_2 + c_3 e_3$ be in $U$.
   By steps 2 to 4, $q_i(D) u = c_i e_i$ lies in $U$ for each $i$.
6. Let $I$ be the set of indices $i$ for which some $u \in U$ has $c_i \ne 0$.
   For $i \in I$, step 5 gives $c_i e_i \in U$ with $c_i \ne 0$, so $e_i \in U$, and hence $U_I \subseteq U$.
7. Every $u \in U$ has $c_i = 0$ for $i \notin I$, by the definition of $I$, so $u \in U_I$.
   Hence $U = U_I$.

## Remarks

The example shows that a diagonal matrix with distinct entries has only finitely many invariant subspaces, one for each subset of the axes.
Steps 3 and 4 are Lagrange interpolation: each $q_i$ is $1$ at the eigenvalue $i$ and $0$ at the others, so $q_i(D)$ is the projection onto the $i$-th axis.
The same argument works for every diagonal $n \times n$ matrix with distinct entries over any field, and it gives $2^n$ invariant subspaces.

The distinct entries are essential.
For $D' = \operatorname{diag}(1, 1, 3)$, every line in the plane $\operatorname{span}(e_1, e_2)$ is invariant, because $D'$ is the identity on that plane.
So over $\R$ this matrix has infinitely many invariant subspaces, and no polynomial in $D'$ can separate $e_1$ from $e_2$.

## Explanations

### L1 human

The matrix $\operatorname{diag}(1, 2, 3)$ stretches the three axes by the factors $1$, $2$ and $3$.
A line or a plane through the origin that the map does not leave must be built from whole axes.
For example, the plane through the first two axes is kept in place.
A tilted line, like the one through $(1, 1, 0)$, is not kept, since the map sends $(1, 1, 0)$ to $(1, 2, 0)$, which points in a new direction.

### L2 human

Let us test the classification on the plane $U$ spanned by $(1, 1, 0)$ and $(0, 0, 1)$, which is not a span of axes.
The map sends the first spanning vector to
$$D (1, 1, 0) = (1, 2, 0).$$
If $(1, 2, 0) = a (1, 1, 0) + b (0, 0, 1)$, then the first entry gives $a = 1$ and the second gives $a = 2$, which is impossible.
So $U$ is not invariant, as the classification predicts.
The typical use of the interpolation method is to show that an invariant subspace of a diagonalizable map is the sum of its intersections with the eigenspaces.
Watch out: when two eigenvalues are equal, the interpolating polynomials do not exist, and the list of invariant subspaces becomes much larger.
