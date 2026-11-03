---
tag: SKJ1CK9YZT
kind: definition
name: Freudenthal triple system
msc: [17C40, 17A40]
defines: 4BWNHY4937
uses: [04C5ZBG1WT, 000AYPA9AJ, 0443XNARDV, 0DGDS5XY84, 01NHFZF2SK]
sources:
  - url: https://en.wikipedia.org/wiki/Freudenthal_magic_square
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] of characteristic different from $2$ and $3$.
Let $M$ be a finite-dimensional [[vector space|000AYPA9AJ]] over $K$.
A *Freudenthal triple system* on $M$ is a pair of a bilinear form $\ip{\cdot}{\cdot} \colon M \times M \to K$ and a [[trilinear map|0443XNARDV]] $t \colon M^3 \to M$ such that:

1. $\ip{\cdot}{\cdot}$ is [[alternating|0DGDS5XY84]] and [[nondegenerate|01NHFZF2SK]].
2. $t(x, y, z)$ is symmetric in $x, y, z$.
3. The $4$-linear form $q(x, y, z, w) = \ip{x}{t(y, z, w)}$ is symmetric in $x, y, z, w$.
4. $t(t(x, x, x), x, y) = \ip{y}{x} \, t(x, x, x) + \ip{y}{t(x, x, x)} \, x$ for all $x, y \in M$.

## Remarks

Example: let $M = K^2$ with $\ip{(a, b)}{(c, d)} = ad - bc$ and $t = 0$.
The form is alternating and nondegenerate, and clauses 2 to 4 hold because both sides of each identity are $0$.
This is a trivial system; the interesting ones have a nonzero quartic form $q(x, x, x, x)$.

The main example has $M = K \oplus K \oplus J \oplus J$, where $J$ is an [[Albert algebra|1MSMVDRAVD]], so $\dim M = 56$.
Its group of automorphisms, the linear maps that preserve both $\ip{\cdot}{\cdot}$ and $t$, is a group of type $E_7$.

Non-example: take $M = K^2$ with the zero bilinear form and $t = 0$.
Clauses 2 to 4 hold, but clause 1 fails because the zero form is degenerate.

The scalars in clause 4 depend on the normalization of $t$, and different authors use different constants.
Some authors write the product as $xyz$ instead of $t(x, y, z)$.
