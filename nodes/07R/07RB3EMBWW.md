---
tag: 07RB3EMBWW
kind: statement
role: theorem
name: Third isomorphism theorem for vector spaces
msc: ["15A03", "16D10"]
topics: [QHKTJ89V6S]
audience: ug1
about: [0BR3FY5Q8M]
uses: [0SVR29SV1V, 0EPTJA5QV4, 0XSJ25Z9M4]
formal:
  - system: lean4
    library: mathlib
    decl: Submodule.quotientQuotientEquivQuotient
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem C (modules)
  - url: https://web.williams.edu/Mathematics/it3/texts/quotients.pdf
---

## Statement

Dividing in two stages, first by a smaller subspace and then by the image of a larger one, gives the same space as dividing by the larger subspace at once.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $W \subseteq U$ be [[subspaces|0EPTJA5QV4]] of $V$.
Then $U / W = \{u + W : u \in U\}$ is a subspace of $V / W$, and the map
$$(V / W) / (U / W) \to V / U, \qquad (v + W) + U / W \mapsto v + U,$$
is well defined, and it is a linear [[isomorphism|0XSJ25Z9M4]] of [[quotient spaces|0SVR29SV1V]].

## Remarks

### A first case

In $V = \R^3$, let $W$ be the $z$-axis and let $U$ be the plane $x = y$, which is $\{(t, t, z)\}$ and so contains the $z$-axis.
The map $(x, y, z) + W \mapsto (x, y)$ identifies $V / W$ with $\R^2$, since two vectors differ by a vector of the $z$-axis exactly when they have the same $x$ and $y$.
Under this identification, $U / W$ becomes the line $\{(t, t)\}$ of $\R^2$.
The form $(x, y) \mapsto x - y$ maps $\R^2$ onto $\R$ with exactly this line as kernel, so the first stage followed by the second stage is measured by $x - y$.
Dividing by $U$ at once is measured by the same number, since $(x, y, z) \mapsto x - y$ maps $\R^3$ onto $\R$ with kernel $U$.
So both sides are copies of $\R$, with the label $x - y$, and the map of the theorem matches equal labels.
The example of [[the chain z-axis, yz-plane, R³|BBQGT4RJKX]] carries out the same check for another plane.

### Why each hypothesis is needed

The inclusion $W \subseteq U$ makes the map well defined.
Without it, take the $x$-axis $W$ and the $y$-axis $U$ in $\R^2$.
The cosets $0 + W$ and $(1, 0) + W$ are equal, but $0 + U \ne (1, 0) + U$, because $(1, 0)$ is not on the $y$-axis.
So the value $v + U$ would depend on the choice of $v$ in its coset of $W$.

The inclusion also makes $U / W$ a quotient of $U$.
Without it, the set $\{u + W : u \in U\}$ is still a subspace of $V / W$, but it is not $U$ divided by $W$.
It equals $(U + W) / W$, and the [[second isomorphism theorem|0APN65D6Y6]] identifies it with $U / (U \cap W)$.

### The correspondence of subspaces

The subspaces of $V / W$ are exactly the spaces $U / W$ with $W \subseteq U \subseteq V$, each one exactly once, by the [[correspondence theorem|GCHY414Y11]].
The third isomorphism theorem adds that the quotients also match: dividing $V / W$ by the subspace that corresponds to $U$ gives $V / U$.
In the first case, the lines through $0$ of $\R^2 = V / W$ correspond to the planes of $\R^3$ that contain the $z$-axis, and the quotient of $\R^2$ by such a line is the quotient of $\R^3$ by its plane.

### What it gives you

In finite dimension both sides have dimension $\dim V - \dim U$, by the [[dimension of a quotient space|0SXDQ6TN00]].
Indeed $\dim (V / W) - \dim (U / W) = (\dim V - \dim W) - (\dim U - \dim W)$, and the two copies of $\dim W$ cancel.
More generally, the [[codimension|JJCGJ1EGCQ]] of $U / W$ in $V / W$ equals the codimension of $U$ in $V$, even in infinite dimension.
In practice, a quotient by a large subspace $U$ can be taken in stages, through any smaller subspace $W$ of $U$.

### The converse

Let $W \subseteq U$ and let $Y$ be a subspace of $V / W$ such that $(v + W) + Y \mapsto v + U$ is a well-defined isomorphism.
Well defined forces every element of $Y$ to go to $0 + U$, so $Y \subseteq U / W$.
Injective forces every element of $U / W$, which goes to $0 + U$, to lie in $Y$.
So $Y = U / W$, and the theorem determines the subspace that we divide by.

### Watch out

Do not apply the theorem when $W \not\subseteq U$.
In that case the image of $U$ in $V / W$ is $(U + W) / W$, and the correct formula has $U + W$ in place of $U$:
$$(V / W) / \big((U + W) / W\big) \cong V / (U + W).$$
For the $x$-axis $W$ and the $y$-axis $U$ in $\R^2$, we have $U + W = \R^2$.
So the double quotient is the zero space, and not the line $V / U$ that a careless use of the theorem would predict.

## History

Emmy Noether stated the isomorphism theorems for modules in general form in a paper of 1927, and the vector space case is a special case.
The analogous theorem for groups uses normal subgroups in place of subspaces.

## Explanations

### L1 human

The theorem works like cancelling in fractions: $\frac{a / c}{b / c} = \frac{a}{b}$.
Think of $V / W$ as space seen with the $z$-axis squashed to a point, which leaves a flat plane.
If you then also squash the image of a plane that contains the $z$-axis, a line in that flat plane, you are left with a line.
Squashing the plane directly in space gives the same line.

### L2 human

Here is a typical use, in the space $V = P_3(\R)$ of polynomials of degree at most $3$.
Let $U$ be the polynomials with $p(0) = 0$, and let $W$ be the polynomials with $p(0) = p'(0) = 0$, the multiples of $x^2$ in $V$, so $W \subseteq U$.

The map $p \mapsto (p(0), p'(0))$ is linear from $V$ onto $\R^2$, since $a + bx$ goes to $(a, b)$, and its kernel is $W$.
So $V / W \cong \R^2$, and under this isomorphism $U / W$ becomes the line of pairs $(0, b)$.
Dividing $\R^2$ by this line leaves the first entry, so
$$(V / W) / (U / W) \cong \R, \qquad p \mapsto p(0).$$
The map $p \mapsto p(0)$ also identifies $V / U$ with $\R$, so the theorem checks out.
Check the dimensions: $(4 - 2) - (3 - 2) = 1 = 4 - 3$.
The lesson is that a quotient by a large subspace can be reached through a quotient by a smaller one.

### L3 human

The [[proof|743PKABTM8]] applies the [[first isomorphism theorem|0MTBGVZ4XJ]] to the surjective map $V / W \to V / U$, $v + W \mapsto v + U$, whose kernel is $U / W$.
In an [[abelian category|Y9CZ3MTNF1]] the theorem says that cokernels compose: the cokernel of $U / W \to V / W$ is the cokernel of $U \to V$.
The same statement holds for groups with normal subgroups, for rings with ideals and for modules.
Mathlib states it as `Submodule.quotientQuotientEquivQuotient`.
