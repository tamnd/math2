---
tag: ZWCSB3YHWM
kind: definition
name: Nondeterministic finite automaton
msc: [68Q45]
defines: SFMYM96C1B
uses: [RABRP2KG81, 1P6EP01HZF, 5MFZ4VNY6D, 00E0YZCERH, W65B6BKZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
---

## Definition

A *nondeterministic finite automaton* (NFA) is a tuple $N = (Q, \Sigma, \Delta, q_0, F)$ where:

1. $Q$ is a nonempty finite set of states;
2. $\Sigma$ is an [[alphabet|RABRP2KG81]];
3. $\Delta \colon Q \times \Sigma \to \mathcal{P}(Q)$ is the *transition function*, with values in the [[power set|00E0YZCERH]] of $Q$;
4. $q_0 \in Q$ is the initial state;
5. $F \subseteq Q$ is the set of accepting states.

The NFA $N$ *accepts* a [[string|1P6EP01HZF]] $w = a_1 a_2 \cdots a_n$ with $a_i \in \Sigma$ when there are states $r_0, r_1, \ldots, r_n \in Q$ with $r_0 = q_0$, $r_i \in \Delta(r_{i-1}, a_i)$ for $1 \le i \le n$, and $r_n \in F$.
The *language of* $N$ is the [[formal language|5MFZ4VNY6D]] $L(N)$ of all strings that $N$ accepts.

## Remarks

Example: over $\Sigma = \set{a, b}$, take $Q = \set{0, 1, 2}$, $q_0 = 0$, $F = \set{2}$, $\Delta(0, a) = \set{0, 1}$, $\Delta(0, b) = \set{0}$, $\Delta(1, a) = \Delta(1, b) = \set{2}$ and $\Delta(2, a) = \Delta(2, b) = \emptyset$.
A run ends in state $2$ exactly when it moves to state $1$ on the second-to-last letter, and that letter is $a$.
So $L(N)$ is the set of words whose second-to-last letter is $a$.
Non-example: an automaton with a transition that reads no symbol, an $\varepsilon$-move, is not an NFA in this sense, because $\Delta$ is only defined on $Q \times \Sigma$; it is an $\varepsilon$-NFA.
A [[DFA|W65B6BKZRY]] $(Q, \Sigma, \delta, q_0, F)$ is the NFA with $\Delta(q, a) = \set{\delta(q, a)}$.
Some authors allow a set of initial states instead of a single one; this does not change the class of accepted languages.
