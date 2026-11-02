---
tag: 417ZRDCHY6
kind: concept
name: Quotient of a topological group
msc: [22A05]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_group
---

## Summary

The quotient of a [[topological group|92700QAB5Y]] $G$ by a subgroup $H$ is the set $G/H$ of left cosets with the quotient topology.
The projection $G \to G/H$ is continuous and open.
The quotient is Hausdorff exactly when $H$ is closed, and when $H$ is normal the quotient is again a topological group.
Quotients give homogeneous spaces such as spheres, which are quotients of rotation groups.

## Explanations

### L1 human

To form the quotient, glue together all elements of $G$ that differ by an element of $H$.
The result is a new space, where a set is open when the set of all elements that land in it is open in $G$.
For example, gluing the real line by the integers wraps it into a circle: $\R / \Z$ is the circle group.
Each point of the circle stands for a whole family $x + \Z$ of real numbers.
