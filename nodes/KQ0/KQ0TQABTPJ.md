---
tag: KQ0TQABTPJ
kind: statement
role: lemma
name: Pumping lemma for context-free languages
msc: [68Q45, 68Q42]
uses: [Q56EWEQYE2, CTCY2R8Q77, 7TMGSPXKJ3, CBR9WAGZGZ]
about: [Q56EWEQYE2]
sources:
  - url: https://en.wikipedia.org/wiki/Pumping_lemma_for_context-free_languages
same_as:
  wikidata: Q2596624
  wikipedia: Pumping lemma for context-free languages
---

## Statement

Let $L \subseteq \Sigma^*$ be a [[context-free language|Q56EWEQYE2]].
Then there is an integer $p \ge 1$ such that every $w \in L$ with $\abs{w} \ge p$ can be written as $w = uvxyz$ with $u, v, x, y, z \in \Sigma^*$ such that:

1. $\abs{vxy} \le p$;
2. $\abs{vy} \ge 1$;
3. $u v^i x y^i z \in L$ for every integer $i \ge 0$.

Here $\abs{w}$ is the length of $w$ and $v^i$ is $v$ repeated $i$ times.

## Remarks

Take a [[context-free grammar|CTCY2R8Q77]] for $L$ in [[Chomsky normal form|7TMGSPXKJ3]] with $k$ nonterminals and set $p = 2^k$.
A parse tree of a word of length at least $p$ is binary, so it has a root-to-leaf path with more than $k$ nonterminals.
So some nonterminal $A$ repeats on the lowest part of this path.
The subtree under the upper $A$ yields $vxy$, the one under the lower $A$ yields $x$, and replacing one subtree by the other, or the reverse, repeatedly gives $u v^i x y^i z$.
Example: $L = \set{a^n b^n c^n : n \ge 0}$ is not context-free.
For $w = a^p b^p c^p$, the part $vxy$ has length at most $p$, so it meets at most two of the three blocks.
Then $u v^2 x y^2 z$ either has letters out of order or has unequal block lengths, so it is not in $L$.
The lemma gives only a necessary condition: some languages that are not context-free satisfy its conclusion.

## Explanations

### L1 human

Take a long enough word of a context-free language.
It has two pieces, not far apart, that can be repeated together any number of times, or deleted together, without leaving the language.
The reason is that a long word needs a tall parse tree, and a tall tree must reuse some placeholder along one branch.
The lemma is mostly used backwards, to show that a language is not context-free.
For instance, $a^n b^n c^n$ fails it, because pumping can raise at most two of the three counts.

### L2 human

The lemma is the context-free analogue of the [[pumping lemma for regular languages|CBR9WAGZGZ]], where one piece is pumped instead of two.
A typical proof that $L$ is not context-free picks a word depending on $p$, considers every split allowed by clauses 1 and 2, and finds an $i$ with $u v^i x y^i z \notin L$.
Since the context-free languages are closed under intersection with regular languages and under homomorphisms, one often first simplifies $L$ in this way.
When the lemma is too weak, Ogden's lemma, which lets one mark the important positions, often works.
