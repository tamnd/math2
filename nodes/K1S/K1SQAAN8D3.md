---
tag: K1SQAAN8D3
kind: definition
name: Product category
msc: [18A05]
defines: AFNE9C4NH6
uses: [A2DE66937D, 859F0TFVA3, 09CEDJYBKP, 0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Product_category
---

## Definition

Let $\mathcal{C}$ and $\mathcal{D}$ be [[categories|A2DE66937D]].
The *product category* $\mathcal{C} \times \mathcal{D}$ is defined as follows:

1. its objects are the pairs $(A, B)$ with $A$ an object of $\mathcal{C}$ and $B$ an object of $\mathcal{D}$;
2. a [[morphism|859F0TFVA3]] $(A, B) \to (A', B')$ is a pair $(f, g)$ with $f \colon A \to A'$ in $\mathcal{C}$ and $g \colon B \to B'$ in $\mathcal{D}$;
3. composition is $(f', g') \circ (f, g) = (f' \circ f, g' \circ g)$, and the identity of $(A, B)$ is $(1_A, 1_B)$.

## Remarks

The category axioms hold because they hold in each coordinate.
There are projection functors $\mathcal{C} \times \mathcal{D} \to \mathcal{C}$ and $\mathcal{C} \times \mathcal{D} \to \mathcal{D}$.
Example: a [[monoid|0N6R902FG1]] $M$ is a category with one object; the product of the one-object categories of $M$ and $N$ is the one-object category of the product monoid $M \times N$.
Indeed its only object is the pair of the two objects, and its morphisms are the pairs $(m, n)$ multiplied coordinatewise.
The set of objects of $\mathcal{C} \times \mathcal{D}$ is the [[Cartesian product|09CEDJYBKP]] of the sets of objects when both categories are small.
A morphism $(f, g)$ is an isomorphism exactly when $f$ and $g$ are both isomorphisms.
