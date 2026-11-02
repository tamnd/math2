---
tag: K7MR77CHP6
kind: statement
role: theorem
name: Poincaré–Birkhoff theorem
msc: ["37E40", "37E30", 37J12]
uses: [0CW52NV5TC, 0QT00PB5G2, 2Z2QVWZ262, Y1YPE6PM52]
about: [0CW52NV5TC]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Birkhoff_theorem
same_as:
  wikidata: Q3527140
  wikipedia: Poincaré–Birkhoff theorem
---

## Statement

Let $A = (\R / \Z) \times [0, 1]$ be the closed [[annulus|0CW52NV5TC]], with the area measure $d\theta \, dr$ given by [[Lebesgue measure|2Z2QVWZ262]].
Let $f \colon A \to A$ be a [[homeomorphism|0QT00PB5G2]] such that:

1. $f$ preserves area.
2. $f$ maps each boundary circle $(\R / \Z) \times \set{0}$ and $(\R / \Z) \times \set{1}$ to itself.
3. $f$ twists the boundary circles in opposite directions: some lift $F \colon \R \times [0, 1] \to \R \times [0, 1]$ of $f$ to the [[universal cover|Y1YPE6PM52]], written $F(x, r) = (x + g(x, r), h(x, r))$, satisfies $g(x, 0) < 0 < g(x, 1)$ for all $x \in \R$.

Then $f$ has at least two fixed points.

## Remarks

Poincaré stated the theorem shortly before his death and checked many special cases, and Birkhoff published a proof in 1913.
Birkhoff's proof works with the lift $F$ on the strip $\R \times [0, 1]$.
The twist condition makes the horizontal displacement $g$ change sign between the two boundaries.
Area preservation then rules out the ways in which $F$ could still avoid a fixed point.
Applied to iterates $f^q$ and lifts shifted by integers $p$, the theorem gives periodic orbits of every rotation number $p/q$ between the rotation numbers of the two boundaries.
Area preservation is necessary: the map with lift $F(x, r) = (x + r - 1/2, r^2)$ satisfies 2 and 3, but a fixed point would need $r^2 = r$ and $r - 1/2 \in \Z$, which is impossible.
This map is not area preserving, since its Jacobian determinant is $2r$.

## Explanations

### L1 human

Picture a ring that is twisted so that its inner edge turns one way and its outer edge turns the other way.
If the twist does not squeeze or stretch any area, then at least two points of the ring end up exactly where they started.
The theorem is a basic tool for finding periodic motions in mechanics.

### L2 human

Area-preserving twist maps of an annulus arise as return maps of Hamiltonian systems with two degrees of freedom, for example near an elliptic periodic orbit or in billiards.
The theorem then produces infinitely many periodic orbits, one family for each rational rotation number in the twist interval.
It is a forerunner of symplectic topology: Arnold's conjecture on fixed points of Hamiltonian diffeomorphisms was proposed as a higher-dimensional generalisation.
