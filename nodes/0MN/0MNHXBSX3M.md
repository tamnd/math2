---
tag: 0MNHXBSX3M
kind: definition
name: Prime element
msc: [13A05]
defines: 01VH21EV6F
uses: [04GNK7K4VP, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_element
    locator: Definition
inventory: [PEMB7C1PQG]
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
An element $p \in R$ is prime if it has these three properties.

1. $p \neq 0$.
2. $p$ is not a [[unit|019NFGFPR5]].
3. For all $a, b \in R$, if $p \mid a b$, then $p \mid a$ or $p \mid b$.

## Remarks

A nonzero $p$ is prime if and only if the principal ideal $(p)$ is a [[prime ideal|06HC6HK0Z8]].
The prime elements of $\mathbb{Z}$ are the numbers $p$ and $-p$ with $p$ a prime number.
In an integral domain, [[prime elements are irreducible|0F0K8DB9TD]].

## Explanations

### L1 human

Euclid's lemma says that a prime number dividing a product divides one of the factors.
A prime element of a ring is an element with this property.
In the integers, $6$ is not prime: $6$ divides $2 \cdot 3$, but not $2$ or $3$.
