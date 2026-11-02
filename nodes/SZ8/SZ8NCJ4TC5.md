---
tag: SZ8NCJ4TC5
kind: definition
name: Semiorder
msc: [06A06, 91B08]
defines: F2C174HHSE
uses: [60FNZ35H6R, VSNQV29KFJ]
sources:
  - url: https://en.wikipedia.org/wiki/Semiorder
---

## Definition

Let $X$ be a set and let $\prec$ be a [[strict partial order|60FNZ35H6R]] on $X$.
Say that $x$ and $y$ are incomparable when neither $x \prec y$ nor $y \prec x$.
The order $\prec$ is a *semiorder* if, for all $a, b, c, d \in X$:

1. if $a \prec b$ and $c \prec d$, then $a \prec d$ or $c \prec b$;
2. if $a \prec b$ and $b \prec c$, then $a \prec d$ or $d \prec c$.

## Remarks

Clause 1 forbids two incomparable two-element chains, and clause 2 forbids a three-element chain with an element incomparable to all three of its elements.
Example: on $\R$, let $x \prec y$ when $x + 1 < y$.
For clause 2, if $a + 1 < b$ and $b + 1 < c$ but $d \le a + 1$, then $d + 1 \le a + 2 < c$, so $d \prec c$; clause 1 has a similar check.
Non-example: the poset with $a \prec b \prec c$ and an element $d$ incomparable to $a$, $b$ and $c$ satisfies clause 1 but fails clause 2.
Every semiorder is an [[interval order|VSNQV29KFJ]].
By a theorem of Scott and Suppes, a finite strict partial order is a semiorder if and only if there is a map $u \colon X \to \R$ with $x \prec y \iff u(x) + 1 < u(y)$.
