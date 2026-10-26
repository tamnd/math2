---
tag: 0X4JKZXJ86
kind: definition
name: Idempotent element
msc: [16U40]
defines: 0N5NJZKKN3
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Idempotent_(ring_theory)
    locator: lead section
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
An element $e \in R$ is idempotent if $e^2 = e$.

## Remarks

In every ring, $0$ and $1$ are idempotent.
In $\mathbb{Z}/6\mathbb{Z}$, the classes of $3$ and $4$ are idempotent, because $9 \equiv 3$ and $16 \equiv 4 \pmod 6$.
If $e$ is idempotent, then $1 - e$ is idempotent, and $e (1 - e) = 0$.
In the [[product|0MNZCN4BQK]] $R \times S$, the elements $(1, 0)$ and $(0, 1)$ are idempotent.

## Explanations

### L1 human

An idempotent does not change when you square it.
Among the integers, only $0$ and $1$ have this property.
Other rings can have more idempotents, for example the projection matrices.
