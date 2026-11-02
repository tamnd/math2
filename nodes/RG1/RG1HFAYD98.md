---
tag: RG1HFAYD98
kind: concept
name: Stieltjes transform
msc: [44A15, "30E20", 44A60]
specializes: [YCK709QB06]
sources:
  - url: https://en.wikipedia.org/wiki/Stieltjes_transformation
same_as:
  wikidata: Q3537578
  wikipedia: Stieltjes transformation
---

## Summary

The Stieltjes transform of a finite measure $\mu$ on the real line is the function $S_\mu(z) = \int \frac{d\mu(t)}{t - z}$ of a complex variable $z$ off the real axis.
It is a [[holomorphic function|0NAHXR1FRH]] that encodes $\mu$ completely, and the measure can be read back from its boundary values on the real axis.
It is central in the [[moment problem|CS7TWHY7JM]], in spectral theory, and in random matrix theory, where limiting eigenvalue distributions are found through their Stieltjes transforms.
For a function $f$ on $(0, \infty)$ the classical form is $\int_0^\infty \frac{f(t)}{x + t}\, dt$, which is the [[Laplace transform|0V49JEZW06]] applied twice.

## Explanations

### L1 human

Think of $\mu$ as a distribution of electric charge along the real line.
The Stieltjes transform at a point $z$ of the plane adds up the contributions $1/(t - z)$ of all charges, a kind of complex potential.
When $z$ comes close to the real line at a point $x$, the imaginary part feels mostly the charge near $x$, so it reveals the density of $\mu$ there.
For one unit charge at $0$, the transform is $-1/z$.
