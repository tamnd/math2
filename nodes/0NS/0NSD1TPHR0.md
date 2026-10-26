---
tag: 0NSD1TPHR0
kind: definition
name: Meromorphic function
msc: [30D30]
defines: 0ZZ7ZYDR8W
uses: [0DG0Z72CQD, 0WPQYW8MTE]
sources:
  - url: https://en.wikipedia.org/wiki/Meromorphic_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Meromorphic_function
    locator: Properties
---

## Definition

Let $U \subseteq \mathbb{C}$ be an open set.
A function $f$ is meromorphic on $U$ if there is a set $P \subseteq U$ with these properties.

1. $P$ has no accumulation point in $U$.
2. $f$ is [[holomorphic|0DG0Z72CQD]] on $U \setminus P$.
3. Each point of $P$ is a [[pole|0WPQYW8MTE]] of $f$.

## Remarks

Rational functions $p/q$, with polynomials $p$ and $q \neq 0$, are meromorphic on $\mathbb{C}$. So are $\tan z$, $\frac{1}{\sin z}$ and the Gamma function.
If $U$ is a [[domain|097KNJFJ7V]], $g$ and $h$ are holomorphic on $U$, and $h$ is not identically zero, then $g/h$ is meromorphic on $U$. The meromorphic functions on a domain form a field.
The function $e^{1/z}$ is not meromorphic on $\mathbb{C}$, because its singularity at $0$ is [[essential|0YKDJBV26S]].
The set $P$ can be infinite. It is countable, and each compact subset of $U$ contains only finitely many points of $P$.

## Explanations

### L1 human

A meromorphic function is holomorphic except at some isolated points, where it has poles.
For example, $\frac{1}{z^2 + 1}$ is holomorphic on $\mathbb{C}$ except at $i$ and $-i$, where it goes to infinity.
