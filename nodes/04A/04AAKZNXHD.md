---
tag: 04AAKZNXHD
kind: concept
name: Greedy colouring
msc: [05C15]
sources:
  - url: https://en.wikipedia.org/wiki/Greedy_coloring
    locator: Algorithm
same_as:
  wikidata: Q5601715
  wikipedia: Greedy coloring
---

## Summary

Greedy colouring is a simple method that makes a [[colouring|0874138YP6]] of a finite [[graph|0JD5C82QMB]].
Put the vertices in an order $v_1, v_2, \dots, v_n$, and use the colours $1, 2, 3, \dots$.
For $i = 1, \dots, n$, give $v_i$ the smallest colour that no earlier neighbour of $v_i$ has.

## Remarks

A vertex $v_i$ has at most $\deg(v_i)$ earlier neighbours. Thus greedy colouring uses at most $\Delta(G) + 1$ colours, where $\Delta(G)$ is the [[maximum degree|0KNAN9F27P]].
The number of colours depends on the order. For each graph, some order gives an optimal colouring, but such an order is hard to find in general.
Greedy colouring can be done in linear time.

## Explanations

### L1 human

Go through the vertices one by one, and give each one the first colour that its coloured neighbours do not use.
It is fast and simple, but it does not always use the least number of colours.
