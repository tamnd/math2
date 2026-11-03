---
tag: 9GX3WH5EQF
kind: concept
name: Integer programming
msc: [90C10]
specializes: [3PX6EV34QK]
sources:
  - url: https://en.wikipedia.org/wiki/Integer_programming
same_as:
  wikidata: Q6042592
  wikipedia: Integer programming
---

## Summary

Integer programming is the optimization of a linear function over the integer points that satisfy finitely many linear inequalities.
It differs from [[linear programming|VNMXB0J2KA]] only by the requirement that the variables be integers, but this makes it much harder: the problem is [[NP-hard|JH780796ZP]].
It models yes-or-no decisions, indivisible quantities and logical conditions, so it covers scheduling, routing, location and many puzzles.
Main solution methods are [[branch and bound|ZZ7C50WN56]], [[cutting planes|PR7VMJN5BH]] and their combination [[branch and cut|AJ786D5KK7]], all built on the [[linear programming relaxation|PYMHHM5Z6F]].

## Explanations

### L1 human

Linear programming may tell a company to build $2.6$ factories, which makes no sense.
Integer programming adds the rule that the answer must be in whole numbers.
That rule turns a smooth problem into a search through a huge number of separate grid points.
Rounding the linear programming answer often does not work: the rounded point may break a constraint or be far from the best one.
Still, good methods solve many large practical integer programs.
