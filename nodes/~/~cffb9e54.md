---
tag: ~cffb9e54
kind: definition
name: Stabiliser
aliases: [stabilizer, isotropy-group]
msc: [20B05]
defines: ~847dc0b4
uses: [~1ff21cb1, ~74c6b403]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Fixed points and stabilizer subgroups
---

## Definition

Let a [[group|G5S1M9]] $G$ [[act|~0ceb002c]] on a set $X$, and let $x \in X$.
The stabiliser of $x$ is the set $G_x = \{g \in G : g \cdot x = x\}$.

## Remarks

The stabiliser $G_x$ is a [[subgroup|~b600248b]] of $G$, but in general it is not normal.
For the action of $S_n$ on $\{1, \dots, n\}$, the stabiliser of $n$ is a subgroup isomorphic to $S_{n-1}$.
For the action of $G$ on itself by conjugation, the stabiliser of $a$ is the [[centraliser|~524f86a3]] $C_G(a)$.

## Explanations

### L1 human

The stabiliser of a point collects the group elements that keep this point in place.
They may move other points.
For the rotations of a square about its centre, only the identity keeps a corner in place.
