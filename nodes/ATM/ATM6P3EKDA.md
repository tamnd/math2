---
tag: ATM6P3EKDA
kind: definition
name: Transfer-matrix method in optics
msc: [78A40, 78A10]
defines: G5Q62JS3JM
uses: [NM024G378A, 9VGK0SP6EQ, 0VD9ZSWWJG, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Transfer-matrix_method_(optics)
---

## Definition

Let layers $j = 1, \dots, N$ fill the slabs $z_{j-1} < z < z_j$, with $z_0 = 0$, thickness $d_j = z_j - z_{j-1}$ and real [[refractive index|9VGK0SP6EQ]] $n_j > 0$.
Let a medium of index $n_0$ fill $z < 0$ and a medium of index $n_s$ fill $z > z_N$; all media are non-magnetic.
A [[plane wave|NM024G378A]] of vacuum wave number $k_0$, polarized along $y$ ($s$-polarization), arrives from $z < 0$ at angle $\theta_0$.
Let $\kappa = k_0 n_0 \sin \theta_0$, and let $q_j = \sqrt{k_0^2 n_j^2 - \kappa^2}$, assumed real and positive, with $q_0$ and $q_s$ defined in the same way.
The field is $E_y = U(z) e^{i \kappa x}$, where $U'' + q_j^2 U = 0$ in layer $j$, and $U$ and $U'$ are continuous at each interface.
The *transfer matrix* of layer $j$ is
$$M_j = \begin{pmatrix} \cos(q_j d_j) & \sin(q_j d_j)/q_j \\ -q_j \sin(q_j d_j) & \cos(q_j d_j) \end{pmatrix},$$
which maps $(U, U')$ at $z_{j-1}$ to $(U, U')$ at $z_j$.
The *transfer-matrix method* computes the [[matrix|0VD9ZSWWJG]] $M = M_N \cdots M_1$ and then the reflection and transmission coefficients $r$ and $t$ from the linear system
$$\begin{pmatrix} t \\ i q_s t \end{pmatrix} = M \begin{pmatrix} 1 + r \\ i q_0 (1 - r) \end{pmatrix}.$$

## Remarks

The system expresses that $U = e^{i q_0 z} + r e^{-i q_0 z}$ for $z < 0$ and $U = t \, e^{i q_s (z - z_N)}$ for $z > z_N$.
Each $M_j$ is the propagator of the [[linear differential equation|0QQRP17Z7S]] $U'' + q_j^2 U = 0$, and $\det M_j = 1$.

Example: a quarter-wave anti-reflection layer at normal incidence.
Take $N = 1$, $\theta_0 = 0$, $n_1 = \sqrt{n_0 n_s}$ and $q_1 d_1 = \pi/2$.
Then $M = \begin{pmatrix} 0 & 1/q_1 \\ -q_1 & 0 \end{pmatrix}$, and the system reads $t = i q_0 (1 - r)/q_1$ and $i q_s t = -q_1 (1 + r)$.
Eliminating $t$ gives $q_0 q_s (1 - r) = q_1^2 (1 + r)$, and $q_1^2 = q_0 q_s$ because $n_1^2 = n_0 n_s$, so $r = 0$.

Non-example: a layer whose index varies along $x$, such as a grating, has no transfer matrix of this form.
Its field is not of the form $U(z) e^{i \kappa x}$, and it couples many diffraction orders.

For $p$-polarization the same method applies to $H_y$, with $U'$ replaced by $U'/n_j^2$, which is continuous.
For absorbing layers the $n_j$ and $q_j$ are complex, and the same formulas hold with the correct branch of the root.

## Explanations

### L1 human

Inside each layer the field is a sum of a forward and a backward wave, so it is fixed by two numbers.
The matrix of the layer tells how these two numbers change from one face to the other.
Multiplying the matrices of all layers gives the effect of the whole stack, and matching with the outside media gives the reflection.
