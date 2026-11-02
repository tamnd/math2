---
tag: TZNR514JQN
kind: concept
name: Temperley–Lieb algebra
msc: [16S99, 57K14, 82B20]
specializes: [3CTW1P4HBP]
sources:
  - url: https://en.wikipedia.org/wiki/Temperley–Lieb_algebra
same_as:
  wikidata: Q4060645
  wikipedia: Temperley–Lieb algebra
---

## Summary

The Temperley–Lieb algebra $TL_n(\delta)$ is an algebra with generators $e_1, \dots, e_{n-1}$ and simple relations depending on a parameter $\delta$.
It first appeared in the work of Temperley and Lieb on lattice models of statistical mechanics.
Jones found it again in the study of subfactors, and it underlies the Jones polynomial of knots.
It has a basis of planar diagrams, and its dimension is the [[Catalan number|0YWZJEABB2]] $\frac{1}{n+1}\binom{2n}{n}$.

## Explanations

### L1 human

Draw $n$ dots on a top line and $n$ dots on a bottom line, and join the $2n$ dots in pairs by curves that do not cross inside the strip.
Such a picture is a basis element of the Temperley–Lieb algebra.
Two pictures are multiplied by stacking one on top of the other and joining the middle dots.
Each closed loop that appears is erased and replaced by a factor $\delta$.
For $n = 2$ there are two pictures, two vertical strands or a cap over a cup, and the cap-cup picture $e_1$ satisfies $e_1^2 = \delta e_1$.
