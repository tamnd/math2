---
tag: FZNC7ETZA8
kind: definition
name: Character of an abelian group
msc: [43A40]
defines: H1WNVN5V7F
uses: [082GHNPJ53, 04EAFVFTF7, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Character_group
---

## Definition

Let $G$ be an [[abelian group|082GHNPJ53]], and let $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ be the [[circle group|04EAFVFTF7]].
A *character* of $G$ is a [[group homomorphism|0JYTG5K9Y4]] $\chi \colon G \to \mathbb{T}$, that is, a map with $\chi(x + y) = \chi(x)\chi(y)$ for all $x, y \in G$.
If $G$ is a topological group, a character of $G$ is usually required to be continuous as well.

## Remarks

Example: for $G = \Z/n\Z$ and an integer $j$, the map $\chi_j(k) = e^{2\pi i jk/n}$ is well defined, because $e^{2\pi i j(k + n)/n} = e^{2\pi i jk/n}$.
It is a character, since $\chi_j(k + l) = e^{2\pi i j(k+l)/n} = \chi_j(k)\chi_j(l)$.
Non-example: the map $\Z \to \C$, $k \mapsto 2^k$, satisfies the homomorphism rule, but its values do not have absolute value $1$, so it is not a character.
The characters of $G$ form an abelian group under pointwise multiplication $(\chi\psi)(x) = \chi(x)\psi(x)$, with identity the trivial character $x \mapsto 1$ and inverse $\overline{\chi}$.
This group is the character group, often written $\widehat{G}$.
For a finite group every homomorphism to $\C^\times$ takes values in $\mathbb{T}$, so some texts define characters as homomorphisms to $\C^\times$.
