---
tag: 9DNDF7AX59
kind: definition
name: Zeros and poles
msc: [30D30, 30C15]
defines: 1TE3QF8EYC
uses: [0NSD1TPHR0, 0CEGEASY49, 0WPQYW8MTE, 0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Zeros_and_poles
---

## Definition

Let $U \subseteq \C$ be an open set and let $f$ be a [[meromorphic function|0NSD1TPHR0]] on $U$.
So there is a closed discrete set $P \subset U$ such that $f$ is [[holomorphic|0DG0Z72CQD]] on $U \setminus P$ and each point of $P$ is a pole of $f$.

1. A *zero* of $f$ is a point $a \in U \setminus P$ with $f(a) = 0$, as in the definition of a [[zero of a holomorphic function|0CEGEASY49]].
2. A *pole* of $f$ is a point $a \in P$, that is, an isolated singularity with $\abs{f(z)} \to \infty$ as $z \to a$, as in the definition of a [[pole|0WPQYW8MTE]].

## Remarks

Example: $f(z) = \dfrac{z - 1}{z^2 + 1}$ on $\C$ has one zero, at $1$, and two poles, at $i$ and $-i$, where the denominator vanishes and the numerator does not.
Non-example: $e^{1/z}$ is not meromorphic on $\C$, and $0$ is neither a zero nor a pole of it.
The point $0$ is an essential singularity: near $0$, $e^{1/z}$ is neither bounded nor tends to $\infty$.
If $U$ is connected and $f$ is not identically $0$, the zeros of $f$ are isolated and the poles of $f$ are the zeros of $1/f$.
The definition extends to meromorphic functions on the Riemann sphere or on a Riemann surface, using local coordinates.
A nonzero rational function, seen on the Riemann sphere, has as many zeros as poles when both are counted with their [[orders|K2S5TAW2BF]].
