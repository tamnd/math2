---
tag: X2RP7SPN67
kind: definition
name: Forward kinematics
msc: [70B15, 93C85]
defines: 1DQ5AE8D8E
uses: [0H3YY8CPKH, MGYKGP7PW3, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Forward_kinematics
---

## Definition

Represent a rigid motion $x \mapsto R x + p$ of $\R^3$, with $R \in SO(3)$ and $p \in \R^3$, by the $4 \times 4$ matrix $\begin{pmatrix} R & p \\ 0 & 1 \end{pmatrix}$; these matrices form the [[Euclidean group|0H3YY8CPKH]] $SE(3)$.
Let a serial chain consist of links $0, 1, \dots, n$, with link $0$ fixed.
Link $i - 1$ and link $i$ are joined by a joint with a real variable $q_i$ ranging over a set $Q_i \subseteq \R$.
For each $i$, let $T_i \colon Q_i \to SE(3)$ give the pose of a frame fixed in link $i$ relative to a frame fixed in link $i - 1$.
The *forward kinematics map* of the chain is the following map.
$$f \colon Q_1 \times \cdots \times Q_n \to SE(3), \qquad f(q_1, \dots, q_n) = T_1(q_1)\, T_2(q_2) \cdots T_n(q_n)$$
Its value is the pose of the frame of link $n$ relative to the frame of link $0$, computed by [[matrix multiplication|076JGP6R3T]].

## Remarks

Example: a planar arm with two revolute joints and links of lengths $l_1, l_2$, seen in the plane $x_3 = 0$.
Here $T_i(q_i)$ is the rotation by $q_i$ about the $x_3$-axis followed by the translation by $l_i$ along the rotated $x_1$-axis.
The product gives the hand position $\big(l_1 \cos q_1 + l_2 \cos(q_1 + q_2),\ l_1 \sin q_1 + l_2 \sin(q_1 + q_2)\big)$ and orientation angle $q_1 + q_2$.

Non-example: in a closed chain such as a four-bar linkage the joint variables are linked by loop equations.
So they do not range over a product $Q_1 \times \cdots \times Q_n$, and no such product formula describes the chain.
The joint space $Q_1 \times \cdots \times Q_n$ is the [[configuration space|MGYKGP7PW3]] of the serial chain.
The derivative of $f$ is the manipulator Jacobian, which relates joint velocities to the velocity of the end link.
