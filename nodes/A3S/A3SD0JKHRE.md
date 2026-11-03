---
tag: A3SD0JKHRE
kind: definition
name: Galilean invariance
msc: [70A05, 70G65]
defines: K2JDS5KH2H
uses: [8CTX67V404, SH7J0X3NCC]
sources:
  - url: https://en.wikipedia.org/wiki/Galilean_invariance
---

## Definition

Consider a [[Newtonian system|SH7J0X3NCC]] of $N$ point particles with positions $x_1(t), \dots, x_N(t) \in \R^3$.
Let $g(t, x) = (t + s, R x + v t + a)$ be a [[Galilean transformation|8CTX67V404]].
The image of a motion $(x_1, \dots, x_N)$ under $g$ is the motion $(\tilde x_1, \dots, \tilde x_N)$ with
$$\tilde x_i(t) = R\, x_i(t - s) + v\,(t - s) + a, \qquad i = 1, \dots, N.$$
The system is *Galilean invariant* if, for each Galilean transformation $g$, the image under $g$ of each motion is again a motion.

## Remarks

Example: let the equations be $m_i \ddot x_i = \sum_{j \ne i} f_{ij}(\abs{x_i - x_j})\,(x_i - x_j)$ with $f_{ij} = f_{ji}$, on the set where all $x_i$ are distinct.
For an image motion, $\ddot{\tilde x}_i(t) = R\, \ddot x_i(t - s)$ and $\tilde x_i - \tilde x_j = R(x_i - x_j)$, with the same length, since $R$ is orthogonal.
So both sides of each equation are multiplied by $R$, and the image is again a motion.
Non-example: a particle tied to the origin by a spring, $m \ddot x = -k x$ with $k > 0$, is not Galilean invariant.
For the shift $\tilde x(t) = x(t) + a$ with $a \ne 0$, one gets $m \ddot{\tilde x} = -k x = -k \tilde x + k a \ne -k \tilde x$.
The fixed origin breaks the symmetry; the system is not isolated.

## Explanations

### L1 human

A law of motion is Galilean invariant if each observer moving uniformly relative to another sees motions that obey the same law.
Shifting the clock, moving or turning the axes, or giving everything a common constant velocity never turns a possible motion into an impossible one.
