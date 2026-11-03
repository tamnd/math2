---
tag: KNWWRAYCSR
kind: definition
name: Pushdown automaton
msc: [68Q45, 68Q04]
defines: 8YEY51Q3B5
uses: [RABRP2KG81, 1P6EP01HZF, 5MFZ4VNY6D, SFMYM96C1B, Q56EWEQYE2]
sources:
  - url: https://en.wikipedia.org/wiki/Pushdown_automaton
---

## Definition

A *pushdown automaton* is a tuple $M = (Q, \Sigma, \Gamma, \delta, q_0, Z_0, F)$ where:

1. $Q$ is a finite set of states;
2. $\Sigma$ is a finite input [[alphabet|RABRP2KG81]];
3. $\Gamma$ is a finite stack alphabet;
4. $\delta$ is a function from $Q \times (\Sigma \cup \set{\varepsilon}) \times \Gamma$ to the finite subsets of $Q \times \Gamma^*$, the transition function;
5. $q_0 \in Q$ is the start state and $Z_0 \in \Gamma$ is the initial stack symbol;
6. $F \subseteq Q$ is the set of accepting states.

A *configuration* is a triple $(q, w, \gamma)$ with $q \in Q$, $w \in \Sigma^*$ the unread input and $\gamma \in \Gamma^*$ the stack, top symbol first.
For $x \in \Sigma \cup \set{\varepsilon}$, $X \in \Gamma$ and $(p, \beta) \in \delta(q, x, X)$, there is a move $(q, xw, X\gamma) \vdash (p, w, \beta\gamma)$.
Let $\vdash^*$ be the reflexive and transitive closure of $\vdash$.
The [[language|5MFZ4VNY6D]] *accepted* by $M$ is
$$L(M) = \set{w \in \Sigma^* : (q_0, w, Z_0) \vdash^* (q, \varepsilon, \gamma) \text{ for some } q \in F, \ \gamma \in \Gamma^*}.$$

## Remarks

Example: for $\set{a^n b^n : n \ge 0}$ take $Q = \set{q_0, q_1, q_2}$, $\Gamma = \set{A, Z_0}$ and $F = \set{q_2}$.
The transitions are $\delta(q_0, a, Z_0) = \set{(q_0, AZ_0)}$, $\delta(q_0, a, A) = \set{(q_0, AA)}$, $\delta(q_0, b, A) = \set{(q_1, \varepsilon)}$, $\delta(q_1, b, A) = \set{(q_1, \varepsilon)}$, $\delta(q_0, \varepsilon, Z_0) = \delta(q_1, \varepsilon, Z_0) = \set{(q_2, Z_0)}$, and all other values are empty.
The machine pushes one $A$ per $a$ and pops one $A$ per $b$.
It can enter $q_2$ only when the stack is back to $Z_0$, so it accepts exactly the words $a^n b^n$.
Non-example: a machine with two independent stacks is not a pushdown automaton, since clause 4 allows only one stack; two stacks already simulate a Turing machine.
Acceptance by empty stack, $(q_0, w, Z_0) \vdash^* (q, \varepsilon, \varepsilon)$ for some $q$, gives the same class of languages.
A language is accepted by a pushdown automaton if and only if it is a [[context-free language|Q56EWEQYE2]].
