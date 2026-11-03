---
tag: X8JZFMSYT1
kind: concept
name: Column generation
msc: [90C06, 90C05]
sources:
  - url: https://en.wikipedia.org/wiki/Column_generation
same_as:
  wikidata: Q3123181
  wikipedia: Column generation
---

## Summary

Column generation is a method for [[linear programs|VNMXB0J2KA]] with far too many variables to write down.
It solves the program on a small set of variables.
Then it uses the dual solution to search for one more variable that can improve the objective.
The search is a separate optimization problem, the pricing problem, which often has a combinatorial structure such as a [[knapsack problem|6G8WNXTJAN]].
It is used for the [[cutting stock problem|1HX9ZFG783]], crew scheduling and vehicle routing, and inside [[branch and price|2A9PYZ3F4H]].

## Explanations

### L1 human

A paper mill cuts wide rolls into narrower pieces, and there are millions of possible cutting patterns.
Writing one variable per pattern gives a linear program far too big to store.
Column generation starts with a handful of patterns and solves the small program.
The prices that the small program puts on each piece then tell which new pattern would pay off, and only that pattern is added.
When no pattern pays off any more, the small program already gives the best answer for all patterns.
