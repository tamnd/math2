---
tag: 73X2JGSE0W
kind: definition
name: Pick matrix
msc: ["30E05", 47A57]
defines: TSPTN464CM
uses: [8G5ABXRK85, 0EKZCX4K3P, 0N1MY1T0W9]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna–Pick_interpolation
---

## Definition

Let $\mathbb{D}$ be the open [[unit disc|8G5ABXRK85]].
Let $n \ge 1$, let $z_1, \ldots, z_n \in \mathbb{D}$ be distinct, and let $w_1, \ldots, w_n \in \C$.
The *Pick matrix* of the data $(z_i, w_i)$ is the $n \times n$ [[matrix|0N1MY1T0W9]] $P$ with entries
$$P_{ij} = \frac{1 - w_i \overline{w_j}}{1 - z_i \overline{z_j}}, \qquad 1 \le i, j \le n.$$

## Remarks

The denominators are not $0$, because $\abs{z_i \overline{z_j}} < 1$.
One has $\overline{P_{ji}} = P_{ij}$, so $P$ is a [[Hermitian matrix|0EKZCX4K3P]].
By [[Nevanlinna–Pick interpolation|4VMSSYB5DN]], with all $w_i \in \mathbb{D}$, there is a holomorphic $f \colon \mathbb{D} \to \mathbb{D}$ with $f(z_i) = w_i$ if and only if $P$ is [[positive semidefinite|0880F9EQCP]].

Example: $n = 2$, $z_1 = 0$, $w_1 = 0$, $z_2 = a$, $w_2 = b$ with $a \ne 0$.
Then $P = \begin{pmatrix} 1 & 1 \\ 1 & \frac{1 - \abs{b}^2}{1 - \abs{a}^2} \end{pmatrix}$, and $\det P = \frac{\abs{a}^2 - \abs{b}^2}{1 - \abs{a}^2}$.
So $P$ is positive semidefinite exactly when $\abs{b} \le \abs{a}$, which matches the [[Schwarz lemma|0MB48XDBY3]].

Non-example: the data must have $z_i \in \mathbb{D}$.
For $z_1 = 1$ on the unit circle the entry $P_{11}$ would have denominator $1 - \abs{z_1}^2 = 0$, so no Pick matrix is defined.

The entries are the values $(1 - w_i \overline{w_j}) k(z_i, z_j)$, where $k(z, w) = \frac{1}{1 - z \bar w}$ is the reproducing kernel of the [[Hardy space|PNNNFJVF6W]] $H^2$.
