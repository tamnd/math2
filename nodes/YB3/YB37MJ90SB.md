---
tag: YB37MJ90SB
kind: statement
role: theorem
name: Fundamental theorem of algebraic K-theory
msc: [19D35, 19D50]
uses: [0B1261B5ED, 5GVFZWMWC8, TV0GX7AQWT, 0SDC934R52, QMY5JTZZB8, 63XXTF6B5M]
about: [5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebraic_K-theory
same_as:
  wikidata: Q17015004
  wikipedia: Fundamental theorem of algebraic K-theory
---

## Statement

Let $R$ be a [[ring|0B1261B5ED]] with identity, let $n \ge 1$, and let $K_n$ be Quillen's [[algebraic K-group|5GVFZWMWC8]].
Let $NK_n(R)$ be the [[NK group|TV0GX7AQWT]] of $R$.
Then there are natural isomorphisms
$$K_n(R[t]) \cong K_n(R) \oplus NK_n(R),$$
$$K_n(R[t, t^{-1}]) \cong K_n(R) \oplus K_{n-1}(R) \oplus NK_n(R) \oplus NK_n(R),$$
for the [[polynomial ring|0SDC934R52]] $R[t]$ and the [[Laurent polynomial ring|QMY5JTZZB8]] $R[t, t^{-1}]$.
If $R$ is Noetherian and every localization of $R$ at a prime ideal is a [[regular local ring|63XXTF6B5M]], then $NK_n(R) = 0$, and so
$$K_n(R[t]) \cong K_n(R), \qquad K_n(R[t, t^{-1}]) \cong K_n(R) \oplus K_{n-1}(R).$$

## Remarks

For regular $R$, Quillen's proof goes through G-theory: the groups $G_n$ of finitely generated modules satisfy $G_n(R[t]) \cong G_n(R)$, and they agree with $K_n$ for regular rings.
The localization sequence for inverting $t$ in $R[t]$ then splits, because the multiplication by $t$ gives a section.
The case of general rings was proved later, for example by Grayson.

For $n = 1$ the statement is the Bass–Heller–Swan theorem.
Example: for a field $F$ and $n = 1$, it gives $K_1(F[t, t^{-1}]) \cong F^\times \oplus \Z$, the units $c t^m$ of $F[t, t^{-1}]$.

The regularity hypothesis is needed for the second pair of formulas.
For $R = k[\varepsilon]/(\varepsilon^2)$ over a field $k$, the class of the unit $1 + \varepsilon t$ is a nonzero element of $NK_1(R)$, so $K_1(R[t]) \ne K_1(R)$.

With Bass's negative K-groups, the same formulas hold for every integer $n$.

## Explanations

### L1 human

The theorem says what happens to K-theory when one adds a variable $t$, or a variable $t$ together with its inverse.
For nice rings, adding $t$ changes nothing, and adding $t$ and $t^{-1}$ adds a copy of the K-group one degree lower.
For other rings there are correction terms, the NK groups.

### L2 human

The formula for $R[t, t^{-1}]$ is the algebraic analogue of the formula for the K-theory of a product with a circle.
Applied repeatedly, it computes the K-theory of $R[t_1^{\pm 1}, \ldots, t_m^{\pm 1}]$ for regular $R$, which is needed for the K-theory of group rings of free abelian groups.
It is also the starting point of Bass's negative K-theory and of homotopy-invariant versions of K-theory.
