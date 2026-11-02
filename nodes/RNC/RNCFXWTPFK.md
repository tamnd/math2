---
tag: RNCFXWTPFK
kind: definition
name: Finitely complete category
msc: [18A35]
defines: PYSBNWCHCF
uses: [A2DE66937D, HJK75HDWFE, CHS5AFJGWE]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_category
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
$\mathcal{C}$ is *finitely complete* if every [[diagram|HJK75HDWFE]] $F \colon J \to \mathcal{C}$ with $J$ a finite category has a [[limit|CHS5AFJGWE]] in $\mathcal{C}$.
Here a category $J$ is finite when it has finitely many objects and finitely many morphisms.

## Remarks

The following are equivalent for a category $\mathcal{C}$:

1. $\mathcal{C}$ is finitely complete.
2. $\mathcal{C}$ has a terminal object, binary products and equalizers.
3. $\mathcal{C}$ has a terminal object and pullbacks.

Example: the category of finite sets is finitely complete.
Its terminal object is a one-point set, and the pullback of $f \colon X \to Z$ and $g \colon Y \to Z$ is the finite set $\set{(x, y) : f(x) = g(y)}$.

Non-example: the totally ordered set $(\Z, \le)$, seen as a category, has all pullbacks but no terminal object.
In a preorder the pullback of $x \to z \leftarrow y$ is $\min(x, y)$, and a terminal object would be a greatest element.
