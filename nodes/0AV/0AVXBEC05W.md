---
tag: 0AVXBEC05W
kind: statement
role: theorem
name: R/P is an integral domain iff P is prime
msc: [13A15]
uses: [0VFW4Y69BT, 06HC6HK0Z8, 09S3PFBEPM]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_ideal
    locator: Properties
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $P$ be an ideal of $R$.
Then the [[quotient ring|0VFW4Y69BT]] $R/P$ is an [[integral domain|09S3PFBEPM]] if and only if $P$ is a [[prime ideal|06HC6HK0Z8]].

## Remarks

The condition $1 + P \neq 0 + P$ in $R/P$ is the condition $P \neq R$.
The condition that $(a + P)(b + P) = 0$ implies $a + P = 0$ or $b + P = 0$ is the condition that $a b \in P$ implies $a \in P$ or $b \in P$.
For example, $\mathbb{Z}/n\mathbb{Z}$ is an integral domain exactly when $n$ is prime or $n = 0$.

## Explanations

### L1 human

The theorem translates a property of the ideal into a property of the quotient ring.
An element is zero in $R/P$ exactly when it lies in $P$.
So "a product in $P$ has a factor in $P$" becomes "a zero product has a zero factor".
