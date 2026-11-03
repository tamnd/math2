---
tag: 85EM72CDVF
kind: definition
name: Finite element method in structural mechanics
msc: [74S05, 65N30]
defines: CGYM9VZC39
uses: [98GZ9DVHTA, G8ZTW9JVX1, A5T30ZHVGH, 5YSP8TWD4Q, 6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_element_method_in_structural_mechanics
---

## Definition

Consider a problem of [[linear elasticity|6W00ZECYT0]] on a domain $\Omega \subset \R^n$ with admissible displacement space $V$.
Its total potential energy is
$$\Pi(v) = \frac12 a(v, v) - \ell(v),$$
where $a(v, w) = \int_\Omega \mathsf{C}\varepsilon(v) : \varepsilon(w)\,dx$ is the strain energy form and $\ell$ is the work of the loads.
The *displacement-based finite element method* for this problem consists of the following steps.

1. Mesh: $\Omega$ is divided into finitely many elements $\Omega_e$ that meet only along faces, edges or vertices, with nodes at prescribed points.
2. Trial space: a finite-dimensional subspace $V_h \subset V$ is spanned by shape functions $N_1, \ldots, N_m$, each a polynomial on every element.
   So $v_h = \sum_{a} d_a N_a$ for a vector $d = (d_1, \ldots, d_m)$ of nodal displacements.
3. Discrete problem: $u_h$ is the minimiser of $\Pi$ on $V_h$, equivalently the solution of $K d = F$.
   Here $K_{ab} = a(N_a, N_b)$ is the [[stiffness matrix|G8ZTW9JVX1]] and $F_a = \ell(N_a)$ is the load vector.
4. Assembly: $K = \sum_e K^{(e)}$ and $F = \sum_e F^{(e)}$, where $K^{(e)}$ and $F^{(e)}$ are the same integrals restricted to $\Omega_e$, computed element by element.

## Remarks

Example: a bar $[0, L]$ of axial stiffness $EA$, clamped at $0$ and loaded by a force $P$ at $L$, with two linear elements of length $h = L/2$.
Each element has stiffness matrix $\frac{EA}{h}\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$, and assembly with $d_0 = 0$ gives $\frac{EA}{h}\begin{pmatrix} 2 & -1 \\ -1 & 1 \end{pmatrix}\begin{pmatrix} d_1 \\ d_2 \end{pmatrix} = \begin{pmatrix} 0 \\ P \end{pmatrix}$.
The solution $d_1 = Ph/(EA)$, $d_2 = 2Ph/(EA) = PL/(EA)$ is exact, since the exact displacement is linear.

Non-example: if the trial functions are discontinuous across element boundaries, $V_h$ is not contained in $H^1(\Omega)$, so clause 2 fails.
Such nonconforming elements need extra checks such as the [[patch test|KFMV57EXB6]].

Step 3 is the [[Rayleigh–Ritz method|5YSP8TWD4Q]] on $V_h$, justified by the [[minimum total potential energy principle|A5T30ZHVGH]].
In engineering notation $K^{(e)} = \int_{\Omega_e} B^T D B\,dx$, where $B$ maps nodal displacements to strains and $D$ is the matrix of elastic constants.
