---
tag: K4CQC2VFF8
kind: definition
name: Lie algebra of a Lie group
msc: ["22E60", 17B05]
defines: WKVBS76432
uses: [7JBRGCVJRB, F45VQ47GPV, 0299VCW1TH, 68FGQEBD6J, 5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_group%E2%80%93Lie_algebra_correspondence
---

## Definition

Let $G$ be a real [[Lie group|7JBRGCVJRB]] with identity element $e$.
For $g \in G$, let $L_g \colon G \to G$ be left translation $h \mapsto gh$, a diffeomorphism of the [[smooth manifold|F45VQ47GPV]] $G$, with differential $dL_g$.
A smooth [[vector field|0299VCW1TH]] $X$ on $G$ is *left-invariant* if $dL_g(X_h) = X_{gh}$ for all $g, h \in G$.
The *Lie algebra of $G$* is the real vector space of left-invariant vector fields on $G$ with the [[bracket of vector fields|68FGQEBD6J]] $[X, Y]$.
It is written $\mathfrak{g}$ or $\operatorname{Lie}(G)$.

## Remarks

The bracket of two left-invariant vector fields is again left-invariant, so $\mathfrak{g}$ is a [[Lie algebra|5JJYBJ6A8K]].
The map $X \mapsto X_e$ is a linear isomorphism from $\mathfrak{g}$ onto the tangent space $T_e G$, with inverse $v \mapsto (g \mapsto dL_g(v))$.
So $\dim \mathfrak{g} = \dim G$, and one often defines $\operatorname{Lie}(G)$ as $T_e G$ with the transported bracket.

Example: for $G = \mathrm{GL}_n(\R)$, an open subset of the space $M_n(\R)$ of real $n \times n$ matrices, one has $T_e G = M_n(\R)$.
The left-invariant field with value $A$ at $e$ is $g \mapsto gA$, and the bracket of the fields $g \mapsto gA$ and $g \mapsto gB$ is the field $g \mapsto g(AB - BA)$.
So $\operatorname{Lie}(\mathrm{GL}_n(\R)) = \mathfrak{gl}_n(\R)$ with the commutator bracket.

Non-example: on the additive group $G = \R$, left translation by $a$ is $x \mapsto x + a$, whose differential is the identity.
The vector field $x \frac{d}{dx}$ is not left-invariant, since its value at $0 + a$ is $a \frac{d}{dx}$ while the translate of its value at $0$ is $0$.
The left-invariant fields on $\R$ are the constant fields $c \frac{d}{dx}$, so $\operatorname{Lie}(\R)$ is the one-dimensional abelian Lie algebra.

Using right-invariant vector fields instead gives the opposite bracket, $-[X, Y]$, and an isomorphic Lie algebra.
