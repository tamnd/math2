---
tag: BXVB6WCMEV
kind: definition
name: Gauge theory
msc: [81T13, 70S15, 53C07]
defines: 2GKJQNQMVN
uses: [GH6CXWFNDJ, 7JBRGCVJRB, 8E37E74XVP, NJ21PN5ZGJ, ZAJFW1S078, 707DEWCCFX, T0WAGV4KP4, SANYJGZ311]
sources:
  - url: https://en.wikipedia.org/wiki/Gauge_theory
---

## Definition

Let $(M, g)$ be an oriented [[pseudo-Riemannian manifold|GH6CXWFNDJ]] with volume form $\mathrm{vol}_g$.
Let $G$ be a [[Lie group|7JBRGCVJRB]] and let $P \to M$ be a [[principal $G$-bundle|8E37E74XVP]].
Let $\rho \colon G \to GL(V)$ be a finite-dimensional representation and let $E = P \times_\rho V$ be the associated vector bundle.
A *classical gauge theory* with gauge group $G$ on $P$ consists of the following data.

1. The fields are pairs $(A, \phi)$, where $A$ is a [[connection|NJ21PN5ZGJ]] on $P$ and $\phi$ is a section of $E$.
2. The [[action|T0WAGV4KP4]] is a functional $S(A, \phi) = \int_M \mathcal{L}(A, \phi) \, \mathrm{vol}_g$.
   Here the [[Lagrangian density|SANYJGZ311]] $\mathcal{L}$ at a point depends only on the [[curvature|ZAJFW1S078]] $F_A$, on $d_A \phi$ and on $\phi$ at that point.
3. The action is gauge invariant: $S(u \cdot A, u \cdot \phi) = S(A, \phi)$ for every element $u$ of the [[gauge group|707DEWCCFX]] $\mathcal{G}(P)$.

The field equations of the theory are the Euler–Lagrange equations of $S$.
The quantum gauge theory is the quantization of this classical theory.

## Remarks

Example: pure electromagnetism on Minkowski space.
Take $G = U(1)$, $P$ trivial and no field $\phi$.
A connection is $A = i a$ for a real $1$-form $a$, with curvature $F_A = i \, da$, and $S(A) = -\frac{1}{2} \int_M da \wedge \star da$.
A gauge transformation $u = e^{i\lambda}$ changes $a$ into $a + d\lambda$ up to a sign convention, and $da$ does not change, so clause 3 holds.
The field equations $d \star da = 0$, together with $d(da) = 0$, are [[Maxwell's equations|9BWWD4QK8Y]] in vacuum.

Non-example: add a mass term $\frac{m^2}{2} \int_M a \wedge \star a$ with $m > 0$, the Proca action.
Under $a \mapsto a + d\lambda$ this term changes, so clause 3 fails.
This is why the gauge field of an unbroken gauge symmetry is massless; a mass needs the [[Higgs mechanism|F985ZCF9SZ]].

When the curvature enters through $\frac{1}{2}\int_M \abs{F_A}^2 \mathrm{vol}_g$, the theory is a [[Yang–Mills theory|A0J2688KZF]].
In physics notation, $A$ is written as a Lie-algebra-valued $1$-form $A_\mu \, dx^\mu$ in a local trivialization, and $d_A \phi$ is written $D_\mu \phi$.
