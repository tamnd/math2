---
tag: 00K4FK4NBH
kind: definition
name: Nullity
msc: [15A03, 15A04]
defines: 0APCFW7639
uses: [02YFME3RGW, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(linear_algebra)
    locator: Properties
---

## Definition

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *nullity* of $T$ is
$$\operatorname{nullity} T = \dim \ker T,$$
the [[dimension|03GSZ8RTZJ]] of the [[kernel|0S23E6YE83]] of $T$.
The nullity of a matrix $A$ is the nullity of the map $x \mapsto Ax$, the dimension of the [[null space|0PHDYNR24D]] of $A$.

## Remarks

The nullity is $0$ if and only if $T$ is injective.
For an $m \times n$ matrix, the nullity is the number of free variables of $Ax = 0$.
By the [[rank–nullity theorem|0W4FSW1TVB]], $\rank T + \operatorname{nullity} T = \dim V$ when $V$ is finite-dimensional.

## Explanations

### L1 human

The nullity counts the dimensions that the map crushes to zero.
The projection of space onto a plane crushes one direction, so its nullity is $1$.
Rank counts what survives, and nullity counts what is lost.
