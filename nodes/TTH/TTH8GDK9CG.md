---
tag: TTH8GDK9CG
kind: definition
name: Calculus of inductive constructions
msc: [03B38, 68V15, 03B40]
defines: JCX8X7VSQB
uses: [TKMY3F6KSA, Q80JWCWNKX, M6W6ZB4PPX]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_constructions
---

## Definition

The *calculus of inductive constructions* is the extension of the [[calculus of constructions|TKMY3F6KSA]] by the following features.

1. Sorts: an impredicative sort $\mathsf{Prop}$ and a hierarchy of universes $\mathsf{Type}_0, \mathsf{Type}_1, \mathsf{Type}_2, \dots$, with $\mathsf{Prop} : \mathsf{Type}_0$ and $\mathsf{Type}_i : \mathsf{Type}_{i+1}$ for each $i$.
2. Products: if $\Gamma \vdash A : s_1$ and $\Gamma, x : A \vdash B : \mathsf{Prop}$, then $\Pi x{:}A.\, B : \mathsf{Prop}$, for every sort $s_1$; if $A : \mathsf{Type}_i$ and $B : \mathsf{Type}_j$ in the extended context, then $\Pi x{:}A.\, B : \mathsf{Type}_{\max(i, j)}$.
   If $A : \mathsf{Prop}$ and $B : \mathsf{Type}_j$, then $\Pi x{:}A.\, B : \mathsf{Type}_j$.
3. Inductive definitions: declarations of [[inductive types|Q80JWCWNKX]] and inductive families in a sort, given by strictly positive constructors.
4. Elimination: for each inductive type, functions out of it are defined by case analysis on the constructors and by structurally recursive fixed points.
   The matching reduction rules are added to conversion.

## Remarks

Example: the natural numbers are the inductive type $\mathsf{nat} : \mathsf{Type}_0$ with $\mathsf{O} : \mathsf{nat}$ and $\mathsf{S} : \mathsf{nat} \to \mathsf{nat}$.
Addition is the fixed point with $\mathsf{plus}\ \mathsf{O}\ m = m$ and $\mathsf{plus}\ (\mathsf{S}\, n)\ m = \mathsf{S}\,(\mathsf{plus}\ n\ m)$, which is accepted because the recursive call is on the smaller argument $n$.

Non-example: the judgment $\mathsf{Type}_0 : \mathsf{Type}_0$ is not derivable; the universe $\mathsf{Type}_i$ only has type $\mathsf{Type}_{i+1}$.
A type of all types would make the system inconsistent by Girard's paradox.

Equality is itself an inductive family: for $A$ a type and $a : A$, the family $\mathsf{eq}\ A\ a$ over $A$ has the single constructor $\mathsf{eq\_refl} : \mathsf{eq}\ A\ a\ a$, a case of a [[dependent type|M6W6ZB4PPX]] defined inductively.
In the system used by Coq the universes are cumulative: a type in $\mathsf{Type}_i$ also lies in $\mathsf{Type}_{i+1}$.
Eliminations from inductive types in $\mathsf{Prop}$ into other sorts are restricted, to keep proofs irrelevant to computation.
