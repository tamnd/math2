---
tag: 0VSNX4P2Q0
kind: statement
role: proposition
name: Cancellation laws
aliases: [cancellation-law]
msc: [20A05]
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Cancellation_property
    locator: lead section
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $a, b, c \in G$.
If $ab = ac$, then $b = c$.
If $ba = ca$, then $b = c$.

## Remarks

The first law is left cancellation and the second law is right cancellation.
To prove the first law, multiply $ab = ac$ on the left by $a^{-1}$.
A consequence is that in the [[Cayley table|0YB2NRP0T5]] of a finite group, no element occurs two times in one row or in one column.
The laws can fail in a [[monoid|0N6R902FG1]]: in $(\mathbb{Z}, \cdot)$, $0 \cdot 1 = 0 \cdot 2$ but $1 \neq 2$.

## Explanations

### L1 human

In a group, you can remove the same element from both sides of an equation, if it is on the same side of each product.
This works because each element has an inverse that undoes it.
Take care with the side: $ab = ca$ does not give $b = c$ in general.
