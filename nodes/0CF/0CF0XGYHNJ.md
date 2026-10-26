---
tag: 0CF0XGYHNJ
kind: statement
role: proposition
name: exp(2 pi i/n) is a primitive root of unity
msc: [11R18]
uses: [0J817RTVG6, 057BH3JC9S]
sources:
  - url: https://en.wikipedia.org/wiki/Root_of_unity
    locator: Trigonometric expression
---

## Statement

Let $n$ be a positive integer.
Then $e^{2 \pi i / n}$ is a [[primitive root of unity|0J817RTVG6]].

## Remarks

Proof: for $1 \le k < n$, the number $\zeta^k = e^{2 \pi i k / n}$ has argument $2 \pi k / n$, which is strictly between $0$ and $2\pi$. Thus $\zeta^k \neq 1$.
For $n = 4$ this number is $i$, and for $n = 2$ it is $-1$.

## Explanations

### L1 human

The first root of unity after $1$, going counterclockwise around the circle, is a primitive one.
Its powers walk around the circle step by step and visit every $n$th root of unity before they return to $1$.
