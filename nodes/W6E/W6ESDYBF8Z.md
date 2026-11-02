---
tag: W6ESDYBF8Z
kind: definition
name: Turing machine
msc: [03D10, 68Q04]
defines: 758EYCN27B
uses: [0BSJ7RQ9BW, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_machine
---

## Definition

A *Turing machine* is a tuple $M = (Q, \Gamma, \sqcup, \Sigma, \delta, q_0, F)$ with the following parts.

1. $Q$ is a finite nonempty [[set|0BSJ7RQ9BW]] of states.
2. $\Gamma$ is a finite set of tape symbols, and $\sqcup \in \Gamma$ is the blank symbol.
3. $\Sigma \subseteq \Gamma \setminus \set{\sqcup}$ is the set of input symbols.
4. $q_0 \in Q$ is the initial state, and $F \subseteq Q$ is the set of halting states.
5. $\delta$ is a partial [[function|0EPAT51DXQ]] from $(Q \setminus F) \times \Gamma$ to $Q \times \Gamma \times \set{L, R}$, the transition function.

A configuration consists of a state $q$, a tape $t \colon \Z \to \Gamma$ with only finitely many non-blank cells, and a head position $p \in \Z$.
If $\delta(q, t(p)) = (q', s, D)$, the next configuration has state $q'$, the symbol $s$ written at cell $p$, and head position $p - 1$ if $D = L$ and $p + 1$ if $D = R$.
The machine *halts* when no transition applies, in particular when it reaches a state in $F$.
On an input word $w \in \Sigma^*$, the computation starts in state $q_0$ with the head at cell $0$.
At the start, $w$ is written from cell $0$ onward and all other cells are blank.

## Remarks

Example: let $Q = \set{q_0, h}$, $\Gamma = \set{0, 1, \sqcup}$, $\Sigma = \set{0, 1}$ and $F = \set{h}$.
Let $\delta(q_0, 0) = (q_0, 1, R)$, $\delta(q_0, 1) = (q_0, 0, R)$ and $\delta(q_0, \sqcup) = (h, \sqcup, R)$.
Each clause holds, and on input $0110$ the machine moves right, writes $1001$, and halts at the first blank.

Non-example: a "machine" with one state for each natural number is not a Turing machine, because clause 1 requires finitely many states.

Many variants are in use: a tape infinite in one direction only, several tapes, or a single halting state.
They all compute the same partial functions, though their running times differ.
