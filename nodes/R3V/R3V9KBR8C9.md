---
tag: R3V9KBR8C9
kind: statement
role: lemma
name: Ogden's lemma
msc: [68Q45, 68Q42]
uses: [Q56EWEQYE2, KQ0TQABTPJ]
about: [Q56EWEQYE2]
sources:
  - url: https://en.wikipedia.org/wiki/Ogden's_lemma
same_as:
  wikidata: Q1855893
  wikipedia: Ogden's lemma
---

## Statement

Let $L \subseteq \Sigma^*$ be a [[context-free language|Q56EWEQYE2]].
Then there is an integer $p \ge 1$ with the following property.
Let $w \in L$, and mark at least $p$ of the positions of $w$.
Then $w$ can be written as $w = uvxyz$ with $u, v, x, y, z \in \Sigma^*$ such that:

1. $v$ and $y$ together contain at least one marked position;
2. $vxy$ contains at most $p$ marked positions;
3. $u v^i x y^i z \in L$ for every integer $i \ge 0$.

## Remarks

The proof follows that of the [[pumping lemma|KQ0TQABTPJ]], but only counts branch points of the parse tree that have marked leaves on both sides.
Marking every position of $w$ gives back the pumping lemma for context-free languages.
Example: $L = \set{a^i b^j c^k d^l : i = 0 \text{ or } j = k = l}$ satisfies the conclusion of the pumping lemma, yet it is not context-free.
To see this, take $w = a b^p c^p d^p$ and mark the $b$s.
Then $vy$ contains a $b$.
If $v$ or $y$ meets two blocks, $u v^2 x y^2 z$ has letters out of order.
Otherwise $v$ and $y$ each lie in one block, so $vy$ meets at most two of the blocks of $b$s, $c$s and $d$s.
Then $u v^2 x y^2 z$ has at least one $a$ and unequal numbers of $b$s, $c$s and $d$s, so it is not in $L$.

## Explanations

### L1 human

Ogden's lemma is a sharper pumping lemma.
It lets one point at the positions of the word that matter, and then guarantees that the pumped pieces touch at least one of those positions.
This stops the pumping from happening in a harmless part of the word.
With it, one can prove that some languages are not context-free even though the ordinary pumping lemma cannot.

### L2 human

The ordinary pumping lemma fails on the example above because the pumped pieces may fall inside the block of $a$s, where pumping changes nothing important.
Marking the $b$s rules this out.
Ogden's lemma is also used to prove that some context-free languages are inherently ambiguous, such as $\set{a^i b^j c^k : i = j \text{ or } j = k}$.
It is still only a necessary condition for being context-free.
