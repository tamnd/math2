---
tag: B7FPT8JTXR
kind: concept
name: Locally ringed space
msc: [14A15, 18F20]
specializes: [KNDXDE7K8M]
sources:
  - url: https://en.wikipedia.org/wiki/Ringed_space
---

## Summary

A locally ringed space is a [[ringed space|KNDXDE7K8M]] in which the ring of germs of functions at each point is a [[local ring|MZ02BKPHJA]].
The unique maximal ideal of that local ring consists of the germs that "vanish at the point".
Schemes, smooth manifolds and complex manifolds are all locally ringed spaces.
This is the common frame in which scheme theory is built.

## Explanations

### L1 human

Think of a space together with a rule that says which functions are allowed on each open set.
At a single point, one looks at the allowed functions near the point, where two functions count as the same if they agree near the point.
For a smooth manifold and a point $p$, such a germ $g$ is invertible exactly when $g(p) \ne 0$.
So the germs that are not invertible are those with $g(p) = 0$, and they form one ideal; this is what "local ring" means.
A locally ringed space is a space where this holds at every point.
