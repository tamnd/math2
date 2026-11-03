---
tag: HGV3FGKAVX
kind: definition
name: Model of computation
msc: [68Q04, 03D10]
defines: YFHEG4GYHW
uses: [RABRP2KG81, 1P6EP01HZF, 0SJ3RX9TXA]
sources:
  - url: https://en.wikipedia.org/wiki/Model_of_computation
---

## Definition

Let $\Sigma$ be an [[alphabet|RABRP2KG81]] and let $\Sigma^*$ be the [[set|0SJ3RX9TXA]] of [[strings|1P6EP01HZF]] over $\Sigma$.
A *model of computation* over $\Sigma$ consists of the following data.

1. A set $\mathcal M$ of machines, each given by a finite description.
2. For each machine $M \in \mathcal M$, a set $C_M$ of configurations, a start map $\mathrm{in}_M \colon \Sigma^* \to C_M$ and a step relation $\to_M$ on $C_M$.
3. For each $M$, a set $H_M \subseteq C_M$ of halting configurations, from which no step is possible, and a map $\mathrm{out}_M \colon H_M \to \Sigma^*$.

A run of $M$ on $w \in \Sigma^*$ is a sequence $c_0 \to_M c_1 \to_M \cdots$ with $c_0 = \mathrm{in}_M(w)$.
The model is *deterministic* if each configuration has at most one successor.
In that case $M$ computes the partial function $f_M \colon \Sigma^* \rightharpoonup \Sigma^*$ given as follows.
If the run on $w$ reaches a halting configuration $c_t$, then $f_M(w) = \mathrm{out}_M(c_t)$ and $t$ is the running time of $M$ on $w$.
Otherwise $f_M(w)$ is undefined.

## Remarks

Example: [[Turing machines|W6ESDYBF8Z]] form a deterministic model.
A configuration is a state, a tape content and a head position, the step relation is given by the transition function, and the output is the tape content at halting.
Non-example: a "machine" given by a table that lists an output for each of the infinitely many inputs is not allowed, because clause 1 requires a finite description.
The term is often used informally, and there is no single standard general definition; the one above covers the usual sequential models.
Circuit models use one circuit for each input length and do not fit this form directly.
