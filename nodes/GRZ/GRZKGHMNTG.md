---
tag: GRZKGHMNTG
kind: definition
name: Polygamma function
msc: ["33B15"]
defines: 3J3QGKPMZQ
uses: [HWRRXB0YXS]
sources:
  - url: https://en.wikipedia.org/wiki/Polygamma_function
---

## Definition

Let $\psi$ be the [[digamma function|HWRRXB0YXS]] and let $m \ge 0$ be an integer.
The *polygamma function of order $m$* is the meromorphic function
$$\psi^{(m)}(z) = \frac{d^m}{dz^m} \psi(z) = \frac{d^{m+1}}{dz^{m+1}} \log \Gamma(z), \qquad z \in \C \setminus \set{0, -1, -2, \ldots}.$$

## Remarks

The series $\psi(z) = -\gamma + \sum_{k=0}^\infty \left(\frac{1}{k+1} - \frac{1}{z+k}\right)$, with $\gamma$ the Euler–Mascheroni constant, can be differentiated term by term.
For $m \ge 1$ this gives
$$\psi^{(m)}(z) = (-1)^{m+1}\, m! \sum_{k=0}^\infty \frac{1}{(z+k)^{m+1}} = (-1)^{m+1}\, m!\, \zeta(m+1, z),$$
where $\zeta(s, z)$ is the [[Hurwitz zeta function|G4SW7HJG88]].

Example: for $m = 2$ and $z = 1$ the series gives $\psi^{(2)}(1) = -2 \sum_{k \ge 1} k^{-3} = -2\zeta(3)$.

Non-example of a valid argument: at $z = -n$ with $n \ge 0$ an integer the term $k = n$ of the series is infinite.
There $\psi^{(m)}$ has a pole of order $m + 1$.

The function $\psi^{(0)} = \psi$ is the digamma function and $\psi^{(1)}$ is the [[trigamma function|5VGVPENA0F]].
The recurrence $\psi^{(m)}(z+1) = \psi^{(m)}(z) + (-1)^m\, m!\, z^{-m-1}$ follows by differentiating $\psi(z+1) = \psi(z) + 1/z$ $m$ times.
