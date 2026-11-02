---
tag: SG5C5TVGRB
kind: concept
name: Quasi-arithmetic mean
msc: ["26E60", 39B22]
sources:
  - url: https://en.wikipedia.org/wiki/Quasi-arithmetic_mean
same_as:
  wikidata: Q583095
  wikipedia: Quasi-arithmetic mean
---

## Summary

A quasi-arithmetic mean is the arithmetic mean taken after a change of scale.
Given a continuous strictly monotone function $\varphi$, the mean of $x_1, \dots, x_n$ is $\varphi^{-1}\big(\frac{1}{n} \sum_i \varphi(x_i)\big)$.
The arithmetic, geometric, harmonic and power means are all of this form.
These means are characterized by a few natural axioms, which is the [[Kolmogorov–Nagumo theorem|9Q5DPYQ5NP]].

## Explanations

### L1 human

To average numbers in a quasi-arithmetic way, first move them to a new scale, take the ordinary average there, and move the result back.
With the logarithm as the scale, the average of $2$ and $8$ is computed as the average of $\ln 2$ and $\ln 8$, which is $\ln 4$, so the mean is $4$.
This is the geometric mean.
With the scale $\varphi(x) = 1/x$, the same recipe gives the harmonic mean, used for averaging speeds over equal distances.
