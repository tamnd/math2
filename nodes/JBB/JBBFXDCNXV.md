---
tag: JBBFXDCNXV
kind: definition
name: Eleven-dimensional supergravity
msc: ["83E50", 81T60, "83E15"]
defines: CRHHG45BVB
uses: [VWBEWVT29C, 0E3G0GRPZ6, 004FRCXH6M, 1Y4WX4XQWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Eleven-dimensional_supergravity
---

## Definition

Let $M$ be an eleven-dimensional spin manifold.
*Eleven-dimensional supergravity* is the [[supergravity|VWBEWVT29C]] theory on $M$ whose fields are:

1. a vielbein $e^a{}_\mu$, giving a Lorentzian metric $g$;
2. one Majorana gravitino $\psi_\mu$, whose spinor index takes $32$ values;
3. a three-form gauge potential $A$, a [[differential form|0E3G0GRPZ6]] with field strength $F = dA$, where $d$ is the [[exterior derivative|004FRCXH6M]].

The bosonic part of its action is
$$S = \frac{1}{2\kappa^2} \int_M \left( R \, {\star 1} - \tfrac12 F \wedge {\star F} - \tfrac16 A \wedge F \wedge F \right).$$
Here $R$ is the scalar curvature of $g$, $\star$ is the [[Hodge star|1Y4WX4XQWJ]] of $g$ and $\kappa$ is the gravitational coupling.
The fermionic terms are fixed by local supersymmetry.
The signs and normalizations depend on conventions.

## Remarks

The gauge transformation $A \mapsto A + d\Lambda$, for a two-form $\Lambda$, leaves $F$ unchanged.
It changes the last term only by an exact form, so the action is gauge invariant on a closed $M$.
Counting physical degrees of freedom: the metric has $44$, the three-form has $\binom{9}{3} = 84$, and the gravitino has $128$, so there are $128$ bosonic and $128$ fermionic ones.
Example: $\mathrm{AdS}_4 \times S^7$ and $\mathrm{AdS}_7 \times S^4$, with $F$ proportional to the volume form of the four-dimensional factor, are solutions.
Non-example: dropping the term $A \wedge F \wedge F$ gives a bosonic theory that is no longer invariant under local supersymmetry.
