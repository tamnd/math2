---
tag: MFN5GYZH5Z
kind: problem
name: P versus NP problem
msc: [68Q15, 68Q17]
uses: [GVT2NKN37K, QQRA9GBW51, JGZWHWA8P8, 3QKF32ZAKN, CTK8AH98Z1, 5HWR2NK8N1]
about: [GVT2NKN37K, QQRA9GBW51]
sources:
  - url: https://en.wikipedia.org/wiki/P_versus_NP_problem
same_as:
  wikidata: Q746242
  wikipedia: P versus NP problem
history:
  posed_by: "Stephen Cook"
  first_stated: "1971"
---

## Problem

Let [[P|GVT2NKN37K]] be the class of languages decided by deterministic Turing machines in polynomial time.
Let [[NP|QQRA9GBW51]] be the class of languages decided by nondeterministic Turing machines in polynomial time.
The problem asks whether $\mathrm{P} = \mathrm{NP}$.

## Remarks

The problem is open.
It is one of the seven Millennium Prize Problems of the Clay Mathematics Institute.
The inclusion $\mathrm{P} \subseteq \mathrm{NP}$ is easy, so the question is whether every language in NP lies in $\mathrm{P}$.
By the [[Cook–Levin theorem|CTK8AH98Z1]], $\mathrm{P} = \mathrm{NP}$ holds exactly when [[SAT|3QKF32ZAKN]] lies in $\mathrm{P}$.
More generally, it holds exactly when some [[NP-complete|JGZWHWA8P8]] problem lies in $\mathrm{P}$.
If $\mathrm{P} = \mathrm{NP}$, then NP is closed under complement, so NP equals [[co-NP|5HWR2NK8N1]].
Most researchers expect that $\mathrm{P} \ne \mathrm{NP}$.
Several known proof methods cannot settle the question, among them relativization, natural proofs and algebrization.

## Explanations

### L1 human

Some problems have solutions that are easy to check, like a filled Sudoku grid.
The question is whether every such problem also has solutions that are easy to find.
"Easy" means that a computer can do it in time bounded by a polynomial in the size of the input.
A yes answer would mean fast algorithms for scheduling, routing, protein folding and the breaking of most public-key cryptography.
A no answer would show that some checking tasks are truly easier than the matching search tasks.
