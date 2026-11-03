---
tag: BHS6KYTZ6V
kind: definition
name: SK1
msc: [19B99, 19B28]
defines: AAB05HS00Y
uses: [0310REJJY8, SXVNJY4XFY, 07C6ECNJET, 00KDZRW4C0, 0V9PMN0RBH, E5JXB0E324]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
    locator: K1
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] with identity and let $R^\times$ be its [[group of units|07C6ECNJET]].
The [[determinant|00KDZRW4C0]] $\det \colon GL(R) \to R^\times$ vanishes on commutators, so it induces a homomorphism $\det \colon K_1(R) \to R^\times$ on [[K1 of a ring|SXVNJY4XFY]].
The group $SK_1(R)$ is its kernel:
$$SK_1(R) = \ker\bigl(\det \colon K_1(R) \to R^\times\bigr).$$

## Remarks

Equivalently, $SK_1(R) = SL(R)/E(R)$, where $SL(R)$ is the union of the [[special linear groups|0V9PMN0RBH]] $SL_n(R)$ and $E(R)$ is the [[elementary subgroup|E5JXB0E324]].
The map $u \mapsto [\mathrm{diag}(u, 1, 1, \dots)]$ splits $\det$, so $K_1(R) \cong R^\times \oplus SK_1(R)$.
Example: for a field $F$, row reduction writes each matrix of determinant $1$ as a product of elementary matrices, so $SK_1(F) = 0$.
Non-example: the definition needs $R$ commutative.
For a noncommutative ring such as a division ring there is no determinant with values in $R^\times$; one uses the Dieudonné determinant or the reduced norm instead.
For a central simple algebra $A$ over a field $F$, one sets $SK_1(A) = \ker(\mathrm{Nrd} \colon K_1(A) \to F^\times)$, where $\mathrm{Nrd}$ is the reduced norm.
