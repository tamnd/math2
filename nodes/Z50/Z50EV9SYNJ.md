---
tag: Z50EV9SYNJ
kind: definition
name: Primitive ideal
msc: [16D60, 16N20]
defines: M0JDQR0V5S
uses: [0894J980RK, 0DDA6CY7GJ, 09VDS2W1E8, G00C22AEDH, 8F6EHDVJ62]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_ideal
---

## Definition

Let $R$ be a [[ring|0894J980RK]] with identity.
A [[two-sided ideal|0DDA6CY7GJ]] $P$ of $R$ is a *left primitive ideal* if there is a [[simple|G00C22AEDH]] left $R$-[[module|09VDS2W1E8]] $M$ with
$$P = \operatorname{ann}_R(M) = \set{r \in R : rm = 0 \text{ for all } m \in M}.$$

## Remarks

Equivalently, $P$ is left primitive if and only if the quotient ring $R/P$ is a left [[primitive ring|8F6EHDVJ62]].
Example: in $\Z$, for a prime $p$ the ideal $p\Z$ is the annihilator of the simple module $\Z/p\Z$, so it is primitive.
Non-example: the zero ideal of $\Z$ is prime but not primitive, since $\Z/0 \cong \Z$ is not a field.
In a commutative ring the primitive ideals are exactly the maximal ideals.
The [[Jacobson radical|XA0DCNH7WY]] $J(R)$ is the intersection of all left primitive ideals of $R$.
Right primitive ideals are defined with right modules; the two notions can differ.
