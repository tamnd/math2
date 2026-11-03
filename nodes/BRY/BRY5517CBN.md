---
tag: BRY5517CBN
kind: definition
name: Tempered representation
msc: ["22E46", "43A65", "22D10"]
defines: 2HM21Z7XN9
uses: [AHV05ZBCYW, 74BPYJNZTM, FX3NEFYFFN, PR8C073VWY, J85Q7QGGHS]
sources:
  - url: https://en.wikipedia.org/wiki/Tempered_representation
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] and let $\lambda_G$ be its [[left regular representation|PR8C073VWY]] on $L^2(G)$.
Let $\pi$ be a [[unitary representation|74BPYJNZTM]] of $G$ on $\mathcal{H}$.
Then $\pi$ is *weakly contained* in $\lambda_G$ if the following holds for every $v \in \mathcal{H}$.
The function $g \mapsto \ip{\pi(g) v}{v}$ is a limit, uniformly on compact subsets of $G$, of finite sums of functions $g \mapsto \ip{\lambda_G(g) w}{w}$ with $w \in L^2(G)$.
An [[irreducible|FX3NEFYFFN]] unitary representation of $G$ is *tempered* if it is weakly contained in $\lambda_G$.

## Remarks

The functions $\ip{\pi(g) v}{v}$ are diagonal [[matrix coefficients|J85Q7QGGHS]] of $\pi$.
For a second countable unimodular group of type I, the tempered representations form the support of the [[Plancherel measure|QESEAKKABM]].

For a connected semisimple Lie group $G$ with finite centre and maximal compact subgroup $K$, a theorem of Cowling, Haagerup and Howe gives an equivalent form.
An irreducible unitary representation $\pi$ is tempered if and only if its $K$-finite matrix coefficients lie in $L^{2 + \varepsilon}(G)$ for every $\varepsilon > 0$.
For reductive groups this growth condition is often taken as the definition.

Example: for $G = \R^n$, or any abelian locally compact group, every unitary character is tempered, since $\lambda_G$ weakly contains every character.
Example: a discrete series representation of a semisimple group is tempered, since it is a subrepresentation of $\lambda_G$.

Non-example: for $G = \mathrm{SL}(2, \R)$ the trivial representation is not tempered.
Its matrix coefficient is the constant function $1$, which is not in $L^{2+\varepsilon}(G)$ because $G$ has infinite Haar measure.
