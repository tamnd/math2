---
tag: 0YXEQWRGP0
kind: definition
name: Choice function
msc: ["03E25"]
defines: 0FWBQ53MPJ
uses: [0XHDTE5YMZ, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Choice_function
    locator: lead section
inventory: [Q27DBT5AVS]
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]] of nonempty sets.
A choice function on $X$ is a [[function|0XHDTE5YMZ]] $c \colon X \to \bigcup X$ such that $c(S) \in S$ for each $S \in X$.

## Remarks

For a finite set $X$, a choice function exists without any axiom of choice.
For the set of nonempty subsets of $\mathbb{N}$, the function that sends each subset to its least element is a choice function.
The [[axiom of choice|0HTGB13FE2]] says that each set of nonempty sets has a choice function.

## Explanations

### L1 human

Think of $X$ as a collection of boxes, none empty.
A choice function names one object in each box.
Sometimes a rule gives it, such as "take the smallest number".
