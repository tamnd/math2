---
tag: AH8MBMD6FF
kind: definition
name: Moore machine
msc: [68Q45]
defines: 6VAZ66YNCA
uses: [NDC0E9BZ94, RABRP2KG81, 1P6EP01HZF, BDWD5J39DJ]
sources:
  - url: https://en.wikipedia.org/wiki/Moore_machine
---

## Definition

A *Moore machine* is a tuple $M = (Q, \Sigma, \Gamma, \delta, \lambda, q_0)$ where:

1. $(Q, \Sigma, \delta, q_0)$ is a [[finite-state machine|NDC0E9BZ94]], with finite set of states $Q$, input [[alphabet|RABRP2KG81]] $\Sigma$, transition function $\delta \colon Q \times \Sigma \to Q$ and initial state $q_0$;
2. $\Gamma$ is an alphabet, the *output alphabet*;
3. $\lambda \colon Q \to \Gamma$ is the *output function*.

On an input [[string|1P6EP01HZF]] $a_1 \cdots a_n$ with $a_i \in \Sigma$, let $q_i = \delta(q_{i-1}, a_i)$ for $1 \le i \le n$.
The *output* of $M$ is the string $\lambda(q_0)\, \lambda(q_1) \cdots \lambda(q_n) \in \Gamma^*$.

## Remarks

Example: let $\Sigma = \Gamma = \set{0, 1}$, $Q = \set{0, 1}$, $q_0 = 0$, $\delta(q, a) = q + a \bmod 2$ and $\lambda(q) = q$.
Then $q_i$ is the parity of the number of $1$'s among $a_1, \ldots, a_i$, and on $0110$ the output is $00100$.
Non-example: a machine with output function $\lambda \colon Q \times \Sigma \to \Gamma$, depending on the input symbol too, fails clause 3; it is a [[Mealy machine|BDWD5J39DJ]].
With this convention the output has length $n + 1$; some authors drop $\lambda(q_0)$ so that input and output have the same length.
A Moore machine gives a Mealy machine with the same states by setting $\lambda'(q, a) = \lambda(\delta(q, a))$; the converse needs, in general, up to $\abs{Q} \cdot \abs{\Gamma}$ states.
