---
tag: 2B02SYNNJS
kind: concept
name: Cavity method
msc: [82B44, 82B20, 60K35]
sources:
  - url: https://en.wikipedia.org/wiki/Cavity_method
same_as:
  wikidata: Q5055181
  wikipedia: Cavity method
---

## Summary

The cavity method studies a large disordered system by comparing it with the same system after one spin or one edge has been removed.
On a tree, the marginals of the system with a hole, or cavity, satisfy exact local recursions.
On large sparse random graphs and in mean-field [[spin glasses|EHPA4B5S5W]], the method assumes that these recursions hold approximately.
It then solves them.
It gives the same predictions as the [[replica trick|4Y5V47G9NH]], often in a form closer to a proof.
It is also the physics origin of belief propagation.

## Explanations

### L1 human

Take a big network of interacting spins and pull one spin out, leaving a hole.
Each neighbour of the hole now feels only the rest of the network, and its state in that situation is its cavity distribution.
Put the spin back: it feels its neighbours through their cavity distributions.
If the network has no short loops, the neighbours of the hole hardly influence each other, and this gives a simple rule that links the cavity distributions together.
On a chain of three spins, the middle spin sees the two end spins, which are independent once the middle spin is removed.
