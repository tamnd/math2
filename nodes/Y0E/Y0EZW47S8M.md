---
tag: Y0EZW47S8M
kind: definition
name: Involution
msc: [08A02, 16W10]
defines: GP56NBN9RY
uses: [0EPAT51DXQ, 0THBK9V825, 0PSKT5W817]
sources:
  - url: https://en.wikipedia.org/wiki/Involution_(mathematics)
---

## Definition

Let $X$ be a set.
An *involution* on $X$ is a [[function|0EPAT51DXQ]] $f \colon X \to X$ such that $f(f(x)) = x$ for all $x \in X$.
Equivalently, $f \circ f = \id_X$, where $\circ$ is [[composition|0THBK9V825]] and $\id_X$ is the [[identity function|0PSKT5W817]] of $X$.

## Remarks

Example: complex conjugation $z \mapsto \bar{z}$ on $\C$ is an involution, because $\overline{\overline{a + bi}} = \overline{a - bi} = a + bi$.

Non-example: the map $x \mapsto x + 1$ on $\Z$ is not an involution, because applying it twice gives $x + 2 \ne x$.

Every involution is a bijection, and it is its own inverse.
The identity map is an involution.
On a finite set, the number of points not fixed by an involution is even, since they come in pairs $\set{x, f(x)}$.
In a group, the map $x \mapsto x^{-1}$ is an involution, because $(x^{-1})^{-1} = x$.
