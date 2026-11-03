---
tag: STBEEGVS59
kind: problem
name: Milloux problem
msc: [31A15, 30C85]
uses: [CFD7BPM51W, EGRH1KN03C, 8G5ABXRK85, NJQ196M1WR]
about: [CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
history:
  posed_by: Henri Milloux
  first_stated: "1924"
---

## Problem

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]] and let $0 < r < 1$.
Consider the [[continua|NJQ196M1WR]] $E \subseteq \overline{\mathbb{D}}$ with $0 \notin E$ that meet both the circle $\abs{z} = r$ and the circle $\abs{z} = 1$.
For such $E$, let $\Omega_E$ be the component of $\mathbb{D} \setminus E$ that contains $0$.
Let $\omega(0, E)$ be the [[harmonic measure|EGRH1KN03C]] at $0$ of $E \cap \partial\Omega_E$ with respect to $\Omega_E$.
Find the infimum of $\omega(0, E)$ over all such $E$, and the continua at which it is attained.

## Remarks

The problem arose in Milloux's work on Picard's theorem and on families of holomorphic functions.
There it was posed as a bound for analytic functions, and the form above is its version in terms of harmonic measure.
It was solved by Beurling in his 1933 thesis.
The answer is that the radial segment $[r, 1]$ is extremal:
$$\omega(0, E) \ge \omega(0, [r, 1]) = 1 - \frac{4}{\pi} \arctan \sqrt{r} = \frac{2}{\pi} \arcsin \frac{1 - r}{1 + r}.$$
The inequality follows from [[Beurling's projection theorem|DDV6E39VSX]]: the circular projection $E^*$ of such a connected $E$ onto the positive radius contains $[r, 1]$.
So $\omega(0, E) \ge \omega(0, E^*) \ge \omega(0, [r, 1])$, the last step because harmonic measure grows when the set grows.
The value for the slit is computed by a conformal map of $\mathbb{D} \setminus [r, 1]$ onto a half-disc or a disc.

## Explanations

### L1 human

Put a connected obstacle in a round room, reaching from the wall to within distance $r$ of the centre.
Release a random walker at the centre.
The question asks which shape of obstacle the walker is least likely to hit before it reaches the wall.
The answer is a straight slit along a radius: any bending or spreading of the obstacle makes it easier to hit.
