---
tag: 3BZFSC5QZ2
kind: concept
name: Priority method
msc: [03D25, 03D28]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_degree
---

## Summary

The priority method is a technique to build [[computably enumerable sets|TN9G24VABN]] with prescribed properties.
The desired property is split into infinitely many requirements, ordered by priority, and the set is built in stages.
When requirements conflict, the one of higher priority wins, and a requirement that loses is injured and starts again.
It was introduced to solve [[Post's problem|1RVF7DWG8C]] and is the main tool for constructions in the theory of [[Turing degrees|P5N2ND3VCG]].

## Explanations

### L1 human

Imagine a list of infinitely many people who each want something from a shared building project.
Their wishes may conflict, so each has a rank: the first person always gets their way, the second gets their way unless the first objects, and so on.
A person whose work is undone just starts over.
If each person is disturbed only finitely often, in the end everyone is satisfied.
In the [[Friedberg–Muchnik theorem|RA358M9QCN]], the wishes say "set $A$ is not computed from $B$ by the $e$-th program" and the same with $A$ and $B$ swapped.
