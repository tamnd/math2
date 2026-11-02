---
tag: QV3V8HJW2F
kind: definition
name: Idempotence
msc: [08A02, 16U40]
defines: 9FS1JFZSX4
uses: [0M418FE7BB, 0EPAT51DXQ, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotence
---

## Definition

1. Let $\ast$ be a [[binary operation|0M418FE7BB]] on a set $S$.
An element $x \in S$ is *idempotent* for $\ast$ if $x \ast x = x$.
The operation $\ast$ is *idempotent* if every element of $S$ is idempotent for $\ast$.
2. Let $X$ be a set.
A [[function|0EPAT51DXQ]] $f \colon X \to X$ is *idempotent* if $f \circ f = f$, that is, $f(f(x)) = f(x)$ for all $x \in X$, where $\circ$ is [[composition|0THBK9V825]].

## Remarks

Example: union is an idempotent operation on the power set of a set $X$, because $Y \cup Y = Y$ for every $Y \subseteq X$.

Non-example: multiplication on $\Z$ is not idempotent, because $2 \cdot 2 = 4 \ne 2$; its only idempotent elements are $0$ and $1$.

The two notions agree.
A function $f \colon X \to X$ is idempotent in the sense of clause 2 if and only if it is idempotent for composition on the set of maps $X \to X$.
A function is idempotent if and only if it fixes every point of its image.
