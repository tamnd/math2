---
tag: YJK71RKVEB
kind: concept
name: Analytic combinatorics
msc: [05A16, 05A15, 30B10]
specializes: [EX382NQTGP]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_combinatorics
same_as:
  wikidata: Q2985062
  wikipedia: Analytic combinatorics
---

## Summary

Analytic combinatorics finds the asymptotic size of combinatorial counts from their [[generating functions|0PHAC833JF]], see the [[definition|XGZ2YYCNWK]].
It views a generating function as a function of a complex variable.
The singularities closest to the origin decide the exponential growth of the coefficients, and the type of these singularities decides the correction factor.
Together with the [[symbolic method|JP11D90EJC]], it is the subject of the book "Analytic Combinatorics" by Philippe Flajolet and Robert Sedgewick.

## Explanations

### L1 human

A generating function packs a whole sequence of counts into one function.
If one plugs complex numbers into that function, it blows up or misbehaves at some point.
The position of the nearest bad point tells how fast the counts grow.
For example, the Catalan generating function first breaks down at $z = 1/4$, so the Catalan numbers grow roughly like $4^n$.
The shape of the breakdown, here a square root, gives the extra factor $n^{-3/2}$.
