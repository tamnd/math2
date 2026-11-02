---
tag: MM0MATN1P8
kind: definition
name: Cohn localization
msc: [16S85, 16S10]
defines: G449HX8H25
uses: [0B1261B5ED, 0VTH8KPCG2, 0VD9ZSWWJG, 0310REJJY8, 4C1AE84N5N, SG7AQ9T8HD, 2P3Y2FRCSZ]
sources:
  - url: https://en.wikipedia.org/wiki/Localization_(commutative_algebra)
    locator: Non-commutative case
---

## Definition

Let $R$ be a [[ring|0B1261B5ED]] with identity and let $\Sigma$ be a set of square [[matrices|0VD9ZSWWJG]] over $R$, of possibly different sizes.
A [[ring homomorphism|0VTH8KPCG2]] $f \colon R \to S$ is *$\Sigma$-inverting* if for every $A \in \Sigma$ the matrix $f(A)$, obtained by applying $f$ to each entry, is invertible over $S$.
The *Cohn localization* (or *universal localization*) of $R$ at $\Sigma$ is a ring $R_\Sigma$ with a $\Sigma$-inverting homomorphism $\lambda \colon R \to R_\Sigma$ with this property.
Every $\Sigma$-inverting homomorphism $f \colon R \to S$ factors as $f = g \circ \lambda$ for exactly one ring homomorphism $g \colon R_\Sigma \to S$.

## Remarks

$R_\Sigma$ exists for every $R$ and $\Sigma$, and it is unique up to a unique isomorphism over $R$.
It can be built by adjoining, for each $n \times n$ matrix $A \in \Sigma$, $n^2$ new generators forming a matrix $\bar A$, with the relations $A \bar A = \bar A A = I_n$.
The map $\lambda$ need not be injective, and $R_\Sigma$ may be the zero ring.
Example: let $R$ be [[commutative|0310REJJY8]] and let $\Sigma$ be the set of $1 \times 1$ matrices $(s)$ with $s$ in a multiplicative set $S$.
A homomorphism is $\Sigma$-inverting exactly when it sends each $s \in S$ to a unit, so $R_\Sigma$ is the [[localization|4C1AE84N5N]] $S^{-1}R$.
More generally, for a right denominator set $S$, that is, a multiplicative set satisfying the right Ore condition and right reversibility, $R_\Sigma$ is the [[Ore localization|SG7AQ9T8HD]] $R S^{-1}$.
Non-example: the identity map $\Z \to \Z$ is not $\Sigma$-inverting for $\Sigma = \set{(2)}$, since $2$ is not a unit in $\Z$; the localization in this case is $\Z[1/2]$.
For the [[free algebra|2P3Y2FRCSZ]] $k\langle X \rangle$ over a field $k$ and $\Sigma$ the set of full matrices, $R_\Sigma$ is a division ring, the free field.
