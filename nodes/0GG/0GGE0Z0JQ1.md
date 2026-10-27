---
tag: 0GGE0Z0JQ1
kind: definition
name: Ring homomorphism
msc: [16B99]
defines: 0VTH8KPCG2
uses: [0894J980RK]
sources:
  - url: https://en.wikipedia.org/wiki/Ring_homomorphism
    locator: lead section
inventory: [ECKQ9H3QS7]
---

## Definition

Let $R$ and $S$ be [[rings|0894J980RK]].
A ring homomorphism from $R$ to $S$ is a map $f \colon R \to S$ with these three properties.

1. $f(a + b) = f(a) + f(b)$ for all $a, b \in R$.
2. $f(a b) = f(a) f(b)$ for all $a, b \in R$.
3. $f(1) = 1$.

## Remarks

A ring homomorphism also satisfies $f(0) = 0$ and $f(-a) = -f(a)$.
For each integer $n \ge 1$, the map $\mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$ that sends $a$ to its class is a ring homomorphism.
The map $\mathbb{Z} \to \mathbb{Z}$, $a \mapsto 2a$, preserves sums but is not a ring homomorphism.
A bijective ring homomorphism is a [[ring isomorphism|0B6QC0C0G1]].

## Explanations

### L1 human

A ring homomorphism translates one ring into another and keeps the arithmetic.
It does not matter if you add or multiply first and then apply $f$, or apply $f$ first.
Reduction modulo $n$ is the main example.
