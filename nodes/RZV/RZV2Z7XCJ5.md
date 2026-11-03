---
tag: RZV2Z7XCJ5
kind: statement
role: theorem
name: Wigner–Eckart theorem
msc: [81R05, "22E70", "20C35"]
uses: [VKWHPCHH6K, 60Q8MJM1MF, FX3NEFYFFN, E5P8AG6CK7, YJRJVZ998D]
about: [VKWHPCHH6K, 60Q8MJM1MF]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner%E2%80%93Eckart_theorem
same_as:
  wikidata: Q195133
  wikipedia: Wigner–Eckart theorem
---

## Statement

Let $\mathcal{H}$ be a Hilbert space with an [[angular momentum operator|VKWHPCHH6K]] $J = (J_1, J_2, J_3)$, and put $J_\pm = J_1 \pm iJ_2$.
Let $\lvert \alpha j m \rangle$ be an orthonormal family of standard angular momentum states, where $\alpha$ is an extra label.
This means $J^2 \lvert \alpha j m \rangle = \hbar^2 j(j+1) \lvert \alpha j m \rangle$ and $J_3 \lvert \alpha j m \rangle = \hbar m \lvert \alpha j m \rangle$.
It also means that $J_\pm$ acts with the Condon–Shortley convention.
Let $k \in \set{0, \frac12, 1, \ldots}$, and let $T_q$, $q = -k, \ldots, k$, be operators forming an irreducible tensor operator of rank $k$:
$$[J_3, T_q] = \hbar q\, T_q, \qquad [J_\pm, T_q] = \hbar \sqrt{k(k+1) - q(q \pm 1)}\; T_{q \pm 1}.$$
Then for all $\alpha, j, \alpha', j'$ there is a number $\langle \alpha' j' \Vert T \Vert \alpha j \rangle$ with the following property.
It does not depend on $m$, $m'$ or $q$, and
$$\langle \alpha' j' m' \rvert T_q \lvert \alpha j m \rangle = \langle j m, k q \mid j' m' \rangle \, \langle \alpha' j' \Vert T \Vert \alpha j \rangle$$
for all $m, m', q$, where $\langle j m, k q \mid j' m' \rangle$ is a [[Clebsch–Gordan coefficient|60Q8MJM1MF]].

## Remarks

The relations say that $T_q \lvert \alpha j m \rangle$ transforms under rotations like the vector $\lvert k q \rangle \otimes \lvert j m \rangle$ of $V_k \otimes V_j$, where $V_j$ is the [[irreducible representation|FX3NEFYFFN]] of [[SU(2)|E5P8AG6CK7]] of dimension $2j + 1$.
So the matrix elements define an intertwining map from $V_k \otimes V_j$ to $V_{j'}$.
By Schur's lemma such maps form a space of dimension at most one, spanned by the Clebsch–Gordan projection.
The reduced matrix element $\langle \alpha' j' \Vert T \Vert \alpha j \rangle$ is the scalar factor; conventions differ by a factor such as $\sqrt{2j' + 1}$.

Example: a vector operator, such as the position $x$ or the electric dipole operator, gives a tensor of rank $k = 1$ with $T_0 = x_3$ and $T_{\pm 1} = \mp \frac{1}{\sqrt2}(x_1 \pm i x_2)$.
The theorem gives the dipole selection rules: the matrix element vanishes unless $m' = m + q$ and $\abs{j - 1} \le j' \le j + 1$, with $j = j' = 0$ excluded.

## Explanations

### L1 human

Many quantities in atomic physics are matrix elements of an operator between two states of definite angular momentum.
The theorem splits each of them into two factors.
The first is geometric: it only depends on directions and is a universal Clebsch–Gordan coefficient.
The second is one physical number that does not depend on the orientation.
So one measurement or computation per pair of levels gives all the others.

### L2 human

The theorem is Schur's lemma applied to the rotation group.
It yields selection rules, since a Clebsch–Gordan coefficient vanishes unless $m' = m + q$ and $j'$ lies between $\abs{j - k}$ and $j + k$.
It also gives the ratios of intensities of spectral lines within a multiplet and the projection theorem for vector operators.
It is often written with the [[3-j symbol|YJRJVZ998D]] in place of the Clebsch–Gordan coefficient.
