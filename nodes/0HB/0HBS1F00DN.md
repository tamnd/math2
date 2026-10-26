---
tag: 0HBS1F00DN
kind: statement
role: theorem
name: Induction on the integers
msc: [11A99]
uses: [0C4JS9RF5M, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Variants
---

## Statement

Let $P(z)$ be a property of [[integers|0C4JS9RF5M]] $z$.
Suppose that $P(0)$ holds.
Suppose that for each natural number $n$, $P(n)$ implies $P(n + 1)$.
Suppose that for each natural number $n$, $P(-n)$ implies $P(-n - 1)$.
Then $P(z)$ holds for every integer $z$.

## Remarks

The proof applies ordinary [[induction|0ASJVEFA9J]] two times: one time to $P(n)$ and one time to $P(-n)$, for natural numbers $n$.
Each integer is $n$ or $-n$ for some natural number $n$, thus the two inductions cover all of $\mathbb{Z}$.

## Explanations

### L1 human

You start at $0$ and you walk in both directions on the number line.
One induction goes up through $1, 2, 3, \dots$, and the other goes down through $-1, -2, -3, \dots$.
