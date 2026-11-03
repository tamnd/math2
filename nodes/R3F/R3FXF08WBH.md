---
tag: R3FXF08WBH
kind: concept
name: Dynamic programming
msc: [90C39, 68W40]
specializes: [9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_programming
same_as:
  wikidata: Q380679
  wikipedia: Dynamic programming
---

## Summary

Dynamic programming is a method for designing algorithms that solves a problem through a family of overlapping subproblems.
The value of each subproblem is given by a recurrence in terms of smaller subproblems, and each value is computed only once and stored.
It applies when optimal solutions are built from optimal solutions of subproblems, and it turns many exponential-time recursions into polynomial-time algorithms.
In optimization and control the recurrence is called the Bellman equation.

## Explanations

### L1 human

The naive recursion $F_n = F_{n-1} + F_{n-2}$ for the [[Fibonacci numbers|0GA9K57A39]] recomputes the same values over and over, and takes exponential time.
Writing the values $F_0, F_1, F_2, \dots$ into a table, each from the two before, takes only $n$ additions.
Dynamic programming is this idea in general: list the subproblems, find how each depends on smaller ones, and fill a table in the right order.
[[Edit distance|W6KG32T7AJ]] and shortest paths are classic examples.
