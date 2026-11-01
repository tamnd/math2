---
tag: GEJYZEY7Y0
kind: definition
name: Filtration of a module
msc: [13A30, 13C05]
defines: WHME2NGANG
uses: [0310REJJY8, 0NZ8JA25WK, 05WDSN597C, 096Z9MP2ME]
sources:
  - url: https://en.wikipedia.org/wiki/Filtration_(mathematics)
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]], let $M$ be an $R$-[[module|0NZ8JA25WK]], and let $I$ be an [[ideal|096Z9MP2ME]] of $R$.
A *filtration* of $M$ is a sequence of [[submodules|05WDSN597C]] $(M_n)_{n \ge 0}$ with $M_0 = M$ and $M_n \supseteq M_{n+1}$ for all $n$.
It is an *$I$-filtration* if moreover $I M_n \subseteq M_{n+1}$ for all $n \ge 0$.
An $I$-filtration is *stable* if there is $n_0$ such that $I M_n = M_{n+1}$ for all $n \ge n_0$.

## Remarks

Example: the $I$-adic filtration $M_n = I^n M$ is a stable $I$-filtration, since $I \cdot I^n M = I^{n+1} M$ for every $n$.
Non-example: for $R = M = \Z$ and $I = 2\Z$, the filtration $M_n = 4^n \Z$ is not a $2\Z$-filtration, since $I M_1 = 8\Z$ is not contained in $M_2 = 16\Z$.
Some authors say $I$-good for stable.
Two stable $I$-filtrations of $M$ have bounded difference: there is $k$ with $M_{n+k} \subseteq M'_n$ and $M'_{n+k} \subseteq M_n$ for all $n$, so they define the same topology.
