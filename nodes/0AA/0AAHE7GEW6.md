---
tag: 0AAHE7GEW6
kind: definition
name: Kernel of a ring homomorphism
msc: [16B99]
defines: 0JN0SQG2JH
uses: [0GGE0Z0JQ1]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(algebra)
    locator: Ring homomorphisms
---

## Definition

Let $f \colon R \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]].
The kernel of $f$ is the set
$$\ker f = \{a \in R : f(a) = 0\}.$$

## Remarks

The kernel of $f$ is a [[two-sided ideal|0DDA6CY7GJ]] of $R$.
The kernel of the reduction map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ is $n\mathbb{Z}$.
The map $f$ is injective if and only if $\ker f = \{0\}$, by the [[kernel criterion|0MMCB8RXGA]].

## Explanations

### L1 human

The kernel collects all the elements that $f$ sends to $0$.
For reduction modulo $5$, the kernel is the set of the multiples of $5$.
