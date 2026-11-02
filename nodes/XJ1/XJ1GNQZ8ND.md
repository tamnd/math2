---
tag: XJ1GNQZ8ND
kind: definition
name: Separated morphism
msc: [14A15]
defines: X30G4V7VAJ
uses: [JXRKH6P1Z4, 1DZMT4S9FB, WWRWYSJDET, ABVBHCA9VW]
sources:
  - url: https://en.wikipedia.org/wiki/Diagonal_morphism_(algebraic_geometry)
---

## Definition

Let $f \colon X \to Y$ be a [[morphism of schemes|JXRKH6P1Z4]], and let $X \times_Y X$ be the [[fiber product|1DZMT4S9FB]] of $f$ with itself, with projections $p_1, p_2$.
The *diagonal* of $f$ is the unique morphism $\Delta \colon X \to X \times_Y X$ with $p_1 \circ \Delta = p_2 \circ \Delta = \id_X$.
The morphism $f$ is *separated* if $\Delta$ is a [[closed immersion|WWRWYSJDET]].
A scheme $X$ is *separated* if the unique morphism $X \to \operatorname{Spec} \Z$ is separated.

## Remarks

Example: every morphism $\operatorname{Spec} A \to \operatorname{Spec} B$ is separated.
The diagonal is $\operatorname{Spec}$ of the multiplication map $A \otimes_B A \to A$, $a \otimes a' \mapsto a a'$, which is surjective, so the diagonal is a closed immersion.
Non-example: let $X$ be the affine line over a field $k$ with a doubled origin, the [[gluing|ABVBHCA9VW]] of two copies of $\mathbb{A}^1_k$ along the identity of $\mathbb{A}^1_k \setminus \set{0}$.
Then $X \to \operatorname{Spec} k$ is not separated.
Let $j_1, j_2 \colon \mathbb{A}^1_k \to X$ be the two inclusions, and let $(j_1, j_2) \colon \mathbb{A}^1_k \to X \times_k X$.
The preimage of the diagonal under $(j_1, j_2)$ is $\mathbb{A}^1_k \setminus \set{0}$, the set where $j_1$ and $j_2$ agree.
This set is not closed in $\mathbb{A}^1_k$, so the image of the diagonal is not closed.
A morphism is separated if and only if its diagonal has closed image, since the diagonal is always an immersion.
