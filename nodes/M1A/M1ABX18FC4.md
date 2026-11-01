---
tag: M1ABX18FC4
kind: statement
role: theorem
name: Jordan–Hölder theorem for modules
msc: ["16D10", "13C05"]
uses: [0894J980RK, 09VDS2W1E8, 0RGZ10DFPG, V6JBKT168T]
about: [CZSCNZH8VY]
sources:
  - url: https://en.wikipedia.org/wiki/Composition_series
---

## Statement

Let $R$ be a [[ring|0894J980RK]] and let $M$ be a left [[module|09VDS2W1E8]] over $R$.
A simple module is a nonzero module with no submodules other than $0$ and itself.
A composition series of $M$ is a chain of [[submodules|0RGZ10DFPG]] $0 = M_0 \subsetneq M_1 \subsetneq \cdots \subsetneq M_n = M$ in which each quotient $M_i / M_{i-1}$ is simple.
Let $0 = M_0 \subsetneq \cdots \subsetneq M_n = M$ and $0 = N_0 \subsetneq \cdots \subsetneq N_m = M$ be two composition series of $M$.
Then $n = m$, and there is a permutation $\sigma$ of $\set{1, \dots, n}$ with $M_i / M_{i-1} \cong N_{\sigma(i)} / N_{\sigma(i) - 1}$ for each $i$.

## Remarks

The proof is by induction on the shortest length of a composition series, comparing the two series through the submodules $M_{n-1}$, $N_{m-1}$ and $M_{n-1} \cap N_{m-1}$.
So the number $n$ and the simple factors, counted with multiplicity, depend only on $M$; the number $n$ is the [[length|CZSCNZH8VY]] of $M$.
For example, $\Z/12\Z$ has the composition series $0 \subset 6\Z/12\Z \subset 3\Z/12\Z \subset \Z/12\Z$ and $0 \subset 6\Z/12\Z \subset 2\Z/12\Z \subset \Z/12\Z$, with factors $\Z/2\Z, \Z/2\Z, \Z/3\Z$ in different orders.
A module that has a composition series is exactly a module of finite length, and then every strict chain of submodules can be refined to a composition series.
The theorem for groups is the [[Jordan–Hölder theorem|0E088ZP533]]; both are cases of the Jordan–Hölder theorem for groups with operators, and the same proof works.

## Explanations

### L1 human

A module of finite length can be cut into simple layers in many ways.
The theorem says that the number of layers and the layers themselves are always the same, up to order.

### L2 human

The theorem makes the [[length of a module|CZSCNZH8VY]] well defined, and it lets one speak of the multiplicity of a simple module in $M$.
Lengths of modules such as $R/I$, for a Noetherian local ring $R$, are the input of Hilbert–Samuel functions and multiplicities.
In representation theory, the simple factors of a representation are its irreducible constituents, which are well defined by this theorem.
