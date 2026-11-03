---
tag: DDVYP8RNG8
kind: statement
role: theorem
name: Powerset construction
msc: [68Q45]
uses: [SFMYM96C1B, W65B6BKZRY, 00E0YZCERH]
about: [SFMYM96C1B, W65B6BKZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Powerset_construction
same_as:
  wikidata: Q2106494
  wikipedia: Powerset construction
---

## Statement

Let $N = (Q, \Sigma, \Delta, q_0, F)$ be a [[nondeterministic finite automaton|SFMYM96C1B]].
Let $\mathcal{P}(Q)$ be the [[power set|00E0YZCERH]] of $Q$.
Define the [[deterministic finite automaton|W65B6BKZRY]] $D = (\mathcal{P}(Q), \Sigma, \delta, \set{q_0}, F_D)$ by
$$\delta(S, a) = \bigcup_{q \in S} \Delta(q, a) \quad \text{and} \quad F_D = \set{S \subseteq Q : S \cap F \ne \emptyset}.$$
Then $L(D) = L(N)$.
In particular, every language accepted by an NFA with $n$ states is accepted by a DFA with at most $2^n$ states.

## Remarks

By induction on the length of $w$, the state $\delta^*(\set{q_0}, w)$ is exactly the set of states that $N$ can reach from $q_0$ by reading $w$.
So $D$ accepts $w$ if and only if some run of $N$ on $w$ ends in $F$.
In practice one builds only the subsets reachable from $\set{q_0}$, which are often few.
The bound $2^n$ cannot be improved in general.
The language of words over $\set{a, b}$ whose $n$-th letter from the end is $a$ has an NFA with $n + 1$ states.
But every DFA for it needs at least $2^n$ states, since it must remember the last $n$ letters.
For an NFA with $\varepsilon$-moves, the same construction works after replacing each set by its $\varepsilon$-closure.

## Explanations

### L1 human

A nondeterministic machine may be in several states at once, in the sense that several runs are possible.
The powerset construction keeps track of the whole set of states that are possible so far.
This set is a single, determined piece of information, so the new machine is deterministic.
The price is size: there are $2^n$ possible sets of $n$ states.

### L2 human

This theorem shows that nondeterminism adds no power to finite automata, unlike the open question for polynomial-time Turing machines.
It is the standard way to prove that NFAs, $\varepsilon$-NFAs and DFAs all accept exactly the [[regular languages|18WVBDCS38]].
Combined with the translation of [[regular expressions|4DMYF2PR4Q]] into $\varepsilon$-NFAs, it is how lexer generators and some search tools turn a pattern into a fast deterministic matcher.
The resulting DFA can then be reduced by [[DFA minimization|1WPX24AEAT]].
