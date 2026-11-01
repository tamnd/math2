---
tag: GYR1XYFEZB
kind: definition
name: Krohn–Rhodes theory
msc: [20M35, 68Q70]
defines: 3WDZY1J002
uses: [0XMEM406JM, 7ZB7MRKPQ9, W1X984PKJ9, 0YMYMNQ0QZ, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Krohn–Rhodes_theory
---

## Definition

The basic notions of Krohn–Rhodes theory are the following.
Let $S$ and $T$ be [[semigroups|0XMEM406JM]].

1. $S$ *divides* $T$ if $S$ is the image of a homomorphism from a subsemigroup of $T$ onto $S$.
2. Let $(X, A)$ and $(Y, B)$ be [[transformation semigroups|7ZB7MRKPQ9]]. Their *wreath product* $(X, A) \wr (Y, B)$ is the transformation semigroup on $X \times Y$ consisting of all maps $(x, y) \mapsto (\varphi(y)(x), \, b(y))$, where $b \in B$ and $\varphi \colon Y \to A$ is any function.
3. The *flip-flop* is the transformation monoid on $\set{0, 1}$ consisting of the identity and the two constant maps.
4. A *Krohn–Rhodes decomposition* of a finite semigroup $S$ is a division of $S$ into the semigroup of an iterated wreath product $(X_1, A_1) \wr \cdots \wr (X_k, A_k)$.
   Each factor $(X_i, A_i)$ is the flip-flop or a finite [[simple group|0YMYMNQ0QZ]] acting on itself by left multiplication.

## Remarks

The set in clause 2 is closed under composition: applying $(\varphi', b')$ and then $(\varphi, b)$ gives the map of the same form with the function $y \mapsto \varphi(b'(y)) \circ \varphi'(y)$ and the element $b \circ b'$.
In the wreath product, the coordinate in $Y$ moves on its own, and it controls how the coordinate in $X$ moves; this is a cascade of two machines.

The Krohn–Rhodes theorem says that every finite semigroup $S$ has a Krohn–Rhodes decomposition in which each simple group divides $S$.

Example: a finite group $G$ with a composition series has a decomposition into its composition factors, with no flip-flops.
For $G = \Z/4\Z$, two copies of $\Z/2\Z$ suffice, as in the carry rule of a two-digit binary counter.

Non-example: the wreath product of two copies of $\Z/2\Z$ contains no flip-flop factor, and its semigroup is a finite group of bijections of $X \times Y$.
Every subsemigroup of a finite group is a group, and so is every homomorphic image of a group.
So the flip-flop, which is not a group, does not divide it, and every decomposition of a finite semigroup that is not a group needs at least one flip-flop.
