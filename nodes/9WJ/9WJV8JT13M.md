---
tag: 9WJV8JT13M
kind: concept
name: Christofides algorithm
msc: [90C27, 68W25, 05C85]
specializes: [4WEVBDQ8SR]
sources:
  - url: https://en.wikipedia.org/wiki/Christofides_algorithm
same_as:
  wikidata: Q498144
  wikipedia: Christofides algorithm
---

## Summary

The Christofides algorithm is an [[approximation algorithm|4WEVBDQ8SR]] for the metric [[travelling salesman problem|XJRHJX2241]], where the distances satisfy the [[triangle inequality|03HF5PMY5T]].
It joins a [[minimum spanning tree|0JW7KT6PQW]] with a minimum-weight [[perfect matching|0NHK9MFFW9]] on the odd-degree vertices, and then shortcuts an Eulerian circuit.
It runs in polynomial time and returns a tour at most $3/2$ times as long as a shortest tour.
For decades this was the best known guarantee for the metric problem.

## Explanations

### L1 human

A tree that connects all cities as cheaply as possible is never longer than the best tour, since deleting one edge of a tour leaves such a connection.
The tree is not a round trip, because some cities have an odd number of tree roads.
The algorithm pairs these odd cities by extra roads of least total length, which costs at most half a tour.
Now every city has an even number of roads, so one can walk all of them in one loop.
Skipping cities already seen gives a tour, and the triangle inequality says the skips never make it longer.
