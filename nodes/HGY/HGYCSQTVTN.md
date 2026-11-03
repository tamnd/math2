---
tag: HGYCSQTVTN
kind: definition
name: DFA minimization
msc: [68Q45]
defines: 1WPX24AEAT
uses: [W65B6BKZRY, 18WVBDCS38]
sources:
  - url: https://en.wikipedia.org/wiki/DFA_minimization
---

## Definition

Let $A = (Q, \Sigma, \delta, q_0, F)$ be a [[deterministic finite automaton|W65B6BKZRY]], with language $L(A)$.
A DFA $B$ is *equivalent* to $A$ when $L(B) = L(A)$.
A DFA $M$ is *minimal* when no DFA equivalent to $M$ has fewer states than $M$.
*DFA minimization* is the problem of computing, from $A$, a minimal DFA equivalent to $A$.

## Remarks

The standard method has two steps.
First, delete the states $q$ that are not reachable, that is, with $q \ne \delta^*(q_0, w)$ for every $w \in \Sigma^*$.
Second, merge equivalent states, where $p$ and $q$ are equivalent when, for every $w \in \Sigma^*$, $\delta^*(p, w) \in F$ if and only if $\delta^*(q, w) \in F$.
Example: over $\set{a}$, the DFA with states $\set{0, 1, 2, 3}$, $\delta(q, a) = q + 1 \bmod 4$, $q_0 = 0$ and $F = \set{0, 2}$ is not minimal.
States $0$ and $2$ are equivalent, as are $1$ and $3$.
Merging them gives an equivalent DFA with $2$ states, which is minimal.
Non-example: deleting state $3$ alone from that DFA does not give an equivalent DFA, because $\delta$ would no longer be defined on $(2, a)$.
For a [[regular language|18WVBDCS38]] $L$, any two minimal DFAs accepting $L$ differ only by a renaming of states.
Known algorithms include Moore's algorithm by partition refinement, Hopcroft's algorithm, which runs in time $O(n s \log n)$ for $n$ states and $s$ letters, and Brzozowski's algorithm by double reversal and determinization.
