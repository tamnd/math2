---
tag: 05N4TQKPH0
kind: statement
role: proposition
name: Subgroup criterion
aliases: [one-step-subgroup-test]
msc: [20A05]
uses: [0N0PXCTYA7]
sources:
  - url: https://en.wikipedia.org/wiki/Subgroup
    locator: Subgroup tests
---

## Statement

Let $G$ be a [[group|G5S1M9]] and let $H$ be a subset of $G$.
Then $H$ is a [[subgroup|0X1JXT47GA]] of $G$ if and only if $H$ is not empty and $ab^{-1} \in H$ for all $a, b \in H$.

## Remarks

If $a \in H$, then $e = aa^{-1} \in H$, then $b^{-1} = eb^{-1} \in H$ for $b \in H$, and then $ab = a(b^{-1})^{-1} \in H$.
In additive notation, the condition is $a - b \in H$ for all $a, b \in H$.
For a finite nonempty subset $H$, it is sufficient that $ab \in H$ for all $a, b \in H$.

## Explanations

### L1 human

This test replaces three checks by one.
You only check that the subset is not empty and that $ab^{-1}$ stays in the subset.
For example, the multiples of $5$ form a subgroup of $(\mathbb{Z}, +)$, because the difference of two multiples of $5$ is a multiple of $5$.
