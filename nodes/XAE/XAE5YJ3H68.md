---
tag: XAE5YJ3H68
kind: concept
name: Effective resistance
msc: [31C20, 05C12, 94C05]
sources:
  - url: https://en.wikipedia.org/wiki/Resistance_distance
---

## Summary

The effective resistance between two vertices of an [[electrical network|T7KRE7J3B4]] is the resistance of the whole network seen from those two vertices.
It is the voltage difference needed to push a unit current from one vertex to the other.
It is a metric on the vertices, called the resistance distance, and it can be computed from the pseudoinverse of the [[graph Laplacian|TN6M6DVZRP]].
For random walks it gives escape probabilities, commute times and criteria for recurrence.

## Explanations

### L1 human

Replace the whole network between $a$ and $b$ by a single resistor that behaves the same way from the outside: its resistance is the effective resistance.
Resistors in series add: two unit resistors in a row have effective resistance $2$.
Resistors in parallel combine by adding conductances: two unit resistors side by side have effective resistance $\tfrac12$.
Many paths between $a$ and $b$ make the effective resistance small, and a single long path makes it large.
