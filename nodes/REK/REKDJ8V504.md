---
tag: REKDJ8V504
kind: definition
name: NP-completeness
msc: [68Q17, 68Q15]
defines: JGZWHWA8P8
uses: [QQRA9GBW51, MHA48AWBXN, V0K79AD81V, 5MFZ4VNY6D, GVT2NKN37K]
sources:
  - url: https://en.wikipedia.org/wiki/NP-completeness
---

## Definition

Let $\Sigma$ be a finite alphabet, and let $C \subseteq \Sigma^*$ be a [[language|5MFZ4VNY6D]].
The language $C$ is *NP-complete* when both conditions hold.

1. $C$ lies in the class [[NP|QQRA9GBW51]].
2. $C$ is [[NP-hard|MHA48AWBXN]], that is, $A \le_p C$ for every $A \in \mathrm{NP}$, where $\le_p$ is [[polynomial-time reducibility|V0K79AD81V]].

## Remarks

Example: the satisfiability problem SAT for propositional formulas is NP-complete, by the Cook–Levin theorem.
It lies in NP, since a satisfying assignment is a certificate that can be checked in polynomial time.

Non-example: the halting problem is NP-hard but not NP-complete.
It fails clause 1, since it is undecidable and every language in NP is decidable.

To show that a language $C$ in NP is NP-complete, it is enough to give $B \le_p C$ for one known NP-complete $B$, since $\le_p$ is transitive.
If some NP-complete language lies in [[P|GVT2NKN37K]], then $\mathrm{P} = \mathrm{NP}$.
