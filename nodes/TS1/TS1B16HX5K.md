---
tag: TS1B16HX5K
kind: concept
name: Karnaugh map
msc: [94C11, "06E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Karnaugh_map
same_as:
  wikidata: Q461528
  wikipedia: Karnaugh map
---

## Summary

A Karnaugh map is a table of the values of a [[Boolean function|0X05GS525E]] of a few variables.
Its cells are arranged so that neighbouring cells differ in exactly one input variable.
With this arrangement, the product terms that imply the function appear as rectangular blocks of $1$'s whose sides are powers of $2$.
It is a hand method for finding a short [[disjunctive normal form|0GVDFAY4KW]], useful for up to about four or five variables.
The [[Quine–McCluskey algorithm|W0HDZBF5FC]] does the same job systematically.

## Explanations

### L1 human

A [[truth table|05RSK4Q657]] lists the values of a function in a column; a Karnaugh map folds them into a rectangle.
Rows and columns are labelled so that moving one step, also around the edges, changes just one input.
Then a block of neighbouring $1$'s means that the function does not care about the inputs that change inside the block.
For example, if the map of $f(x, y)$ has $1$'s in the whole row $x = 1$, then that row is the term $x$.
Covering all $1$'s with few large blocks gives a short formula.
