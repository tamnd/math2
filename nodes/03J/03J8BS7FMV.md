---
tag: 03J8BS7FMV
kind: definition
name: Separable polynomial
msc: [12F10]
defines: 0RZ89QWTSJ
uses: [0AD4VS02H3]
sources:
  - url: https://en.wikipedia.org/wiki/Separable_polynomial
    locator: lead section
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $f \in R[x]$.
The polynomial $f$ is separable if there are $a, b \in R[x]$ with $a f + b f' = 1$, where $f'$ is the [[formal derivative|0AD4VS02H3]] of $f$.

## Remarks

Over a [[field|0QA8CHH8MG]] $K$, $f$ is separable if and only if $f$ has no repeated root in an [[algebraic closure|0MCXX29HWY]] of $K$.
The polynomial $f = x^2 - 2$ is separable over $\mathbb{Q}$, because $f' = 2x$ and $-\tfrac{1}{2} f + \tfrac{1}{4} x f' = 1$.
Over $\mathbb{F}_p(t)$, the irreducible polynomial $x^p - t$ is not separable, because its derivative is $0$.
Some older texts call an irreducible polynomial separable when it has distinct roots, and extend this to other polynomials factor by factor.

## Explanations

### L1 human

A separable polynomial has distinct roots, in a field that is large enough to contain all of them.
Over the rational numbers, every irreducible polynomial is separable.
Inseparable irreducible polynomials only appear in prime characteristic.
