---
tag: 0E2HSCKZ6C
kind: statement
role: theorem
name: Orbit-stabiliser theorem
aliases: [orbit-stabilizer-theorem]
msc: [20B05]
uses: [00F2JFA41J, 0RGGF8ZS6D, 05FD317V2W, 0AZG100DKH]
sources:
  - url: https://en.wikipedia.org/wiki/Group_action
    locator: Orbit–stabilizer theorem
---

## Statement

Let a [[group|G5S1M9]] $G$ [[act|0WCY42EV9V]] on a set $X$, and let $x \in X$.
Then the map $gG_x \mapsto g \cdot x$ is a well defined bijection from the set of the [[left cosets|03DEH43F4H]] of the [[stabiliser|0AYMP41THN]] $G_x$ to the [[orbit|0YQPZB5Q1G]] $G \cdot x$.
In particular, $|G \cdot x| = [G : G_x]$.

## Remarks

The key equivalence is $g \cdot x = h \cdot x$ if and only if $g^{-1}h \in G_x$, if and only if $gG_x = hG_x$.
The bijection is compatible with the actions: it sends $k \cdot gG_x$ to $k \cdot (g \cdot x)$ for each $k \in G$.
So each transitive action of $G$ is isomorphic to the [[action on the left cosets|0AZG100DKH]] of a stabiliser.

## Explanations

### L1 human

Two group elements move $x$ to the same point exactly when they differ by an element that fixes $x$.
So the points of the orbit correspond to the cosets of the stabiliser.
A big stabiliser means a small orbit, and a small stabiliser means a big orbit.
