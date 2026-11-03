---
tag: K41C7EGQEQ
kind: definition
name: Jordan–Wigner transformation
msc: [82B20, 81V74, 81S05]
defines: 94PEKQHHHT
uses: [EY0X2NKA3S]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan%E2%80%93Wigner_transformation
---

## Definition

Let $N \ge 1$ and let $\mathcal{H} = (\C^2)^{\otimes N}$ be the [[tensor product|EY0X2NKA3S]] of $N$ copies of $\C^2$, with basis vectors $\lvert 0 \rangle = (1, 0)$ and $\lvert 1 \rangle = (0, 1)$ in each factor.
Let $Z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ and $a = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, so that $a \lvert 1 \rangle = \lvert 0 \rangle$ and $a \lvert 0 \rangle = 0$.
For an operator $T$ on $\C^2$ and $1 \le j \le N$, let $T_j$ be the operator on $\mathcal{H}$ that acts as $T$ on the $j$-th factor.
It acts as the identity on the other factors.
The *Jordan–Wigner transformation* defines, for $1 \le j \le N$, the operators
$$c_j = Z_1 Z_2 \cdots Z_{j-1} \, a_j, \qquad c_j^\dagger = Z_1 Z_2 \cdots Z_{j-1} \, a_j^\dagger.$$
These operators satisfy the canonical anticommutation relations
$$\set{c_i, c_j^\dagger} = \delta_{ij}, \qquad \set{c_i, c_j} = \set{c_i^\dagger, c_j^\dagger} = 0,$$
where $\set{A, B} = AB + BA$.

## Remarks

Check of the relations: on one site $a a^\dagger + a^\dagger a$ is the identity, and $Z a = a = -a Z$, so $Z$ and $a$ anticommute.
For $i < j$, the products $c_i c_j$ and $c_j c_i$ differ only at site $i$, where they contain $a_i Z_i$ and $Z_i a_i = -a_i Z_i$, so $c_i c_j = -c_j c_i$.
The occupation number is $n_j = c_j^\dagger c_j = (1 - Z_j)/2$, and the inverse map is $a_j = (1 - 2n_1) \cdots (1 - 2n_{j-1}) \, c_j$.

Example: with the Pauli matrices $X = a + a^\dagger$ and $Y = i(a^\dagger - a)$, one finds $X_j X_{j+1} + Y_j Y_{j+1} = 2(c_j^\dagger c_{j+1} + c_{j+1}^\dagger c_j)$.
So the XX chain $\sum_j (X_j X_{j+1} + Y_j Y_{j+1})$ with open ends is a quadratic form in the fermion operators.
The same computation applies to the [[transverse-field Ising model|PJZ35X5QHM]] and to the [[XXZ model|NR4JGQ7XTB]], where the $Z_j Z_{j+1}$ term becomes a fermion interaction.

Non-example: the operators $a_j$ without the string do not anticommute on different sites.
For instance $a_1 a_2 = a_2 a_1 \ne 0$, so $\set{a_1, a_2} = 2 a_1 a_2 \ne 0$.

Conventions differ between sources: some use $\sigma^+$ or $\sigma^-$ in place of $a$, or the string $\prod_{k<j}(-Z_k)$.
