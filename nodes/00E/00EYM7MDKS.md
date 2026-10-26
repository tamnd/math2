---
tag: 00EYM7MDKS
kind: concept
name: Hasse diagram
aliases: [order-diagram]
msc: [06A06]
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Hasse_diagram
    locator: lead section
same_as:
  wikidata: Q901446
  wikipedia: Hasse diagram
---

## Summary

A Hasse diagram is a drawing of a finite [[partially ordered set|011C29Q1S1]].
Each element is a point, and there is a line upward from $a$ to $b$ when $b$ covers $a$.
This means that $a < b$ and no $c$ satisfies $a < c < b$.
Then $a \le b$ exactly when one can go from $a$ to $b$ by a path that goes only upward.

## Remarks

The diagram does not draw the loops of reflexivity or the lines that transitivity implies.
The Hasse diagram of the power set of $\{1, 2, 3\}$ under $\subseteq$ is the picture of a cube.

## Explanations

### L1 human

A Hasse diagram is a minimal picture of an order.
For the divisors of $12$ under divisibility, put $1$ at the bottom and $12$ at the top.
Draw a line from $2$ to $4$ and from $2$ to $6$.
Do not draw a line from $2$ to $12$, because the path through $4$ already shows it.
