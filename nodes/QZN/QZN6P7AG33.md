---
tag: QZN6P7AG33
kind: statement
role: theorem
name: Valuative criterion
msc: [14A15]
uses: [JXRKH6P1Z4, ND6XEY68P4, AHTE5DVX61, X30G4V7VAJ, 9537RKBZPP, QSX12D8RQM, 0F2PTGX1A2, FB45BHHA2J]
about: [X30G4V7VAJ, 9537RKBZPP]
sources:
  - url: https://en.wikipedia.org/wiki/Valuative_criterion
same_as:
  wikidata: Q17104492
  wikipedia: Valuative criterion
---

## Statement

Let $f \colon X \to Y$ be a [[morphism|JXRKH6P1Z4]] [[of finite type|AHTE5DVX61]], where $X$ is a [[Noetherian scheme|ND6XEY68P4]].
Let $R$ be a [[valuation ring|QSX12D8RQM]] with [[field of fractions|0F2PTGX1A2]] $K$, and let $\operatorname{Spec}$ denote the [[spectrum|FB45BHHA2J]].
Let $i \colon \operatorname{Spec} K \to \operatorname{Spec} R$ be induced by the inclusion $R \subseteq K$.
Consider pairs of morphisms $u \colon \operatorname{Spec} K \to X$ and $v \colon \operatorname{Spec} R \to Y$ with $f \circ u = v \circ i$.
A *lift* of such a pair is a morphism $h \colon \operatorname{Spec} R \to X$ with $h \circ i = u$ and $f \circ h = v$.

1. $f$ is [[separated|X30G4V7VAJ]] if and only if, for all such $R$, every such pair has at most one lift.
2. $f$ is [[proper|9537RKBZPP]] if and only if, for all such $R$, every such pair has exactly one lift.

## Remarks

The space $\operatorname{Spec} R$ has a generic point and a closed point, so it is an algebraic picture of a small curve.
The space $\operatorname{Spec} K$ is that curve with its special point removed.
Existence of a lift says that a curve in $X$ that is defined except at one point extends over that point, so limits exist; uniqueness says that limits are unique.
For the proof, one realizes each specialization of points by a morphism from the spectrum of a valuation ring.
This turns the closedness of images into the existence of lifts.
For example, $\mathbb{A}^1_k \to \operatorname{Spec} k$ is not proper: with $R = k[t]_{(t)}$ and $u$ given by $x \mapsto 1/t$, there is no lift, since $1/t \notin R$.
In $\mathbb{P}^1_k$ the same point is $[1 : 1/t] = [t : 1]$, which does extend over $t = 0$.
If $Y$ is also Noetherian, then in both parts it suffices to use discrete valuation rings.

## Explanations

### L1 human

The criterion tests properness with small curves.
Take a curve in $X$ with one point punched out, lying over a full curve in $Y$.
The map is proper exactly when one can always fill in the missing point, and in exactly one way.
This is the algebraic form of the fact that a space is compact when every sequence has a limit point.

### L2 human

The definition of a proper morphism asks for universal closedness, which is hard to check directly.
The valuative criterion replaces it by a lifting problem that one can test on explicit rings.
It gives quick proofs that projective morphisms are proper and that properness is stable under composition and base change.
It also underlies the construction of compact moduli spaces, where one shows that a family over a punctured curve has a unique limit.
More general forms drop the Noetherian hypothesis and state the criterion for quasi-compact and quasi-separated morphisms.
