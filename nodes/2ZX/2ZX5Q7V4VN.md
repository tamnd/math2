---
tag: 2ZX5Q7V4VN
kind: statement
role: theorem
name: Projections correspond to direct sum decompositions
msc: ["15A04"]
topics: [QHKTJ89V6S]
audience: ug1
about: [033DA1WE8Y, 0XYYT5KNTX]
uses: [0RH4E3CAV9, 041JTZCK9Q, 02YFME3RGW, 0JB228DCWB]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.isComplEquivProj
    match: variant
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Properties and classification
  - book: isbn:9783031410253
    locator: Section 3E
---

## Statement

Choosing a projection on a space is the same as choosing an ordered pair of complementary subspaces.
Let $V$ be a vector space over a field $F$.

1. If $P$ is a [[projection|0RH4E3CAV9]] on $V$, then $V = \operatorname{im} P \oplus \ker P$, where $\operatorname{im} P$ is the [[image|0JB228DCWB]] and $\ker P$ is the [[kernel|02YFME3RGW]].
   Also $P v = v$ for every $v \in \operatorname{im} P$, and $I - P$ is a projection with image $\ker P$ and kernel $\operatorname{im} P$.
2. If $V = U \oplus W$ is a [[direct sum|041JTZCK9Q]], then the map $P_{U, W}(u + w) = u$, for $u \in U$ and $w \in W$, is a projection with image $U$ and kernel $W$.
3. The maps $P \mapsto (\operatorname{im} P, \ker P)$ and $(U, W) \mapsto P_{U, W}$ are inverse bijections between the set of projections on $V$ and the set of ordered pairs $(U, W)$ of subspaces with $V = U \oplus W$.

## Remarks

### Why each hypothesis is needed

The equation $P^2 = P$ is what makes part 1 work.
For the map $N(x, y) = (y, 0)$, which has $N^2 = 0 \ne N$, the image and the kernel are both the $x$-axis, so they do not split $\R^2$; see [[the nilpotent map|1MX3PFN4BB]].

The sum in part 2 must be direct.
If $U + W = V$ but $U \cap W \ne \{0\}$, then some vector has two decompositions $u + w$, and "the $U$-part" is not defined.
For the $xy$-plane and the $yz$-plane in $\R^3$, the vector $(0, 1, 0)$ is $(0, 1, 0) + 0$ and also $0 + (0, 1, 0)$.

Linearity is needed as well.
The map $x \mapsto |x|$ on $\R$ satisfies $f \circ f = f$, but its image $[0, \infty)$ is not a subspace, so no direct sum appears.

### What it gives you

The [[existence of complements|0P9T8WHNMH]] now gives, for every subspace $U$, a projection with image $U$.
A projection is diagonalizable with eigenvalues in $\{0, 1\}$, and in a basis adapted to $\operatorname{im} P \oplus \ker P$ its matrix is $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$.
In finite dimension this gives $\operatorname{rank} P + \dim \ker P = \dim V$ at once.

Here is a worked use.
The projection of $\R^3$ onto the plane $U$ given by $x + y + z = 0$ along the $x$-axis is found from the decomposition
$$(x, y, z) = (x + y + z)(1, 0, 0) + (-y - z, y, z),$$
so $P(x, y, z) = (-y - z, y, z)$, and $I - P$ sends $(x, y, z)$ to $(x + y + z, 0, 0)$.
Check: $P(-y - z, y, z) = (-y - z, y, z)$, so $P^2 = P$.

The same idea works for more summands.
Families $P_1, \dots, P_k$ of projections with $P_i P_j = 0$ for $i \ne j$ and $\sum_i P_i = I$ correspond to decompositions $V = U_1 \oplus \cdots \oplus U_k$.

### The converse and what the image misses

Part 3 is already a two-way statement, so it contains its converse.
The image alone does not determine the projection.
The projections with image $U$ correspond to the complements of $U$, one for each complement.
For the $x$-axis in $\R^2$ these are the maps $(x, y) \mapsto (x - m y, 0)$, one for each $m \in \R$.

## History

The correspondence between idempotents and direct sum decompositions is classical in ring theory.
There the splitting of a ring by an idempotent $e$ and its partner $1 - e$ is called the Peirce decomposition, after Benjamin Peirce.

## Explanations

### L1 human

Choosing a projection is the same as choosing two subspaces that split the space.
The projection keeps the part of each vector in the first subspace and throws away the part in the second.
Swapping the roles of the two subspaces gives the partner projection $I - P$.

### L2 human

Take $P(x, y) = (x + y, 0)$ on $\R^2$.

1. We have $P^2(x, y) = P(x + y, 0) = (x + y, 0) = P(x, y)$, so $P$ is a projection.
2. The image of $P$ is the $x$-axis, and its kernel is the line $x + y = 0$, that is, $\R(1, -1)$.
3. The decomposition of $(x, y)$ is $P(x, y) + (I - P)(x, y) = (x + y, 0) + (-y, y)$.
4. The partner $(I - P)(x, y) = (-y, y)$ is a projection with image $\R(1, -1)$ and kernel the $x$-axis.

The trap is to think that $P$ is determined by its image.
The projection $(x, y) \mapsto (x, 0)$ has the same image and the different kernel $\R(0, 1)$.

### L3 human

In the ring $\operatorname{End}(V)$, the theorem identifies the idempotents with the direct sum decompositions of $V$ into two parts.
This works for modules over any ring: a submodule $U$ is a direct summand exactly when it is the image of an idempotent endomorphism.
Mathlib states the bijection between the complements of $U$ and the projections onto $U$ as `Submodule.isComplEquivProj`.
In a Hilbert space, the orthogonal projections are the idempotents that are also self-adjoint, and they correspond to the closed subspaces.
