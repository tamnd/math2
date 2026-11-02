---
tag: DJMXZX0G9G
kind: definition
name: Oracle machine
msc: [03D10, 03D30]
defines: Z5CCVBME2V
uses: [758EYCN27B]
sources:
  - url: https://en.wikipedia.org/wiki/Oracle_machine
---

## Definition

An *oracle machine* is a [[Turing machine|758EYCN27B]] with these extra parts:

1. a second tape, the *oracle tape*, on which the machine can read and write;
2. three special states: a *query state* $q_?$, a *yes state* $q_{\mathrm{yes}}$ and a *no state* $q_{\mathrm{no}}$.

Let $O \subseteq \N$ be a set, the *oracle*.
The machine $M$ *with oracle* $O$, written $M^O$, runs like a Turing machine, except at the query state.
Suppose $M^O$ enters $q_?$ while the oracle tape holds the binary code of a number $n$.
Then its next state is $q_{\mathrm{yes}}$ if $n \in O$ and $q_{\mathrm{no}}$ if $n \notin O$.
A partial function $f \colon \N \to \N$ is *computable relative to* $O$ if there is an oracle machine $M$ with this property.
For every $x$, the run of $M^O$ on input $x$ halts with output $f(x)$ when $f(x)$ is defined, and does not halt otherwise.

## Remarks

Example: let $M$ copy its input $x$ to the oracle tape, enter $q_?$, and then output $1$ from $q_{\mathrm{no}}$ and $0$ from $q_{\mathrm{yes}}$.
For each oracle $O$, the machine $M^O$ halts on every input and computes the characteristic function of $\N \setminus O$.

Non-example: a device that may query two sets $O_1$ and $O_2$ is not an oracle machine, because an oracle machine queries one fixed set.
It can be simulated by an oracle machine with the single oracle $\set{2n : n \in O_1} \cup \set{2n + 1 : n \in O_2}$.

A machine that never enters $q_?$ is an ordinary Turing machine, so every computable function is computable relative to every oracle.
Oracle machines can be listed effectively as $M_0, M_1, \ldots$, and $\Phi_e^O$ often denotes the partial function computed by $M_e^O$.
