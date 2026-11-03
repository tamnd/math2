---
tag: AGHWGCM8GY
kind: definition
name: NP-hardness
msc: [68Q17, 68Q15]
defines: MHA48AWBXN
uses: [QQRA9GBW51, V0K79AD81V, 5MFZ4VNY6D]
sources:
  - url: https://en.wikipedia.org/wiki/NP-hardness
---

## Definition

Let $\Sigma$ be a finite alphabet, and let $H \subseteq \Sigma^*$ be a [[language|5MFZ4VNY6D]].
The language $H$ is *NP-hard* when $A \le_p H$ for every $A \in \mathrm{NP}$.
Here NP is the class [[NP|QQRA9GBW51]], and $\le_p$ is [[polynomial-time reducibility|V0K79AD81V]].

## Remarks

Example: the halting problem $\mathrm{HALT}$, the set of pairs $(M, w)$ such that the Turing machine $M$ halts on input $w$, is NP-hard.
Let $A \in \mathrm{NP}$, decided by a nondeterministic machine $N$.
Let $M_N$ be a deterministic machine that simulates all branches of $N$ on its input, halts if some branch accepts, and loops forever otherwise.
Map $w$ to $(M_N, w)$.
Since $M_N$ is fixed, this map is computable in polynomial time, and $w \in A$ exactly when $M_N$ halts on $w$.
So $A \le_p \mathrm{HALT}$, though $\mathrm{HALT}$ is not decidable and so not in NP.

Non-example: the empty language is not NP-hard.
Reducing a language $A$ to it needs $f(x) \in \emptyset$ for $x \in A$, so only $A = \emptyset$ reduces to it, while NP contains nonempty languages.

Since $\le_p$ is transitive, a language is NP-hard as soon as some NP-hard language reduces to it.
Some authors use Cook reductions instead of Karp reductions in this definition.
