---
tag: 2CX7RPPXA9
kind: example
name: Category of groups
msc: [20J15, 18A05]
instance_of: [A2DE66937D]
uses: [G5S1M9, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_groups
same_as:
  wikidata: Q3912012
  wikipedia: Category of groups
---

## Example

The *category of groups* $\mathbf{Grp}$ has the [[groups|G5S1M9]] as objects and the [[group homomorphisms|0JYTG5K9Y4]] $f \colon G \to H$ as morphisms.
Composition is the composition of maps, and the identity morphism of $G$ is the identity map $\id_G$.
This is a [[category|A2DE66937D]].
If $f \colon G \to H$ and $g \colon H \to K$ are homomorphisms, then $g(f(xy)) = g(f(x)f(y)) = g(f(x))\,g(f(y))$, so $g \circ f$ is a homomorphism.
The identity map is a homomorphism, and composition of maps is associative, so both axioms of a category hold.

## Remarks

The trivial group is a [[zero object|AQET9YHH6F]]: from each group there is exactly one homomorphism to it, and from it exactly one homomorphism to each group.
The [[product|S5744QZV4N]] of $G$ and $H$ is the [[direct product|00HF4RJ5QN]] $G \times H$, and the [[coproduct|4FJ0S71P58]] is the [[free product|TM7QS7P7X9]] $G * H$.
The monomorphisms are the injective homomorphisms, and the epimorphisms are the surjective homomorphisms.
Forgetting the group structure gives a functor to the category of sets, whose left adjoint sends a set to the [[free group|020Z5SEN27]] on it.
$\mathbf{Grp}$ is not an [[abelian category|Y9CZ3MTNF1]]: for example, the coproduct $\Z * \Z$ differs from the product $\Z \times \Z$, since the first group is not abelian.

## Explanations

### L1 human

The category of groups collects all groups and all structure-preserving maps between them into one object of study.
Many group constructions become instances of general patterns there: the direct product is a categorical product and the free product is a coproduct.
For example, the map $\Z \to \Z/2\Z$ that sends an integer to its parity is a morphism of this category.
