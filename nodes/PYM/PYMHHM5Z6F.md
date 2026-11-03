---
tag: PYMHHM5Z6F
kind: concept
name: Linear programming relaxation
msc: [90C10, 90C05, 90C11]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_programming_relaxation
same_as:
  wikidata: Q1512771
  wikipedia: Linear programming relaxation
---

## Summary

The linear programming relaxation of an [[integer program|9GX3WH5EQF]] or [[mixed-integer linear program|3PX6EV34QK]] is the [[linear program|VNMXB0J2KA]] obtained by dropping the integrality conditions.
Its optimal value bounds the optimal value of the integer program: from above for a maximization, from below for a minimization.
The relaxation can be solved quickly, and its bound drives [[branch and bound|ZZ7C50WN56]], [[cutting-plane methods|PR7VMJN5BH]] and many approximation algorithms.
When the relaxation has an integral optimal vertex, it solves the integer program outright.
This happens, for example, when the constraint matrix is [[totally unimodular|VSD67A49XC]] and the right-hand side is integral.

## Explanations

### L1 human

Asking for whole-number answers makes a problem hard.
The relaxation simply forgets that rule and lets the variables take fractional values.
Since more answers are now allowed, the best relaxed answer is at least as good as the best whole-number answer, so it gives a bound.
If the relaxed answer happens to be whole numbers already, the hard problem is solved.
