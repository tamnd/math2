---
tag: 7ZKBV18BFG
kind: problem
name: Word problem for an algebra
msc: [08A50, 03D40]
uses: [43M1WFPYGQ, AJNZJD8442, KZSB5E471K]
about: [43M1WFPYGQ]
sources:
  - url: https://en.wikipedia.org/wiki/Word_problem_(mathematics)
    locator: History
history:
  posed_by: "Axel Thue"
  first_stated: "1914"
---

## Problem

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of finite signature, and let $A = \langle X \mid R \rangle_{\mathcal{V}}$ be an algebra given by a finite [[presentation|43M1WFPYGQ]], with $X$ and $R$ finite.
The *word problem* for this presentation asks for an algorithm, that is, a [[computable function|KZSB5E471K]], with the following task.
For any two terms $s$ and $t$ over $X$, it decides whether $s$ and $t$ denote the same element of $A$.
The problem is *solvable* for $A$ if such an algorithm exists.
The *uniform word problem* for $\mathcal{V}$ asks for one algorithm that takes the finite presentation as part of its input.

## Remarks

Solvability does not depend on the choice of the finite presentation of $A$.
Suppose that $\mathcal{V}$ is finitely based.
Then the set of pairs $(s, t)$ with $s = t$ in $A$ is computably enumerable, by listing all derivations from $R$ and the identities of $\mathcal{V}$.
The difficulty is to certify that $s \neq t$.
The problem is unsolvable in general.
Markov and Post independently gave finitely presented semigroups with unsolvable word problem in 1947.
Novikov and Boone gave finitely presented groups with unsolvable [[word problem for groups|PBGTTAVMMT]].
It is solvable in many classes, for example for finitely presented abelian groups and for one-relator groups, the latter by a theorem of Magnus.
When the relations together with the identities of $\mathcal{V}$ can be oriented into a finite convergent rewriting system, normal forms solve it.

## Explanations

### L1 human

An algebra given by generators and relations is like a puzzle: different expressions may name the same element because the relations say so.
The word problem asks for a mechanical procedure that always tells whether two given expressions are equal.
For many familiar algebras such a procedure exists.
A famous discovery of the twentieth century is that for some finitely presented semigroups and groups no procedure can exist at all.
