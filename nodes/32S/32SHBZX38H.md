---
tag: 32SHBZX38H
kind: definition
name: Wigner D-matrix
msc: [33C80, "22E70", 81R05]
defines: QQPC9ASQHR
uses: [E5P8AG6CK7, FX3NEFYFFN, 9V6PRD1Z90]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner_D-matrix
---

## Definition

Let $j \in \set{0, \frac12, 1, \frac32, \dots}$, and let $V_j$ be the [[irreducible representation|FX3NEFYFFN]] of [[SU(2)|E5P8AG6CK7]] of dimension $2j + 1$, with an invariant inner product.
Let $J_x, J_y, J_z$ be the Hermitian operators on $V_j$ that represent the Lie algebra, with $[J_x, J_y] = i J_z$ and its cyclic permutations.
Let $\lvert j m \rangle$, for $m = j, j - 1, \dots, -j$, be the orthonormal basis of $V_j$ such that $J_z \lvert j m \rangle = m \lvert j m \rangle$ and $(J_x \pm i J_y) \lvert j m \rangle = \sqrt{j(j+1) - m(m \pm 1)}\, \lvert j, m \pm 1 \rangle$.
For Euler angles $\alpha, \beta, \gamma \in \R$, the *Wigner D-matrix* is the $(2j+1) \times (2j+1)$ matrix with entries
$$D^j_{m' m}(\alpha, \beta, \gamma) = \langle j m' \rvert\, e^{-i \alpha J_z} e^{-i \beta J_y} e^{-i \gamma J_z} \lvert j m \rangle,$$
where $m', m \in \set{j, j-1, \dots, -j}$.
The *small d-matrix* is $d^j_{m' m}(\beta) = D^j_{m' m}(0, \beta, 0)$.

## Remarks

Since $J_z$ is diagonal, $D^j_{m' m}(\alpha, \beta, \gamma) = e^{-i m' \alpha}\, d^j_{m' m}(\beta)\, e^{-i m \gamma}$.
The entries of $d^j(\beta)$ are real, and Wigner's formula is
$$d^j_{m' m}(\beta) = \sum_{s} \frac{(-1)^{m' - m + s} \sqrt{(j+m')!\,(j-m')!\,(j+m)!\,(j-m)!}}{(j+m-s)!\, s!\, (m'-m+s)!\, (j-m'-s)!} \left(\cos\tfrac{\beta}{2}\right)^{2j+m-m'-2s} \left(\sin\tfrac{\beta}{2}\right)^{m'-m+2s},$$
summed over the integers $s$ for which all factorials have nonnegative arguments.

Example: for $j = \frac12$, $J_y = \frac12 \sigma_y$ with the Pauli matrix $\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$, and $\sigma_y^2 = I$.
So $e^{-i \beta J_y} = \cos\frac{\beta}{2}\, I - i \sin\frac{\beta}{2}\, \sigma_y$, which gives $d^{1/2}_{\frac12 \frac12} = \cos\frac{\beta}{2}$ and $d^{1/2}_{\frac12, -\frac12} = -\sin\frac{\beta}{2}$.
Wigner's formula with $m' = \frac12$, $m = -\frac12$ has only the term $s = 0$, and it also gives $-\sin\frac{\beta}{2}$.

Non-example: the matrix $\begin{pmatrix} \cos\frac{\beta}{2} & \sin\frac{\beta}{2} \\ \sin\frac{\beta}{2} & \cos\frac{\beta}{2} \end{pmatrix}$ is not a D-matrix, since it is not unitary for $\sin \beta \ne 0$, while every $D^j$ is unitary.

For integer $j = \ell$, $d^\ell_{00}(\beta) = P_\ell(\cos\beta)$, the [[Legendre polynomial|QFYGJVA996]].
Also $\overline{D^\ell_{m 0}(\alpha, \beta, \gamma)} = \sqrt{\frac{4\pi}{2\ell+1}}\, Y_\ell^m(\beta, \alpha)$, where $Y_\ell^m$ is a [[spherical harmonic|3F32Y21HP4]] with polar angle $\beta$ and azimuth $\alpha$.
The bra-ket notation $\langle u \rvert A \lvert v \rangle$ means the inner product of $u$ with $A v$.
