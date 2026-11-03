---
tag: PSEAAC4MC0
kind: statement
role: theorem
name: Homotopy invariance of K-theory for regular rings
msc: [19D35, 19D50]
uses: [0670T59HGE, 0SDC934R52, BFFA03GE3V, 5GVFZWMWC8, YZSR4QKDQQ, DYV91576BQ, TV0GX7AQWT, 07C6ECNJET, 7N50GA46W1]
about: [5GVFZWMWC8]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Statement

Let $R$ be a regular ring, that is, a left [[Noetherian ring|0670T59HGE]] in which every finitely generated left module $M$ has a finite resolution.
Here the resolution of $M$ is by finitely generated [[projective modules|BFFA03GE3V]].
Let $R[t]$ be the [[polynomial ring|0SDC934R52]] in one central variable $t$ over $R$.
Then the inclusion $R \to R[t]$ induces isomorphisms
$$K_n(R) \xrightarrow{\ \cong\ } K_n(R[t])$$
of [[algebraic K-groups|5GVFZWMWC8]] for all $n \ge 0$.

## Remarks

Quillen proved that $G_n(R) \cong G_n(R[t])$ for every left Noetherian ring $R$, where $G_n$ is [[G-theory|YZSR4QKDQQ]], the K-theory of finitely generated modules.
If $R$ is regular, so is $R[t]$, and the [[resolution theorem|DYV91576BQ]] gives $K_n = G_n$ for both rings; this yields the statement.
By induction, $K_n(R) \cong K_n(R[t_1, \ldots, t_m])$ for all $m$.

Example: for a field $k$, $K_0(k[t_1, \ldots, t_m]) \cong \Z$ and $K_1(k[t_1, \ldots, t_m]) \cong k^\times$.
The first fact agrees with the [[Quillen–Suslin theorem|7N50GA46W1]], which says more: every finitely generated projective module over $k[t_1, \ldots, t_m]$ is free.

The regularity hypothesis is necessary.
Let $R = k[\varepsilon]/(\varepsilon^2)$ for a field $k$.
The element $1 + \varepsilon t$ is a [[unit|07C6ECNJET]] of $R[t]$, since $(1 + \varepsilon t)(1 - \varepsilon t) = 1$, but it is not in $R$.
For a commutative ring, the determinant $K_1 \to$ (units) is split surjective, so the class of $1 + \varepsilon t$ is not in the image of $K_1(R)$, and $K_1(R) \to K_1(R[t])$ is not onto.
The failure is measured by the groups [[$NK_n(R)$|TV0GX7AQWT]], the cokernels of $K_n(R) \to K_n(R[t])$.

## Explanations

### L1 human

Replacing a ring $R$ by the polynomial ring $R[t]$ is the algebraic analogue of multiplying a space by a line, which does not change its homotopy type.
The theorem says that K-theory does not see this change, as long as $R$ is regular, that is, has no singularities.
For a singular ring, nilpotent elements create new units in $R[t]$ and so new K-theory.

### L2 human

Homotopy invariance is why K-theory of regular schemes behaves like a cohomology theory in algebraic geometry, and it is one of the axioms behind motivic homotopy theory.
For non-regular rings, the defect $NK_n$ is the subject of the fundamental theorem of algebraic K-theory and of Bass's nil groups.
Forcing homotopy invariance on all rings leads to Karoubi–Villamayor K-theory and to Weibel's homotopy K-theory, which agree with $K$ on regular rings.
