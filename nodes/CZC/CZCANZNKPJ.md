---
tag: CZCANZNKPJ
kind: definition
name: Hemicontinuity
msc: [54C60, "26E25"]
defines: XNMKX7H4FD
uses: [0CQHFPGJ45, 03CPD1HGF3, 02BH3MCBQB, 0ZCY0Z80B6, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Hemicontinuity
---

## Definition

Let $X$ and $Y$ be [[topological spaces|0CQHFPGJ45]].
Let $\Gamma$ be a [[multivalued function|03CPD1HGF3]] from $X$ to $Y$, that is, a map that sends each $x \in X$ to a nonempty subset $\Gamma(x) \subseteq Y$.
Let $x_0 \in X$.

1. $\Gamma$ is *upper hemicontinuous* at $x_0$ if the following holds for every [[open|02BH3MCBQB]] set $V \subseteq Y$ with $\Gamma(x_0) \subseteq V$.
   There is a [[neighbourhood|0ZCY0Z80B6]] $U$ of $x_0$ with $\Gamma(x) \subseteq V$ for all $x \in U$.
2. $\Gamma$ is *lower hemicontinuous* at $x_0$ if the following holds for every open set $V \subseteq Y$ with $\Gamma(x_0) \cap V \ne \emptyset$.
   There is a neighbourhood $U$ of $x_0$ with $\Gamma(x) \cap V \ne \emptyset$ for all $x \in U$.

$\Gamma$ is upper (lower) hemicontinuous if it is so at every point of $X$, and *continuous* if it is both.

## Remarks

Some authors say upper and lower semicontinuous instead of hemicontinuous.
If $\Gamma(x) = \set{f(x)}$ for a function $f \colon X \to Y$, then each of the two conditions is equivalent to the [[continuity|0VGFHTM75Y]] of $f$ at $x_0$.

Example: let $\Gamma \colon \R \to \R$ with $\Gamma(0) = [0, 1]$ and $\Gamma(x) = \set{0}$ for $x \ne 0$.
It is upper hemicontinuous at $0$: an open $V \supseteq [0, 1]$ contains $0$, so $\Gamma(x) \subseteq V$ for all $x$.

Non-example: the same $\Gamma$ is not lower hemicontinuous at $0$.
The open set $V = (1/2, 2)$ meets $\Gamma(0)$, but $\Gamma(x) \cap V = \emptyset$ for every $x \ne 0$.
