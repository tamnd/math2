---
tag: 0VSNX4P2Q0
kind: statement
role: proposition
name: Cancellation laws
aliases: [cancellation-law]
msc: [20A05]
about: [G5S1M9]
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

### L2 agent

The cancellation laws let us remove a common factor from both sides of an equation. The factor must be on the same side in both products.

The proof of left cancellation has three steps:

1. Suppose that $ab = ac$.
2. Multiply both sides on the left by $a^{-1}$.
3. Associativity and $a^{-1}a = e$ give $b = c$.

A worked example in $S_3$, with composition from right to left:

1. Let $a = (1\,2)$. Suppose that $ax = (1\,2\,3)$ and $ay = (1\,2\,3)$.
2. Then $ax = ay$, so $x = y$ by left cancellation.
3. Thus $x = a^{-1}(1\,2\,3) = (1\,2)(1\,2\,3) = (2\,3)$ is the only solution.

This shows a useful consequence. For fixed $a$ and $c$, the equation $ax = c$ has exactly one solution, $x = a^{-1}c$. Thus each row of the Cayley table of a finite group contains each element exactly one time. The same is true for each column.

A common error is to cancel across sides. From $ab = ca$ we cannot conclude $b = c$. In $S_3$, let $a = (1\,2)$, $b = (1\,3)$ and $c = (2\,3)$. Then $ab = (1\,3\,2)$ and $ca = (1\,3\,2)$, but $b \ne c$.

The laws need inverses. In the monoid $(\mathbb{Z}, \cdot)$, $0 \cdot 1 = 0 \cdot 2$, but $1 \ne 2$, because $0$ has no inverse.
