---
tag: GZBSV8DYGS
kind: concept
name: Almost periodic function
msc: [43A60, 42A75]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_periodic_function
same_as:
  wikidata: Q1066983
  wikipedia: Almost periodic function
---

## Summary

An almost periodic function is a function that nearly repeats itself.
For any tolerance there are many shifts that change it by less than the tolerance.
On the real line, the uniformly almost periodic functions are exactly the uniform limits of finite sums $\sum c_k e^{i\lambda_k x}$ with arbitrary real frequencies $\lambda_k$.
They extend the theory of Fourier series from [[periodic functions|0ATF6Q0633]] to functions such as $\cos x + \cos(\sqrt{2} x)$.
The notion was created by Harald Bohr, and it extends to abelian groups, where it is linked to the [[Bohr compactification|G852FHZ3W1]].

## Explanations

### L1 human

The function $\cos x + \cos(\sqrt{2} x)$ is not periodic, because the two periods $2\pi$ and $\sqrt{2} \cdot 2\pi$ have an irrational ratio.
Still, one can find shifts $\tau$ for which both $\tau / 2\pi$ and $\sqrt{2}\tau / 2\pi$ are very close to whole numbers.
Shifting by such a $\tau$ changes the function by very little everywhere.
Functions with plenty of such near-periods are called almost periodic.
There are several precise versions: uniform ones due to Bohr, and mean-square ones due to Stepanov, Weyl and Besicovitch.
