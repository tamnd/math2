---
tag: JP11D90EJC
kind: concept
name: Symbolic method
msc: [05A15]
sources:
  - url: https://en.wikipedia.org/wiki/Symbolic_method_(combinatorics)
same_as:
  wikidata: Q124054218
  wikipedia: Symbolic method (combinatorics)
---

## Summary

The symbolic method translates a description of a combinatorial class into an equation for its [[generating function|0PHAC833JF]], see the [[definition|39HWNYW5EF]].
Each construction, such as disjoint union, pair or sequence, has a fixed rule that acts on generating functions.
Unlabelled classes lead to ordinary generating functions, and labelled classes lead to [[exponential generating functions|0JHXPVFKT0]].
It is the first part of [[analytic combinatorics|YJK71RKVEB]], whose second part extracts asymptotics from the equations.

## Explanations

### L1 human

A binary tree is either empty, or a root with a left and a right binary tree.
The symbolic method turns this sentence directly into the equation $B(z) = 1 + z B(z)^2$.
Here "or" becomes $+$, "with" becomes a product, and the root becomes a factor $z$.
Solving the equation gives the [[Catalan numbers|0YWZJEABB2]] as the coefficients of $B(z)$.
The point is that one never counts by hand: the grammar of the objects does the work.
