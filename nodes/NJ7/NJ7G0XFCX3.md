---
tag: NJ7G0XFCX3
kind: definition
name: Regular language
msc: [68Q45]
defines: 18WVBDCS38
uses: [5MFZ4VNY6D, W65B6BKZRY, RABRP2KG81]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_language
---

## Definition

Let $\Sigma$ be an [[alphabet|RABRP2KG81]].
A [[formal language|5MFZ4VNY6D]] $L \subseteq \Sigma^*$ is *regular* when there is a [[deterministic finite automaton|W65B6BKZRY]] $A$ with input alphabet $\Sigma$ such that $L(A) = L$.

## Remarks

Example: over $\Sigma = \set{a, b}$, the language of words with an even number of $a$'s is regular.
The DFA with states $\set{0, 1}$, initial and accepting state $0$, where $a$ swaps the two states and $b$ fixes them, accepts it.
Non-example: $\set{a^n b^n : n \ge 0}$ is not regular.
Suppose a DFA with $k$ states accepted it.
Then two of the words $a^0, a^1, \ldots, a^k$, say $a^i$ and $a^j$ with $i \ne j$, would lead to the same state.
So $a^i b^i$ and $a^j b^i$ would be both accepted or both rejected.
This is a contradiction, since $a^i b^i \in L$ and $a^j b^i \notin L$.
Equivalent forms: $L$ is regular if and only if it is accepted by a nondeterministic finite automaton, if and only if it is the language of a regular expression.
Every finite language is regular.
