---
tag: ~0ebcb6d4
kind: statement
role: proposition
name: The only ideals of a field are zero and the whole field
msc: ["12E99"]
uses: [~92ce2090, ~521b4541]
sources:
  - url: https://en.wikipedia.org/wiki/Ideal_(ring_theory)
    locator: Examples and properties
---

## Statement

Let $K$ be a [[field|~92ce2090]] and let $I$ be an [[ideal|~521b4541]] of $K$.
Then $I = \{0\}$ or $I = K$.

## Remarks

The proof: if $a \in I$ and $a \neq 0$, then $1 = a^{-1} a \in I$, so $r = r \cdot 1 \in I$ for each $r \in K$.
The converse holds: a nonzero commutative ring whose only ideals are $\{0\}$ and the whole ring is a field.
For each nonzero $a$, the ideal $(a)$ is the whole ring, so $1 = b a$ for some $b$.

## Explanations

### L1 human

If an ideal of a field contains a nonzero element, then it contains $1$, because you can divide.
Once an ideal contains $1$, it contains every element.
So a field has only the two trivial ideals.
