---
tag: 0DQVHMYAGA
kind: statement
role: theorem
name: Bézout's identity
aliases: [bezout-lemma, bezouts-lemma]
msc: [11A05]
uses: [02WF878BH1]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity
    locator: lead section
same_as:
  wikidata: Q513028
  wikipedia: Bézout's identity
---

## Statement

Let $a$ and $b$ be integers, and let $d = \gcd(a, b)$ be their [[greatest common divisor|02WF878BH1]].
Then there are integers $x$ and $y$ such that $a x + b y = d$.

## Remarks

The integers $x$ and $y$ are not unique. If $(x, y)$ is a solution, then $(x + k b / d, \; y - k a / d)$ is also a solution for each integer $k$, when $d \neq 0$.
The set of all integers $a x + b y$ is the set of the multiples of $d$.
The [[extended Euclidean algorithm|0964YQFSA8]] computes one pair $(x, y)$.
For example, $\gcd(12, 42) = 6$ and $12 \cdot (-3) + 42 \cdot 1 = 6$.

## Explanations

### L1 human

With coins of value $a$ and $b$, and if you can give and take back coins, you can pay exactly the amount $\gcd(a, b)$.
For example, with coins of $4$ and $6$, you pay $2 = 2 \cdot 4 - 1 \cdot 6$.
You cannot pay $1$ this way, because each sum $4 x + 6 y$ is even.
