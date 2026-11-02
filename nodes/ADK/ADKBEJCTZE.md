---
tag: ADKBEJCTZE
kind: definition
name: 3-j symbol
msc: [33C80, 81R05, "22E70"]
defines: YJRJVZ998D
uses: [E5P8AG6CK7, FX3NEFYFFN, 0BF2DE2SYK, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/3-j_symbol
---

## Definition

For $j \in \set{0, \frac12, 1, \dots}$, let $V_j$ be the [[irreducible representation|FX3NEFYFFN]] of [[SU(2)|E5P8AG6CK7]] of dimension $2j+1$, with the standard [[orthonormal basis|0S9GGTR0EX]] $\lvert j m \rangle$, $m = j, j-1, \dots, -j$, of the Condon–Shortley convention.
Let $j_1, j_2, J$ be such that $V_J$ occurs in the [[tensor product|0BF2DE2SYK]] $V_{j_1} \otimes V_{j_2}$, that is, $\abs{j_1 - j_2} \le J \le j_1 + j_2$ and $j_1 + j_2 + J \in \Z$.
Let $\lvert J M \rangle$ be the basis of a copy of $V_J$ in $V_{j_1} \otimes V_{j_2}$.
The *Clebsch–Gordan coefficients* $\langle j_1 m_1, j_2 m_2 \mid J M \rangle$ are its coordinates:
$$\lvert J M \rangle = \sum_{m_1, m_2} \langle j_1 m_1, j_2 m_2 \mid J M \rangle\, \lvert j_1 m_1 \rangle \otimes \lvert j_2 m_2 \rangle,$$
where the copy is fixed by the convention that all coefficients are real and $\langle j_1 j_1, j_2 (J - j_1) \mid J J \rangle > 0$.
The *3-j symbol* is
$$\begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} = \frac{(-1)^{j_1 - j_2 - m_3}}{\sqrt{2 j_3 + 1}}\, \langle j_1 m_1, j_2 m_2 \mid j_3, -m_3 \rangle.$$
It is set to $0$ when $j_1, j_2, j_3$ fail the conditions above or some $\abs{m_i} > j_i$.

## Remarks

The symbol is $0$ unless $m_1 + m_2 + m_3 = 0$, since $J_z$ is additive on tensor products.
It is unchanged by an even permutation of its columns and is multiplied by $(-1)^{j_1 + j_2 + j_3}$ by an odd permutation.
The orthogonality relation reads $\sum_{m_1, m_2} (2 j_3 + 1) \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} \begin{pmatrix} j_1 & j_2 & j_3' \\ m_1 & m_2 & m_3' \end{pmatrix} = \delta_{j_3 j_3'} \delta_{m_3 m_3'}$.

Example: for $j_1 = j_2 = \frac12$ and $J = 0$, the invariant vector is $\lvert 0 0 \rangle = \frac{1}{\sqrt2}\left(\lvert \tfrac12 \tfrac12 \rangle \otimes \lvert \tfrac12, -\tfrac12 \rangle - \lvert \tfrac12, -\tfrac12 \rangle \otimes \lvert \tfrac12 \tfrac12 \rangle\right)$.
So $\begin{pmatrix} \frac12 & \frac12 & 0 \\ \frac12 & -\frac12 & 0 \end{pmatrix} = \frac{(-1)^{0}}{1} \cdot \frac{1}{\sqrt2} = \frac{1}{\sqrt2}$.
This agrees with the general value $\begin{pmatrix} j & j & 0 \\ m & -m & 0 \end{pmatrix} = \frac{(-1)^{j-m}}{\sqrt{2j+1}}$.

Non-example: $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix} = 0$, because $m_1 + m_2 + m_3 = 2 \ne 0$.

Physicists write the coefficients $\langle j_1 m_1, j_2 m_2 \mid J M \rangle$ also as $C^{J M}_{j_1 m_1 j_2 m_2}$.
