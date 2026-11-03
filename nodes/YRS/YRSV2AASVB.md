---
tag: YRSV2AASVB
kind: definition
name: Euler angles
msc: [70B10, 15B10]
defines: 7WGBNTRQ2S
uses: [0CGYNDCWRR, 0XNZWJ96HK]
sources:
  - url: https://en.wikipedia.org/wiki/Euler_angles
---

## Definition

For $\theta \in \R$, let
$$R_z(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta & 0 \\ \sin\theta & \cos\theta & 0 \\ 0 & 0 & 1 \end{pmatrix}, \qquad R_x(\theta) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos\theta & -\sin\theta \\ 0 & \sin\theta & \cos\theta \end{pmatrix}$$
be the [[rotations|0XNZWJ96HK]] of $\R^3$ by the angle $\theta$ about the $z$-axis and the $x$-axis.
Let $R$ be an element of the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$.
A triple $(\alpha, \beta, \gamma)$ of real numbers is a triple of *Euler angles* of $R$, in the $z$-$x$-$z$ convention, if:

1. $\alpha \in [0, 2\pi)$, $\beta \in [0, \pi]$ and $\gamma \in [0, 2\pi)$;
2. $R = R_z(\alpha)\, R_x(\beta)\, R_z(\gamma)$.

## Remarks

Every $R \in SO(3)$ has a triple of Euler angles, and the triple is unique when $0 < \beta < \pi$.
The angle $\beta$ is determined by $\cos\beta = R_{33}$, the entry in the third row and third column.

Example: the triple $(\pi/2, 0, 0)$ gives $R = R_z(\pi/2)$, the quarter turn about the $z$-axis.
But $(0, 0, \pi/2)$ and $(\pi/4, 0, \pi/4)$ give the same $R$, since $R_x(0)$ is the identity; at $\beta = 0$ only $\alpha + \gamma$ is determined (gimbal lock).

Non-example: the product $R_z(\alpha) R_z(\beta) R_z(\gamma) = R_z(\alpha + \beta + \gamma)$ is not of the form in clause 2.
Such products only give rotations about the $z$-axis, so three rotations about one axis cannot serve as Euler angles.

Other conventions use other axis sequences.
Proper Euler angles have equal first and third axes, such as $z$-$y$-$z$.
Tait–Bryan angles use three distinct axes, such as yaw, pitch and roll about $z$, $y$, $x$.
The product $R_z(\alpha) R_x(\beta) R_z(\gamma)$ can be read as rotations about the fixed axes in the order $\gamma$, $\beta$, $\alpha$.
It can also be read as rotations about the moving body axes in the order $\alpha$, $\beta$, $\gamma$.
