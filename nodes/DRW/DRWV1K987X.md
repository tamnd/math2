---
tag: DRWV1K987X
kind: concept
name: Weakest precondition
msc: [68Q60, 03B70]
uses: [H1M6RSBJ5H]
sources:
  - url: https://en.wikipedia.org/wiki/Predicate_transformer_semantics
---

## Summary

The weakest precondition $\mathrm{wp}(C, Q)$ of a command $C$ and a postcondition $Q$ is a condition on the starting state.
It is the most general condition that guarantees that $C$ terminates in a state satisfying $Q$.
Edsger W. Dijkstra introduced it in 1975, with his language of guarded commands.
He used it to define the meaning of programs and to derive programs from their specifications.
The map $Q \mapsto \mathrm{wp}(C, Q)$ is a predicate transformer, and it can be computed by structural rules for every construct except loops.
It is the backward-reasoning counterpart of [[Hoare logic|H1M6RSBJ5H]] and the basis of many verification tools.

## Explanations

### L1 human

Suppose you want $x$ to be positive after the command $x := x - 3$.
Then you need $x - 3 > 0$ before, that is, $x > 3$.
This condition, $x > 3$, is the weakest precondition: every starting state that works satisfies it, and every state that satisfies it works.
Working backwards in this way from the goal through each command gives what a program needs at its start.
