---
tag: QMJ7C22FAG
kind: definition
name: Descriptive complexity theory
msc: [68Q19, 03C13, 68Q15]
defines: YRHZEF2JMZ
uses: [983GZBQYT4, PWHJZYBNEY, ESPYW94XGR, DKFGQTRYZE]
sources:
  - url: https://en.wikipedia.org/wiki/Descriptive_complexity_theory
---

## Definition

Let $\mathcal L$ be a logic and let $\mathcal C$ be a [[complexity class|ESPYW94XGR]].
Fix a finite relational [[signature|PWHJZYBNEY]] $\sigma$.
A finite $\sigma$-[[structure|983GZBQYT4]] is encoded as a binary string by listing the tuples of each relation for some ordering of its universe.
The logic $\mathcal L$ *captures* $\mathcal C$ if the following holds for every $\sigma$ and every class $K$ of finite $\sigma$-structures that is closed under isomorphism.

The class $K$ belongs to $\mathcal C$ if and only if some $\mathcal L$-[[sentence|DKFGQTRYZE]] $\varphi$ defines $K$.
This means that a finite $\sigma$-structure is in $K$ exactly when it satisfies $\varphi$.

*Descriptive complexity theory* is the study of which logics capture which complexity classes.

## Remarks

Example: existential second-order logic captures NP, by Fagin's theorem.
For instance, the class of $3$-colorable graphs is in NP, and it is defined by an existential second-order sentence that guesses three color classes.

Non-example: first-order logic does not capture the class P.
Over the empty signature, the class of finite sets with an even number of elements can be decided in polynomial time.
Yet no first-order sentence defines it, as one shows with Ehrenfeucht–Fraïssé games.

On ordered structures, where $\sigma$ contains a linear order, first-order logic with a least fixed point operator captures P (Immerman and Vardi).
Whether some logic captures P on all finite structures is a major open question.
