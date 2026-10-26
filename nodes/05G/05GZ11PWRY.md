---
tag: 05GZ11PWRY
kind: definition
name: Homeomorphism
msc: [54C05]
defines: 0QT00PB5G2
uses: [0SY9ECQ19Q, 0SNQEF7Z53, 0W766JAPSN]
sources:
  - url: https://en.wikipedia.org/wiki/Homeomorphism
    locator: Definition
---

## Definition

Let $X$ and $Y$ be [[topological spaces|0CNQXVBHCX]].
A function $f \colon X \to Y$ is a homeomorphism when $f$ is [[bijective|0SNQEF7Z53]], $f$ is [[continuous|0SY9ECQ19Q]], and the [[inverse function|0W766JAPSN]] $f^{-1} \colon Y \to X$ is continuous.
The spaces $X$ and $Y$ are homeomorphic when there is a homeomorphism $X \to Y$.

## Remarks

Equivalently, $f$ is a bijection and, for each $U \subseteq X$, the set $U$ is open if and only if $f(U)$ is open.
The map $x \mapsto x / (1 - |x|)$ is a homeomorphism from $(-1, 1)$ to $\mathbb{R}$.
A continuous bijection need not be a homeomorphism: $t \mapsto (\cos t, \sin t)$ from $[0, 2\pi)$ to the circle is one example. For a compact domain and a Hausdorff target, [[it is always a homeomorphism|0430ETCMKD]].
Homeomorphisms keep each [[topological property|02SMVGC690]].

## Explanations

### L1 human

A homeomorphism is a way to deform one space into another by stretching and bending, without tearing or gluing.
A coffee cup and a doughnut are homeomorphic, but a sphere and a doughnut are not.
