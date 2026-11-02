---
tag: YZXV7CHF5R
kind: definition
name: Slice category
msc: [18A25]
defines: 1TC7W7BQT3
uses: [A2DE66937D, 859F0TFVA3, PC6HG1JEGM]
sources:
  - url: https://en.wikipedia.org/wiki/Comma_category
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]] and let $X$ be an object of $\mathcal{C}$.
The *slice category* $\mathcal{C}/X$ is defined as follows:

1. its objects are the pairs $(A, h)$ with $h \colon A \to X$ a [[morphism|859F0TFVA3]] of $\mathcal{C}$;
2. a morphism $(A, h) \to (A', h')$ is a morphism $f \colon A \to A'$ of $\mathcal{C}$ with $h' \circ f = h$;
3. composition and identities are those of $\mathcal{C}$.

## Remarks

It is the [[comma category|PC6HG1JEGM]] $(1_{\mathcal{C}} \downarrow X)$, where $X$ also denotes the functor from the one-morphism category that picks $X$.
Dually, the *coslice category* $X/\mathcal{C}$ has as objects the morphisms $X \to A$, and morphisms $f$ with $f \circ h = h'$.
Example: in the category of sets, an object of $\mathbf{Set}/\set{0, 1}$ is a set $A$ with a map $h \colon A \to \set{0, 1}$, that is, a set split into two labelled parts.
Write $e$ for the identity map of $\set{0, 1}$; then $e$ is a morphism from $(\set{0, 1}, e)$ to itself, since $e \circ e = e$.
Non-example: let $s \colon \set{0, 1} \to \set{0, 1}$ swap $0$ and $1$.
The identity map $e$ is not a morphism from $(\set{0, 1}, e)$ to $(\set{0, 1}, s)$, since $s \circ e = s \ne e$.
The object $(X, 1_X)$ is a terminal object of $\mathcal{C}/X$.
