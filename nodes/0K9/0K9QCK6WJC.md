---
tag: 0K9QCK6WJC
kind: statement
role: theorem
name: General Leibniz rule
msc: [26A24]
uses: [084NGSTWM7, 0V9A43H7WV]
sources:
  - url: https://en.wikipedia.org/wiki/General_Leibniz_rule
    locator: lead section
same_as:
  wikidata: Q2586745
  wikipedia: General Leibniz rule
---

## Statement

Let $n$ be a natural number, and let $f$ and $g$ be $n$ times differentiable real functions on an open interval $I$.
Then $f g$ is $n$ times differentiable on $I$, and
$$(f g)^{(n)} = \sum_{k=0}^{n} \binom{n}{k} f^{(k)} g^{(n-k)}.$$

## Remarks

The proof is an induction on $n$ with the [[product rule|0V9A43H7WV]], like the proof of the binomial theorem.
For $n = 1$ it is the product rule. For $n = 2$ it is $(f g)'' = f'' g + 2 f' g' + f g''$.
Mathlib states it as `iteratedDeriv_mul`.

## Explanations

### L1 human

The rule for the $n$-th derivative of a product looks like the binomial formula for $(a + b)^n$.
Each term distributes $n$ differentiations between the two factors.
