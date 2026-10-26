---
tag: 0JW2FHW7G3
kind: definition
name: Existential quantifier
msc: [03B10]
defines: 0MSRQHCNN9
uses: [0T3DPBG981]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_quantification
    locator: lead section
---

## Definition

Let $X$ be a set and let $P(x)$ be a [[predicate|0T3DPBG981]] on $X$.
The existential quantification of $P$ over $X$ is the proposition $\exists x \in X, \, P(x)$, read "there exists $x$ in $X$ such that $P(x)$".
It is true when $P(a)$ is true for at least one $a \in X$, and false otherwise.

## Remarks

When $X$ is empty, $\exists x \in X, \, P(x)$ is false for each $P$.
For a finite set $X = \{a_1, \dots, a_n\}$, the statement is equivalent to $P(a_1) \lor \dots \lor P(a_n)$.
The [[uniqueness quantifier|0N3ADS4CHH]] $\exists!$ says that exactly one element exists.

## Explanations

### L1 human

"There is an even prime number" is $\exists n \in \mathbb{N}, \, (n \text{ is even} \land n \text{ is prime})$.
To prove it, one example is enough: $n = 2$.
