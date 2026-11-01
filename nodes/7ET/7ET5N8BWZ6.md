---
tag: 7ET5N8BWZ6
kind: definition
name: Mittag-Leffler star
msc: ["30B40", "30B10"]
defines: C21ECQ1H84
uses: [0VP56B4EMX, 0660QX1VPR, 0M3YQJ81NB, 0JDE56HWQ8]
sources:
  - url: https://en.wikipedia.org/wiki/Mittag-Leffler_star
---

## Definition

Let $a \in \C$, and let $f(z) = \sum_{k \ge 0} c_k (z - a)^k$ be a [[power series|0VP56B4EMX]] with positive [[radius of convergence|0660QX1VPR]].
For $z \in \C$, let $\gamma_z \colon [0, 1] \to \C$ be the segment $\gamma_z(t) = a + t(z - a)$.
The *Mittag-Leffler star* of $f$ with respect to $a$ is the set of all $z \in \C$ with the following property.
$f$ has an [[analytic continuation|0M3YQJ81NB]] along the [[path|0JDE56HWQ8]] $\gamma_z$.

## Remarks

Example: for $f(z) = 1/(1 - z) = \sum_k z^k$ and $a = 0$, the point $z = i$ lies in the star, because the segment from $0$ to $i$ avoids $1$ and $1/(1-z)$ is holomorphic on $\C \setminus \set{1}$.
The star is $\C \setminus [1, \infty)$.
Non-example: $z = 2$ is not in the star, because the segment from $0$ to $2$ passes through the pole $1$, where no continuation exists.
The star is open, it contains the disc of convergence, and with each point $z$ it contains the whole segment from $a$ to $z$.
For an entire function the star is all of $\C$.
