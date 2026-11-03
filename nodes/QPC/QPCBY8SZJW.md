---
tag: QPCBY8SZJW
kind: definition
name: Wave function collapse
msc: [81P15, 81P05]
defines: RMEE72SQME
uses: [HM2HHE3J51, DF5RN297GE, 0B8KZRT28M, 4NQN47A92F, V1JTB52E8C, MF4DYZ4YAX]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_function_collapse
---

## Definition

Let $\mathcal{H}$ be a complex [[Hilbert space|HM2HHE3J51]] and let $A$ be an [[observable|DF5RN297GE]] on $\mathcal{H}$ with discrete spectrum.
For each eigenvalue $a$ of $A$, let $P_a$ be the [[orthogonal projection|0B8KZRT28M]] onto the eigenspace of $a$.
Let the system be in the pure [[state|4NQN47A92F]] given by a unit vector $\psi \in \mathcal{H}$.
Let a measurement of $A$ give the value $a$, which by the [[Born rule|MF4DYZ4YAX]] happens with probability $p_a = \norm{P_a \psi}^2$, and assume $p_a > 0$.
The *collapse*, or *projection postulate*, replaces $\psi$ by the post-measurement state
$$\psi_a = \frac{P_a \psi}{\norm{P_a \psi}}.$$
For a [[density operator|V1JTB52E8C]] $\rho$ with $p_a = \tr(P_a \rho) > 0$, the post-measurement state is
$$\rho_a = \frac{P_a \rho P_a}{\tr(P_a \rho)}.$$

## Remarks

Example: on $\C^2$ let $A = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and $\psi = (1, 1)/\sqrt{2}$.
Then $P_1 = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$, $p_1 = 1/2$ and $\psi_1 = (1, 0)$, a unit eigenvector of $A$ for the eigenvalue $1$.
Non-example: the vector $P_1 \psi = (1/\sqrt{2}, 0)$ is not the post-measurement state, since its norm is not $1$.
The update is idempotent: measuring $A$ again in the state $\psi_a$ gives $a$ with probability $1$.
The density operator form is also called the Lüders rule.
