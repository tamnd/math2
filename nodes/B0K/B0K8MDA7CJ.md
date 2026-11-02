---
tag: B0K8MDA7CJ
kind: concept
name: Cobweb plot
msc: ["37E05", 26A18, 37M99]
sources:
  - url: https://en.wikipedia.org/wiki/Cobweb_plot
same_as:
  wikidata: Q5139042
  wikipedia: Cobweb plot
---

## Summary

A cobweb plot is a picture of an orbit of a map of the real line.
It is drawn on top of the graph of the map and the diagonal $y = x$.
The orbit is traced by a path that goes alternately vertically to the graph and horizontally to the diagonal.
It shows at a glance whether an orbit converges to a [[fixed point|R6QVS6P21N]], cycles around a [[periodic point|T75CZ5H47N]], or wanders.
Cobweb plots are a standard first tool for maps of an interval such as the logistic map.

## Explanations

### L1 human

Draw the graph of the map $f$ and the line $y = x$ in the same picture.
Start at a value $x_0$ on the line, and go up or down to the graph to read off $f(x_0)$.
Then go sideways to the line to make $f(x_0)$ the new starting value.
Repeating these two moves draws a staircase or a spiral.
For $f(x) = \cos x$, the path spirals in to the point where the graph of $\cos$ crosses the diagonal, near $0.739$.
A staircase means the orbit approaches the fixed point from one side, and a spiral means it jumps from side to side.
