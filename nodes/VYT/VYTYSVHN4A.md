---
tag: VYTYSVHN4A
kind: example
name: Trefoil knot
msc: [57K10]
instance_of: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Trefoil_knot
same_as:
  wikidata: Q168620
  wikipedia: Trefoil knot
---

## Example

The *trefoil knot* is the image of the map $f \colon \R / 2\pi\Z \to \R^3$ given by
$$f(t) = \bigl((2 + \cos 3t) \cos 2t, \ (2 + \cos 3t) \sin 2t, \ \sin 3t\bigr).$$
The map is continuous, and it is injective.
Indeed, if $f(t) = f(s)$, the last coordinate and the distance $2 + \cos 3t$ from the $z$-axis give $3t \equiv 3s \pmod{2\pi}$.
The angle around the $z$-axis gives $2t \equiv 2s \pmod{2\pi}$.
Then $t - s$ is a multiple of $2\pi/3$ and of $\pi$, so of $2\pi$.
Hence the image is a [[knot|QYEAZTYGPT]].
It lies on a torus, and it winds $2$ times around the axis of the torus and $3$ times around its core.
So it is the [[torus knot|NS60VV786W]] of type $(2, 3)$.

## Remarks

Its [[crossing number|SWJZ4QRF9W]] is $3$, and it is the only knot with crossing number $3$ up to mirror image.
It is [[tricolorable|KNAGK0W65G]] while the unknot is not, so it is not the unknot.
Its [[knot group|AQVHM3FP0D]] has the presentation $\langle x, y \mid xyx = yxy \rangle$, which is isomorphic to $\langle a, b \mid a^2 = b^3 \rangle$.
Its Alexander polynomial is $t^{-1} - 1 + t$, and its genus is $1$.
It is not equivalent to its mirror image, a fact that the Jones polynomial detects.

## Explanations

### L1 human

The trefoil is the simplest real knot: tie an overhand knot in a string and glue the ends together.
Any picture of it has at least three crossings, and the standard picture has three lobes like a clover leaf.
It comes in two mirror forms, left-handed and right-handed, and these cannot be moved into each other.
