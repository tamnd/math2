---
tag: 1XNJHTW6TK
kind: definition
name: Weak ordering
msc: [06A06, 06A05]
defines: PW2NKAPXWA
uses: [SWB1ZXFVKY, 0SGTMBEWRF]
sources:
  - url: https://en.wikipedia.org/wiki/Weak_ordering
---

## Definition

Let $A$ be a set and let $<$ be a [[strict partial order|SWB1ZXFVKY]] on $A$.
Two elements $a, b \in A$ are *incomparable* when neither $a < b$ nor $b < a$.
The relation $<$ is a *strict weak ordering* when incomparability is transitive.
That is, for all $a, b, c \in A$: if $a, b$ are incomparable and $b, c$ are incomparable, then $a, c$ are incomparable.

## Remarks

Let $f \colon A \to \R$ be any function and set $a < b$ when $f(a) < f(b)$.
This is a strict weak ordering: $a$ and $b$ are incomparable exactly when $f(a) = f(b)$, and equality of values is transitive.
On $A = \set{a, b, c}$, the strict partial order whose only relation is $a < b$ is not a strict weak ordering.
Here $a$ and $c$ are incomparable and $c$ and $b$ are incomparable, but $a$ and $b$ are comparable.
In a strict weak ordering, incomparability is an [[equivalence relation|0SGTMBEWRF]], and $<$ induces a strict total order on its classes.
The non-strict form is a total preorder: a [[preorder|0RXS8R6K37]] $\lesssim$ in which $a \lesssim b$ or $b \lesssim a$ for all $a, b$.
Strict weak orderings and total preorders on $A$ correspond one to one, by $a \lesssim b$ if and only if not $b < a$.

## Explanations

### L1 human

A weak ordering is a ranking with ties.
Tied elements form groups, and the groups stand in a line.
