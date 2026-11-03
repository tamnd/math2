---
tag: 9NW7KCBSME
kind: concept
name: Nodal analysis
msc: [94C05, 05C50]
sources:
  - url: https://en.wikipedia.org/wiki/Nodal_analysis
same_as:
  wikidata: Q1203451
  wikipedia: Nodal analysis
---

## Summary

Nodal analysis is a systematic method to compute the voltages and currents of a linear circuit.
Its unknowns are the potentials of the nodes, measured from a chosen reference node.
It writes the current law of [[Kirchhoff's circuit laws|9B0V41V2F8]] at every other node.
For a network of resistors and current sources this gives a square linear system whose matrix is a reduced [[Laplacian matrix|TN6M6DVZRP]] of the circuit graph.
It is the basis of most circuit simulation programs, usually in the extended form of [[modified nodal analysis|QD3R6CZQ3J]].

## Explanations

### L1 human

Pick one node of the circuit and call its voltage zero, like sea level on a map.
Give every other node an unknown voltage.
At each of these nodes, the currents flowing out through the resistors must add up to the current pushed in by the sources.
This gives one equation per node, and solving them gives all the voltages at once.
For a single node joined to ground by resistors $R_1$ and $R_2$ and fed by a current $J$, the equation is $V/R_1 + V/R_2 = J$.
