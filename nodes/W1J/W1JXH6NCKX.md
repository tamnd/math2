---
tag: W1JXH6NCKX
kind: concept
name: Doubling measure
msc: [28A12, 30L99]
specializes: [DYR1QFNGNJ]
sources:
  - url: https://en.wikipedia.org/wiki/Doubling_space
---

## Summary

A doubling measure on a metric space is a Borel measure with the following property, for a fixed constant $C$.
Doubling the radius of any ball multiplies its measure by at most $C$.
Lebesgue measure on $\R^n$ is the model example, with constant $2^n$.
Many tools of real analysis on $\R^n$ extend to metric spaces with a doubling measure.
Examples are the Vitali covering lemma, maximal function bounds and the Lebesgue differentiation theorem.
A metric space that carries a doubling measure is a doubling metric space.

## Explanations

### L1 human

Take any ball and look at the ball with the same centre and twice the radius.
For a doubling measure, the big ball never has more than $C$ times the mass of the small ball, with the same $C$ for all balls.
So mass is spread out without sudden thin spots next to heavy ones.
On the line with ordinary length, doubling an interval doubles its length, so $C = 2$ works.
