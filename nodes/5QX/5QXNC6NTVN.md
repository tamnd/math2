---
tag: 5QXNC6NTVN
kind: concept
name: Cellular automaton
msc: [37B15, 68Q80]
sources:
  - url: https://en.wikipedia.org/wiki/Cellular_automaton
same_as:
  wikidata: Q189156
  wikipedia: Cellular automaton
---

## Summary

A cellular automaton is a grid of cells, each in one of finitely many states.
All cells update at the same time by one local rule.
The new state of a cell depends only on the old states of the cells in a fixed finite neighbourhood.
As a dynamical system it is a continuous map of the configuration space that commutes with the shifts, by the [[Curtis–Hedlund–Lyndon theorem|N35QM9G83G]].
Very simple rules can produce complex behaviour, so cellular automata serve as models in physics and biology and as a model of computation.

## Explanations

### L1 human

Imagine a row of light bulbs, each on or off.
At each tick of a clock, every bulb looks at itself and its two neighbours and decides whether to be on or off by a fixed table.
All bulbs follow the same table and switch at the same moment.
In rule 90, a bulb is on at the next tick exactly when one of its two neighbours, but not both, is on now.
Started from a single lit bulb, this rule draws a Sierpinski triangle over time.
Conway's Game of Life is a famous two-dimensional example.
See the [[definition|2CM2MC5HQ6]].
