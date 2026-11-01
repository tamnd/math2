---
tag: WER1M071EK
kind: definition
name: Natural boundary
msc: [30B40, 30B30]
defines: PQFEA12AHA
uses: [0DG0Z72CQD, 0JJ9J1XZ8G, 0M3YQJ81NB, 097KNJFJ7V]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_continuation
---

## Definition

Let $U \subseteq \C$ be a [[domain|097KNJFJ7V]] and let $f$ be [[holomorphic|0DG0Z72CQD]] on $U$.
A point $\zeta$ of the [[boundary|0JJ9J1XZ8G]] $\partial U$ is a *regular point* of $f$ if the following holds.
There are an open disc $B$ centered at $\zeta$ and a holomorphic function $g$ on $B$ such that $g = f$ on some connected component of $B \cap U$.
That component must have $\zeta$ in its closure.
The boundary $\partial U$ is a *natural boundary* of $f$ if no point of $\partial U$ is a regular point of $f$.

## Remarks

The most common case is a power series with radius of convergence $R$, with $U$ its open disc of convergence.
On the circle of convergence there is always at least one point that is not regular.
Example: $f(z) = \sum_{n \ge 0} z^{2^n}$ on the unit disc has the unit circle as natural boundary.
If $\zeta^{2^k} = 1$, then $f(r\zeta) = \sum_{n < k} (r\zeta)^{2^n} + \sum_{n \ge k} r^{2^n} \to \infty$ as $r \to 1^-$.
Such $\zeta$ are dense in the circle, while $f$ would be bounded near a regular point.
Non-example: $\frac{1}{1 - z} = \sum_{n \ge 0} z^n$ does not have the unit circle as natural boundary.
Each point $\zeta \neq 1$ with $\abs{\zeta} = 1$ is regular, since $\frac{1}{1 - z}$ is holomorphic on a disc around $\zeta$.
