---
tag: AZES1C6VMT
kind: definition
name: Order embedding
msc: [06A06]
defines: RH0HD05BMN
uses: [011C29Q1S1, 0WFF6AZPBP]
sources:
  - url: https://en.wikipedia.org/wiki/Order_embedding
---

## Definition

Let $(P, \le_P)$ and $(Q, \le_Q)$ be [[partially ordered sets|011C29Q1S1]].
A map $f \colon P \to Q$ is an *order embedding* when, for all $x, y \in P$,
$$x \le_P y \iff f(x) \le_Q f(y).$$

## Remarks

The inclusion $\Q \to \R$ is an order embedding, since the order of $\Q$ is the restriction of the order of $\R$.
Let $P = \set{a, b}$ with $a$ and $b$ incomparable, and let $Q = \set{0, 1}$ with $0 < 1$.
The map $f(a) = 0$, $f(b) = 1$ is [[monotone|0WFF6AZPBP]], but it is not an order embedding: $f(a) \le f(b)$ while $a \not\le b$.
An order embedding is injective: $f(x) = f(y)$ gives $x \le y$ and $y \le x$, so $x = y$ by antisymmetry.
So $f$ is an [[order isomorphism|0Y74KN99A5]] from $P$ onto its image $f(P)$ with the induced order.
For total orders, a strictly increasing map is the same as an order embedding.

## Explanations

### L1 human

An order embedding keeps every comparison and creates no new ones.
It shows one ordered set as an ordered part of another.
