---
tag: HSP09EW4V3
kind: definition
name: Subtyping
msc: [68N15, 03B40]
defines: ZPAJ0MKY7Y
uses: [2DP940895E, AVVQEG0MRJ, 0VABYWJWH9]
sources:
  - url: https://en.wikipedia.org/wiki/Subtyping
---

## Definition

Consider a [[type system|AVVQEG0MRJ]] with a typing relation $\Gamma \vdash t : T$, such as the [[simply typed lambda calculus|2DP940895E]] extended with record types $\set{l_1 : T_1, \dots, l_n : T_n}$ with distinct labels $l_i$.
A *subtyping relation* is a relation $S <: T$ on types that is closed under these rules.

1. Reflexivity: $T <: T$.
2. Transitivity: if $S <: U$ and $U <: T$, then $S <: T$.
3. Functions: if $T_1 <: S_1$ and $S_2 <: T_2$, then $S_1 \to S_2 <: T_1 \to T_2$.
4. Records: $\set{l_1 : S_1, \dots, l_n : S_n} <: \set{k_1 : T_1, \dots, k_m : T_m}$ if each label $k_j$ equals some label $l_i$, and $S_i <: T_j$ for that $i$.

The type system is linked to $<:$ by the subsumption rule: if $\Gamma \vdash t : S$ and $S <: T$, then $\Gamma \vdash t : T$.
The relation $<:$ is usually taken to be the least relation closed under the rules, together with chosen relations between base types, such as $\mathsf{Int} <: \mathsf{Real}$.

## Remarks

Example: $\set{x : \mathsf{Int}, y : \mathsf{Int}} <: \set{x : \mathsf{Int}}$ by rule 4, since the label $x$ occurs on the left and $\mathsf{Int} <: \mathsf{Int}$ by rule 1.
So a function of type $\set{x : \mathsf{Int}} \to \mathsf{Int}$ may be applied to a point with two coordinates.

Non-example: with $\mathsf{Int} <: \mathsf{Real}$, one does not get $\mathsf{Int} \to \mathsf{Int} <: \mathsf{Real} \to \mathsf{Int}$.
Rule 3 would need $\mathsf{Real} <: \mathsf{Int}$, which fails; and indeed a function defined only on integers cannot accept every real.
The opposite inclusion $\mathsf{Real} \to \mathsf{Int} <: \mathsf{Int} \to \mathsf{Int}$ does hold.

By rules 1 and 2, subtyping is a [[preorder|0VABYWJWH9]] on types.
Rule 3 says that the arrow is contravariant in its argument and covariant in its result.
