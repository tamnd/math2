---
tag: 84SE8XMWR8
kind: definition
name: Topological order
msc: [81V70, 81T45, 82B10]
defines: 84DS4AGYNX
uses: [0NEGN5CRSC, XSA203109Z]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_order
---

## Definition

Let $\Sigma$ be a closed surface.
For each $L \ge 1$, let $\Lambda_L$ be a lattice on $\Sigma$ of linear size $L$, with a finite-dimensional site space at each site.
Let $H_L = \sum_X h_X$ be a [[self-adjoint|0NEGN5CRSC]] Hamiltonian that is a sum of terms $h_X$ of bounded norm, each supported on a set $X$ of bounded diameter.
Let $P_L$ be the projection onto the span of the eigenvectors whose eigenvalues lie within $\varepsilon_L$ of the smallest one, with $\varepsilon_L \to 0$.
The family $(H_L)$ has *topological order* if:

1. there is $\Delta > 0$, independent of $L$, such that all other eigenvalues exceed the smallest one by at least $\Delta$;
2. there are $c > 0$ and $\delta_L \to 0$ such that each operator $O$ supported on a ball of diameter at most $cL$ satisfies $\norm{P_L O P_L - \lambda_O P_L} \le \delta_L \norm{O}$ for some $\lambda_O \in \C$;
3. the rank of $P_L$, for large $L$, depends on the topology of $\Sigma$ and is larger than $1$ for some surface $\Sigma$.

## Remarks

Clause 2 says that no local observable distinguishes the ground states, so no local [[order parameter|XSA203109Z]] separates them.
Definitions in the literature vary; some also require that the ground states cannot be connected to a product state by a short local unitary circuit.

Example: Kitaev's toric code on a square lattice of linear size $L$ on a surface of genus $g$, with one spin on each edge.
Its Hamiltonian is $H_L = -\sum_v A_v - \sum_p B_p$.
Here $A_v$ is the product of $\sigma^x$ on the edges at a vertex $v$, and $B_p$ is the product of $\sigma^z$ on the edges of a face $p$.
All these terms commute and have eigenvalues $\pm 1$, so the gap is at least $2$, and the ground space has dimension $4^g$.
An operator that changes one ground state into another must act along a loop that winds around the surface, so its support has diameter of order $L$.

Non-example: the classical Ising Hamiltonian $-\sum \sigma^z_x \sigma^z_y$ on a torus has the two ground states with all spins up or all down.
The single-site operator $\sigma^z_x$ takes the value $+1$ on one and $-1$ on the other, so clause 2 fails, and the degeneracy $2$ does not depend on the surface.
