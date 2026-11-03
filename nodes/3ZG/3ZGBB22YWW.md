---
tag: 3ZGBB22YWW
kind: definition
name: Direct stiffness method
msc: [74S05, 74K10]
defines: 7511XGF6MJ
uses: [G8ZTW9JVX1, E5ZHQSHB97]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_stiffness_method
---

## Definition

Consider a linear elastic framed structure, for example a [[truss|E5ZHQSHB97]].
It is made of members $e = 1, \ldots, M$ joined at nodes.
Let $d \in \R^m$ be the vector of all nodal degrees of freedom in global coordinates: displacements and, for frames, rotations.
Let $F \in \R^m$ be the vector of external nodal loads.
The *direct stiffness method* consists of the following steps.

1. Member stiffness: for each member, a matrix $k_e$ maps its local end displacements to its end forces in local coordinates.
2. Transformation: a matrix $T_e$ maps the global degrees of freedom of the member's nodes to its local end displacements.
3. Assembly: the global [[stiffness matrix|G8ZTW9JVX1]] is $K = \sum_e L_e^T T_e^T k_e T_e L_e$.
   Here $L_e$ selects from $d$ the degrees of freedom of the nodes of member $e$.
4. Solution: the rows and columns of the supported degrees of freedom are removed, and the reduced system $K d = F$ is solved.
   Member forces are then $k_e T_e L_e d$, and support reactions follow from the removed rows.

## Remarks

Example: two springs of stiffness $k_1$ and $k_2$ in series along a line, with nodes $0, 1, 2$, node $0$ fixed and a load $P$ at node $2$.
Each spring has $k_e = k\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$, and assembly gives
$$K = \begin{pmatrix} k_1 & -k_1 & 0 \\ -k_1 & k_1 + k_2 & -k_2 \\ 0 & -k_2 & k_2 \end{pmatrix}.$$
Removing node $0$ and solving gives $d_1 = P/k_1$ and $d_2 = P/k_1 + P/k_2$.

Non-example: if no node is supported, step 4 removes nothing and $K$ is singular, since a rigid translation $d = (1, 1, 1)$ gives $Kd = 0$; the method then has no unique solution.

For a pin-jointed bar of axial stiffness $EA$ and length $L$, $k_e = \frac{EA}{L}\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$ in the axial direction.
