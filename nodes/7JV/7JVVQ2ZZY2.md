---
tag: 7JVVQ2ZZY2
kind: definition
name: Local homeomorphism
msc: [54C10, 54C05]
defines: MDH71ZZ8XX
uses: [0CQHFPGJ45, 02BH3MCBQB, 0QT00PB5G2, 0WS9P12FQR]
sources:
  - url: https://en.wikipedia.org/wiki/Local_homeomorphism
---

## Definition

Let $X$ and $Y$ be [[topological spaces|0CQHFPGJ45]] and let $f \colon X \to Y$ be a map.
The map $f$ is a *local homeomorphism* if every $x \in X$ has an [[open|02BH3MCBQB]] neighbourhood $U$ with the following two properties.
The set $f(U)$ is open in $Y$.
The restriction $f|_U \colon U \to f(U)$ is a [[homeomorphism|0QT00PB5G2]], where $U$ and $f(U)$ carry the [[subspace topology|0WS9P12FQR]].

## Remarks

A local homeomorphism is [[continuous|0VGFHTM75Y]] and [[open|0YCG648KDD]].
Every homeomorphism is a local homeomorphism, and so is the inclusion of an open subset.

Example: $p \colon \R \to S^1$, $p(t) = (\cos 2\pi t, \sin 2\pi t)$.
For $x \in \R$, take $U = (x - 1/2, x + 1/2)$.
Then $p(U)$ is the circle minus one point, which is open, and $p|_U$ is a continuous bijection onto it with a continuous inverse given by a branch of the angle.

Non-example: $f \colon \C \to \C$, $f(z) = z^2$.
Every neighbourhood $U$ of $0$ contains some $\varepsilon \ne 0$ and $-\varepsilon$, with $f(\varepsilon) = f(-\varepsilon)$, so $f|_U$ is not injective.
At every $z \ne 0$, however, $f$ is a local homeomorphism.
