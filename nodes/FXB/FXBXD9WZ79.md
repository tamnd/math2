---
tag: FXBXD9WZ79
kind: definition
name: Character group
msc: [43A40, 20K30]
defines: FPRA2KEHFF
uses: [G5S1M9, 0JYTG5K9Y4, 082GHNPJ53, H1WNVN5V7F, FMW57WNPDB]
sources:
  - url: https://en.wikipedia.org/wiki/Character_group
---

## Definition

Let $G$ be a [[group|G5S1M9]], and let $\C^\times$ be the multiplicative group of nonzero complex numbers.
A *character* of $G$ is a [[group homomorphism|0JYTG5K9Y4]] $\chi \colon G \to \C^\times$.
The *character group* of $G$, written $\widehat{G}$ or $\mathrm{Char}(G)$, is the set of all characters of $G$ with the product $(\chi \psi)(g) = \chi(g)\psi(g)$.

## Remarks

The product of two characters is a character, because $\C^\times$ is [[abelian|082GHNPJ53]].
The identity is the trivial character $g \mapsto 1$, and the inverse of $\chi$ is $g \mapsto \chi(g)^{-1}$.
So $\widehat{G}$ is an abelian group, even when $G$ is not.
Every character is trivial on commutators, so $\widehat{G}$ equals the character group of the abelianization of $G$.

Example: for $G = S_3$, a character factors through $S_3 / A_3 \cong \Z/2\Z$, so the characters are the trivial character and the sign, and $\widehat{S_3} \cong \Z/2\Z$.

Non-example: the trace of the two-dimensional irreducible representation of $S_3$ is a character in the sense of representation theory, but it is not a homomorphism to $\C^\times$.
Its value at the identity is $2$, while a homomorphism sends the identity to $1$.

If $G$ is finite, every value $\chi(g)$ is a root of unity, since $g^n = e$ for $n = \abs{G}$, so $\chi$ takes values in the unit circle.
Then $\widehat{G}$ is the group of [[characters of the abelian group|H1WNVN5V7F]] $G$ when $G$ is abelian.
For a locally compact abelian group one keeps only the continuous characters with values in the unit circle, which gives the [[Pontryagin dual|FMW57WNPDB]].
