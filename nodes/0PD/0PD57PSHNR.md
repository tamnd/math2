---
tag: 0PD57PSHNR
kind: definition
name: Circuit
msc: [05C38]
defines: 09F2QPVQY7
uses: [062MQGP8M5]
sources:
  - url: https://en.wikipedia.org/wiki/Cycle_(graph_theory)
    locator: Circuit and cycle
---

## Definition

Let $G$ be a [[graph|0JD5C82QMB]].
A circuit in $G$ is a closed [[trail|062MQGP8M5]] of positive length.
That is a walk $(w_0, w_1, \dots, w_k)$ with $k \ge 1$, $w_k = w_0$, and pairwise distinct edges.

## Remarks

A circuit may visit a vertex more than once. A [[cycle|07CT9RDY7Q]] is a circuit with no repeated vertex other than the start.
In a simple graph each circuit has length at least $3$.
Some authors use the word circuit for a cycle. Others use the word tour.

## Explanations

### L1 human

A circuit is a trail that ends where it starts.
It is a round trip that never uses the same edge twice.
