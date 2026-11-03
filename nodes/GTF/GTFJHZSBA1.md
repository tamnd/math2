---
tag: GTFJHZSBA1
kind: definition
name: Denavit–Hartenberg parameters
msc: [70B15, 93C85]
defines: 41426EQJHF
uses: [1DQ5AE8D8E, 0H3YY8CPKH]
sources:
  - url: https://en.wikipedia.org/wiki/Denavit%E2%80%93Hartenberg_parameters
---

## Definition

Let a serial chain have joint axes $z_0, z_1, \dots, z_{n-1}$, which are lines in $\R^3$.
Attach to link $i$ a right-handed orthonormal frame with origin $o_i$ and axes $x_i, y_i, z_i$.
The frames follow the *Denavit–Hartenberg convention* when the following holds for each $i \ge 1$.
The axis $x_i$ lies along a common normal of $z_{i-1}$ and $z_i$, pointing from $z_{i-1}$ to $z_i$, and $o_i$ is its foot on $z_i$.
The *Denavit–Hartenberg parameters* of joint $i$ are then:

1. $d_i$, the signed distance along $z_{i-1}$ from $o_{i-1}$ to the foot of the common normal;
2. $\theta_i$, the angle about $z_{i-1}$ from $x_{i-1}$ to $x_i$;
3. $a_i$, the length of the common normal, the distance between $z_{i-1}$ and $z_i$;
4. $\alpha_i$, the angle about $x_i$ from $z_{i-1}$ to $z_i$.

The pose of frame $i$ relative to frame $i - 1$ is then the following matrix in $SE(3)$.
$$T_i = \begin{pmatrix} \cos\theta_i & -\sin\theta_i \cos\alpha_i & \sin\theta_i \sin\alpha_i & a_i \cos\theta_i \\ \sin\theta_i & \cos\theta_i \cos\alpha_i & -\cos\theta_i \sin\alpha_i & a_i \sin\theta_i \\ 0 & \sin\alpha_i & \cos\alpha_i & d_i \\ 0 & 0 & 0 & 1 \end{pmatrix}$$
It is the product, in this order, of four motions.
First rotate by $\theta_i$ about $z$ and translate by $d_i$ along $z$.
Then translate by $a_i$ along $x$ and rotate by $\alpha_i$ about $x$.

## Remarks

For a revolute joint $\theta_i$ is the joint variable and the other three are constants; for a prismatic joint $d_i$ is the variable.
The [[forward kinematics|1DQ5AE8D8E]] map is $T_1 T_2 \cdots T_n$.

Example: a planar arm with two parallel revolute axes and link lengths $l_1, l_2$ has $d_i = 0$, $\alpha_i = 0$, $a_i = l_i$ and $\theta_i = q_i$.
Then $T_1 T_2$ has translation part $\big(l_1 \cos q_1 + l_2 \cos(q_1 + q_2),\ l_1 \sin q_1 + l_2 \sin(q_1 + q_2),\ 0\big)$.

Non-example: the translation by $1$ along the $y$-axis is in $SE(3)$ but is not of the form $T_i$.
Its translation part $(a \cos\theta, a \sin\theta, d) = (0, 1, 0)$ forces $\theta \equiv \pi/2$ modulo $2\pi$ (or $\theta \equiv -\pi/2$ with $a = -1$), and then the rotation part cannot be the identity.
This reflects that four parameters suffice only because the frames are chosen by the convention; a general rigid motion needs six.
When $z_{i-1}$ and $z_i$ are parallel, the common normal is not unique, and $d_i$ is fixed by an extra choice.
