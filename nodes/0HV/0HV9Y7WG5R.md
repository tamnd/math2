---
tag: 0HV9Y7WG5R
kind: definition
name: Group homomorphism
aliases: [homomorphism-of-groups]
msc: [20A05]
defines: 0JYTG5K9Y4
uses: [G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: lead section
---

## Definition

Let $G$ and $H$ be [[groups|G5S1M9]].
A group homomorphism from $G$ to $H$ is a map $\varphi \colon G \to H$ such that $\varphi(ab) = \varphi(a) \varphi(b)$ for all $a, b \in G$.
Here the product $ab$ is taken in $G$ and the product $\varphi(a) \varphi(b)$ is taken in $H$.

## Remarks

The map $n \mapsto 2^n$ is a homomorphism from $(\mathbb{Z}, +)$ to $(\mathbb{Q}^\times, \cdot)$.
The map $x \mapsto e^x$ is a homomorphism from $(\mathbb{R}, +)$ to the positive real numbers with multiplication.
For each pair of groups, the map that sends each element of $G$ to the identity of $H$ is a homomorphism, the trivial homomorphism.
The composite of two homomorphisms is a homomorphism.

## Explanations

### L1 human

A homomorphism translates one group into another so that products go to products.
It does not matter if you multiply first and then translate, or translate first and then multiply.
The logarithm turns multiplication of positive numbers into addition, and this is why it is a homomorphism.
