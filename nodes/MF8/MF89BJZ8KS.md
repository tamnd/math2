---
tag: MF89BJZ8KS
kind: definition
name: Projective algebra
msc: [08B30, 18G05]
defines: PZ41AE18X4
uses: [KBXSZC6BV1, GTS4DRRMZR, 68PFSGP39B, BFFA03GE3V]
sources:
  - url: https://en.wikipedia.org/wiki/Projective_object
---

## Definition

Fix a signature and let $\mathcal{K}$ be a class of algebras of this signature.
An algebra $A \in \mathcal{K}$ is *projective* in $\mathcal{K}$ if the following holds.
For all $B, C \in \mathcal{K}$, every surjective [[homomorphism|KBXSZC6BV1]] $g \colon B \to C$ and every homomorphism $f \colon A \to C$, there is a homomorphism $h \colon A \to B$ with $g \circ h = f$.

## Remarks

In a variety, epimorphisms of the category of algebras need not be surjective.
So this notion can differ from a projective object of the category; universal algebra uses the surjective version.
In a variety, an algebra is projective exactly when it is a [[retract|68PFSGP39B]] of a [[free algebra|GTS4DRRMZR]].

Example: every free algebra $F$ on a set $X$ in a variety is projective.
Given $g \colon B \to C$ surjective and $f \colon F \to C$, choose $b_x \in B$ with $g(b_x) = f(x)$ for each $x \in X$.
The homomorphism $h \colon F \to B$ with $h(x) = b_x$ satisfies $g \circ h = f$, since both sides agree on the generators $X$.
In the variety of modules over a ring, the projective algebras are the [[projective modules|BFFA03GE3V]].

Non-example: $\Z/2\Z$ is not projective in the variety of abelian groups.
Take $g \colon \Z \to \Z/2\Z$ the reduction map and $f = \id$.
Every homomorphism $h \colon \Z/2\Z \to \Z$ is zero, because $\Z$ has no element of order $2$, so $g \circ h = 0 \ne f$.
