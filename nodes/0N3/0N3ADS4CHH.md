---
tag: 0N3ADS4CHH
kind: definition
name: Uniqueness quantifier
msc: [03B10]
defines: 0QAJHFGZZJ
uses: [0JW2FHW7G3, 0B88PQTJ66]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
---

## Definition

Let $X$ be a set and let $P(x)$ be a [[predicate|0T3DPBG981]] on $X$.
The proposition $\exists! x \in X, \, P(x)$ is true when exactly one $a \in X$ makes $P(a)$ true.
In terms of the other quantifiers, it is the proposition
$$\exists x \in X, \, \bigl( P(x) \land \forall y \in X, \, (P(y) \to y = x) \bigr).$$

## Remarks

A proof of $\exists! x, \, P(x)$ usually has two parts: existence, an $x$ with $P(x)$, and uniqueness, if $P(x)$ and $P(y)$ then $x = y$.
For example, $\exists! x \in \mathbb{R}, \, 2x + 1 = 7$ is true, with $x = 3$.

## Explanations

### L1 human

"There is exactly one even prime" says two things.
There is an even prime, namely $2$, and no other number is an even prime.
