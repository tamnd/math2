---
tag: DBZE1J20HK
kind: concept
name: Basis pursuit
msc: [94A12, 90C25, 90C05]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_pursuit
same_as:
  wikidata: Q4867576
  wikipedia: Basis pursuit
---

## Summary

Basis pursuit is the optimization problem of finding, among all solutions of an underdetermined linear system $Ax = b$, one with the smallest $\ell^1$ norm.
The $\ell^1$ norm favours solutions with few nonzero entries, so basis pursuit is a tractable stand-in for the search for the sparsest solution.
It can be solved as a [[linear program|VNMXB0J2KA]].
It is a central tool of [[compressed sensing|6V8E0AQNHA]], where it recovers sparse vectors exactly under conditions on $A$.
See the [[definition|M4W36502NS]].

## Explanations

### L1 human

When there are fewer equations than unknowns, a linear system has infinitely many solutions.
Often the solution we want is sparse: most of its entries are zero.
Finding the sparsest solution directly is hard, but minimizing the sum of absolute values is easy and often gives the same answer.
Picture the set of solutions as a flat plane and the $\ell^1$ ball as a diamond with sharp corners on the axes.
As the diamond grows, it usually first touches the plane at a corner, which is a sparse point.
The [[lasso|KZ226116HW]] is a close relative that allows the equations to hold only approximately.
