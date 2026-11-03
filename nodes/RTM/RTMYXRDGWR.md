---
tag: RTMYXRDGWR
kind: example
name: Semiautomaton as a unary algebra
msc: [08A60, 20M35, 68Q70]
instance_of: [XD10P9CJMD]
sources:
  - url: https://en.wikipedia.org/wiki/Semiautomaton
---

## Example

A *semiautomaton* is a triple $(Q, \Sigma, \delta)$ with a set of states $Q$ and a set of input letters $\Sigma$.
The map $\delta \colon Q \times \Sigma \to Q$ is the transition function.
For each letter $a \in \Sigma$ put $\delta_a(q) = \delta(q, a)$.
Then each $\delta_a$ maps $Q$ to $Q$, so $(Q, (\delta_a)_{a \in \Sigma})$ is a [[unary algebra|XD10P9CJMD]] with index set $\Sigma$.
Conversely, a unary algebra $(Q, (f_a)_{a \in \Sigma})$ gives the semiautomaton with $\delta(q, a) = f_a(q)$, so the two notions are the same data.

Concretely, let $Q = \set{\mathrm{even}, \mathrm{odd}}$ and $\Sigma = \set{0, 1}$, with $\delta_0$ the identity of $Q$ and $\delta_1$ the map that swaps $\mathrm{even}$ and $\mathrm{odd}$.
Reading a binary word moves the state according to the parity of the number of letters $1$ read so far.

Under this translation, a homomorphism of unary algebras is a map of states that commutes with every transition.
A subalgebra is a set of states closed under all transitions.
A congruence is an equivalence of states compatible with all transitions.
A [[deterministic finite automaton|W65B6BKZRY]] is a finite semiautomaton with a start state and a set of accepting states added.

## Explanations

### L1 human

A semiautomaton is a machine that changes its state each time it reads a letter.
For each letter there is a rule that sends every state to a new state.
So each letter is a map from the set of states to itself, and the machine is a set with a family of such maps.
That is exactly a unary algebra, so the tools of universal algebra, such as quotients and homomorphisms, apply directly to machines.
