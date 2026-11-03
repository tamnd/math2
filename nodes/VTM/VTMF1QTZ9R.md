---
tag: VTMF1QTZ9R
kind: definition
name: PSPACE-completeness
msc: [68Q17, 68Q15]
defines: JWC9CE07Q2
uses: [T9NTRY93ZT, V0K79AD81V, 5MFZ4VNY6D, GVT2NKN37K, QQRA9GBW51]
sources:
  - url: https://en.wikipedia.org/wiki/PSPACE-complete
---

## Definition

Let $\Sigma$ be a finite alphabet, and let $C \subseteq \Sigma^*$ be a [[language|5MFZ4VNY6D]].
The language $C$ is *PSPACE-complete* when both conditions hold.

1. $C$ lies in the class [[PSPACE|T9NTRY93ZT]].
2. $A \le_p C$ for every $A \in \mathrm{PSPACE}$, where $\le_p$ is [[polynomial-time reducibility|V0K79AD81V]].

A language that satisfies condition 2 is called PSPACE-hard.

## Remarks

Example: the language TQBF of true fully quantified Boolean formulas, such as $\forall x \, \exists y \, (x \lor y) \land (\neg x \lor \neg y)$, is PSPACE-complete.
It lies in PSPACE because a recursive evaluation over the quantifiers reuses space and needs space polynomial in the formula.
Hardness comes from encoding a polynomial-space computation by a quantified formula.

Non-example: the empty language lies in PSPACE but fails condition 2.
Only the empty language reduces to it, while PSPACE contains nonempty languages.

Other PSPACE-complete problems are generalized geography and the universality of regular expressions, which asks whether a regular expression describes all strings.
If a PSPACE-complete language lies in [[P|GVT2NKN37K]], then $\mathrm{P} = \mathrm{PSPACE}$.
If one lies in [[NP|QQRA9GBW51]], then $\mathrm{NP} = \mathrm{PSPACE}$.
