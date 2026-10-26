---
tag: 0TMZ89Q5KA
kind: concept
name: Set-builder notation
aliases: [set-comprehension]
msc: ["03E20"]
uses: [0SJ3RX9TXA, 0T3DPBG981]
sources:
  - url: https://en.wikipedia.org/wiki/Set-builder_notation
    locator: lead section
same_as:
  wikidata: Q3352804
  wikipedia: Set-builder notation
---

## Summary

Set-builder notation describes a [[set|0SJ3RX9TXA]] by a property of its [[elements|0EZ758XE73]].
For a set $X$ and a [[predicate|0T3DPBG981]] $P(x)$ on $X$, the set $\{x \in X \mid P(x)\}$ has as elements exactly the $a \in X$ such that $P(a)$ is true.

## Remarks

A colon is a common alternative to the bar: $\{x \in X : P(x)\}$.
Example: $\{n \in \mathbb{Z} \mid n \text{ is even}\}$ is the set of even integers.
The form $\{f(x) \mid x \in X\}$ denotes the set of the values $f(x)$. This is the [[image|0Q3F20XB0A]] of $X$ under $f$.
Without the bound $x \in X$, the notation $\{x \mid P(x)\}$ can lead to [[Russell's paradox|0HESMMSYEG]].

## Explanations

### L1 human

Instead of a list of elements, you give a test.
$\{x \in \mathbb{R} \mid x^2 = 4\}$ means "all real numbers whose square is $4$".
This set is $\{-2, 2\}$.
