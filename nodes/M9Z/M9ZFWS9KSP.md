---
tag: M9ZFWS9KSP
kind: definition
name: Plurisubharmonic exhaustion function
msc: [32U10, 32T35]
defines: FGSKR6ZS3Q
uses: [FF2P7ER3QT, JSGWAN2RJV, 0R6EWFKRCF, 80MTNXWW80]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]], for example a domain in $\C^n$.
A *plurisubharmonic exhaustion function* on $X$ is a function $\varphi \colon X \to [-\infty, \infty)$ such that:

1. $\varphi$ is [[plurisubharmonic|FF2P7ER3QT]] on $X$.
2. $\varphi$ is an exhaustion: for every $c \in \R$, the set $\set{x \in X : \varphi(x) < c}$ is relatively compact in $X$, that is, its closure in $X$ is [[compact|0R6EWFKRCF]].

It is *smooth and strictly plurisubharmonic* if moreover $\varphi$ is $C^\infty$ and its [[Levi form|80MTNXWW80]] is positive definite at every point, in local holomorphic coordinates.

## Remarks

Example: on $\C^n$, $\varphi(z) = \abs{z}^2$ is a smooth strictly plurisubharmonic exhaustion function.
Its Levi form is $\abs{w}^2$, and its sublevel sets are open balls.
Non-example: on the unit ball $B \subseteq \C^n$, $\varphi(z) = \abs{z}^2$ is still strictly plurisubharmonic but is not an exhaustion, since $\set{\varphi < 2} = B$ is not relatively compact in $B$.
On $B$, the function $-\log(1 - \abs{z}^2)$ is a smooth strictly plurisubharmonic exhaustion function.
For a domain $\Omega \subsetneq \C^n$, an equivalent form of clause 2 for continuous $\varphi$ is that $\varphi(z) \to +\infty$ as $z$ tends to $\partial\Omega$ or, when $\Omega$ is unbounded, as $\abs{z} \to \infty$.
