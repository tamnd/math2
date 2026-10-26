---
tag: 0TXTSEMHR5
kind: definition
name: Limit of a function
msc: [26A03]
defines: 0PKRYB8ATM
uses: [07EGCNHAVW]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_function
    locator: More general definition using limit points and subsets
---

## Definition

Let $D$ be a subset of $\mathbb{R}$, let $f \colon D \to \mathbb{R}$ be a function, and let $a$ be a [[limit point|07EGCNHAVW]] of $D$.
A real number $L$ is the limit of $f$ at $a$ if the following holds.
For each open interval $V$ containing $L$ there is an open interval $U$ containing $a$ with $f(x) \in V$ for all $x \in U \cap D$ with $x \ne a$.
The notation is $\lim_{x \to a} f(x) = L$, or $f(x) \to L$ as $x \to a$.

## Remarks

The value of $f$ at $a$ plays no role, and $a$ need not lie in $D$.
The [[epsilon-delta definition|0GBZDAFPX8]] states the same condition with numbers. The [[sequential characterization|000MXHEY22]] states it with sequences.
The limit is unique when it exists, since $a$ is a limit point of $D$.
Mathlib expresses limits with filters, as `Filter.Tendsto`.

## Explanations

### L1 human

The limit of $f$ at $a$ is the value that $f(x)$ approaches as $x$ comes close to $a$.
Only the values near $a$ matter, not the value at $a$ itself.
