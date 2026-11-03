---
tag: BJYK6SYPYK
kind: definition
name: Mesh analysis
msc: [94C05, 94C15]
defines: 5KKY8RPFB4
uses: [0NC9R64TXP, 0Z05VCBQ7Y, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Mesh_analysis
---

## Definition

Consider a circuit whose graph is a [[planar graph|0NC9R64TXP]], drawn in the plane without crossings.
Assume that the graph is 2-connected, so that every face of the drawing is bounded by a cycle.
Each branch $e$ is a resistor $r_e > 0$, possibly in series with an independent voltage source.
The *meshes* are the bounded faces $f_1, \dots, f_m$ of the drawing; each is bounded by a [[cycle|0Z05VCBQ7Y]], oriented clockwise.
To each mesh $f_k$ assign an unknown *mesh current* $I_k$.
The current of a branch $e$ is the sum of $\pm I_k$ over the meshes whose boundary contains $e$.
The sign is $+$ when the clockwise orientation of $f_k$ agrees with the reference direction of $e$.
Define the $m \times m$ matrix $R$ and the vector $E$ by:

1. $R_{kk}$ is the sum of $r_e$ over the branches on the boundary of $f_k$;
2. $R_{kl}$, for $k \ne l$, is minus the sum of $r_e$ over the branches shared by $f_k$ and $f_l$;
3. $E_k$ is the sum of the source voltages around $f_k$, each counted positive when it drives current clockwise around $f_k$.

The *mesh equations* are the [[system of linear equations|0GT4WWGWH2]] $R I = E$, and *mesh analysis* is the method of writing and solving them.

## Remarks

Branch currents built from mesh currents satisfy the current law automatically, since each mesh current enters and leaves every node it passes.
The mesh equations are the voltage law around each mesh, with Ohm's law inserted.
If the circuit has $b$ branches and $n$ nodes, Euler's formula gives $m = b - n + 1$ meshes, usually far fewer unknowns than branch currents.
Example: let two meshes share a resistor $r_3$, with $r_1$ and a source $E_1$ in the left mesh and $r_2$ in the right one.
This gives $R = \begin{pmatrix} r_1 + r_3 & -r_3 \\ -r_3 & r_2 + r_3 \end{pmatrix}$ and $E = (E_1, 0)$.
Non-example: a circuit whose graph is not planar has no meshes in this sense; one then uses loop analysis with the fundamental cycles of a spanning tree.
The matrix $R$ is symmetric and positive definite, so the mesh equations have exactly one solution.
