---
tag: DDV6E39VSX
kind: statement
role: theorem
name: Beurling's projection theorem
msc: [30C85, 31A15]
uses: [CFD7BPM51W, 8G5ABXRK85]
about: [CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Statement

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]] and let $E \subseteq \overline{\mathbb{D}}$ be a closed set with $0 \notin E$.
Let $E^* = \set{\abs{z} : z \in E} \subseteq (0, 1]$ be the circular projection of $E$ onto the positive radius.
For a closed set $A \subseteq \overline{\mathbb{D}}$ with $0 \notin A$, let $\Omega_A$ be the component of $\mathbb{D} \setminus A$ that contains $0$.
Let $\omega(0, A)$ be the [[harmonic measure|CFD7BPM51W]] of $A \cap \partial\Omega_A$ for $\Omega_A$ at the point $0$.
Then
$$\omega(0, E) \ge \omega(0, E^*).$$

## Remarks

The projection keeps, for each radius $r$, whether $E$ meets the circle $\abs{z} = r$, and squeezes the part of $E$ on that circle to a single point on the positive axis.
So among sets that meet the same circles, a radial slit is the hardest to hit from the centre.
Projecting onto any other radius gives the same value of $\omega(0, E^*)$, by rotation invariance.
Proofs use symmetrisation methods.
Example: if $E$ is a connected set that meets both circles $\abs{z} = r$ and $\abs{z} = 1$, then $E^* = [r, 1]$.
So $\omega(0, E)$ is at least the harmonic measure of the slit $[r, 1]$ in $\mathbb{D} \setminus [r, 1]$, which can be computed by a conformal map.
This gives Beurling's estimate that a Brownian path from $0$ hits $E$ before leaving the disc with probability bounded below in terms of $r$ only.

## Explanations

### L1 human

Place an obstacle inside a round room and release a random walker at the centre.
Compare obstacles that reach the same distances from the centre.
The theorem says that the obstacle squeezed onto a single radius is the one the walker is least likely to hit before it reaches the wall.
Spreading the obstacle around the circles can only make it easier to hit.

### L2 human

Beurling's projection theorem is a basic comparison tool for harmonic measure in the plane.
It gives lower bounds for the harmonic measure of connected sets.
These lead to estimates on the boundary behaviour of conformal maps and to Hölder bounds for harmonic measure of connected boundaries.
It is closely related to the Milloux problem, which asks for the same kind of extremal set.
