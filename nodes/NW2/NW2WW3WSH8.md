---
tag: NW2WW3WSH8
kind: definition
name: Zero morphism
msc: [18A20, 18A05]
defines: YF9F9EG6M3
uses: [A2DE66937D, 859F0TFVA3, AQET9YHH6F, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_morphism
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
A *system of zero morphisms* on $\mathcal{C}$ is a choice of a [[morphism|859F0TFVA3]] $0_{XY} \colon X \to Y$ for all objects $X$ and $Y$, with the following property.
For all objects $W, Z$ and all morphisms $g \colon W \to X$ and $f \colon Y \to Z$:
$$f \circ 0_{XY} = 0_{XZ} \quad \text{and} \quad 0_{XY} \circ g = 0_{WY}.$$
A category with such a choice is a *category with zero morphisms*, and the morphisms $0_{XY}$ are its *zero morphisms*.

## Remarks

A category has at most one system of zero morphisms: if $0$ and $0'$ are two, then $0_{XY} = 0'_{YY} \circ 0_{XY} = 0'_{XY}$.
If $\mathcal{C}$ has a [[zero object|AQET9YHH6F]] $0$, setting $0_{XY}$ equal to the composite of the unique morphisms $X \to 0$ and $0 \to Y$ gives a system of zero morphisms.

Example: in the category of groups, let $0_{GH}$ send every element of $G$ to the identity $e_H$ of $H$.
For a [[group homomorphism|0JYTG5K9Y4]] $f \colon H \to K$, $f(e_H) = e_K$, so $f \circ 0_{GH} = 0_{GK}$; and $0_{GH} \circ g$ is again constant at $e_H$, so $0_{GH} \circ g = 0_{G'H}$ for $g \colon G' \to G$.

Non-example: the category of sets has no system of zero morphisms.
There is no function at all from a non-empty set $X$ to the empty set, so $0_{X \emptyset}$ cannot be chosen.
