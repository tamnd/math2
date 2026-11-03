---
tag: W78WHCMS03
kind: definition
name: Conjugate beam method
msc: [74K10, 74G05]
defines: FCGFMFM68F
uses: [13FGKM7NQ0, Q6XAPXMGH0, KQPKN2D1R9]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugate_beam_method
---

## Definition

Let a real beam occupy $0 \le x \le L$ and follow the [[Euler–Bernoulli beam equation|13FGKM7NQ0]] with bending stiffness $EI(x)$.
Let it have [[bending moment|Q6XAPXMGH0]] $M(x)$ and deflection $w(x)$ in the direction of the load, so that $w'' = -M/(EI)$.
The *conjugate beam* is a beam of the same length with these properties.

1. It carries the distributed load $\bar q(x) = M(x)/(EI(x))$.
2. Its supports are changed from those of the real beam.
   A clamped end becomes a free end, and a free end becomes a clamped end.
   A simply supported end stays simply supported.
   An interior support becomes an internal hinge, and an internal hinge becomes an interior support.

The *conjugate beam method* computes the shear force $\bar V$ and bending moment $\bar M$ of the conjugate beam by statics, and uses
$$w'(x) = \bar V(x), \qquad w(x) = \bar M(x).$$

## Remarks

The rule works because $\bar M'' = -\bar q = -M/(EI) = w''$, and the support changes of clause 2 turn the conditions on $w$ and $w'$ into the same conditions on $\bar M$ and $\bar V$.
For example a clamped end has $w = w' = 0$, which for the conjugate beam reads $\bar M = \bar V = 0$, the conditions of a free end.

Example: a cantilever of length $L$, clamped at $x = 0$, with a force $P$ at $x = L$ has $M(x) = -P(L - x)$.
The conjugate beam is free at $0$ and clamped at $L$, and carries a triangular load of total size $PL^2/(2EI)$ whose centroid is at distance $2L/3$ from $x = L$.
Its moment at the clamped end has size $PL^2/(2EI) \cdot 2L/3 = PL^3/(3EI)$, which is the tip deflection of the real beam.

Non-example: a conjugate beam with the same supports as a real cantilever would be clamped at $0$ and would give $w(0) \neq 0$ in general.
This contradicts the clamped end, so clause 2 is needed.

The conjugate beam of a statically determinate real beam is also determinate.
That of an indeterminate beam can be unstable as a structure but still in equilibrium under its load.
