---
tag: WDJXQFPF8E
kind: definition
name: Deterministic finite automaton
msc: [68Q45]
defines: W65B6BKZRY
uses: [NDC0E9BZ94, RABRP2KG81, 1P6EP01HZF, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
---

## Definition

A *deterministic finite automaton* (DFA) is a tuple $A = (Q, \Sigma, \delta, q_0, F)$ where:

1. $(Q, \Sigma, \delta, q_0)$ is a [[finite-state machine|NDC0E9BZ94]], with states $Q$, [[alphabet|RABRP2KG81]] $\Sigma$, transition function $\delta \colon Q \times \Sigma \to Q$ and initial state $q_0$;
2. $F \subseteq Q$ is the set of *accepting states*.

The *extended transition function* $\delta^* \colon Q \times \Sigma^* \to Q$ is given by $\delta^*(q, \varepsilon) = q$ and $\delta^*(q, wa) = \delta(\delta^*(q, w), a)$ for every [[string|1P6EP01HZF]] $w \in \Sigma^*$ and $a \in \Sigma$.
The automaton $A$ *accepts* $w$ when $\delta^*(q_0, w) \in F$.
The *language of* $A$ is the [[formal language|5MFZ4VNY6D]] $L(A) = \set{w \in \Sigma^* : \delta^*(q_0, w) \in F}$.

## Remarks

Example: let $\Sigma = \set{a, b}$, $Q = \set{0, 1}$, $q_0 = 0$, $F = \set{0}$, $\delta(q, a) = 1 - q$ and $\delta(q, b) = q$.
Then $\delta^*(0, w)$ is the number of $a$'s in $w$ modulo $2$, so $L(A)$ is the set of words with an even number of $a$'s.
Non-example: a diagram in which state $0$ has two arrows labelled $a$ is not a DFA.
The reason is that $\delta$ must assign one state to each pair $(q, a)$; such diagrams are nondeterministic finite automata.
A diagram with no arrow labelled $b$ out of some state is also not a DFA in this sense.
Some authors allow such *partial* DFAs and complete them with a non-accepting sink state.
