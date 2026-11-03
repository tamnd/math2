---
tag: S44D0TNQYV
kind: definition
name: Inertia tensor and principal axes
msc: ["70E15", "70E17"]
defines: WVGTEH6P10
uses: [EZ9P9ERKNE, 08ANASGBXV, 0VR671PHE5, 0BQAA2BK3Q, 06J4PXRG22]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_of_inertia
    locator: Inertia tensor
---

## Definition

Let a [[rigid body|EZ9P9ERKNE]] occupy a bounded region $B \subseteq \R^3$ with a continuous mass density $\rho \colon B \to [0, \infty)$.
Fix a point $O$ and write $x = (x_1, x_2, x_3)$ for the position of a point of $B$ relative to $O$.
The *inertia tensor* of the body about $O$ is the $3 \times 3$ matrix $I_O$ with entries
$$(I_O)_{jk} = \int_B \rho(x) \big( \abs{x}^2 \delta_{jk} - x_j x_k \big) \, dV, \qquad j, k = 1, 2, 3,$$
where $\delta_{jk}$ is $1$ if $j = k$ and $0$ otherwise.
The matrix $I_O$ is [[symmetric|0VR671PHE5]].
A *principal axis* of the body at $O$ is a line through $O$ spanned by an [[eigenvector|0BQAA2BK3Q]] of $I_O$.
The corresponding eigenvalues are the *principal moments of inertia* at $O$.

## Remarks

By the [[spectral theorem|06J4PXRG22]], there is an orthonormal basis of $\R^3$ made of eigenvectors of $I_O$, so every body has three mutually perpendicular principal axes at each point.
For a unit vector $n$, the number $n^T I_O n$ is the [[moment of inertia|08ANASGBXV]] of the body about the line through $O$ in the direction $n$.
For a body turning about the fixed point $O$ with angular velocity $\omega$, the angular momentum about $O$ is $I_O \omega$ and the kinetic energy is $\tfrac12 \omega^T I_O \omega$.
The matrix $I_O$ is positive semidefinite, and it is positive definite unless all the mass lies on one line through $O$.
For point masses $m_i$ at positions $x^{(i)}$, the integral is replaced by the sum $\sum_i m_i \big(\abs{x^{(i)}}^2 \delta_{jk} - x^{(i)}_j x^{(i)}_k\big)$.

Example: a uniform box of mass $M$ and side lengths $a, b, c$, centred at $O$ with edges along the coordinate axes.
The products $x_j x_k$ with $j \ne k$ integrate to $0$ by symmetry, and $\int_B \rho\, x_1^2 \, dV = M a^2 / 12$.
So $I_O = \operatorname{diag}\big(M(b^2 + c^2)/12, \ M(a^2 + c^2)/12, \ M(a^2 + b^2)/12\big)$, and the coordinate axes are principal axes.

Non-example: for two point masses $m$ at $(1, 1, 0)$ and $(-1, -1, 0)$, the off-diagonal entry is $(I_O)_{12} = -2m \ne 0$.
So the $x_1$-axis is not a principal axis; the principal axes are the lines spanned by $(1, 1, 0)$, $(1, -1, 0)$ and $(0, 0, 1)$.
