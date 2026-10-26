---
tag: 04GNK7K4VP
kind: definition
name: Divisibility in a commutative ring
msc: [13A05]
defines: 07RGNK57ED
uses: [0GYGHKX834]
sources:
  - url: https://en.wikipedia.org/wiki/Divisibility_(ring_theory)
    locator: Definition
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $a, b \in R$.
The element $a$ divides $b$, written $a \mid b$, if there is $c \in R$ with $b = a c$.
Then $a$ is a divisor of $b$, and $b$ is a multiple of $a$.

## Remarks

The relation $a \mid b$ holds if and only if $(b) \subseteq (a)$ for the [[principal ideals|00A2EDFT9Q]].
Every element divides $0$, and $0$ divides only $0$.
A [[unit|019NFGFPR5]] divides every element.
In $\mathbb{Z}[i]$, $1 + i$ divides $2$, because $2 = (1 + i)(1 - i)$.

## Explanations

### L1 human

Divisibility in a ring works as for integers: $a$ divides $b$ if $b$ is $a$ times some element of the ring.
The answer depends on the ring: $2$ does not divide $1$ in $\mathbb{Z}$, but it does in $\mathbb{Q}$.
