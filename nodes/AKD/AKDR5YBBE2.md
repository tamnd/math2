---
tag: AKDR5YBBE2
kind: statement
role: theorem
name: Rice's theorem
msc: [03D25, 03D20]
uses: [KZSB5E471K, PPGD5KW8JC, MFJXPAF0R0]
about: [KZSB5E471K, PPGD5KW8JC]
sources:
  - url: https://en.wikipedia.org/wiki/Rice's_theorem
same_as:
  wikidata: Q1893717
  wikipedia: Rice's theorem
---

## Statement

Fix a standard [[Gödel numbering|MFJXPAF0R0]] of programs, and let $\varphi_e$ be the partial [[computable function|KZSB5E471K]] of one argument computed by program $e$.
Let $\mathcal P$ be a set of partial computable functions $\N \rightharpoonup \N$ that is neither empty nor the set of all partial computable functions.
Then the index set $\set{e \in \N : \varphi_e \in \mathcal P}$ is not a [[computable set|PPGD5KW8JC]].

## Remarks

Replacing $\mathcal P$ by its complement if needed, assume the empty function is not in $\mathcal P$, and pick $\psi \in \mathcal P$.
For each $e$, let $g(e)$ be a program that on input $y$ first runs program $e$ on input $e$, and then, if that halts, computes $\psi(y)$.
By the [[smn theorem|YWX4FCFPAP]], $g$ is total computable.
Then $\varphi_{g(e)} = \psi$ if program $e$ halts on $e$, and $\varphi_{g(e)}$ is the empty function otherwise.
So a decision procedure for the index set would decide the [[halting problem|Z7TN2B35B0]].

Example: the set of programs that compute a total function, and the set of programs that output $0$ on input $0$, are not computable.

Both conditions on $\mathcal P$ are needed: if $\mathcal P$ is empty or contains all partial computable functions, the index set is $\emptyset$ or $\N$, which are computable.
The theorem concerns properties of the computed function, not of the program text.
A property such as "the program has fewer than $10$ instructions" is decidable.

## Explanations

### L1 human

Rice's theorem says that no algorithm can decide any interesting property of what programs do.
"Interesting" means that some programs have the property and some do not, and that it depends only on the input-output behaviour.
So no tool can decide, for every program, whether it ever prints $0$ or whether it computes the squaring function.

### L2 human

The theorem generalises the undecidability of the [[halting problem|Z7TN2B35B0]] to all non-trivial semantic properties.
Its proof is a many-one reduction from the halting set, built with the smn theorem.
The Rice–Shapiro theorem goes further and describes which index sets are computably enumerable.
In practice, program analysis tools work around the theorem by giving approximate answers.
