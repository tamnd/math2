---
tag: E560RGEKPP
kind: concept
name: Multi-objective optimization
msc: [90C29, 90B50]
specializes: [RK115S1G5T]
sources:
  - url: https://en.wikipedia.org/wiki/Multi-objective_optimization
same_as:
  wikidata: Q2052203
  wikipedia: Multi-objective optimization
---

## Summary

Multi-objective optimization studies problems with several objective functions to be minimized at the same time, such as cost and risk.
Usually no single point minimizes all objectives, so the solutions are the Pareto optimal points: those that cannot improve one objective without worsening another.
The set of their objective vectors is the [[Pareto front|NJ1QWE4Q3Y]], and a decision maker picks a point on it.
Standard techniques reduce the problem to single-objective ones, for example by weighted sums or by turning all but one objective into constraints.

## Explanations

### L1 human

When you buy a car you may want it both cheap and fast, and these goals conflict.
A car is a sensible choice if no other car is both cheaper and faster.
Multi-objective optimization finds all such sensible choices and leaves the final trade-off to you.
For two objectives $f_1(x) = x$ and $f_2(x) = 1 - x$ on $[0, 1]$, every $x$ is sensible, since lowering one value raises the other.
