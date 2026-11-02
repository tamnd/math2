---
tag: M848AHBRCM
kind: concept
name: Amalgamated free product
msc: [08B25, "20E06"]
sources:
  - url: https://en.wikipedia.org/wiki/Free_product
---

## Summary

An amalgamated free product glues several algebras of a [[variety|AJNZJD8442]] along a common algebra that maps into each of them.
It is the most general algebra of the variety that receives maps from all the pieces.
In it, the images of the common part are identified.
In category terms it is the colimit of the diagram formed by the maps out of the common algebra.
For two pieces it is the pushout.
For groups, amalgamated free products are central in combinatorial group theory and in the Seifert–van Kampen theorem.

## Explanations

### L1 human

Start with two algebras $B$ and $C$ that both receive a map from a third algebra $A$.
To get the amalgamated free product, form the [[free product|HHNWHS1XTN]] of $B$ and $C$.
Then force the two images of each element of $A$ to be equal.
For example, glue the cyclic groups $\Z/4\Z$ and $\Z/6\Z$ along their subgroups of order $2$.
The result is a group that contains both, in which the two elements of order $2$ coincide; it is isomorphic to $SL_2(\Z)$.
