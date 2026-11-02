---
tag: QQEASX79RW
kind: counterexample
name: Alexander horned sphere
msc: [57M30, 57N45]
uses: [3VX06XRVZG, T62369RFH6, 00ZG9Y9TR4, S1XK3HXHFX]
sources:
  - url: https://en.wikipedia.org/wiki/Alexander_horned_sphere
same_as:
  wikidata: Q1361755
  wikipedia: Alexander horned sphere
---

## Counterexample

The Alexander horned sphere is a subset $\Sigma \subset \R^3$ built by an infinite process.
It is the image of a [[topological embedding|00ZG9Y9TR4]] of the $2$-[[sphere|T62369RFH6]] $S^2$.
Start with a ball and pull out two horns that grow towards each other.
Near their tips, let each horn split into a pair of thinner horns.
Let the two pairs hook through each other like two links of a chain, without touching.
Repeat this splitting inside each pair, at smaller and smaller scales, infinitely often.
The limit set of the surfaces is $\Sigma$; the tips shrink to a Cantor set of points, and $\Sigma$ is still homeomorphic to $S^2$.

The closure of the bounded component of $\R^3 \setminus \Sigma$ is homeomorphic to the closed ball $D^3$.
The unbounded component is not simply connected.
A loop around the base of one horn cannot be shrunk to a point in the complement.
Each attempt to slide it off the horns is blocked by the next pair of hooked horns.
So the closure of the unbounded component is not homeomorphic to the closure of the complement of a round ball, whose [[fundamental group|S1XK3HXHFX]] is trivial.

## Remarks

The example shows that the [[Schoenflies theorem|3VX06XRVZG]] fails in dimension $3$ without its local flatness hypothesis.
The sphere $\Sigma$ is not locally flat at the points of the Cantor set.
J. W. Alexander described it in 1924.
Gluing two copies of the closed bounded side along $\Sigma$ gives a space homeomorphic to $S^3$, a result of R. H. Bing.

## Explanations

### L1 human

In the plane, every loop bounds a disk on the inside and the rest of the plane on the outside, both as nice as possible.
In space one would expect the same for a sphere, but the horned sphere breaks this.
Its horns branch and interlock forever, so a rubber band around a horn on the outside can never be pulled free.
The surface is still a perfect topological sphere; the problem is only how it sits in space.
