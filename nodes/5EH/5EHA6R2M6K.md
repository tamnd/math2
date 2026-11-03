---
tag: 5EHA6R2M6K
kind: problem
name: Constraint satisfaction problem
msc: [68Q17, 68Q25]
uses: [052JJ9YVNM, GVT2NKN37K, JGZWHWA8P8, QQRA9GBW51]
about: [052JJ9YVNM]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
same_as:
  wikidata: Q1128326
  wikipedia: Constraint satisfaction problem
history:
  posed_by: "Ugo Montanari"
  first_stated: "1974"
  notes: "Montanari introduced networks of constraints in 1974."
---

## Problem

Let $D$ be a finite set, the domain.
Let $\Gamma$ be a finite set of relations on $D$, each a subset of $D^k$ for some arity $k \ge 1$.
An instance of $\mathrm{CSP}(\Gamma)$ consists of a finite set $V$ of variables and a finite list of constraints.
Each constraint is a pair $((v_1, \dots, v_k), R)$ with $v_1, \dots, v_k \in V$ and $R \in \Gamma$ of arity $k$.
The *constraint satisfaction problem* $\mathrm{CSP}(\Gamma)$ asks whether some map $s \colon V \to D$ satisfies every constraint, that is, $(s(v_1), \dots, s(v_k)) \in R$ for each constraint.

## Remarks

Every $\mathrm{CSP}(\Gamma)$ lies in [[NP|QQRA9GBW51]], since an assignment $s$ is a certificate.
Equivalently, $\mathrm{CSP}(\Gamma)$ asks whether a given finite relational structure has a [[homomorphism|052JJ9YVNM]] to the fixed structure $(D; \Gamma)$.

Example: let $D = \set{1, 2, 3}$ and $\Gamma = \set{\ne}$, the relation of distinct pairs.
Then an instance is a graph, with one constraint for each edge, and $\mathrm{CSP}(\Gamma)$ is graph $3$-colouring, which is [[NP-complete|JGZWHWA8P8]].
With $D = \set{1, 2}$ instead, the problem is $2$-colouring, which lies in [[P|GVT2NKN37K]].

Schaefer's dichotomy theorem of 1978 settles the case $\abs{D} = 2$.
Tomás Feder and Moshe Vardi conjectured in 1993 that for every finite $D$ and $\Gamma$, $\mathrm{CSP}(\Gamma)$ is in P or NP-complete.
Andrei Bulatov and Dmitriy Zhuk proved this conjecture independently in 2017.

## Explanations

### L1 human

Many puzzles have the form: give each variable a value from a fixed list so that a set of rules holds.
Sudoku, map colouring and timetabling all fit this pattern.
The rules may only use relations from a fixed list, and the question is whether all rules can hold at once.
Which lists of relations make the puzzle easy, and which make it hard, is a main question of the area.
