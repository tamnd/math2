---
tag: GTDMNAMPD9
kind: concept
name: Tanner graph
msc: [94B05, 94B35]
sources:
  - url: https://en.wikipedia.org/wiki/Tanner_graph
same_as:
  wikidata: Q7683664
  wikipedia: Tanner graph
---

## Summary

The Tanner graph of a [[parity-check matrix|Y4JB44WWFG]] is a [[bipartite graph|0ZVQKTRKVQ]].
It has one node for each code bit and one node for each parity check, with an edge when the bit appears in the check.
It turns a [[linear code|E85KREWV60]] into a graph on which message-passing decoders, such as [[belief propagation|Q6GZN4JWJP]], run.
Properties of the graph, such as its girth and its expansion, govern how well these decoders work.
Tanner introduced these graphs in 1981.

## Explanations

### L1 human

Draw the code bits as circles in one row and the parity checks as squares in another row.
Join a circle to a square when that bit takes part in that check.
A codeword is then a labelling of the circles by $0$ and $1$ such that each square sees an even number of ones.
For the code with the single check $x_1 + x_2 + x_3 = 0$, the graph is a star: one square joined to three circles.
