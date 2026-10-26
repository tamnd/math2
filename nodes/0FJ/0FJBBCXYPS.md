---
tag: 0FJBBCXYPS
kind: statement
role: proposition
name: Chromatic number of a complete bipartite graph
msc: [05C15]
uses: [0V0GC7BQAN, 0C5M7AM6FH]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_bipartite_graph
    locator: lead section
---

## Statement

Let $m, n \ge 1$ be integers.
Then the [[chromatic number|0C5M7AM6FH]] of the [[complete bipartite graph|0V0GC7BQAN]] $K_{m,n}$ is $2$.

## Remarks

Give one colour to each of the two parts. Each edge joins the two parts, so this is a colouring with $2$ colours.
One colour is not enough, because $K_{m,n}$ has an edge.
More generally, a [[bipartite|07DVHJ8N0A]] graph with at least one edge has chromatic number $2$.

## Explanations

### L1 human

Colour one side of $K_{m,n}$ red and the other side blue.
Every edge goes from red to blue, so two colours are enough, and one colour is too few.
