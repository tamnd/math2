---
tag: K3WXSG7WBX
kind: definition
name: Satisfiability
msc: [03B05, 03B10]
defines: QN7M1JCGT9
uses: [09K9MWD2QQ, HYJ10AF6RT, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/Satisfiability
---

## Definition

1. A formula $\varphi$ of [[propositional logic|09K9MWD2QQ]] is *satisfiable* if some truth assignment to its variables gives $\varphi$ the value true.
2. Let $\sigma$ be a signature and $\varphi$ a first-order [[formula|HYJ10AF6RT]] over $\sigma$. Then $\varphi$ is *satisfiable* if there are a $\sigma$-[[structure|983GZBQYT4]] $M$ and an assignment $s$ of elements of $M$ to the variables with $M \models \varphi[s]$.
3. A set $\Gamma$ of formulas is *satisfiable* if one interpretation makes all formulas of $\Gamma$ true at once.

A formula or set that is not satisfiable is *unsatisfiable*.

## Remarks

The formula $(p \lor q) \land \neg p$ is satisfiable: the assignment $p = \mathsf{F}$, $q = \mathsf{T}$ makes both conjuncts true.
The set $\set{p, \; p \to q, \; \neg q}$ is unsatisfiable: if $p$ and $p \to q$ are true then $q$ is true, so $\neg q$ is false.
Each of its three formulas is satisfiable on its own, so clause 3 is stronger than satisfiability of each member.
A formula $\varphi$ is valid, for example a [[tautology|05006AJ7DZ]], exactly when $\neg \varphi$ is unsatisfiable.
