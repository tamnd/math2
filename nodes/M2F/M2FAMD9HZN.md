---
tag: M2FAMD9HZN
kind: concept
name: Normalization
msc: [14A15, 13B22, 14B05]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_scheme
---

## Summary

The normalization of an [[integral scheme|17NVR4XBHK]] $X$ is a [[normal scheme|EK261G1XP9]] $\tilde{X}$ with a morphism $\tilde{X} \to X$.
It is built by taking the [[integral closure|G0V86SJBQW]] of each affine coordinate ring in its fraction field.
It is the best normal approximation of $X$: every dominant morphism from a normal integral scheme to $X$ factors through it.
For curves it resolves singularities, which makes it a basic tool in the study of singular curves.

## Explanations

### L1 human

Normalization repairs the mildest singularities of a space by adding the functions that "should" be there.
The cusp $y^2 = x^3$ is traced by $t \mapsto (t^2, t^3)$.
The function $t = y/x$ is missing on the cusp, and adding it gives back the ordinary line with coordinate $t$.
So the normalization of the cusp is the line, mapped onto the cusp by $t \mapsto (t^2, t^3)$.
A curve that crosses itself is pulled apart at the crossing in the same way.
