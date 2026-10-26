---
tag: 0D2MXBV21T
kind: definition
name: Restriction of a function
msc: ["03E20"]
defines: 0NF1KGDXX3
uses: [0XHDTE5YMZ, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Restriction_(mathematics)
    locator: lead section
---

## Definition

Let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]] and let $S$ be a [[subset|0FE8Q5S42Y]] of $A$.
The restriction of $f$ to $S$ is the function $f|_S \colon S \to B$ with $f|_S(s) = f(s)$ for each $s \in S$.

## Remarks

The graph of $f|_S$ is $\{(s, f(s)) \mid s \in S\}$, a subset of the graph of $f$.
The function $f$ is an extension of $f|_S$.
Example: $x \mapsto x^2$ on $\mathbb{R}$ is not [[injective|0PVG1CRAJN]], but its restriction to $[0, \infty)$ is injective.

## Explanations

### L1 human

To restrict a function, you keep its rule and allow fewer inputs.
Restrictions often make a function injective, so that it has an inverse on a smaller domain.
