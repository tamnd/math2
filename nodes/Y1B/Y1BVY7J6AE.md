---
tag: Y1BVY7J6AE
kind: concept
name: Falling and rising factorials
msc: [05A10, 33B15]
sources:
  - url: https://en.wikipedia.org/wiki/Falling_and_rising_factorials
same_as:
  wikidata: Q2339261
  wikipedia: Falling and rising factorials
---

## Summary

The falling factorial $x^{\underline{n}}$ multiplies $n$ consecutive factors going down from $x$, and the rising factorial $x^{\overline{n}}$ multiplies $n$ consecutive factors going up from $x$.
Both are polynomials of degree $n$ in $x$, and both reduce to the [[factorial|0XWG0JGDFW]] $n!$ for a suitable choice of $x$.
The falling factorial counts ordered selections without repetition, and the rising factorial (the Pochhammer symbol of special functions) appears in hypergeometric series.
The node [[falling factorial|0SJNCJCCQG]] treats the falling case alone.

## Explanations

### L1 human

Start at a number and multiply it by the next few numbers below it: that is a falling factorial.
Multiply it by the next few numbers above it instead: that is a rising factorial.
For example, $5^{\underline{3}} = 5 \cdot 4 \cdot 3 = 60$ and $5^{\overline{3}} = 5 \cdot 6 \cdot 7 = 210$.
The number $60$ counts the ways to give gold, silver and bronze medals to $3$ of $5$ runners.
Both products start at $x$ and use $n$ factors, so with $x = n$ falling or $x = 1$ rising they give $n!$.
