---
tag: GBXD38Y52R
kind: definition
name: Trigamma function
msc: ["33B15"]
defines: 5VGVPENA0F
uses: [HWRRXB0YXS]
sources:
  - url: https://en.wikipedia.org/wiki/Trigamma_function
---

## Definition

Let $\psi$ be the [[digamma function|HWRRXB0YXS]].
The *trigamma function* is the meromorphic function
$$\psi_1(z) = \psi'(z) = \frac{d^2}{dz^2} \log \Gamma(z), \qquad z \in \C \setminus \set{0, -1, -2, \ldots}.$$

## Remarks

Equivalently, $\psi_1(z) = \sum_{k=0}^\infty \frac{1}{(z+k)^2}$, and $\psi_1$ is the [[polygamma function|3J3QGKPMZQ]] $\psi^{(1)}$.

Example: $\psi_1(1) = \sum_{k \ge 1} k^{-2} = \frac{\pi^2}{6}$.
Also $\psi_1(\frac12) = \sum_{k \ge 0} \frac{4}{(2k+1)^2} = 4 \cdot \frac{\pi^2}{8} = \frac{\pi^2}{2}$.

Non-example of a valid argument: at $z = 0$ the term $k = 0$ is $1/0^2$, so $\psi_1$ has a double pole there, as at every non-positive integer.

The recurrence $\psi_1(z+1) = \psi_1(z) - \frac{1}{z^2}$ and the reflection formula $\psi_1(1-z) + \psi_1(z) = \frac{\pi^2}{\sin^2 \pi z}$ hold for all $z$ that are not integers.
