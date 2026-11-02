---
tag: 70QWWYQQG9
kind: example
name: Jónsson–Tarski algebra
msc: [08A99, 08B20]
instance_of: [AJNZJD8442]
uses: [QJGPT2W0FT, Q2W26ZY10B, 0GG9TVW90M, GTS4DRRMZR, PZMGQMDN25]
sources:
  - url: https://en.wikipedia.org/wiki/Jónsson–Tarski_algebra
same_as:
  wikidata: Q18208351
  wikipedia: Jónsson–Tarski algebra
---

## Example

A *Jónsson–Tarski algebra* is an [[algebra|QJGPT2W0FT]] $(A, \cdot, L, R)$ with a binary operation $\cdot$ and two [[unary operations|Q2W26ZY10B]] $L$ and $R$ such that, for all $x, y \in A$:

1. $L(x \cdot y) = x$;
2. $R(x \cdot y) = y$;
3. $L(x) \cdot R(x) = x$.

These laws say exactly that $(x, y) \mapsto x \cdot y$ is a [[bijection|0GG9TVW90M]] from $A \times A$ to $A$, with inverse $x \mapsto (L(x), R(x))$.
Since the laws are identities, Jónsson–Tarski algebras form a [[variety|AJNZJD8442]].

A concrete instance is the set $A$ of infinite binary sequences $s = (s_0, s_1, s_2, \dots)$.
Let $s \cdot t = (s_0, t_0, s_1, t_1, \dots)$ interleave the two sequences.
Let $L(s) = (s_0, s_2, s_4, \dots)$ and $R(s) = (s_1, s_3, s_5, \dots)$.
Then $L(s \cdot t) = s$ and $R(s \cdot t) = t$ because the even places of $s \cdot t$ hold $s$ and the odd places hold $t$.
Also $L(s) \cdot R(s) = s$ because interleaving the even and odd places rebuilds $s$.

## Remarks

A Jónsson–Tarski algebra with more than one element is infinite.
Indeed, if $A$ is finite with $n$ elements, a bijection $A \times A \to A$ forces $n^2 = n$, so $n \le 1$.
Jónsson and Tarski showed that in this variety the [[free algebra|GTS4DRRMZR]] on one generator is [[isomorphic|PZMGQMDN25]] to the free algebra on $n$ generators for every finite $n \ge 1$.
So the number of free generators is not an invariant here, unlike for vector spaces.

## Explanations

### L1 human

A Jónsson–Tarski algebra is a set with a perfect way to pack two elements into one and unpack them again.
Packing $x$ and $y$ gives $x \cdot y$, and the maps $L$ and $R$ recover the left and right parts.
Every element arises from exactly one pair in this way.
Infinite binary sequences give an example: shuffle two sequences together like two decks of cards, and unshuffle to get them back.
No finite set with more than one element can do this, since it has more pairs than elements.
