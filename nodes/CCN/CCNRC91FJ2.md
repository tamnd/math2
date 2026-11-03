---
tag: CCNRC91FJ2
kind: definition
name: Mealy machine
msc: [68Q45]
defines: BDWD5J39DJ
uses: [NDC0E9BZ94, RABRP2KG81, 1P6EP01HZF]
sources:
  - url: https://en.wikipedia.org/wiki/Mealy_machine
---

## Definition

A *Mealy machine* is a tuple $M = (Q, \Sigma, \Gamma, \delta, \lambda, q_0)$ where:

1. $(Q, \Sigma, \delta, q_0)$ is a [[finite-state machine|NDC0E9BZ94]], with finite set of states $Q$, input [[alphabet|RABRP2KG81]] $\Sigma$, transition function $\delta \colon Q \times \Sigma \to Q$ and initial state $q_0$;
2. $\Gamma$ is an alphabet, the *output alphabet*;
3. $\lambda \colon Q \times \Sigma \to \Gamma$ is the *output function*.

On an input [[string|1P6EP01HZF]] $a_1 a_2 \cdots a_n$ with $a_i \in \Sigma$, let $q_i = \delta(q_{i-1}, a_i)$ for $1 \le i \le n$.
The *output* of $M$ is the string $\lambda(q_0, a_1)\, \lambda(q_1, a_2) \cdots \lambda(q_{n-1}, a_n) \in \Gamma^*$.

## Remarks

Example: let $\Sigma = \Gamma = \set{0, 1}$ and $Q = \set{s, 0, 1}$ with $q_0 = s$.
Put $\delta(q, a) = a$ for all $q$ and $a$, $\lambda(s, a) = 0$, and $\lambda(q, a) = 1$ if $q = a$ and $0$ otherwise, for $q \in \set{0, 1}$.
The state after reading a nonempty word is its last bit, so on $0010$ the output is $0100$: a $1$ marks each bit equal to the bit before it.
Non-example: consider a machine that writes $1$ exactly when the number of $1$'s read so far is a perfect square.
It is not a Mealy machine, because no finite set of states can store the information it needs.
The output word always has the same length as the input word.
