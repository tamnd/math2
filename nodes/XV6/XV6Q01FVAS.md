---
tag: XV6Q01FVAS
kind: concept
name: Coroot
msc: ["17B22", "17B20"]
sources:
  - url: https://en.wikipedia.org/wiki/Root_system
---

## Summary

The coroot of a root $\alpha$ is the vector $\alpha^\vee = 2\alpha/(\alpha, \alpha)$, which rescales $\alpha$ so that the reflection in the hyperplane orthogonal to $\alpha$ reads $x \mapsto x - (x, \alpha^\vee)\alpha$.
The coroots of a root system form again a root system, the dual root system.
In a semisimple Lie algebra, the coroot of $\alpha$ is an element $h_\alpha$ of the Cartan subalgebra.
It lies in the copy of $\mathfrak{sl}_2$ attached to $\alpha$, and $\alpha(h_\alpha) = 2$.

## Explanations

### L1 human

The coroot points in the same direction as the root, but its length is changed so that pairing a root with its own coroot gives $2$.
Long roots get short coroots and short roots get long coroots.
For example, if a root has length $1$, its coroot has length $2$; if a root has length $\sqrt{2}$, its coroot is the root itself.
