---
tag: 4A7VAXPG4F
kind: concept
name: Pluriharmonic function
msc: [32U05, 31C10]
specializes: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Pluriharmonic_function
same_as:
  wikidata: Q4365897
  wikipedia: Pluriharmonic function
---

## Summary

A pluriharmonic function is a real function on an open subset of $\C^n$ whose restriction to every complex line is [[harmonic|0DEB0JMN0W]].
Equivalently, all its mixed derivatives $\partial^2 u / \partial z_j \partial \bar z_k$ vanish.
Locally, pluriharmonic functions are exactly the real parts of [[holomorphic functions|507C34W0ZT]].
They are the functions $u$ such that both $u$ and $-u$ are [[plurisubharmonic|FF2P7ER3QT]].

## Explanations

### L1 human

In one complex variable, harmonic functions are the real parts of holomorphic functions.
In several variables, the real parts of holomorphic functions satisfy more equations than the Laplace equation: they are harmonic on each complex line.
These functions are called pluriharmonic.
For example, $u(z_1, z_2) = \operatorname{Re}(z_1 z_2)$ is pluriharmonic on $\C^2$.
The function $\abs{z_1}^2 - \abs{z_2}^2$ is harmonic on $\R^4$ but not pluriharmonic, since on the line $z_2 = 0$ it is $\abs{z_1}^2$, which is not harmonic.
