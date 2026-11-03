---
tag: 6PX3TEMCZ9
kind: definition
name: Automata theory
msc: [68Q45]
defines: 2ZSYVRGQ05
uses: [YFHEG4GYHW, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/Automata_theory
---

## Definition

*Automata theory* is the branch of theoretical computer science that studies abstract machines, called *automata*.
An automaton is a [[model of computation|YFHEG4GYHW]] that reads an input word symbol by symbol and moves between internal states by fixed transition rules.
Automata theory studies:

1. the [[formal languages|5MFZ4VNY6D]] that automata of a given kind accept, and the relations or functions that they compute;
2. the comparison of different kinds of automata by the classes of languages they accept;
3. the algorithmic problems about automata, such as emptiness, equivalence and minimization.

## Remarks

A typical result of the field is that deterministic and nondeterministic finite automata accept the same languages.
A question outside the field, in this sense, is the speed of a particular computer program on real hardware: it concerns an implementation and not an abstract machine.
The kinds of automata are usually ordered by their memory: finite automata have a fixed finite memory, pushdown automata add a stack, and Turing machines have an unbounded tape.
