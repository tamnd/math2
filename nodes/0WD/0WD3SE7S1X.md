---
tag: 0WD3SE7S1X
kind: statement
role: theorem
name: R/M is a field iff M is maximal
msc: [13A15]
uses: [0VFW4Y69BT, 09J6KGT65G, 0QA8CHH8MG, 0D1R4SVMBQ, 0M6G75E95E]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_ideal
    locator: Properties
---

## Statement

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $M$ be an ideal of $R$.
Then the [[quotient ring|0VFW4Y69BT]] $R/M$ is a [[field|0QA8CHH8MG]] if and only if $M$ is a [[maximal ideal|09J6KGT65G]].

## Remarks

The proof uses the [[correspondence theorem|0D1R4SVMBQ]]: the ideals of $R/M$ are the images of the ideals of $R$ that contain $M$.
So $M$ is maximal if and only if $R/M$ is nonzero and has only the two ideals $\{0\}$ and $R/M$.
A nonzero commutative ring with only these two ideals is a field, by the [[converse for fields|0M6G75E95E]].
For example, $\mathbb{Z}/p\mathbb{Z}$ is a field because $p\mathbb{Z}$ is maximal for $p$ prime.

## Explanations

### L1 human

The quotient by an ideal is a field exactly when the ideal is as large as possible.
In the integers, $(5)$ is maximal, and $\mathbb{Z}/5\mathbb{Z}$ is a field.
The ideal $(6)$ is not maximal, and $\mathbb{Z}/6\mathbb{Z}$ is not a field.
