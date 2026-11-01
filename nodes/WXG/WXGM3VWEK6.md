---
tag: WXGM3VWEK6
kind: definition
name: Algebraic number field
msc: [11R04, 11R21]
defines: MWBDFS2KJ5
uses: [04C5ZBG1WT, 0EQWVHF3W5, 0EAJ2XXADC, 0NCJ5WXN6Z, 0MNF0BYFQC, 0C3QBCR46M]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_number_field
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]] that contains the field $\Q$ of [[rational numbers|0NCJ5WXN6Z]].
Then $K$ is an *algebraic number field* (or *number field*) if it has finite dimension as a vector space over $\Q$.
This dimension is the [[degree|0EAJ2XXADC]] $[K : \Q]$ of the [[field extension|0EQWVHF3W5]] $K / \Q$, also called the degree of $K$.

## Remarks

Example: $K = \Q(i) = \set{a + bi : a, b \in \Q}$, a subfield of $\C$.
It contains $\Q$, and $1, i$ is a basis over $\Q$, so $[K : \Q] = 2$ and $K$ is a number field.
Non-example: $\R$ contains $\Q$, but it is not of finite dimension over $\Q$, since a finite-dimensional space over $\Q$ is countable and $\R$ is not.
Another non-example: the field of all algebraic numbers is an algebraic extension of $\Q$ of infinite degree.
Every element of a number field is an [[algebraic number|0MNF0BYFQC]], and by the primitive element theorem every number field is $\Q(\alpha)$ for one algebraic number $\alpha$.
The elements of $K$ that are roots of a [[monic polynomial|0C3QBCR46M]] with integer coefficients form a subring $\mathcal{O}_K$, the ring of integers of $K$.
