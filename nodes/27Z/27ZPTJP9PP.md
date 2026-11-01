---
tag: 27ZPTJP9PP
kind: definition
name: Free monoid
msc: [20M05]
defines: CV013KHVJG
uses: [0N6R902FG1, 0SJ3RX9TXA, 0XHDTE5YMZ]
sources:
  - url: https://en.wikipedia.org/wiki/Free_monoid
---

## Definition

Let $A$ be a [[set|0SJ3RX9TXA]], called the alphabet.
A *word* over $A$ is a finite sequence $a_1 a_2 \cdots a_n$ with $n \ge 0$ and each $a_i \in A$; the word with $n = 0$ is the empty word $\varepsilon$.
The *free monoid* on $A$ is the set $A^*$ of all words over $A$ with the operation of concatenation,
$$(a_1 \cdots a_n)(b_1 \cdots b_m) = a_1 \cdots a_n b_1 \cdots b_m,$$
and with identity element $\varepsilon$.

## Remarks

Concatenation is associative and $\varepsilon$ is a two-sided identity, so $A^*$ is a [[monoid|0N6R902FG1]].
Universal property: for every monoid $M$ and every [[map|0XHDTE5YMZ]] $f \colon A \to M$, there is exactly one monoid homomorphism $\bar f \colon A^* \to M$ with $\bar f(a) = f(a)$ for $a \in A$, namely $\bar f(a_1 \cdots a_n) = f(a_1) \cdots f(a_n)$.
A monoid is called free if it is isomorphic to some $A^*$.
The free semigroup $A^+$ is $A^*$ without the empty word.

Example: for $A = \set{a}$, the map $a^n \mapsto n$ is an isomorphism from $A^*$ onto the monoid $(\N, +)$ with $0 \in \N$.

Non-example: the monoid $(\Z, +)$ is not free.
In a free monoid, $uv = \varepsilon$ forces $u = v = \varepsilon$, because lengths add; but in $\Z$, $1 + (-1) = 0$ with $1 \ne 0$.
