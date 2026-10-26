---
tag: 0FCWA16FZE
kind: definition
name: Divisors of a natural number
msc: [11A05]
defines: 0F4JSQE2EK
uses: [096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor
    locator: Definition
---

## Definition

Let $n$ be a positive integer.
The set of divisors of $n$ is the set of positive integers $d$ that [[divide|096PW7Q014]] $n$:
$$D(n) = \{ d \in \mathbb{Z}_{>0} : d \mid n \}.$$

## Remarks

The set $D(n)$ is finite, because each $d \in D(n)$ satisfies $1 \le d \le n$. It always contains $1$ and $n$.
For example, $D(12) = \{1, 2, 3, 4, 6, 12\}$.
The map $d \mapsto n/d$ is a bijection from $D(n)$ to itself.
Sums over $D(n)$ define the [[divisor function|0YEW47VJ0J]] and the [[Dirichlet convolution|0KH1N66QWW]].

## Explanations

### L1 human

The divisors of $n$ are the numbers that go into $n$ with no remainder.
They come in pairs $d$ and $n/d$. For $n = 12$, the pairs are $1$ and $12$, $2$ and $6$, and $3$ and $4$.
