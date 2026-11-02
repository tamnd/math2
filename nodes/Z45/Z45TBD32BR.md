---
tag: Z45TBD32BR
kind: definition
name: Exact category in the sense of Barr
msc: ["18E08"]
defines: G9ZNDNT3YY
uses: [2SM3JRJXA4, E70DQGM8X5, Y2NP1JFR86, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_category
---

## Definition

Let $\mathcal{C}$ be a finitely complete category and $X$ an object of $\mathcal{C}$.
An *internal equivalence relation* on $X$ is a pair $r_1, r_2 \colon R \to X$ with this property.
For every object $T$, the set $\set{(r_1 \circ t, r_2 \circ t) : t \colon T \to R}$ is an [[equivalence relation|0G8VEZ3WTK]] on the set $\mathcal{C}(T, X)$, and $t$ is determined by this pair.
The relation is *effective* if it is the [[kernel pair|E70DQGM8X5]] of some morphism $f \colon X \to Y$.
The category $\mathcal{C}$ is *exact in the sense of Barr* if both conditions hold.

1. $\mathcal{C}$ is a [[regular category|2SM3JRJXA4]].
2. Every internal equivalence relation in $\mathcal{C}$ is effective.

## Remarks

The second part of the first clause says that $(r_1, r_2) \colon R \to X \times X$ is a [[monomorphism|Y2NP1JFR86]].
The kernel pair of any morphism is always an internal equivalence relation, so clause 2 asks for the converse.

Example: the category of sets is Barr-exact.
An equivalence relation $R \subseteq X \times X$ is the kernel pair of the quotient map $X \to X / R$.

Non-example: the category of torsion-free abelian groups.
In $\Z$, the subgroup $R = \set{(a, b) : a \equiv b \pmod 2}$ of $\Z \times \Z$ is torsion-free and is an internal equivalence relation.
Let $f \colon \Z \to Y$ be a homomorphism into a torsion-free group with $f(2) = 0$.
Then $2 f(1) = 0$, so $f(1) = 0$ and the kernel pair of $f$ is all of $\Z \times \Z$.
So $R$ is not effective and clause 2 fails.
