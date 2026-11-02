---
tag: 5MDSVRCDZW
kind: definition
name: Naive set theory
msc: ["03E30", "03A05"]
defines: XGAMQBSE1G
uses: [JRBRNZT680, 0SJ3RX9TXA, 0TB16T2C97, 0HESMMSYEG, 0HE5WDQ9FJ]
sources:
  - url: https://en.wikipedia.org/wiki/Naive_set_theory
---

## Definition

*Naive set theory*, in its formal reading, is the [[set theory|JRBRNZT680]] in first-order logic with the relation symbol $\in$ and these two axioms.

1. Extensionality: two [[sets|0SJ3RX9TXA]] with the same elements are equal, as in the [[axiom of extensionality|0TB16T2C97]].
2. Unrestricted comprehension: for each formula $\varphi(x)$, possibly with parameters, in which $y$ is not free, $\exists y\, \forall x\, (x \in y \leftrightarrow \varphi(x))$.

In a wider sense, naive set theory is the informal use of sets in ordinary language, without a fixed list of axioms.

## Remarks

Example: the comprehension instance for $\varphi(x) = (x \ne x)$ gives a set with no elements, the empty set, and extensionality makes it unique.
Non-example: the formal theory is inconsistent, so it has no model.
Indeed, take $\varphi(x) = (x \notin x)$; comprehension gives $y$ with $\forall x\, (x \in y \leftrightarrow x \notin x)$, and $x = y$ gives $y \in y \leftrightarrow y \notin y$.
This is [[Russell's paradox|0HESMMSYEG]].
[[Zermelo–Fraenkel set theory|0HE5WDQ9FJ]] replaces unrestricted comprehension by the separation scheme $\exists y\, \forall x\, (x \in y \leftrightarrow x \in a \wedge \varphi(x))$, which only forms subsets of a given set $a$.
