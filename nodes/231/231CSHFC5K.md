---
tag: 231CSHFC5K
kind: definition
name: Quotient category
msc: [18A32, 18A05]
defines: 43MP9NWS6H
uses: [A2DE66937D, 859F0TFVA3, 0G8VEZ3WTK, 28NQ0KRHD3]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_category
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
A *congruence* $R$ on $\mathcal{C}$ is a family of [[equivalence relations|0G8VEZ3WTK]] $\sim_{X,Y}$, one on each set $\Hom(X, Y)$ of [[morphisms|859F0TFVA3]], with this property.
If $f \sim f'$ for $f, f' \colon X \to Y$, then $g \circ f \circ h \sim g \circ f' \circ h$ for all $h \colon W \to X$ and $g \colon Y \to Z$.
The *quotient category* $\mathcal{C}/R$ has the same objects as $\mathcal{C}$.
Its morphisms $X \to Y$ are the equivalence classes $[f]$ of morphisms $f \colon X \to Y$, with composition $[g] \circ [f] = [g \circ f]$ and identities $[\id_X]$.

## Remarks

The compatibility condition makes the composition $[g] \circ [f] = [g \circ f]$ independent of the chosen representatives.
The quotient [[functor|28NQ0KRHD3]] $Q \colon \mathcal{C} \to \mathcal{C}/R$ is the identity on objects and sends $f$ to $[f]$.
It is universal: a functor $G \colon \mathcal{C} \to \mathcal{D}$ with $G(f) = G(f')$ whenever $f \sim f'$ factors uniquely as $G = \bar{G} \circ Q$.

Example: view the monoid $(\Z, +)$ as a category with one object, whose morphisms are the integers and whose composition is addition.
Let $m \sim n$ when $m - n$ is even.
If $m \sim m'$ then $(k + m + l) - (k + m' + l) = m - m'$ is even, so $\sim$ is a congruence, and the quotient is the one-object category of the group $\Z/2\Z$.

Non-example: on the same category let $m \sim n$ when $m = n$ or $\{m, n\} = \{0, 1\}$.
This is an equivalence relation, but $0 \sim 1$ while $0 + 1 = 1$ and $1 + 1 = 2$ are not related, so it is not compatible with composition and gives no quotient category.
