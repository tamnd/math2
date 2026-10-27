---
tag: 0K26YKNBSA
kind: definition
name: Zero divisor
msc: [16U99]
defines: 0NNRDW10RZ
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_divisor
    locator: lead section
inventory: [A7EKMZA5XT]
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
An element $a \in R$ is a left zero divisor if there is a nonzero $x \in R$ with $a x = 0$.
An element $a \in R$ is a right zero divisor if there is a nonzero $y \in R$ with $y a = 0$.
An element is a zero divisor if it is a left or a right zero divisor.

## Remarks

In a [[commutative ring|0GYGHKX834]], left and right zero divisors are the same.
In $\mathbb{Z}/6\mathbb{Z}$, the classes of $2$ and $3$ are zero divisors, because $2 \cdot 3 = 0$.
Some authors do not count $0$ as a zero divisor. With the definition above, $0$ is a zero divisor of every nonzero ring.
A [[unit|019NFGFPR5]] is never a zero divisor.

## Explanations

### L1 human

In the integers, a product is zero only when one factor is zero.
In other rings this can fail.
In the integers modulo $6$, $2 \cdot 3 = 6 = 0$, but neither $2$ nor $3$ is zero.
