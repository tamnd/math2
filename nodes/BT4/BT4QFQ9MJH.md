---
tag: BT4QFQ9MJH
kind: definition
name: Tilting theory
msc: [16G10, "16E35"]
defines: XXYQV6R1PR
uses: [04C5ZBG1WT, 3CTW1P4HBP, MR9QCH1PNA, 4P7GBWJ4RR, E2P29GCD9T, G00C22AEDH, AWSBZWWMG9]
sources:
  - url: https://en.wikipedia.org/wiki/Tilting_theory
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $A$ be a finite-dimensional [[associative algebra|3CTW1P4HBP]] over $k$.
A finitely generated left $A$-module $T$ is a *tilting module* if:

1. the [[projective dimension|MR9QCH1PNA]] of $T$ is at most $1$;
2. $\operatorname{Ext}^1_A(T, T) = 0$, where $\operatorname{Ext}$ is the [[Ext functor|4P7GBWJ4RR]];
3. the number of isomorphism classes of [[indecomposable|E2P29GCD9T]] direct summands of $T$ equals the number of isomorphism classes of [[simple|G00C22AEDH]] $A$-modules.

*Tilting theory* studies the relation between $A$ and the [[endomorphism ring|AWSBZWWMG9]] $B = \End_A(T)$ of a tilting module $T$, through the functors $\Hom_A(T, \cdot)$ and $\operatorname{Ext}^1_A(T, \cdot)$.

## Remarks

Example: $T = A$ is a tilting module, since it is projective and its indecomposable summands are the indecomposable projectives, one for each simple module.
Example: let $A$ be the path algebra of $1 \to 2$, with $S_2 = P_2$, $P_1$ and $S_1$ as indecomposables, and let $T = P_1 \oplus S_1$.
The projective resolution $0 \to P_2 \to P_1 \to S_1 \to 0$ gives clause 1.
Clause 2 holds since $P_1$ is projective and injective and $\operatorname{Ext}^1_A(S_1, S_1) = 0$, and clause 3 holds with $2$ summands.
Non-example: $T = S_1 \oplus S_2$ fails clause 2, since the non-split sequence $0 \to S_2 \to P_1 \to S_1 \to 0$ gives $\operatorname{Ext}^1_A(S_1, S_2) \ne 0$.
Happel proved that for a tilting module $T$ the bounded derived categories of $\operatorname{mod} A$ and $\operatorname{mod} B$ are equivalent as triangulated categories.
