---
tag: 98TJTT6GZN
kind: definition
name: Positive harmonic function
msc: [31B05, 31A05]
defines: EYMQ82Z8XJ
uses: [0DEB0JMN0W, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_harmonic_function
---

## Definition

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be an [[open set|02BH3MCBQB]].
A *positive harmonic function* on $\Omega$ is a [[harmonic function|0DEB0JMN0W]] $u \colon \Omega \to \R$ such that $u(x) > 0$ for every $x \in \Omega$.

## Remarks

Example: on the upper half-plane $\set{(x, y) : y > 0}$, the function $u(x, y) = y$ is positive harmonic, since $\Delta u = 0$ and $y > 0$ there.
Non-example: $u(x, y) = x$ on the same half-plane is harmonic but takes negative values, for instance at $(-1, 1)$.
Some authors call a harmonic function with $u \ge 0$ nonnegative harmonic; on a connected open set, the minimum principle shows that such a function is either identically $0$ or positive everywhere.
On a ball, positive harmonic functions satisfy [[Harnack's inequality|YNH832D50W]].
