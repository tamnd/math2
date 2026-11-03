---
tag: X4R728TVZE
kind: statement
role: theorem
name: Chasles' theorem
msc: [70B10, 53A17]
uses: [0H3YY8CPKH, 0XNZWJ96HK, 0R5QPQ3AGJ, 2ZVG43GSKA]
about: [0H3YY8CPKH, NVBD7Y86ES]
sources:
  - url: https://en.wikipedia.org/wiki/Chasles%27_theorem_(kinematics)
same_as:
  wikidata: Q17004813
  wikipedia: Chasles' theorem (kinematics)
---

## Statement

Let $g \colon \R^3 \to \R^3$ be a rigid motion that keeps the orientation, that is, $g(x) = R x + b$ with $R \in SO(3)$ and $b \in \R^3$.
Then $g$ is a [[translation|0R5QPQ3AGJ]] or a *screw displacement*.
That is, if $R \ne I$, there are a line $L \subset \R^3$ with unit direction vector $u$, an angle $\theta \in (0, 2\pi)$ and a number $d \in \R$ with this property.
The map $g$ is the [[rotation|0XNZWJ96HK]] by $\theta$ about $L$ followed by the translation by $d u$.

## Remarks

Proof idea: by [[Euler's rotation theorem|2ZVG43GSKA]], $R$ is a rotation by some $\theta$ about an axis with unit direction $u$.
Write $b = d u + b_\perp$ with $b_\perp$ orthogonal to $u$.
On the plane orthogonal to $u$, the map $x \mapsto R x + b_\perp$ is a plane rotation by $\theta \ne 0$ followed by a translation.
It has a fixed point $p$, as $R - I$ is invertible on that plane.
Then $g$ is the rotation by $\theta$ about the line $L = p + \R u$ followed by the translation $d u$ along $L$.

Example: $g(x_1, x_2, x_3) = (-x_2 + 2,\ x_1,\ x_3 + 5)$ has $R$ the quarter turn about the $x_3$-axis.
Its axis is the vertical line through $p = (1, 1, 0)$, since $(-1 + 2, 1) = (1, 1)$, and $d = 5$.

The orientation hypothesis is needed: the reflection $x \mapsto (x_1, x_2, -x_3)$ is a rigid motion that is not a screw displacement.
The analogous statement in the plane says that every orientation-preserving rigid motion is a translation or a rotation about a point.

## Explanations

### L1 human

Move a solid object from one place to another without bending it.
Chasles' theorem says the same final position could be reached by a single screw motion: turn about one line while sliding along that same line.
A bolt being screwed into a nut is the picture to keep in mind.

### L2 human

The theorem is the starting point of [[screw theory|NVBD7Y86ES]] and describes the elements of the [[Euclidean group|0H3YY8CPKH]] $SE(3)$ geometrically.
Applied to infinitesimal motions, it shows that the velocity field of a rigid body is at each instant that of a screw motion, with an instantaneous screw axis.
In the plane, the same idea gives the [[instant centre of rotation|WQT8X3V2JQ]].
It is used to parametrise displacements in robot kinematics.
