---
tag: FJFFENN8SC
kind: definition
name: Two-port network
msc: [94C05]
defines: CEM0TDK67M
uses: [T7KRE7J3B4, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Two-port_network
---

## Definition

A *two-port network* is a circuit with four distinguished terminals grouped into two ports, $(1, 1')$ and $(2, 2')$.
It is subject to the port condition: for $k = 1, 2$, the current $I_k$ entering terminal $k$ equals the current leaving terminal $k'$.
The port variables are the voltages $V_k = \varphi(k) - \varphi(k')$ and the currents $I_k$, for $k = 1, 2$.
Consider sinusoidal steady state at a fixed frequency, with complex amplitudes.
The two-port is *linear* if the set of possible values of $(V_1, I_1, V_2, I_2)$ is a $2$-dimensional complex subspace of $\C^4$.
If this subspace is the graph of a linear map $(I_1, I_2) \mapsto (V_1, V_2)$, the [[matrix|0VD9ZSWWJG]] $Z$ with
$$\begin{pmatrix} V_1 \\ V_2 \end{pmatrix} = Z \begin{pmatrix} I_1 \\ I_2 \end{pmatrix}$$
is the *impedance matrix* ($z$-parameters) of the two-port.

## Remarks

Other choices of the independent pair give the admittance matrix $Y$ ($I = Y V$), the hybrid parameters ($h$) and the transmission or $ABCD$ parameters, which express $(V_1, I_1)$ through $(V_2, -I_2)$.
Example: the T-network has an impedance $z_a$ from $1$ to a middle node $m$ and an impedance $z_b$ from $m$ to $2$.
A third impedance $z_c$ joins $m$ to the common wire $1' = 2'$.
The current law at $m$ gives a current $I_1 + I_2$ through $z_c$, so $V_1 = (z_a + z_c) I_1 + z_c I_2$ and $V_2 = z_c I_1 + (z_b + z_c) I_2$.
Thus $Z = \begin{pmatrix} z_a + z_c & z_c \\ z_c & z_b + z_c \end{pmatrix}$, which is symmetric, as for every reciprocal two-port.
Non-example: four terminals with a single resistor joining $1$ to $2'$ do not form a two-port, since a current entering at $1$ leaves at $2'$ and not at $1'$.
A two-port may lack some parameter sets.
For example, the series impedance $z$ from $1$ to $2$, with $1'$ joined to $2'$, has $I_1 + I_2 = 0$, so it has no $Z$, but it has $Y = \frac{1}{z}\begin{pmatrix} 1 & -1 \\ -1 & 1 \end{pmatrix}$.
