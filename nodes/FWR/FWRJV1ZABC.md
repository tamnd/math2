---
tag: FWRJV1ZABC
kind: definition
name: Kleene's T predicate
msc: [03D20]
defines: S9DK13K5PS
uses: [MFJXPAF0R0, HBK5QHC1GC, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Kleene's_T_predicate
---

## Definition

Fix a [[Gödel numbering|MFJXPAF0R0]] of the programs for [[partial recursive functions|HBK5QHC1GC]] of one argument.
Fix also a coding of finite sequences of natural numbers by natural numbers.
Let $\varphi_e$ denote the partial function computed by the program with number $e$.
*Kleene's T predicate* is the relation $T \subseteq \N^3$ defined as follows.
The triple $(e, x, c)$ is in $T$ if and only if the following holds.
The number $e$ is the number of a program, and $c$ codes a complete halting computation of that program on input $x$.
For each $k \ge 1$ there is a similar relation $T_k(e, x_1, \ldots, x_k, c)$ for programs with $k$ arguments.

## Remarks

Kleene's normal form theorem says two things.
First, $T$ is [[primitive recursive|5NVA2JRHPV]].
Second, there is a primitive recursive function $U$ such that $\varphi_e(x) \simeq U(\mu c \, T(e, x, c))$ for all $e$ and $x$.
Here $\simeq$ means that both sides are undefined, or both are defined and equal.

Example: if $e$ is a program for the successor function, then for each $x$ there is a $c$ with $T(e, x, c)$, and $U(c) = x + 1$ for the least such $c$.

Non-example: if $e$ is a program that never halts, then $T(e, x, c)$ fails for all $x$ and $c$, since no $c$ codes a halting computation.

The halting set $\set{e : \varphi_e(e) \text{ is defined}}$ equals $\set{e : \exists c \, T(e, e, c)}$, so it is $\Sigma^0_1$ in the [[arithmetical hierarchy|7CVJCQKY41]].
