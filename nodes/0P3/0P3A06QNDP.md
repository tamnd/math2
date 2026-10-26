---
tag: 0P3A06QNDP
kind: statement
role: theorem
name: Negation of a universal statement
msc: [03B10]
uses: [0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB]
sources:
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
---

## Statement

Let $X$ be a set and let $P(x)$ be a [[predicate|0T3DPBG981]] on $X$.
In classical logic, the negation of $\forall x \in X, \, P(x)$ is logically equivalent to $\exists x \in X, \, \neg P(x)$.
$$\neg \bigl( \forall x \in X, \, P(x) \bigr) \equiv \exists x \in X, \, \neg P(x)$$

## Remarks

The direction from $\exists x, \, \neg P(x)$ to $\neg \forall x, \, P(x)$ is valid in intuitionistic logic. The other direction needs classical logic.
This law explains why one [[counterexample|0ED72CTBNP]] refutes a universal statement.
For a finite $X$, it is a form of [[De Morgan's laws|09PKJKA6J0]].

## Explanations

### L1 human

"Not every student passed" means "some student did not pass".
To deny that all elements have a property, you show one element without it.
