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
We show that the $D$-[[invariant subspaces|0ACX5QT8TE]] are exactly the $8$ subspaces $\operatorname{span}\set{e_i : i \in I}$ for $I \subseteq \set{1, 2, 3}$.

1. Each such span is invariant, since $D e_i = i \, e_i$ lies in the span for each $i \in I$.
2. Conversely, let $U$ be invariant. Then $D^k(U) \subseteq U$ for each $k$, by induction on $k$. So $p(D)(U) \subseteq U$ for each [[polynomial|0E3MV6E6MG]] $p$, since $U$ is a subspace.
3. Let $q_1(x) = \frac{(x - 2)(x - 3)}{2}$. Then $q_1(1) = 1$, $q_1(2) = 0$ and $q_1(3) = 0$, so $q_1(D) = \operatorname{diag}(1, 0, 0)$.
4. In the same way, $q_2(x) = -(x - 1)(x - 3)$ gives $q_2(D) = \operatorname{diag}(0, 1, 0)$, and $q_3(x) = \frac{(x - 1)(x - 2)}{2}$ gives $q_3(D) = \operatorname{diag}(0, 0, 1)$.
5. Let $u = c_1 e_1 + c_2 e_2 + c_3 e_3 \in U$. By steps 2 to 4, $c_i e_i = q_i(D) u \in U$ for each $i$.
6. Let $I$ be the set of $i$ such that some $u \in U$ has $c_i \ne 0$. By step 5, $e_i \in U$ for each $i \in I$.
7. Each $u \in U$ is a combination of the $e_i$ with $i \in I$, by the definition of $I$. So $U = \operatorname{span}\set{e_i : i \in I}$.

## Remarks

The example shows that a diagonalizable map with distinct eigenvalues has only finitely many invariant subspaces.
If two diagonal entries are equal, the situation changes.
For $D = \operatorname{diag}(1, 1, 3)$, every line in the plane $\operatorname{span}(e_1, e_2)$ is invariant, so there are infinitely many invariant subspaces.
Step 3 is Lagrange interpolation: it builds a polynomial in $D$ that is the projection onto one eigenspace.

## Explanations

### L1 human

The matrix $\operatorname{diag}(1, 2, 3)$ stretches the three axes by the factors $1$, $2$ and $3$.
A flat or straight part of space that the map does not leave must be built from whole axes.
For example, the plane through the first two axes is kept in place.
A tilted line, like the one through $(1, 1, 0)$, is not kept, since it goes to the line through $(1, 2, 0)$.

### L2 human

Let us check the claim for the plane $U$ spanned by $(1, 1, 0)$ and $(0, 0, 1)$.

1. We have $D(1, 1, 0) = (1, 2, 0)$.
2. If $(1, 2, 0) = a(1, 1, 0) + b(0, 0, 1)$, then $a = 1$ and $a = 2$, which is impossible.
3. So $U$ is not invariant, as the classification says, since $U$ is not a span of standard basis vectors.

The typical use of the method is to prove that an invariant subspace of a diagonalizable map is a sum of pieces of its eigenspaces.
The trap is to forget the hypothesis that the entries are distinct.
