---
tag: FZ25BQTKNT
kind: statement
role: theorem
name: Semistable reduction theorem
msc: [14H10, 14D06]
uses: [4JF1SGYZ5Y, XJM2MT4S3Y, 6W8TDV9VVN, H03GKRVBJ1, 9537RKBZPP, ZQ84M9D9TC, K0EQTBRPE3]
about: [XJM2MT4S3Y, NK9ATH4WB6]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_curve
---

## Statement

Let $R$ be a [[discrete valuation ring|4JF1SGYZ5Y]] with field of fractions $K$.
Let $C$ be a smooth projective geometrically connected [[curve|XJM2MT4S3Y]] over $K$ of [[genus|6W8TDV9VVN]] $g \ge 2$.
Then there are a finite separable extension $K'$ of $K$ and a discrete valuation ring $R' \subset K'$ with $R' \cap K = R$.
Moreover there is a stable curve $\mathcal{C}'$ over $R'$ whose generic fibre is isomorphic to $C \times_K K'$.

Here a *stable curve* over $R'$ is a [[proper|9537RKBZPP]] flat morphism $\mathcal{C}' \to \operatorname{Spec} R'$ with the following properties.
Its geometric fibres are connected reduced curves of [[arithmetic genus|H03GKRVBJ1]] $g$ whose only singularities are ordinary double points.
Each smooth rational component of a fibre meets the other components in at least $3$ points.

## Remarks

The theorem is due to Deligne and Mumford; one of their proofs deduces it from the semistable reduction of the [[Jacobian|ZQ84M9D9TC]] of $C$.
The stable model $\mathcal{C}'$ is unique up to isomorphism.
In terms of [[moduli of curves|NK9ATH4WB6]], it says that the moduli space $\overline{M}_g$ of stable curves satisfies the existence part of the valuative criterion of properness.
The extension of $K$ cannot be dropped in general.
The analogue for elliptic curves shows this: over $K = \Q_p$ with $p \ge 5$, the curve $y^2 = x^3 + p$ has additive reduction, so it has no semistable model over $\Z_p$.
Over $K' = \Q_p(\pi)$ with $\pi^6 = p$, the substitution $x = \pi^2 x'$, $y = \pi^3 y'$ gives $y'^2 = x'^3 + 1$, which has good reduction.

## Explanations

### L1 human

Take a family of smooth curves that degenerates at one point, like a family over a small disc whose central member is singular.
The theorem says that after a finite change of the parameter, one can replace the bad central curve by a mild one.
The mild curve may have several pieces, but they only cross each other in simple nodes.
So degenerations of smooth curves can always be tamed.

### L2 human

The theorem is the key input in the proof that $\overline{M}_g$ is proper.
The base change $K'/K$ is the arithmetic form of taking a root $t = s^n$ of the parameter.
For abelian varieties, the analogue is Grothendieck's semistable reduction theorem.
After a finite extension, the identity component of the special fibre of the [[Néron model|K0EQTBRPE3]] is an extension of an abelian variety by a torus.
