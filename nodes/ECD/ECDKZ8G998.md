---
tag: ECDKZ8G998
kind: definition
name: Concrete category
msc: [18A05, 18A22]
defines: FYBRP16KAN
uses: [A2DE66937D, 28NQ0KRHD3, GRG8WEBSH5, G5S1M9, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Concrete_category
---

## Definition

A *concrete category* is a pair $(\mathcal{C}, U)$ where $\mathcal{C}$ is a [[category|A2DE66937D]] and $U \colon \mathcal{C} \to \mathbf{Set}$ is a [[faithful|GRG8WEBSH5]] [[functor|28NQ0KRHD3]] to the category of sets and functions.
The functor $U$ is the *forgetful functor*, and $U(A)$ is the *underlying set* of $A$.
A category $\mathcal{C}$ is *concretizable* if such a faithful functor exists.

## Remarks

Example: the category of [[groups|G5S1M9]] with the functor sending a group to its underlying set is concrete.
Two [[homomorphisms|0JYTG5K9Y4]] $G \to H$ with the same underlying function are equal, so $U$ is faithful.
Non-example: the pair (groups, $P$), where $P$ sends every group to a one-point set, is not a concrete category.
The homomorphisms $x \mapsto 0$ and $x \mapsto x$ of $\Z$ are different but have the same image under $P$, so $P$ is not faithful.
Every small category $\mathcal{C}$ is concretizable.
Send $A$ to the set of all morphisms with codomain $A$, and $f \colon A \to B$ to the map $g \mapsto f \circ g$.
This functor is faithful, since $f$ is the image of $1_A$.
