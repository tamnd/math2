---
tag: 5S2RVZ6G8Z
kind: definition
name: Modified nodal analysis
msc: [94C05, 94C60]
defines: QD3R6CZQ3J
uses: [9NW7KCBSME, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Modified_nodal_analysis
---

## Definition

Consider a circuit on a finite set of nodes with a reference node $x_0$.
Its branches are resistive branches, independent current sources and independent voltage sources $k = 1, \dots, p$.
Voltage source $k$ joins a node $a_k$ to a node $b_k$ and prescribes $\varphi(a_k) - \varphi(b_k) = E_k$.
Let $G$ and $J$ be the conductance matrix and the source current vector of [[nodal analysis|9NW7KCBSME]].
They are built from the resistive branches and the current sources only.
Let $j_k$ be the unknown current that leaves node $a_k$ through source $k$ and enters node $b_k$.
Let $B$ be the matrix with rows indexed by the nodes other than $x_0$ and columns indexed by $k$.
Its entries are $B_{a_k k} = 1$, $B_{b_k k} = -1$ and $0$ otherwise.
The *modified nodal equations* are the [[system of linear equations|0GT4WWGWH2]]
$$\begin{pmatrix} G & B \\ B^{T} & 0 \end{pmatrix} \begin{pmatrix} \varphi \\ j \end{pmatrix} = \begin{pmatrix} J \\ E \end{pmatrix}$$
for the node potentials $\varphi$ (with $\varphi(x_0) = 0$) and the source currents $j$.
*Modified nodal analysis* is the method of writing and solving these equations.

## Remarks

The first block row is the current law at each node, now counting the currents through the voltage sources; the second block row prescribes the source voltages.
Example: one node $1$, a resistor $R$ from $1$ to $x_0$, and a voltage source $E$ from $1$ to $x_0$.
The equations are $\varphi(1)/R + j = 0$ and $\varphi(1) = E$, so $\varphi(1) = E$ and $j = -E/R$: the source delivers the current $E/R$ into node $1$.
Non-example: plain nodal analysis cannot handle the same circuit.
The current through the source is not given by Ohm's law, so the node equation at $1$ cannot be written.
The system is uniquely solvable when the resistive graph is connected and the voltage sources contain no cycle, so that $B$ has full column rank.
Inductors, capacitors and controlled sources are added in the same way, with extra rows and columns.
