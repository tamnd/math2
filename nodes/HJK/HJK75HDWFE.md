---
tag: HJK75HDWFE
kind: concept
name: Diagram
msc: [18A10, 18A30]
specializes: [28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Diagram_(category_theory)
same_as:
  wikidata: Q843237
  wikipedia: Diagram (category theory)
---

## Summary

A diagram of shape $J$ in a [[category|A2DE66937D]] $\mathcal{C}$ is a [[functor|28NQ0KRHD3]] from an index category $J$ to $\mathcal{C}$.
It picks out a family of objects and morphisms of $\mathcal{C}$, arranged in the pattern given by $J$, with the compositions that $J$ prescribes.
Diagrams are the input of limits and colimits: products, equalizers, pullbacks and their duals are limits and colimits of diagrams of particular shapes.

## Explanations

### L1 human

A diagram is a picture of objects and arrows drawn inside a category, following a fixed template.
The template $J$ says how many objects there are and which arrows join them, and the functor says which actual objects and arrows fill the template.
For example, the template with two objects and two parallel arrows $\bullet \rightrightarrows \bullet$ picks out a pair of maps $f, g \colon X \to Y$.
The template with two objects and no arrows between them picks out just a pair of objects.
