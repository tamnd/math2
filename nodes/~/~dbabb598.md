---
tag: ~dbabb598
kind: statement
role: theorem
name: Rank–nullity theorem
aliases: [dimension-theorem-for-linear-maps]
msc: [15A03, 15A04]
uses: [~a8d1eb96, ~b68bd749]
sources:
  - url: https://en.wikipedia.org/wiki/Rank–nullity_theorem
    locator: Stating the theorem
same_as:
  wikidata: Q303402
  wikipedia: Rank–nullity theorem
---

## Statement

Let $F$ be a field, let $V$ be a finite-dimensional vector space over $F$, and let $W$ be a vector space over $F$.
Let $T \colon V \to W$ be a [[linear map|~2402e937]].
Then
$$\dim \im T + \dim \ker T = \dim V,$$
that is, $\rank T + \operatorname{nullity} T = \dim V$, with the [[rank|~bbb6f915]] and the [[nullity|~40113303]] of $T$.

## Remarks

For an $m \times n$ matrix $A$, this says $\rank A + \dim \{x : Ax = 0\} = n$.
A proof extends a basis of $\ker T$ to a basis of $V$; the images of the new vectors form a basis of $\im T$.
The theorem also follows from the [[first isomorphism theorem|~a5a7374a]] $V / \ker T \cong \im T$.

## Explanations

### L1 human

Each dimension of the domain either survives in the image or is crushed into the kernel.
So the dimensions of image and kernel add up to the dimension of the domain.
A map from $\R^5$ to $\R^3$ has a kernel of dimension at least $2$.
