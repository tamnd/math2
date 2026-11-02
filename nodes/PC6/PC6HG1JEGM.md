---
tag: PC6HG1JEGM
kind: concept
name: Comma category
msc: [18A25]
sources:
  - url: https://en.wikipedia.org/wiki/Comma_category
same_as:
  wikidata: Q1780005
  wikipedia: Comma category
---

## Summary

Let $S \colon \mathcal{A} \to \mathcal{C}$ and $T \colon \mathcal{B} \to \mathcal{C}$ be [[functors|28NQ0KRHD3]].
The comma category $(S \downarrow T)$ has as objects the morphisms $S(A) \to T(B)$ of $\mathcal{C}$.
Its morphisms are the pairs of morphisms that make the evident square commute.
It turns morphisms of one category into objects of a new category.
[[Slice categories|1TC7W7BQT3]], arrow categories and [[categories of elements|S9EJKKRHW1]] are special comma categories.
[[Universal properties|EN4DD2FAJH]] and [[adjoint functors|TZHF6ZM92S]] can be expressed as initial or terminal objects of comma categories.

## Explanations

### L1 human

A comma category collects arrows of a category $\mathcal{C}$ that go from one kind of object to another, and treats each arrow as a new object.
An arrow between two such objects is a pair of maps at the two ends that fits with them in a commuting square.
For example, taking all arrows of $\mathcal{C}$ at both ends gives the arrow category, whose objects are morphisms $h \colon X \to Y$ of $\mathcal{C}$.
In the arrow category of sets, the map $\R \to \R$, $x \mapsto x^2$, is one object, and the inclusion $\Z \to \R$ is another.
