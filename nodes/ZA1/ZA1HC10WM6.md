---
tag: ZA1HC10WM6
kind: concept
name: Transform pair
msc: [44A05]
sources:
  - url: https://en.wikipedia.org/wiki/Integral_transform
---

## Summary

A transform pair is a function $f$ together with its image $F = Tf$ under an [[integral transform|YCK709QB06]] $T$.
It is often written $f \leftrightarrow F$ or $f(t) \leftrightarrow F(s)$.
Tables of transform pairs are the main working tool of the [[Laplace transform|0V49JEZW06]] and the [[Fourier transform|DPVM34ADZV]].
They let one go back from $F$ to $f$ without computing an [[inverse transform|GC96MQC0PP]].

## Explanations

### L1 human

A transform pair is one line of a dictionary between two languages.
On the left is a function of time, on the right is its transform.
For the Laplace transform, $e^{at} \leftrightarrow 1/(s - a)$ is such a line.
When a calculation ends with $1/(s - a)$, one looks up the line and reads off $e^{at}$.
This only works because the transform is one-to-one on the functions in the table.
