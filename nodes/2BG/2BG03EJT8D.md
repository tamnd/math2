---
tag: 2BG03EJT8D
kind: concept
name: Universal coalgebra
msc: [08C05, 18C10, 68Q55]
sources:
  - url: https://en.wikipedia.org/wiki/F-coalgebra
---

## Summary

Universal coalgebra is the general study of coalgebras for an endofunctor of the category of sets.
Such a coalgebra is a set of states $X$ with a map $X \to F(X)$.
The map tells what can be observed of a state and which states come next.
It is the dual of [[universal algebra|W82R6N0GM9]]: algebras build elements from smaller ones, coalgebras unfold states into their behaviour.
Streams, automata, labelled transition systems and many other state-based systems are coalgebras, and the theory treats their behaviour and their bisimulations in one framework.
The general notion over any category is the [[F-coalgebra|6BS0300CMV]].

## Explanations

### L1 human

Think of a machine with hidden states that you can only watch from outside.
At each state it shows you something and then moves to a next state.
A coalgebra records exactly this: for each state, what you see and where you go.
For example, a stream of numbers is a coalgebra for $F(X) = \N \times X$: each state gives a head $n \in \N$ and a next state.
Two states are treated as equal when no experiment can tell them apart.
