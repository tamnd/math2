---
tag: 3QKF32ZAKN
kind: problem
name: Boolean satisfiability problem
msc: [68Q17, 03B05]
uses: [09K9MWD2QQ, QN7M1JCGT9, 0B3D4C8YF2, QQRA9GBW51, GVT2NKN37K]
about: [QN7M1JCGT9]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_satisfiability_problem
same_as:
  wikidata: Q875276
  wikipedia: Boolean satisfiability problem
history:
  posed_by: "Stephen A. Cook"
  first_stated: "1971"
  notes: "Cook proved that the problem is NP-complete; Leonid Levin found the same result independently."
---

## Problem

Let $x_1, \dots, x_n$ be propositional variables.
An input is a formula $\varphi$ of [[propositional logic|09K9MWD2QQ]] in the variables $x_1, \dots, x_n$, written as a string over a finite alphabet.
The *Boolean satisfiability problem* SAT asks whether $\varphi$ is [[satisfiable|QN7M1JCGT9]].
That is, it asks whether some assignment of the values true and false to $x_1, \dots, x_n$ makes $\varphi$ true.
Often the input is restricted to formulas in [[conjunctive normal form|0B3D4C8YF2]], a conjunction of clauses, each a disjunction of literals.
For $k \ge 1$, the problem $k$-SAT is SAT for formulas in conjunctive normal form whose clauses have at most $k$ literals.

## Remarks

SAT lies in [[NP|QQRA9GBW51]], since a satisfying assignment is a certificate that can be checked in time polynomial in the length of $\varphi$.
By the Cook–Levin theorem, SAT is NP-complete, and so is 3-SAT.
In contrast, 2-SAT lies in [[P|GVT2NKN37K]]: it reduces to finding strongly connected components of a directed graph built from the clauses.
Trying all $2^n$ assignments decides SAT, and no algorithm is known that runs in polynomial time on all inputs.
Modern SAT solvers, based on backtracking with clause learning, nevertheless solve many large instances from practice.

Example: $(x_1 \lor \neg x_2) \land (\neg x_1 \lor x_2) \land (x_1 \lor x_2)$ is satisfiable, with $x_1$ and $x_2$ both true.
The formula $x_1 \land \neg x_1$ is not satisfiable.

## Explanations

### L1 human

A formula built from yes-or-no variables with "and", "or" and "not" is given.
The question is whether the variables can be set so that the whole formula comes out true.
With $n$ variables there are $2^n$ settings to try, which grows very fast.
SAT was the first problem shown to be NP-complete, and it is the starting point for most proofs that other problems are hard.
