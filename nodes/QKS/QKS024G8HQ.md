---
tag: QKS024G8HQ
kind: statement
role: theorem
name: Atiyah–Segal completion theorem
msc: [19L47, 55N91, 55R35]
uses: [4R0ZJ95BKQ, RKTX9MN7Q3, KBN13NPYJQ, 9TFC6ADC1C, WA796ZCNRX, 9E4JE4902G, DE29ZC399Z]
about: [4R0ZJ95BKQ, WA796ZCNRX]
sources:
  - url: https://en.wikipedia.org/wiki/Atiyah–Segal_completion_theorem
same_as:
  wikidata: Q4815879
  wikipedia: Atiyah–Segal completion theorem
---

## Statement

Let $G$ be a [[compact Lie group|9TFC6ADC1C]], let $R(G)$ be its [[representation ring|RKTX9MN7Q3]], and let $I = \ker(\dim \colon R(G) \to \Z)$ be the augmentation ideal.
Let $X$ be a finite $G$-CW complex, and let $EG \to BG$ be the universal principal $G$-bundle, with $BG$ the [[classifying space|WA796ZCNRX]] of $G$.
The K-theory of the infinite complex $EG \times_G X$ is defined as the inverse limit of the K-theory of its finite subcomplexes.
The projection $EG \times X \to X$ induces a ring homomorphism $\alpha \colon K_G^*(X) \to K^*(EG \times_G X)$.
It goes from [[equivariant K-theory|4R0ZJ95BKQ]] to the [[complex K-theory|9E4JE4902G]] of the Borel construction.
The target is complete for the $I$-adic topology.
The theorem states that $\alpha$ induces an isomorphism
$$K_G^*(X)^\wedge_I \xrightarrow{\cong} K^*(EG \times_G X),$$
where $K_G^*(X)^\wedge_I$ is the [[$I$-adic completion|KBN13NPYJQ]] of the $R(G)$-module $K_G^*(X)$.

## Remarks

The special case $X = \text{point}$ gives $K^0(BG) \cong R(G)^\wedge_I$ and $K^1(BG) = 0$.
Atiyah had proved this case earlier for finite groups.
The general proof embeds $G$ in a unitary group, which reduces the theorem to explicit computations for unitary groups and their maximal tori.

Example: for the circle group $G = U(1)$, $R(G) = \Z[t, t^{-1}]$ and $I = (t - 1)$.
With $x = t - 1$, the completion is the power series ring $\Z[\![x]\!]$.
On the other side, $BU(1) = \C P^\infty$ and $K^0(\C P^n) = \Z[x]/(x^{n+1})$ with $x = [H] - 1$, so the inverse limit is also $\Z[\![x]\!]$.

Completion is needed: $R(G)$ itself is much smaller than $K^0(BG)$; for $G = \Z/2$, $R(G) = \Z[s]/(s^2 - 1)$ is countable, while $K^0(B\Z/2) \cong \Z \oplus \Z_2$, with $\Z_2$ the uncountable group of $2$-adic integers.

The [[Segal conjecture|DE29ZC399Z]] is the analogous statement for stable cohomotopy and the Burnside ring.

## Explanations

### L1 human

Equivariant K-theory of a point is the representation ring of the group, which is algebraic data.
The K-theory of the classifying space $BG$ is a topological invariant of the group.
The theorem says that the second is obtained from the first by a completion, which adds certain infinite sums.
So the topology of $BG$, as seen by K-theory, is determined by the representations of $G$.

### L2 human

The theorem is a model for many completion results relating equivariant invariants of $G$-spaces to non-equivariant invariants of Borel constructions.
It is used to compute the K-theory of classifying spaces of finite and compact Lie groups.
It also shows what the Borel construction loses: exactly the information in $K_G^*(X)$ that disappears under $I$-adic completion.
