---
tag: NGT5YCVAMR
kind: concept
name: Coercive functional
msc: [49J45, "58E30"]
sources:
  - url: https://en.wikipedia.org/wiki/Coercive_function
---

## Summary

A functional on a normed space is coercive if its values tend to $+\infty$ as the norm of the argument tends to infinity.
Then every minimising sequence is bounded, which is the compactness step of the [[direct method|TE379HBTY0]].
In reflexive spaces bounded sequences have weakly convergent subsequences, so coercivity and weak lower semicontinuity together give a minimiser.
The word is related to, but different from, a [[coercive bilinear form|86KRHS6X22]].

## Explanations

### L1 human

A coercive function grows without bound in every direction far from the origin.
So its low values all lie in a bounded region, and a search for the minimum cannot escape to infinity.
On the real line, $f(x) = x^2$ is coercive, while $f(x) = e^x$ is not, since it stays small as $x \to -\infty$.
The function $e^x$ indeed has no minimum: its infimum $0$ is approached only far away.
