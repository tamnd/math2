---
tag: 7NNF74EYDX
kind: statement
role: theorem
name: Church–Rosser theorem
msc: [03B40, 68N18, 68Q42]
uses: [BD756KR8FM, Y9B9CVY6SJ, FPD6AN79QX]
about: [Y9B9CVY6SJ]
sources:
  - url: https://en.wikipedia.org/wiki/Church%E2%80%93Rosser_theorem
same_as:
  wikidata: Q1308502
  wikipedia: Church–Rosser theorem
---

## Statement

Let $M$, $N_1$ and $N_2$ be terms of the [[lambda calculus|BD756KR8FM]].
Let $\twoheadrightarrow_\beta$ denote multi-step [[beta reduction|Y9B9CVY6SJ]].
If $M \twoheadrightarrow_\beta N_1$ and $M \twoheadrightarrow_\beta N_2$, then there is a term $P$ such that $N_1 \twoheadrightarrow_\beta P$ and $N_2 \twoheadrightarrow_\beta P$.

## Remarks

The one-step relation $\to_\beta$ does not have this diamond property directly, because a step can duplicate or erase redexes.
The standard proof, due to Tait and Martin-Löf, uses parallel reduction, which contracts any set of existing redexes at once.
Parallel reduction has the diamond property, and its reflexive transitive closure equals $\twoheadrightarrow_\beta$, which gives the theorem.

Corollary: a term has at most one [[beta normal form|FPD6AN79QX]], up to renaming of bound variables.
If $M$ reduces to normal forms $N_1$ and $N_2$, the common reduct $P$ must equal both, since normal forms do not reduce.

Example: $M = (\lambda x.\, x\, x)((\lambda y.\, y)\, z)$ reduces to $N_1 = ((\lambda y.\, y)\, z)((\lambda y.\, y)\, z)$ and to $N_2 = (\lambda x.\, x\, x)\, z$.
Both reduce to $P = z\, z$.

A second corollary is consistency: $\lambda x.\, \lambda y.\, x$ and $\lambda x.\, \lambda y.\, y$ are distinct normal forms, so they are not $\beta$-convertible.
The theorem also holds for $\beta\eta$-reduction.

## Explanations

### L1 human

A lambda term can often be simplified in several places, so there are many ways to compute with it.
The theorem says that the choice never matters in the end.
Any two computations from the same start can always be brought back together.
So if a final answer exists, it is unique.

### L2 human

In rewriting language, the theorem says that $\beta$-reduction is confluent.
It implies that $M =_\beta N$ holds exactly when $M$ and $N$ have a common reduct.
This makes the equational theory of the lambda calculus consistent and gives unique values to programs.
Alonzo Church and J. Barkley Rosser proved it in 1936.
For terminating systems, confluence can also be reached through Newman's lemma from local confluence, but $\beta$-reduction is not terminating.
