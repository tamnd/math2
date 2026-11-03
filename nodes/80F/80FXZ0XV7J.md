---
tag: 80FXZ0XV7J
kind: definition
name: Galilean transformation
msc: [70A05, 70G65]
defines: 8CTX67V404
uses: [0QRBVFJ50X, 0JF0TVYGWT, Q05G0NZDNB]
sources:
  - url: https://en.wikipedia.org/wiki/Galilean_transformation
---

## Definition

Let $s \in \R$, let $a, v \in \R^3$, and let $R$ be a $3 \times 3$ [[orthogonal matrix|0QRBVFJ50X]].
The *Galilean transformation* with these data is the map $g \colon \R \times \R^3 \to \R \times \R^3$ given by
$$g(t, x) = (t + s,\; R x + v t + a).$$
Here $t$ is a time coordinate and $x$ a space coordinate.
When $s = 0$, $a = 0$ and $R$ is the identity, $g(t, x) = (t, x + v t)$ is called a *Galilean boost* with velocity $v$.

## Remarks

Each Galilean transformation is an [[affine map|0JF0TVYGWT]], and the Galilean transformations form a group under composition.
It maps [[inertial frames|Q05G0NZDNB]] to inertial frames: in terms of the new time $t' = t + s$, a free motion $x(t) = x_0 + u t$ becomes $x'(t') = R x_0 + a + (R u + v)(t' - s)$, again of constant velocity.
Example: under the boost with velocity $v$, a particle with constant velocity $u$ gets velocity $u + v$; this is the Galilean rule for adding velocities.
Non-example: the map $(t, x) \mapsto (t, x + t^2 e)$ with $e \ne 0$ is not Galilean, since it is not affine in $t$; it describes an accelerating frame.
A Lorentz transformation is not Galilean either, since it changes the time coordinate by an amount that depends on $x$.
Some texts require $\det R = 1$, that is, they leave out reflections.

## Explanations

### L1 human

A Galilean transformation changes the clock by a fixed offset, moves and turns the space axes, and lets the new frame drift at a constant velocity.
It is how two observers who move uniformly relative to each other translate their descriptions of the same motion.
