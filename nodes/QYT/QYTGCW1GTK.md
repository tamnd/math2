---
tag: QYTGCW1GTK
kind: concept
name: Pringsheim convergence
msc: [40B05, 40A05]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_limit
---

## Summary

Pringsheim convergence is the usual notion of convergence for a [[double sequence|B70G8FYPG0]] $(a_{m,n})$.
The double sequence converges to $L$ when $a_{m,n}$ is close to $L$ as soon as both indices $m$ and $n$ are large.
It is the basis for the theory of double series and for comparing double limits with iterated limits.

## Explanations

### L1 human

Think of the terms $a_{m,n}$ written in an infinite table with rows $m$ and columns $n$.
Pringsheim convergence to $L$ means that, outside a large enough corner square of the table, every entry is within any given tolerance of $L$.
For example, $a_{m,n} = \frac{1}{m} + \frac{1}{n}$ tends to $0$ in this sense.
On the other hand, $a_{m,n} = \frac{m}{m+n}$ has no double limit: on the diagonal it is $\frac12$, but far out along a row it is near $0$.
