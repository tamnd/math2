---
tag: TKG3YF2G5A
kind: definition
name: Filtered category
msc: [18A30]
defines: 975PMY4FG8
uses: [A2DE66937D, 859F0TFVA3]
sources:
  - url: https://en.wikipedia.org/wiki/Filtered_category
---

## Definition

Let $J$ be a [[category|A2DE66937D]].
$J$ is *filtered* if:

1. $J$ has at least one object.
2. For any two objects $a$ and $b$ of $J$, there are an object $c$ and [[morphisms|859F0TFVA3]] $a \to c$ and $b \to c$.
3. For any two morphisms $f, g \colon a \to b$ of $J$, there is a morphism $h \colon b \to c$ with $h \circ f = h \circ g$.

## Remarks

Equivalently, every diagram $F \colon K \to J$ with $K$ a finite category has a cocone.
A colimit over a filtered category is a *filtered colimit*.
The dual notion is a *cofiltered* category.

Example: a [[directed set|D9RY4667K6]] $(I, \le)$, seen as a category with one arrow $i \to j$ when $i \le j$, is filtered.
Clause 1 holds because a directed set is not empty, and clause 2 is the existence of a common upper bound.
Clause 3 holds because there is at most one arrow between two objects, so $f = g$.

Non-example: the category with two objects $a, b$, two arrows $f, g \colon a \to b$ and only identities besides, is not filtered.
Clause 3 fails: the only arrow out of $b$ is $\id_b$, and $\id_b \circ f \neq \id_b \circ g$.
