---
tag: 0QKVE1GD9A
kind: statement
role: theorem
name: Euclidean domains are principal ideal domains
msc: [13F07]
uses: [0GJ2HRG95T, 0RZYDVZ475]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_ideal_domain
    locator: Properties
---

## Statement

Let $R$ be a [[Euclidean domain|0GJ2HRG95T]].
Then $R$ is a [[principal ideal domain|0RZYDVZ475]].

## Remarks

The proof: let $I \neq 0$ be an ideal and let $b \in I$ be a nonzero element with $\delta(b)$ minimal. For $a \in I$, write $a = b q + r$. Then $r \in I$ and $\delta(r) < \delta(b)$ is impossible, so $r = 0$ and $I = (b)$.
The converse is false: $\mathbb{Z}[\tfrac{1 + \sqrt{-19}}{2}]$ is a principal ideal domain that is not Euclidean.

## Explanations

### L1 human

Take a nonzero element of the ideal that is as small as possible.
Every other element of the ideal leaves remainder zero when you divide it by this one.
So the smallest element generates the ideal.
