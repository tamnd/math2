---
tag: 0MCR8ZAXQD
kind: definition
name: Minimal element
msc: [06A06]
defines: 0BXEZV83GY
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_and_minimal_elements
    locator: lead section
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]] and let $S$ be a [[subset|0FE8Q5S42Y]] of $P$.
An element $m \in S$ is a minimal element of $S$ when no $s \in S$ satisfies $s < m$.
Equivalently, for each $s \in S$, $s \le m$ implies $s = m$.

## Remarks

It is the [[maximal element|0TZEEFTNCC]] for the reversed order $\ge$.
In $\{2, 3, 4, 6, 9\}$ under divisibility, the minimal elements are $2$ and $3$.
A [[well-founded relation|0230ECX1Q5]] is one in which each nonempty subset has a minimal element.

## Explanations

### L1 human

A minimal element has nothing below it.
Among the integers greater than $1$ under divisibility, the minimal elements are the primes.
