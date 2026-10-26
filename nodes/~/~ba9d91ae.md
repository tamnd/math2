---
tag: ~ba9d91ae
kind: statement
role: theorem
name: Intermediate value theorem
aliases: [bolzano-theorem]
msc: [26A15]
uses: [~9520bdea]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Theorem
same_as:
  wikidata: Q245098
  wikipedia: Intermediate value theorem
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be [[continuous|~9520bdea]].
Let $y$ be a real number between $f(a)$ and $f(b)$.
Then there is $c \in [a, b]$ with $f(c) = y$.

## Remarks

Assume $f(a) < y < f(b)$. Let $c$ be the supremum of $\{ x \in [a, b] : f(x) < y \}$. Continuity gives $f(c) \le y$ and $f(c) \ge y$.
The proof needs the completeness of $\mathbb{R}$. Over $\mathbb{Q}$, the function $x^2 - 2$ changes sign on $[1, 2]$ but has no rational zero.
It gives the [[existence of $n$-th roots|~2d2db242]], and it shows that each odd degree real polynomial has a real root.
Mathlib states it as `intermediate_value_Icc`.

## History

Bernard Bolzano first proved the theorem in 1817.

## Explanations

### L1 human

A continuous function on an interval cannot skip values.
To get from $f(a)$ to $f(b)$, its graph must cross every horizontal line in between.
