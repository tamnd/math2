---
tag: GWJWP187QE
kind: statement
role: theorem
name: Hironaka's resolution for complex spaces
msc: [32S45, "14E15"]
uses: [831N2Q4GCB, SB3MY7XQM9, JSGWAN2RJV, ZW5A88PCPK, 15XEBGNGHC, 0VQYCCQVJ5, MB52NDA6WN, C4KGYAFPN7, BP0ZYHGD0S]
about: [SB3MY7XQM9]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_of_singularities
---

## Statement

Let $X$ be a [[reduced complex space|831N2Q4GCB]] whose topology has a countable basis.
Let $X_{\mathrm{reg}}$ and $X_{\mathrm{sing}}$ be its sets of [[regular and singular points|ZW5A88PCPK]].
Then there are a [[complex manifold|JSGWAN2RJV]] $\tilde{X}$ and a [[proper|15XEBGNGHC]] surjective holomorphic map $\pi \colon \tilde{X} \to X$ such that:

1. $\pi$ restricts to a biholomorphic map $\pi^{-1}(X_{\mathrm{reg}}) \to X_{\mathrm{reg}}$;
2. $\pi^{-1}(X_{\mathrm{sing}})$ is [[nowhere dense|0VQYCCQVJ5]] in $\tilde{X}$.

In particular $\pi$ is a [[modification|SB3MY7XQM9]] of $X$, called a resolution of singularities.

## Remarks

Hironaka proved [[resolution of singularities|MB52NDA6WN]] for algebraic varieties over fields of characteristic $0$; the method was then carried over to complex spaces.
The resolution is built from a sequence of [[blow-ups|C4KGYAFPN7]] along smooth centres contained in the singular locus, chosen by a local invariant that drops at each step.
For a non-compact space infinitely many blow-ups may be needed, but they form a locally finite family, and the canonical choice of centres lets local resolutions glue.
The map can also be chosen so that $\pi^{-1}(X_{\mathrm{sing}})$ is a hypersurface with normal crossings.

Example: for a reduced curve, the [[normalization|BP0ZYHGD0S]] is a resolution; for the cusp $\set{z_1^2 = z_2^3}$ it is $t \mapsto (t^3, t^2)$ from $\C$.
For the cone $\set{z_1 z_2 = z_3^2}$ in $\C^3$, one blow-up of the vertex gives a resolution whose exceptional set is a projective line.

## Explanations

### L1 human

A singular complex space can be replaced by a smooth one that maps onto it and agrees with it away from the singular points.
Over the singular points, the smooth space may have whole curves or surfaces instead of single points.
So questions about singular spaces can often be moved to manifolds, where calculus is available.

### L2 human

Resolution is used to define invariants of singularities and to prove local estimates such as the Łojasiewicz inequality.
It also extends integration and Hodge theory to singular spaces, and reduces questions on plurisubharmonic functions and multiplier ideals to normal crossing situations.
The resolution is not unique: blowing up a point of $\tilde{X}$ over $X_{\mathrm{sing}}$ gives another one.
