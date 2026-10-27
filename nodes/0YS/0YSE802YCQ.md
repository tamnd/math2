---
tag: 0YSE802YCQ
kind: definition
name: Group action
aliases: [g-set, left-group-action]
msc: [20B05]
defines: 0WCY42EV9V
uses: [G5S1M9, 0RJMNEN3BJ, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Left group action
inventory: [ZWHBCNSQPK]
---

## Definition

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $X$ be a set.
A (left) action of $G$ on $X$ is a map $G \times X \to X$, $(g, x) \mapsto g \cdot x$, with these two properties:

1. $e \cdot x = x$ for each $x \in X$.
2. $g \cdot (h \cdot x) = (gh) \cdot x$ for all $g, h \in G$ and $x \in X$.

## Remarks

For each $g \in G$, the map $x \mapsto g \cdot x$ is a bijection of $X$, with inverse $x \mapsto g^{-1} \cdot x$.
The map that sends $g$ to this bijection is a [[group homomorphism|0JYTG5K9Y4]] from $G$ to the [[symmetric group|0515A6D2Y1]] $\operatorname{Sym}(X)$.
Conversely, each homomorphism $G \to \operatorname{Sym}(X)$ gives an action of $G$ on $X$.
A right action is a map $X \times G \to X$ with $x \cdot e = x$ and $(x \cdot g) \cdot h = x \cdot (gh)$.

## Explanations

### L1 human

A group action lets the elements of a group move the points of a set.
The identity does not move any point, and moving by $h$ and then by $g$ is the same as moving by $gh$.
For example, the rotations of a square move the four corners of the square.
