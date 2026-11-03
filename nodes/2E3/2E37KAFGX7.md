---
tag: 2E37KAFGX7
kind: definition
name: Nodal analysis
msc: [94C05, 05C50]
defines: 9NW7KCBSME
uses: [T7KRE7J3B4, TN6M6DVZRP, 0GT4WWGWH2, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Nodal_analysis
---

## Definition

Consider a circuit on a finite set $V$ of nodes whose branches are of two kinds.
A resistive branch joins two distinct nodes $x, y$ and has a conductance $g > 0$.
A current source branch injects a given current into one node and draws it from another.
Assume that the graph formed by the resistive branches, an [[electrical network|T7KRE7J3B4]], is connected, and fix a reference node $x_0 \in V$.
For $x, y \in V \setminus \set{x_0}$ define:

1. $G_{xx}$ as the sum of the conductances of all resistive branches at $x$;
2. $G_{xy}$, for $x \ne y$, as minus the sum of the conductances of the resistive branches joining $x$ and $y$;
3. $J_x$ as the total current injected into $x$ by the current sources.

The *nodal equations* are the [[system of linear equations|0GT4WWGWH2]] $G \varphi = J$ for the unknown node potentials $\varphi = (\varphi(x))_{x \ne x_0}$, with $\varphi(x_0) = 0$.
*Nodal analysis* is the method of writing and solving these equations; the branch voltages and currents then follow from Ohm's law.

## Remarks

The matrix $G$ is the [[Laplacian matrix|TN6M6DVZRP]] of the weighted graph of resistive branches with the row and column of $x_0$ deleted.
Since this graph is connected, $G$ is symmetric and [[positive definite|0KX66CZMBB]], so the nodal equations have exactly one solution.
Example: take nodes $x_0, 1, 2$ and a triangle of resistive branches of conductance $1$ on them.
A current source injects $J_1 = 3$ into node $1$ and draws it from $x_0$.
Then $G = \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$, $J = (3, 0)$, and $\varphi(1) = 2$, $\varphi(2) = 1$.
Non-example: let node $2$ be joined to the others only through a current source.
Then the resistive graph is not connected, $G$ is singular, and the potential of node $2$ is not determined.
Voltage sources do not fit this scheme directly, because their current is not a function of the node potentials.
[[Modified nodal analysis|QD3R6CZQ3J]] handles them.
