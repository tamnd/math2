---
tag: RZNFYDHD1T
kind: statement
role: theorem
name: Johnson's theorem on amenable group algebras
msc: [43A07, 46H20, 43A20]
uses: [AHV05ZBCYW, 6GD25S53ND, 6P9AE21Q7X, CEAT9BESKK, ZYNY2VFECQ]
about: [6P9AE21Q7X, CEAT9BESKK, 6GD25S53ND]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_Banach_algebra
---

## Statement

Let $G$ be a [[locally compact group|AHV05ZBCYW]] with left Haar measure, and let $L^1(G)$ be its [[group algebra|6GD25S53ND]].
Call $G$ [[amenable|CEAT9BESKK]] if there is a left-invariant [[mean|ZYNY2VFECQ]] on $L^\infty(G)$.
Then $L^1(G)$ is an [[amenable Banach algebra|6P9AE21Q7X]] if and only if $G$ is amenable.

## Remarks

The idea of the proof: suppose $G$ is amenable and let $D \colon L^1(G) \to X^*$ be a bounded derivation.
The action of $L^1(G)$ on $X^*$ extends to an action of the point masses $\delta_x$, $x \in G$, and $D$ extends to them as well.
Averaging the bounded family $x \mapsto \delta_{x^{-1}} \cdot D(\delta_x)$ of elements of $X^*$ with the invariant mean gives an element of $X^*$ that implements $D$ as an inner derivation.
Conversely, if $L^1(G)$ is amenable, one applies the definition to a suitable bimodule built from $L^\infty(G)$ and constants; the element that makes the derivation inner yields an invariant mean.

Example: abelian groups and compact groups are amenable, so $\ell^1(\Z)$, $L^1(\R)$ and $L^1(G)$ for compact $G$ are amenable Banach algebras.

Non-example: the free group $F_2$ on two generators is not amenable, so $\ell^1(F_2)$ is not an amenable Banach algebra.

The theorem was proved by B. E. Johnson in 1972, in the work where he introduced amenable Banach algebras; their name comes from this theorem.

## Explanations

### L1 human

Amenability of a group means that one can average bounded functions on the group in a way that does not change under translation.
Amenability of a Banach algebra is a condition about derivations, which is the algebraic shadow of being able to average.
Johnson's theorem says that the two notions match for the group algebra: the group can be averaged exactly when its group algebra is amenable.

### L2 human

The theorem lets one translate questions about amenable groups into Banach algebra cohomology, and it motivated the whole study of amenable Banach algebras.
For the measure algebra the situation is different: $M(G)$ is amenable only when $G$ is discrete and amenable (Dales, Ghahramani and Helemskii).
On the Fourier side, amenability of $G$ corresponds instead to a bounded approximate identity in the Fourier algebra, by [[Leptin's theorem|Q7NFY5N96E]].
For C\*-algebras, amenability is equivalent to nuclearity, and the reduced group C\*-algebra of a discrete group is nuclear exactly when the group is amenable.
