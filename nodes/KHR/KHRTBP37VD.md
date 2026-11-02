---
tag: KHRTBP37VD
kind: concept
name: Laplace–Stieltjes transform
msc: [44A10, 26A42, "60E10"]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace%E2%80%93Stieltjes_transform
same_as:
  wikidata: Q3997728
  wikipedia: Laplace–Stieltjes transform
---

## Summary

The Laplace–Stieltjes transform of a function $g$ on $[0, \infty)$ is $\int_0^\infty e^{-s t} \, dg(t)$, a [[Riemann–Stieltjes integral|JT9AFHG0NA]] against $g$ instead of an ordinary integral of $g$.
It extends the [[Laplace transform|0V49JEZW06]]: when $g$ has a density $f$, it is the Laplace transform of $f$.
It also handles jumps of $g$, that is, point masses.
In probability, applied to the distribution function of a nonnegative random variable $X$, it gives $\mathbb{E}[e^{-s X}]$.

## Explanations

### L1 human

Think of $g$ as describing how mass is laid out along the half-line: $g(t)$ is the total mass in $[0, t]$.
The transform weights each bit of mass at position $t$ by $e^{-s t}$ and adds up.
A single point mass at $a$ gives just $e^{-a s}$.
A uniform spread of mass with density $1$ gives $1/s$, the ordinary Laplace transform of the constant $1$.
