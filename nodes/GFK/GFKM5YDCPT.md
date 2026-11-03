---
tag: GFKM5YDCPT
kind: definition
name: Next-generation matrix
msc: [92D30, 15B48]
defines: KY7W9E9ECS
uses: [BX5ZA16MM6, VY4H52692D, 0G4X36AE0X, 3PR407YKHN, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Next-generation_matrix
---

## Definition

Consider a [[compartmental model|BX5ZA16MM6]] whose state is $(x, y)$, where $x \in [0, \infty)^m$ lists the $m$ infected compartments and $y$ the others.
Write the equations of the infected compartments as $x_i' = \mathcal{F}_i(x, y) - \mathcal{V}_i(x, y)$ for $i = 1, \dots, m$.
Here $\mathcal{F}_i$ is the rate of new infections in compartment $i$, and $\mathcal{V}_i$ collects all other transfers into and out of compartment $i$.
Let $(0, y_0)$ be a disease-free [[equilibrium point|0G4X36AE0X]].
Define the $m \times m$ [[matrices|0N1MY1T0W9]]
$$F = \left[ \frac{\partial \mathcal{F}_i}{\partial x_j}(0, y_0) \right], \qquad V = \left[ \frac{\partial \mathcal{V}_i}{\partial x_j}(0, y_0) \right],$$
and assume that $V$ is invertible.
The *next-generation matrix* is $K = F V^{-1}$.

## Remarks

Under the usual hypotheses, $F$ has nonnegative entries and $V^{-1}$ has nonnegative entries, so $K$ has nonnegative entries.
The entry $K_{ij}$ is the expected number of new infections in compartment $i$ caused by one host that entered compartment $j$.
The [[basic reproduction number|VY4H52692D]] is the [[spectral radius|3PR407YKHN]] $R_0 = \rho(F V^{-1})$.

Example: in the [[SEIR model|P1ANHAY6XY]] the infected compartments are $E$ and $I$, and at the disease-free equilibrium $S = N$.
New infections enter $E$ at rate $\beta S I / N$, so $F = \begin{pmatrix} 0 & \beta \\ 0 & 0 \end{pmatrix}$ and $V = \begin{pmatrix} \sigma & 0 \\ -\sigma & \gamma \end{pmatrix}$.
Then $V^{-1} = \frac{1}{\sigma \gamma} \begin{pmatrix} \gamma & 0 \\ \sigma & \sigma \end{pmatrix}$ and $K = \begin{pmatrix} \beta / \gamma & \beta / \gamma \\ 0 & 0 \end{pmatrix}$.
The eigenvalues of $K$ are $\beta/\gamma$ and $0$, so $R_0 = \beta / \gamma$.

Non-example: if $\mathcal{V}$ has no outflow from some infected compartment, then $V$ has a zero row and is not invertible.
For instance, an SI model, in which infected hosts never leave $I$, has $V = 0$, and the next-generation matrix is not defined.

The splitting into $\mathcal{F}$ and $\mathcal{V}$ is not unique, and different splittings can give different matrices with the same threshold at $1$.
