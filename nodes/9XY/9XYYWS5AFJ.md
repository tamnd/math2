---
tag: 9XYYWS5AFJ
kind: definition
name: Grothendieck construction
msc: [18D30, 18A25]
defines: 272T16NWZ9
uses: [A2DE66937D, 28NQ0KRHD3, AFNE9C4NH6]
sources:
  - url: https://en.wikipedia.org/wiki/Category_of_elements
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]], let $\mathbf{Cat}$ be the category of small categories, and let $F \colon \mathcal{C} \to \mathbf{Cat}$ be a [[functor|28NQ0KRHD3]].
The *Grothendieck construction* of $F$ is the category $\int F$ given as follows.

1. An object is a pair $(c, x)$ with $c$ an object of $\mathcal{C}$ and $x$ an object of $F(c)$.
2. A morphism $(c, x) \to (c', x')$ is a pair $(f, \varphi)$ with $f \colon c \to c'$ in $\mathcal{C}$ and $\varphi \colon F(f)(x) \to x'$ in $F(c')$.
3. The composite of $(f, \varphi) \colon (c, x) \to (c', x')$ and $(g, \psi) \colon (c', x') \to (c'', x'')$ is $(g \circ f, \ \psi \circ F(g)(\varphi))$.
4. The identity of $(c, x)$ is $(\id_c, \id_x)$.

The projection functor $p \colon \int F \to \mathcal{C}$ sends $(c, x)$ to $c$ and $(f, \varphi)$ to $f$.

## Remarks

Example: if $F$ is the constant functor with value a small category $\mathcal{D}$, then $F(f) = \id_{\mathcal{D}}$ for every $f$.
A morphism $(c, x) \to (c', x')$ is then a pair $(f, \varphi)$ with $\varphi \colon x \to x'$ in $\mathcal{D}$, so $\int F$ is the [[product category|AFNE9C4NH6]] $\mathcal{C} \times \mathcal{D}$.

Non-example: the disjoint union of the categories $F(c)$, with no morphisms between different fibres, is not $\int F$ when $\mathcal{C}$ has a non-identity morphism $f \colon c \to c'$ and $F(c)$ is non-empty.
Clause 2 gives the morphism $(f, \id_{F(f)(x)}) \colon (c, x) \to (c', F(f)(x))$ between two fibres.

When each $F(c)$ is a set seen as a category with only identity morphisms, $\int F$ is the category of elements of $F$.
For a functor $F \colon \mathcal{C}^{\mathrm{op}} \to \mathbf{Cat}$ the dual construction takes morphisms $(f, \varphi)$ with $f \colon c \to c'$ and $\varphi \colon x \to F(f)(x')$ in $F(c)$; its projection is a fibration.
