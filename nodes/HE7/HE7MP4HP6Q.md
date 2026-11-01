---
tag: HE7MP4HP6Q
kind: statement
role: theorem
name: Structure theorem for Artinian rings
msc: ["13E10"]
uses: [ZV04WWYE2Y, 09J6KGT65G, X6JD4AG973, MZ02BKPHJA, 0MNZCN4BQK]
about: [20QEAM8AX2]
sources:
  - url: https://en.wikipedia.org/wiki/Artinian_ring
---

## Statement

Let $R$ be a commutative [[Artinian ring|ZV04WWYE2Y]].
Then $R$ has only finitely many [[maximal ideals|09J6KGT65G]] $\mathfrak{m}_1, \dots, \mathfrak{m}_n$.
Each [[localization|X6JD4AG973]] $R_{\mathfrak{m}_i}$ is an Artinian [[local ring|MZ02BKPHJA]], and the natural map $R \to R_{\mathfrak{m}_1} \times \cdots \times R_{\mathfrak{m}_n}$ is a ring isomorphism.

## Remarks

In an Artinian ring the Jacobson radical $\mathfrak{m}_1 \cap \cdots \cap \mathfrak{m}_n$ is nilpotent, so $\mathfrak{m}_1^k \cdots \mathfrak{m}_n^k = 0$ for some $k$.
The ideals $\mathfrak{m}_i^k$ are pairwise coprime, so the [[Chinese remainder theorem|0W97J8QED7]] gives $R \cong \prod_i R/\mathfrak{m}_i^k$.
One then checks that $R/\mathfrak{m}_i^k \cong R_{\mathfrak{m}_i}$.
For example, $\Z/12\Z \cong \Z/4\Z \times \Z/3\Z$, and these factors are the localizations at the maximal ideals $(2)$ and $(3)$.
The decomposition is unique: in any decomposition of $R$ as a finite [[product of rings|0MNZCN4BQK]] of local rings, the factors are, up to isomorphism and order, the rings $R_{\mathfrak{m}_i}$.

## Explanations

### L1 human

Every commutative Artinian ring splits into finitely many pieces, one for each maximal ideal.
Each piece is local: it has only one maximal ideal.
So to understand Artinian rings, it is enough to understand Artinian local rings.

### L2 human

Together with the [[Akizuki–Hopkins–Levitzki theorem|C7X657TF19]], this reduces many questions about zero-dimensional Noetherian rings to the local case.
Geometrically, the spectrum of an Artinian ring is a finite discrete set of points, and the ring is the product of the "fat points" at each of them.
An Artinian local ring is the kind of ring met as $R/I$ for a Noetherian local ring $R$ and an ideal $I$ primary to the maximal ideal.
