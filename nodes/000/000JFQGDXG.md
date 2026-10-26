---
tag: 000JFQGDXG
kind: statement
role: theorem
name: The integers are a Euclidean domain
msc: [11A05]
uses: [0GJ2HRG95T, 0JHM6JK7FD]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_domain
    locator: Examples
---

## Statement

The [[ring of integers|0JHM6JK7FD]] $\mathbb{Z}$ is a [[Euclidean domain|0GJ2HRG95T]], with the absolute value $\delta(n) = |n|$ as Euclidean function.
That is, for all $a, b \in \mathbb{Z}$ with $b \neq 0$, there are $q, r \in \mathbb{Z}$ with $a = b q + r$ and $0 \le r < |b|$.

## Remarks

The proof: let $r$ be the least element of $\{a - b q : q \in \mathbb{Z}\} \cap \mathbb{N}$. Then $r < |b|$, because otherwise $r - |b|$ would be a smaller element of this set.
The pair $(q, r)$ with $0 \le r < |b|$ is unique.
Consequences: $\mathbb{Z}$ is a [[principal ideal domain|0RZYDVZ475]], and integers factor uniquely into primes.

## Explanations

### L1 human

This is division with remainder from school, made precise.
Dividing $17$ by $5$ gives $17 = 3 \cdot 5 + 2$, and the remainder $2$ is smaller than $5$.
It works for negative numbers too: $-17 = (-4) \cdot 5 + 3$.
