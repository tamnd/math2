---
tag: VQ7D5N3MV7
kind: example
name: Cusp catastrophe
msc: [58K35, 37G10]
illustrates: [23RVD8K8RB, KSAFWZVB8K]
uses: [0YTCMFB4HC, KSAFWZVB8K, 2XDRZV3GSA]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Example

The *cusp catastrophe* is the two-parameter family of functions
$$V_{a,b}(x) = x^4 + a x^2 + b x, \qquad x, a, b \in \R.$$
Its [[critical points|0YTCMFB4HC]] solve $4x^3 + 2a x + b = 0$, and such a point is degenerate when also $12 x^2 + 2a = 0$.

Bifurcation set: a degenerate critical point $x$ has $a = -6x^2$ and then $b = -4x^3 - 2ax = 8x^3$.
Eliminating $x$ gives the curve
$$8 a^3 + 27 b^2 = 0,$$
a semicubical parabola with a cusp at the origin, lying in the half-plane $a \le 0$.
Check: with $a = -6x^2$ and $b = 8x^3$, one has $8a^3 = -1728 x^6$ and $27 b^2 = 1728 x^6$.

Number of critical points: the cubic $4x^3 + 2ax + b$ has discriminant $-16(8a^3 + 27b^2)$.
So for $8a^3 + 27b^2 < 0$, inside the cusp, there are three critical points, two local minima and one local maximum between them.
For $8a^3 + 27b^2 > 0$, outside the cusp, there is one critical point, a minimum.
The family is the [[universal unfolding|KSAFWZVB8K]] of the germ $x^4$, whose codimension is $2$.

## Explanations

### L1 human

Now the curve can have two valleys, and the ball sits in one of them.
Inside the cusp-shaped region of the two knobs $a$ and $b$, both valleys exist; outside it, only one does.
If you turn the knob $b$ slowly, the ball stays in its valley until that valley disappears at the edge of the cusp.
Then it jumps to the other valley.
Turning $b$ back, the ball does not jump back at the same place but only at the opposite edge, which is called hysteresis.
The cusp is the simplest catastrophe with this memory effect, and its [[bifurcation diagram|2XDRZV3GSA]] is the cusp curve.
