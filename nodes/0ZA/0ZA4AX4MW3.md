---
tag: 0ZA4AX4MW3
kind: statement
role: theorem
name: Cauchy criterion for sequences
msc: [40A05]
uses: [0QZMTN5AXX, 0AZ3R52593, 0G6D8E7CTA, 0KDJD249DT]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_sequence
    locator: Completeness
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Cauchy sequences
---

## Statement

Let $(a_n)$ be a real sequence.
Then $(a_n)$ converges if and only if $(a_n)$ is a [[Cauchy sequence|0QZMTN5AXX]].

## Remarks

One direction is [[convergent sequences are Cauchy|0QY87R9CY3]].
For the other direction, a Cauchy sequence is [[bounded|0G6D8E7CTA]], so it has a convergent subsequence by the [[Bolzano–Weierstrass theorem|0KDJD249DT]]. A Cauchy sequence with a convergent subsequence converges to the same limit.
The criterion says that $\mathbb{R}$ is a complete metric space. It fails in $\mathbb{Q}$.
Its value is that it proves convergence without a candidate for the limit.

## Explanations

### L1 human

To show that a sequence has a limit, you often need to know the limit first.
The Cauchy criterion avoids this. It is enough to show that the terms become close to each other.
