---
tag: WQJQBFBSC8
kind: definition
name: Arthur–Merlin protocol
msc: [68Q10, 68Q15, 68Q87]
defines: 289YQN382E
uses: [7PFQZJF1DX, GVT2NKN37K, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/Arthur–Merlin_protocol
---

## Definition

An *Arthur–Merlin protocol* is an [[interactive proof system|7PFQZJF1DX]] of the following kind.
Every message of the verifier, Arthur, is a fresh uniform random string.
Arthur's final decision is a deterministic polynomial-time function of the input and all messages.
The prover is called Merlin.

Let $L \subseteq \set{0,1}^*$ be a language.
In the conditions below, $r$ is uniform in $\set{0,1}^{q(\abs{x})}$ and $m$ ranges over $\set{0,1}^{q(\abs{x})}$.
The language $L$ is in the class *AM* if there are a polynomial $q$ and a language $R$ in [[P|GVT2NKN37K]] such that:

1. if $x \in L$, then $\Pr_r[\exists m \ (x, r, m) \in R] \ge 2/3$;
2. if $x \notin L$, then $\Pr_r[\exists m \ (x, r, m) \in R] \le 1/3$.

The class *MA* is defined in the same way with Merlin's message first.
So $L \in \mathrm{MA}$ if there are $q$ and $R$ as above with the following two properties.
If $x \in L$, then $\exists m \ \Pr_r[(x, r, m) \in R] \ge 2/3$.
If $x \notin L$, then $\forall m \ \Pr_r[(x, r, m) \in R] \le 1/3$.

## Remarks

Example: every language in NP is in MA, and so in AM.
If $x \in L$ if and only if $\exists m \ (x, m) \in R_0$ with $R_0 \in \mathrm{P}$, let $R = \set{(x, r, m) : (x, m) \in R_0}$, which ignores $r$; both clauses hold with probabilities $1$ and $0$.

Non-example: the protocol for graph non-isomorphism in which Arthur hides his choice of graph is not an Arthur–Merlin protocol, because its random bits are private.
Graph non-isomorphism is nevertheless in AM, through a different protocol based on set lower bounds with hash functions.

Babai showed that every protocol with a constant number of rounds of public coins gives the class AM.
Goldwasser and Sipser showed that private coins can be replaced by public coins with two more rounds, so the classes defined by a constant number of rounds coincide with AM.
