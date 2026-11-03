---
tag: GQ4ZA4ZEQD
kind: definition
name: Schelling's segregation model
msc: [91D25, 91D10]
defines: KCD76ERWF7
uses: [5QXNC6NTVN]
sources:
  - url: https://en.wikipedia.org/wiki/Schelling's_model_of_segregation
---

## Definition

Let $G$ be a finite grid of cells, each cell having a set of neighbouring cells, usually the $8$ surrounding cells.
Fix a tolerance $\tau \in [0, 1]$.
A *state* of *Schelling's segregation model* assigns to each cell one of three values: empty, type $A$ or type $B$.
An agent is *satisfied* if no neighbouring cell is occupied, or if at least the fraction $\tau$ of occupied neighbouring cells hold its type.
The dynamics repeats the following step:

1. choose an unsatisfied agent, if one exists;
2. move it to an empty cell, chosen by a fixed rule such as uniformly at random or the nearest cell where it would be satisfied;
3. stop when every agent is satisfied, or after a fixed number of steps.

## Remarks

Example: take a line of cells with neighbours at distance $1$ and $\tau = 1/2$.
In the pattern $A A B B$ every agent is satisfied, since each has one neighbour of its own type among at most two.
Non-example: the alternating pattern $A B A B$ with $\tau = 1/2$ is not a stopping state, since the inner agents have $0$ of $2$ neighbours of their own type.
Simulations with $\tau$ near $1/3$ already tend to reach states with far more same-type neighbours than $\tau$ requires.
Many variants exist, with different neighbourhoods, moving rules, numbers of types and tolerances per type.
The model resembles a [[cellular automaton|5QXNC6NTVN]], but agents move instead of cells changing state by a fixed local rule.
