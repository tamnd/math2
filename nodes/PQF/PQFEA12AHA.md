---
tag: PQFEA12AHA
kind: concept
name: Natural boundary
msc: [30B40, 30B30]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_continuation
---

## Summary

A holomorphic function on a domain has the boundary as natural boundary if it cannot be continued across any boundary point.
See the [[definition|WER1M071EK]].
It is the extreme case of the obstruction to [[analytic continuation|0M3YQJ81NB]].
The typical example is a [[power series|0D6KXBHKC0]] with large gaps, whose circle of convergence is a natural boundary by the [[Hadamard gap theorem|DA8M8VZZHC]].

## Explanations

### L1 human

Many holomorphic functions given on a disc can be extended past the circle, except at a few bad points.
For $1/(1 - z)$, only the point $1$ is bad.
For some functions, every point of the circle is bad, so the disc is the end of the world for the function.
Then the circle is called a natural boundary.
An example is $z + z^2 + z^4 + z^8 + \cdots$, which blows up near each root of unity whose order is a power of $2$, and these points are dense on the circle.
