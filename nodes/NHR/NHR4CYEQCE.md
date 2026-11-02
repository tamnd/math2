---
tag: NHR4CYEQCE
kind: example
name: Variety of lattices
msc: [06B20, 08B99]
instance_of: [AJNZJD8442]
uses: [WH4SFAACAS, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Lattice_(order)
---

## Example

Take the signature with two binary operations $\vee$ and $\wedge$.
The *variety of lattices* is the class of algebras $(L, \vee, \wedge)$ with the [[identities|PKD440G2XW]]
$$x \vee y = y \vee x, \qquad (x \vee y) \vee z = x \vee (y \vee z), \qquad x \vee (x \wedge y) = x,$$
together with the same three identities with $\vee$ and $\wedge$ exchanged.
These algebras are exactly the [[lattices|WH4SFAACAS]].
The order is recovered by $x \le y$ if and only if $x \vee y = y$.
In this order, $x \vee y$ and $x \wedge y$ are the join and the meet.
The class is a [[variety|AJNZJD8442]], since it is defined by identities.

## Remarks

The idempotent laws $x \vee x = x$ and $x \wedge x = x$ follow from the absorption laws: $x \vee x = x \vee (x \wedge (x \vee x)) = x$.
The [[distributive lattices|0HM0HQCK6N]] and the [[modular lattices|QX7WZ92QAK]] form subvarieties, each defined by one more identity.
The class of complete lattices is not a variety in this signature.
For example, the rational numbers in $[0, 1]$ form a sublattice of the complete lattice $[0, 1]$, but this sublattice is not complete.

## Explanations

### L1 human

A lattice is usually defined as an ordered set in which any two elements have a least upper bound and a greatest lower bound.
The same structures can be described by a short list of equations for the two operations join and meet.
So lattices form a variety, and the tools of universal algebra apply to them.
