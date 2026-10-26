---
tag: 0D1VWQGZZ7
kind: definition
name: Conjugate elements
aliases: [conjugacy]
msc: ["20E45"]
defines: 0DXD4QSZ8A
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Definition
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $a, b \in G$.
The element $b$ is conjugate to $a$ when there is $g \in G$ with $b = gag^{-1}$.
The element $gag^{-1}$ is called the conjugate of $a$ by $g$.

## Remarks

Conjugacy is an equivalence relation on $G$; its classes are the conjugacy classes.
In an [[abelian group|082GHNPJ53]], $gag^{-1} = a$, so each element is conjugate only to itself.
Conjugate elements have the same [[order|0WE2NHZJ7B]].
In the group of invertible matrices, conjugate matrices are similar matrices.

## Explanations

### L1 human

Conjugating $a$ by $g$ means: first undo $g$, then do $a$, then do $g$ again (reading the product from right to left).
The result does the same thing as $a$, but in a place that $g$ has moved.
For example, two rotations of a cube by the same angle about different axes are conjugate.
