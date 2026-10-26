---
tag: 0GZB2SN0PH
kind: example
name: Function space
msc: [15A03, "46E99"]
instance_of: [000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Function_space
    locator: lead section
same_as:
  wikidata: Q934367
  wikipedia: Function space
---

## Example

Let $F$ be a field, let $X$ be a set, and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
The set $V^X$ of all functions $f \colon X \to V$ is a vector space over $F$ with the pointwise operations
$$(f + g)(x) = f(x) + g(x), \qquad (af)(x) = a\, f(x)$$
for $f, g \in V^X$, $a \in F$ and $x \in X$.
The zero vector is the function with value $0$ at each point.

## Remarks

For $X = \{1, \dots, n\}$ and $V = F$, this is the [[coordinate space|0XM8BZD76G]] $F^n$.
The continuous functions $[0, 1] \to \R$ form a subspace of $\R^{[0, 1]}$.
If $X$ is infinite and $V \ne 0$, then $V^X$ is infinite-dimensional.

## Explanations

### L1 human

We add two functions by adding their values at each point.
We scale a function by scaling its values.
With these rules, functions behave like vectors, and the zero function is the zero vector.
