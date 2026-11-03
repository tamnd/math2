---
tag: JRB4QD04AN
kind: statement
role: theorem
name: Kleene's theorem
msc: [68Q45]
uses: [18WVBDCS38, 4DMYF2PR4Q, SFMYM96C1B]
about: [18WVBDCS38, 4DMYF2PR4Q]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene%27s_algorithm
---

## Statement

Let $\Sigma$ be an alphabet and let $L \subseteq \Sigma^*$ be a language.
Then $L$ is a [[regular language|18WVBDCS38]], that is, accepted by a finite automaton, if and only if $L = L(r)$ for some [[regular expression|4DMYF2PR4Q]] $r$ over $\Sigma$.

## Remarks

From expression to automaton, one argues by induction on $r$.
There are $\varepsilon$-NFAs for $\emptyset$, $\varepsilon$ and single letters.
Then $\varepsilon$-moves glue automata for $r$ and $s$ into automata for $r + s$, $rs$ and $r^*$.
These are then made deterministic by the [[powerset construction|DDVYP8RNG8]].
From automaton to expression, number the states $1, \ldots, n$.
Let $R^k_{ij}$ be the set of words that lead from state $i$ to state $j$ through intermediate states numbered at most $k$.
Then $R^k_{ij} = R^{k-1}_{ij} \cup R^{k-1}_{ik} (R^{k-1}_{kk})^* R^{k-1}_{kj}$, so by induction on $k$ each $R^k_{ij}$ has a regular expression; this is Kleene's algorithm.
For example, the DFA for words with an even number of $a$'s over $\set{a, b}$ yields an expression such as $(b + ab^*a)^*$.

## Explanations

### L1 human

There are two natural ways to describe a set of words.
One is a machine with finitely many states that checks them.
The other is a pattern built from letters with "or", "followed by" and "repeat".
Kleene's theorem says these two ways describe exactly the same sets.
So any pattern can be compiled into a machine, and any finite machine can be summarised by a pattern.

### L2 human

The theorem is the bridge between the algebraic and the machine view of [[regular languages|18WVBDCS38]].
The direction from expressions to automata is used in every tool that searches text by patterns.
The direction from automata to expressions shows, for example, that the complement of a language given by an expression also has an expression, since complements of DFA languages are easy.
The expressions produced by Kleene's algorithm can be exponentially long in the number of states.
