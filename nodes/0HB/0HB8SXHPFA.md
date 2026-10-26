---
tag: 0HB8SXHPFA
kind: definition
name: Markov property
msc: [60J05]
defines: 0B77KZCQ51
uses: [0QH5ENKZM1, 0YAMJRK04E, 0ZJ87ZZ8PK]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_property
    locator: Markov property in general
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a probability space, let $T \subseteq [0, \infty)$, and let $(\mathcal{F}_t)_{t \in T}$ be a filtration: σ-algebras with $\mathcal{F}_s \subseteq \mathcal{F}_t \subseteq \mathcal{F}$ for $s \le t$.
Let $(X_t)_{t \in T}$ be a [[stochastic process|0QH5ENKZM1]] with values in $(S, \mathcal{S})$ such that each $X_t$ is $\mathcal{F}_t$-measurable.
The process has the Markov property with respect to $(\mathcal{F}_t)$ if, for all $s \le t$ in $T$ and each $A \in \mathcal{S}$,
$$P(X_t \in A \mid \mathcal{F}_s) = P(X_t \in A \mid X_s) \quad \text{almost surely}.$$

## Remarks

Here $P(B \mid \mathcal{G}) = E[1_B \mid \mathcal{G}]$ is a [[conditional expectation|0YAMJRK04E]].
For a discrete-time process with a countable state space and the natural filtration, the property becomes $P(X_{n+1} = j \mid X_0, \dots, X_n) = P(X_{n+1} = j \mid X_n)$. This defines a Markov chain.
The property says that the future is [[conditionally independent|0ZJ87ZZ8PK]] of the past, given the present.
The strong Markov property is the same statement with a stopping time in place of the fixed time $s$.

## Explanations

### L1 human

A process with the Markov property forgets how it reached its present state.
To predict its future, the present state is all the information that you need.
