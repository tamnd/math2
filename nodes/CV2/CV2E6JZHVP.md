---
tag: CV2E6JZHVP
kind: definition
name: Arithmetical hierarchy
msc: [03D55, 03F30]
defines: 7CVJCQKY41
uses: [HYJ10AF6RT, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetical_hierarchy
---

## Definition

Work in the first-order language of arithmetic with symbols $0$, $S$, $+$, $\cdot$ and $<$, interpreted in the standard model $\N$ of the [[natural numbers|0MWKJ44V5A]].
A bounded quantifier has the form $\exists x < t$ or $\forall x < t$, where $t$ is a term not containing $x$.
The classes of [[formulas|HYJ10AF6RT]] $\Sigma_n$ and $\Pi_n$ are defined by induction on $n$.

1. $\Sigma_0 = \Pi_0$ is the class of formulas in which every quantifier is bounded.
2. A formula is $\Sigma_{n+1}$ if it has the form $\exists x_1 \cdots \exists x_k \, \psi$ with $\psi$ in $\Pi_n$.
3. A formula is $\Pi_{n+1}$ if it has the form $\forall x_1 \cdots \forall x_k \, \psi$ with $\psi$ in $\Sigma_n$.

A set $A \subseteq \N^m$ is $\Sigma^0_n$ if $A = \set{\bar a : \N \models \varphi(\bar a)}$ for some $\Sigma_n$ formula $\varphi$, and $\Pi^0_n$ if the same holds with a $\Pi_n$ formula.
A set is $\Delta^0_n$ if it is both $\Sigma^0_n$ and $\Pi^0_n$.
A set is *arithmetical* if it is $\Sigma^0_n$ for some $n$.

## Remarks

Example: the halting set $K = \set{e : \exists c \, T(e, e, c)}$ is $\Sigma^0_1$, where $T$ is [[Kleene's T predicate|S9DK13K5PS]].
Every primitive recursive relation is $\Delta^0_1$, so $T$ is defined by a $\Sigma_1$ formula, and so is $K$.
The set $\set{e : \forall x \, \exists c \, T(e, x, c)}$ of programs computing total functions is $\Pi^0_2$.

Non-example: the set of Gödel numbers of sentences true in $\N$ is not arithmetical, by [[Tarski's undefinability theorem|YRV6SYK2BY]].

A set is $\Sigma^0_n$ if and only if its complement is $\Pi^0_n$.
The inclusions $\Sigma^0_n \cup \Pi^0_n \subseteq \Delta^0_{n+1}$ hold, and each is strict.
The classes $\Sigma^0_1$ and $\Delta^0_1$ are the computably enumerable and the computable sets.
