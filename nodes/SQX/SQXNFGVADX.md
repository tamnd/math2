---
tag: SQXNFGVADX
kind: concept
name: Boolean circuit
msc: [68Q06, 94C11]
specializes: [YFHEG4GYHW]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_circuit
same_as:
  wikidata: Q837479
  wikipedia: Boolean circuit
---

## Summary

A Boolean circuit is a network of logic gates, AND, OR and NOT, wired without loops, that computes a [[Boolean function|0X05GS525E]] of its input bits.
Its size is the number of gates and its depth is the length of the longest path from an input to an output.
Unlike a Turing machine, a circuit has a fixed number of inputs.
So a problem is solved by a family of circuits, one for each input length.
Every problem in P has circuits of polynomial size, so lower bounds on circuit size are one route to lower bounds in complexity theory.

## Explanations

### L1 human

Picture wires carrying the values $0$ or $1$ into small boxes.
An AND box outputs $1$ when both of its input wires carry $1$, an OR box when at least one does, and a NOT box flips its input.
Boxes feed into other boxes, but never back into themselves, and the last box gives the answer.
For example, the exclusive or of $x$ and $y$ is $(x \wedge \neg y) \vee (\neg x \wedge y)$, built from five boxes.
Every function of finitely many bits can be built this way, but some need very many boxes.
