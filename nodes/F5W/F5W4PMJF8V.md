---
tag: F5W4PMJF8V
kind: definition
name: Angular momentum
msc: [70A05, 70F10]
defines: 7147M98XNR
uses: [HFDS8NCJ1A, 0SEDGXG9S3]
sources:
  - url: https://en.wikipedia.org/wiki/Angular_momentum
---

## Definition

Let a particle of mass $m > 0$ have position $x(t) \in \R^3$ and [[momentum|HFDS8NCJ1A]] $p(t) = m \dot x(t)$ at time $t$, and let $c \in \R^3$ be a fixed point.
The *angular momentum* of the particle about $c$ at time $t$ is
$$L(t) = \big(x(t) - c\big) \times p(t),$$
where $\times$ is the [[cross product|0SEDGXG9S3]] of $\R^3$.
For $N$ particles with positions $x_i$ and momenta $p_i$, the *total angular momentum* about $c$ is $L = \sum_{i=1}^{N} (x_i - c) \times p_i$.

## Remarks

Example: let $x(t) = (R \cos \omega t, R \sin \omega t, 0)$ with $R > 0$ and $c = 0$.
Then $\dot x = (-R\omega \sin \omega t, R \omega \cos \omega t, 0)$ and $L = (0, 0, m R^2 \omega)$, a constant vector along the axis of rotation.
Non-example: a particle moving on a line through $c$, say $x(t) = c + t u$, has $L = t u \times m u = 0$; it has momentum but no angular momentum about $c$.
When no point is named, $c$ is the origin.
The angular momentum depends on the choice of $c$; for the total angular momentum, moving $c$ to $c'$ adds $(c - c') \times P$, where $P$ is the total momentum.

## Explanations

### L1 human

Angular momentum measures how much a body swings around a chosen point.
Only the part of the velocity across the line to the point counts, and the farther away the body is, the more it counts.
