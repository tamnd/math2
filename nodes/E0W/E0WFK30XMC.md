---
tag: E0WFK30XMC
kind: definition
name: Clebsch–Gordan coefficients
msc: [81R05, 17B10, "22E70"]
defines: 60Q8MJM1MF
uses: [TZAZ163QGK, HFW8642GBK, 0BF2DE2SYK, 8WBY6R28CR]
sources:
  - url: https://en.wikipedia.org/wiki/Clebsch%E2%80%93Gordan_coefficients
---

## Definition

For $j \in \set{0, \tfrac{1}{2}, 1, \tfrac{3}{2}, \dots}$, let $V_j$ be the [[irreducible|HFW8642GBK]] [[representation|TZAZ163QGK]] of $\mathfrak{su}(2)$ of dimension $2j + 1$, with operators $J_z$ and $J_\pm$.
Let $\lvert j, m \rangle$, $m = -j, -j + 1, \dots, j$, be its standard basis: $J_z \lvert j, m \rangle = m \lvert j, m \rangle$ and $J_\pm \lvert j, m \rangle = \sqrt{j(j + 1) - m(m \pm 1)}\, \lvert j, m \pm 1 \rangle$.
In the [[tensor product|0BF2DE2SYK]] $V_{j_1} \otimes V_{j_2}$, the operators act by $J = J^{(1)} \otimes 1 + 1 \otimes J^{(2)}$.
For each $J$ with $\abs{j_1 - j_2} \le J \le j_1 + j_2$ and $J - j_1 - j_2 \in \Z$, there is a copy of $V_J$ in $V_{j_1} \otimes V_{j_2}$.
It has a standard basis $\lvert J, M \rangle$, fixed up to one overall phase.
The Condon–Shortley convention fixes this phase by requiring the coefficient of $\lvert j_1, j_1 \rangle \otimes \lvert j_2, J - j_1 \rangle$ in $\lvert J, J \rangle$ to be real and positive.
The *Clebsch–Gordan coefficients* are the numbers $\langle j_1 m_1; j_2 m_2 \mid J M \rangle$ in
$$\lvert J, M \rangle = \sum_{m_1, m_2} \langle j_1 m_1; j_2 m_2 \mid J M \rangle \, \lvert j_1, m_1 \rangle \otimes \lvert j_2, m_2 \rangle.$$

## Remarks

The coefficients are real, and they vanish unless $M = m_1 + m_2$.
For fixed $j_1, j_2$ they form an orthogonal matrix.
Example: $j_1 = j_2 = \tfrac{1}{2}$, with $\lvert \uparrow \rangle = \lvert \tfrac12, \tfrac12 \rangle$ and $\lvert \downarrow \rangle = \lvert \tfrac12, -\tfrac12 \rangle$.
Then $\lvert 1, 1 \rangle = \lvert \uparrow\uparrow \rangle$, $\lvert 1, 0 \rangle = (\lvert \uparrow\downarrow \rangle + \lvert \downarrow\uparrow \rangle)/\sqrt{2}$, and $\lvert 0, 0 \rangle = (\lvert \uparrow\downarrow \rangle - \lvert \downarrow\uparrow \rangle)/\sqrt{2}$.
Check for $\lvert 0, 0 \rangle$: $J_+ \lvert \downarrow \rangle = \lvert \uparrow \rangle$ and $J_+ \lvert \uparrow \rangle = 0$, so $J_+ \lvert 0, 0 \rangle = (\lvert \uparrow\uparrow \rangle - \lvert \uparrow\uparrow \rangle)/\sqrt{2} = 0$, as for a vector of spin $0$.
So $\langle \tfrac12\, \tfrac12; \tfrac12\, {-\tfrac12} \mid 0\, 0 \rangle = 1/\sqrt{2}$.
Non-example: $(\lvert \downarrow\uparrow \rangle - \lvert \uparrow\downarrow \rangle)/\sqrt{2}$ also spans the spin $0$ part, but its coefficient of $\lvert \uparrow\downarrow \rangle$ is negative, so it breaks the Condon–Shortley convention.
The Wigner $3j$ symbols are the same numbers up to a sign and a factor $\sqrt{2J + 1}$.
