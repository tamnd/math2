---
tag: T7KRE7J3B4
kind: concept
name: Electrical network
msc: [31C20, 94C05, 05C81]
sources:
  - url: https://en.wikipedia.org/wiki/Electrical_network
---

## Summary

In discrete potential theory, an electrical network is a graph whose edges carry positive conductances, the reciprocals of resistances.
Voltages on the vertices and currents on the edges obey Ohm's law and Kirchhoff's laws.
A voltage with no sources at a vertex is a [[discrete harmonic function|WRY0M7SW59]] there.
Networks turn questions about [[random walks|04VZE3FZXF]], such as recurrence, into questions about [[effective resistance|XAE5YJ3H68]].

## Explanations

### L1 human

Picture a graph made of wires, where each wire has a resistance.
Connect a battery to two vertices; a current flows and every vertex gets a voltage.
At every other vertex the current in equals the current out, and this makes the voltage there a weighted average of the neighbouring voltages.
For two unit resistors in a row between $a$ and $b$, the voltage at the middle vertex is halfway between the voltages at $a$ and $b$.
The same averaging rule governs a random walker on the graph, which is why circuits help to study random walks.
