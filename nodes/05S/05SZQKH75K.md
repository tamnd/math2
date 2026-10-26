---
tag: 05SZQKH75K
kind: statement
role: theorem
name: Negation of an existential statement
msc: [03B10]
uses: [0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
---

## Statement

Let $X$ be a set and let $P(x)$ be a [[predicate|0T3DPBG981]] on $X$.
The negation of $\exists x \in X, \, P(x)$ is logically equivalent to $\forall x \in X, \, \neg P(x)$.
$$\neg \bigl( \exists x \in X, \, P(x) \bigr) \equiv \forall x \in X, \, \neg P(x)$$

## Remarks

This equivalence is valid in intuitionistic logic as well as in classical logic.
Together with the [[negation of a universal statement|0P3A06QNDP]], it gives a rule. To negate a quantified statement, swap each $\forall$ and $\exists$ and negate the predicate.

## Explanations

### L1 human

"No student failed" means "every student did not fail".
To deny that some element has a property, you must show that each element lacks it.
