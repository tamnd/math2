---
tag: WP0YB7VC59
kind: example
name: Category of sets
msc: [18B05]
instance_of: [A2DE66937D]
uses: [0BSJ7RQ9BW, 0EPAT51DXQ, 09NWETVTNY, 01RVCMSN5N]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_sets
same_as:
  wikidata: Q2518298
  wikipedia: Category of sets
---

## Example

The *category of sets*, written $\mathbf{Set}$, has these parts.
Its objects are all [[sets|0BSJ7RQ9BW]].
A morphism from $A$ to $B$ is a [[function|0EPAT51DXQ]] $f \colon A \to B$.
Composition is the composition of functions, $(g \circ f)(a) = g(f(a))$, and the identity of $A$ is the identity function $\id_A$.

This is a [[category|A2DE66937D]].
Composition of functions is associative, since both $(h \circ g) \circ f$ and $h \circ (g \circ f)$ send $a$ to $h(g(f(a)))$.
The identity laws hold, since $f \circ \id_A$ and $\id_B \circ f$ both send $a$ to $f(a)$.
The collection of all sets is not a set, so $\mathbf{Set}$ is a large category.
Each hom-set $\mathbf{Set}(A, B)$ is a set, so $\mathbf{Set}$ is locally small.

## Remarks

The empty set is an initial object and every one-point set is a terminal object.
The monomorphisms are the [[injective functions|09NWETVTNY]] and the epimorphisms are the [[surjective functions|01RVCMSN5N]].
Products are cartesian products and coproducts are disjoint unions; in fact $\mathbf{Set}$ has all small limits and colimits.
It is cartesian closed, with the set of functions $B^A$ as exponential object, and it is an elementary topos whose subobject classifier is a two-element set.

## Explanations

### L1 human

The category of sets is the most basic category: its objects are sets and its arrows are functions.
Most other familiar categories, such as groups or topological spaces, are sets with extra structure and functions that respect it.
Many notions of category theory are modelled on what happens in sets, such as products, unions, images and quotients.
