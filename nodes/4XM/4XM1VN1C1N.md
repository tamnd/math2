---
tag: 4XM1VN1C1N
kind: concept
name: Weak operator topology
msc: [47L05, 46L10, 46A03]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_operator_topology
same_as:
  wikidata: Q3277121
  wikipedia: Weak operator topology
---

## Summary

The weak operator topology is a topology on the bounded operators on a Hilbert space.
In it, a net of operators converges when all its matrix coefficients $\langle T x, y \rangle$ converge.
It is much coarser than the norm topology, so more sets are compact and more nets converge.
It is the topology used to define [[von Neumann algebras|PSFWQVZ0FS]], and its closed unit ball is compact.

## Explanations

### L1 human

An operator on a Hilbert space can be tested by feeding it a vector $x$ and reading off one component $\langle Tx, y \rangle$ of the output.
In the weak operator topology, operators are close when these numbers are close for finitely many chosen $x$ and $y$.
This is a very forgiving notion of closeness.
For example, the right shift $S$ on sequences moves each entry one step to the right, so the powers $S^n$ push every vector away to infinity.
Every fixed component of $S^n x$ then tends to $0$, so $S^n \to 0$ in this topology, although each $S^n$ preserves lengths.
