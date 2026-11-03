---
tag: 7YMY641GBN
kind: definition
name: Operator product expansion
msc: [81T40, 81T05, 17B69]
defines: EN02ENDWWD
uses: [W031YNVRE3, 99KYX4BDRD]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_product_expansion
---

## Definition

Let a [[quantum field theory|W031YNVRE3]] on $\R^d$ be given by the correlation functions of a family of local fields.
Let $\set{\mathcal{O}_k}$ be a basis of its local fields.
An *operator product expansion* for two fields $\mathcal{O}_i$ and $\mathcal{O}_j$ is an expansion with coefficient functions $C_{ij}^{\;k}$:
$$\mathcal{O}_i(x) \, \mathcal{O}_j(y) = \sum_k C_{ij}^{\;k}(x - y) \, \mathcal{O}_k(y).$$
It must hold inside correlation functions.
That is, for all fields $\mathcal{O}_{l_1}, \dots, \mathcal{O}_{l_n}$ and distinct points $z_1, \dots, z_n$,
$$\langle \mathcal{O}_i(x) \, \mathcal{O}_j(y) \prod_{m=1}^n \mathcal{O}_{l_m}(z_m) \rangle = \sum_k C_{ij}^{\;k}(x - y) \langle \mathcal{O}_k(y) \prod_{m=1}^n \mathcal{O}_{l_m}(z_m) \rangle$$
as $x \to y$, in the sense of an asymptotic expansion.

## Remarks

In a [[conformal field theory|99KYX4BDRD]] the sum converges whenever $\abs{x - y}$ is smaller than the distance from $y$ to every $z_m$.
Grouping each primary field with its derivatives, for scalar primaries the leading term of $C_{ij}^{\;k}$ is $\lambda_{ijk} \abs{x - y}^{\Delta_k - \Delta_i - \Delta_j}$, where the numbers $\lambda_{ijk}$ are the OPE coefficients.
The scaling dimensions $\Delta_k$ and the coefficients $\lambda_{ijk}$ form the CFT data.

Example: in two-dimensional conformal field theory, write $z$ for a complex coordinate.
The stress tensor $T$ of a theory with central charge $c$ has the operator product expansion
$$T(z) \, T(w) = \frac{c/2}{(z - w)^4} + \frac{2 T(w)}{(z - w)^2} + \frac{\partial T(w)}{z - w} + \text{regular terms},$$
which is equivalent to the commutation relations of the Virasoro algebra.
For the free boson with $\langle \phi(z)\phi(w) \rangle = -\log(z - w)$ for its holomorphic part, the current $\partial\phi$ satisfies $\partial\phi(z) \, \partial\phi(w) = -(z - w)^{-2} + \text{regular terms}$.

Non-example: the product $\phi(x)^2$ of a free field at one point is not obtained by setting $x = y$ in $\phi(x)\phi(y)$.
The coefficient of the identity field, $C(x - y) = \langle \phi(x)\phi(y) \rangle$, is singular at $x = y$.
The operator product expansion shows that one must subtract this term to define $\phi^2$.
