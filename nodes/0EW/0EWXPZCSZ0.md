---
tag: 0EWXPZCSZ0
kind: statement
role: theorem
name: Impossibility of trisecting the angle
msc: [12F05]
uses: [00J3DCCEK5, 0SSSM1D475, 0VNE161QCK, 0819CQ1V8H]
sources:
  - url: https://en.wikipedia.org/wiki/Angle_trisection
    locator: Proof of impossibility
---

## Statement

The angle $\pi/3$, that is, $60^\circ$, cannot be [[trisected|00J3DCCEK5]] with straightedge and compass.
Equivalently, $\cos(\pi/9)$ is not a [[constructible number|0FMN2MN7TM]].

## Remarks

The proof: $\cos 3\theta = 4 \cos^3 \theta - 3 \cos \theta$ shows that $c = \cos(\pi/9)$ is a root of $8x^3 - 6x - 1$. Then $u = 2c$ is a root of $x^3 - 3x - 1$.
The polynomial $x^3 - 3x - 1$ has no rational root, by the [[rational root theorem|0819CQ1V8H]]. So it is [[irreducible|0VNE161QCK]], and $[\mathbb{Q}(c) : \mathbb{Q}] = 3$.
Since $3$ is not a power of $2$, the number $c$ is not constructible.
The angle $\pi/3$ itself is constructible, so no general trisection method exists.

## History

Pierre Wantzel published the proof in 1837.

## Explanations

### L1 human

If you could trisect every angle, you could trisect $60^\circ$ and construct an angle of $20^\circ$.
The cosine of $20^\circ$ has degree $3$ over the rationals, so it is not constructible.
