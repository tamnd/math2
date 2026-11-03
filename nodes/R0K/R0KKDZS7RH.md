---
tag: R0KKDZS7RH
kind: definition
name: Reed–Frost model
msc: [92D30, 60J10]
defines: DG0ZDTRKHW
uses: [033TJBZDG0, 0VRWZDWW6B]
sources:
  - url: https://en.wikipedia.org/wiki/Reed%E2%80%93Frost_model
---

## Definition

Let $p \in (0, 1)$ be the probability of an infectious contact between a given infectious and a given susceptible host during one generation, and let $q = 1 - p$.
Let $S_0 \ge 0$ and $I_0 \ge 1$ be integers.
The *Reed–Frost model* is the [[Markov chain|033TJBZDG0]] $(S_t, I_t)_{t \ge 0}$ on pairs of nonnegative integers with the following rules.

1. $(S_0, I_0)$ is the initial state.
2. Given $(S_t, I_t)$, the number $I_{t+1}$ has the [[binomial distribution|0VRWZDWW6B]] with parameters $S_t$ and $1 - q^{I_t}$.
3. $S_{t+1} = S_t - I_{t+1}$.

Here $S_t$ is the number of susceptible hosts and $I_t$ the number of hosts infected in generation $t$, who are infectious during generation $t$ only.

## Remarks

The probability $1 - q^{I_t}$ is the chance that a susceptible host has an infectious contact with at least one of the $I_t$ infectious hosts, all contacts being independent.
The chain is absorbed when $I_t = 0$, and the final size is $S_0 - S_\infty$.

Example: take $S_0 = 2$ and $I_0 = 1$.
In generation $1$ the number of new cases is binomial with parameters $2$ and $p$.
So $P(I_1 = 0) = q^2$, $P(I_1 = 1) = 2 p q$ and $P(I_1 = 2) = p^2$.
If $I_1 = 1$, the last susceptible host is infected in generation $2$ with probability $p$.

Non-example: a model in which each susceptible host is infected with probability $p \, I_t$ is not the Reed–Frost model.
It fails clause 2, and the number $p \, I_t$ can even exceed $1$.

The Greenwood model is the variant in which the infection probability is $p$ whenever $I_t \ge 1$, independently of $I_t$.
