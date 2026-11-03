---
tag: 7DSXBWD96M
kind: statement
role: theorem
name: Parikh's theorem
msc: [68Q45, 68R15]
uses: [Q56EWEQYE2, 18WVBDCS38, B66JYY3K58]
about: [Q56EWEQYE2]
sources:
  - url: https://en.wikipedia.org/wiki/Parikh's_theorem
same_as:
  wikidata: Q7137090
  wikipedia: Parikh's theorem
---

## Statement

Let $\Sigma = \set{a_1, \dots, a_k}$ be a finite alphabet.
The *Parikh map* $\psi \colon \Sigma^* \to \N^k$ sends a word $w$ to $(\abs{w}_{a_1}, \dots, \abs{w}_{a_k})$, where $\abs{w}_{a}$ is the number of occurrences of $a$ in $w$.
A set $M \subseteq \N^k$ is *linear* if $M = \set{v_0 + n_1 v_1 + \cdots + n_m v_m : n_1, \dots, n_m \in \N}$ for some $v_0, \dots, v_m \in \N^k$, and *semilinear* if it is a finite union of linear sets.
Let $L \subseteq \Sigma^*$ be a [[context-free language|Q56EWEQYE2]].
Then:

1. the set $\psi(L)$ is semilinear;
2. there is a [[regular language|18WVBDCS38]] $R \subseteq \Sigma^*$ with $\psi(R) = \psi(L)$.

## Remarks

The two parts are equivalent, because the Parikh images of regular languages are exactly the semilinear sets.
The proof decomposes parse trees.
Each tree is built from a bounded tree by inserting pumping pieces, as in the pumping lemma, and each pumping piece adds a vector from a finite set.
Example: $L = \set{a^n b^n : n \ge 0}$ has $\psi(L) = \set{(n, n) : n \in \N}$, a linear set with $v_0 = (0,0)$ and $v_1 = (1,1)$, and the regular language $(ab)^*$ has the same image.
A consequence is that every context-free language over a one-letter alphabet is regular.
The theorem does not say that $L$ itself is regular: $\set{a^n b^n}$ is not.

## Explanations

### L1 human

If one only counts how many times each letter occurs, and forgets the order, a context-free language looks just like a regular one.
The nesting that makes context-free languages more powerful is invisible to letter counts.
For instance, the words $a^n b^n$ and the words $(ab)^n$ have the same letter counts.
The possible letter counts always form a finite union of simple arithmetic patterns.

### L2 human

Parikh's theorem is a tool to show that a language is not context-free: if its letter counts do not form a semilinear set, it is not.
For example, $\set{a^{n^2} : n \ge 0}$ is not context-free, since $\set{n^2}$ is not a finite union of arithmetic progressions.
The semilinear sets are exactly the subsets of $\N^k$ definable in [[Presburger arithmetic|B66JYY3K58]], which links the theorem to logic.
It is also used in the verification of systems with counters.
