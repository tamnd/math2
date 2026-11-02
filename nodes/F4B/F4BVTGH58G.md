---
tag: F4BVTGH58G
kind: definition
name: Domain theory
msc: [06B35, 68Q55, 03B70]
defines: Q2P5D74Q1V
uses: [7TSXP95QN6, D9RY4667K6, RDM7J5J9HQ, C6GAHS1Z2P, ZR8A03FV67, 1SAAZG46DG, DBD64TH52D, BD756KR8FM]
sources:
  - url: https://en.wikipedia.org/wiki/Domain_theory
---

## Definition

Let $P$ be a [[directed-complete partial order|7TSXP95QN6]] and let $\ll$ be its [[way-below relation|RDM7J5J9HQ]].
The dcpo $P$ is a *continuous domain* if for every $x \in P$ the set $\set{y \in P : y \ll x}$ is [[directed|D9RY4667K6]] with supremum $x$.
It is an *algebraic domain* if for every $x \in P$ the set of compact elements below $x$ is directed with supremum $x$.
*Domain theory* is the study of continuous domains and related classes such as [[Scott domains|1SAAZG46DG]].
It studies them together with the [[Scott-continuous maps|C6GAHS1Z2P]] between them and their [[Scott topologies|ZR8A03FV67]].

## Remarks

Example: the interval $[0, 1]$ is a continuous domain that is not algebraic; $\set{y : y \ll x} = [0, x)$ for $x > 0$, with supremum $x$, while the only compact element is $0$.
Example: the partial functions from $\N$ to $\N$, ordered by extension, form an algebraic domain whose compact elements are the finite partial functions.
Non-example: the lattice of closed subsets of $[0, 1]$, ordered by inclusion, is a dcpo, but only $\varnothing$ is way below $[0, 1]$, so it is not a continuous domain.
A central tool is the [[least fixed point|DBD64TH52D]]: a Scott-continuous map $f$ on a pointed dcpo has the least fixed point $\bigvee_n f^n(\bot)$.
Such fixed points give the meaning of recursive programs and of terms of the [[lambda calculus|BD756KR8FM]].
