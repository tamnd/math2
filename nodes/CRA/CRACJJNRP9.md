---
tag: CRACJJNRP9
kind: proof
name: Proof of Cavalieri's principle for Jordan measurable solids
msc: ["28A75"]
proves: 0GTZ2F3PQY
uses: [0565DC8RMK, 0QRQVH0CRW, 09FQT057T7, 021XJAQVDC, 080RWVVSB6, 069P20KYQT]
sources:
  - url: https://terrytao.files.wordpress.com/2011/01/measure-book1.pdf
    locator: Section 1.1
  - url: https://en.wikipedia.org/wiki/Cavalieri%27s_principle
    locator: Generalisation to measures
---

## Proof

We prove the formula first for simple sets, and then squeeze $E$ between simple sets.

1. Let $E$, $a \le b$, $E_z$ and $A(z)$ be as in the statement. We use the boxes, simple sets and measure $m$ of the definition of [[Jordan measure|0565DC8RMK]], in $\R^3$ and in $\R^2$. So $\operatorname{vol}(E) = m(E)$ and $A(z) = m(E_z)$.
2. Case $a = b$. The set $E$ is bounded, so $E \subseteq [-r, r) \times [-r, r) \times [a, a + \varepsilon)$ for some $r > 0$ and every $\varepsilon > 0$. Hence $m(E) \le m^*(E) \le 4 r^2 \varepsilon$ for every $\varepsilon > 0$. So $\operatorname{vol}(E) = 0 = \int_a^a A(z) \, dz$. From now on, let $a < b$.
3. Lemma 1: let $J$ be an interval with endpoints $c \le d$ in $[a, b]$, and let $\chi$ be its indicator function on $[a, b]$. Then $\chi$ is integrable and $\int_a^b \chi \, dz = d - c$.
4. Proof of Lemma 1. Let $\eta > 0$. Take the [[partition|069P20KYQT]] of $[a, b]$ whose points are $a$, $b$ and those of $c \pm \eta$, $d \pm \eta$ that lie in $(a, b)$.
5. Outside $[c - \eta, d + \eta]$ we have $\chi = 0$, so the upper [[Darboux sum|0QRQVH0CRW]] is at most $d - c + 2\eta$. On $[c + \eta, d - \eta]$ we have $\chi = 1$, so the lower Darboux sum is at least $d - c - 2\eta$.
6. Since $\eta$ is arbitrary, the upper and lower [[Darboux integrals|09FQT057T7]] of $\chi$ are both $d - c$. By [[the agreement of Darboux and Riemann integrals|021XJAQVDC]], Lemma 1 follows.
7. Lemma 2: let $S$ be a simple set in $\R^3$. Write $S$ as a disjoint union of nonempty boxes $Q_l = P_l \times I_l$, where $P_l$ is a half-open rectangle in $\R^2$ and $I_l = [c_l, d_l)$, for $l = 1, \dots, p$. Then for each $z \in \R$, $S_z = \set{(x, y) : (x, y, z) \in S}$ is a simple set and $m(S_z) = \sum_l \abs{P_l} \chi_l(z)$, where $\chi_l$ is the indicator function of $I_l$.
8. Proof of Lemma 2. We have $S_z = \bigcup_{l : z \in I_l} P_l$. These $P_l$ are pairwise disjoint: a common point $(x, y)$ of two of them would give a common point $(x, y, z)$ of two boxes $Q_l$. So $m(S_z) = \sum_{l : z \in I_l} \abs{P_l}$, which is the claim.
9. Also $m(S) = \sum_l \abs{Q_l} = \sum_l \abs{P_l} (d_l - c_l)$, by the definition of the volume of a box.
10. Let $S \subseteq E$ be a simple set, written as in Lemma 2. Each $Q_l$ is nonempty and lies in $E$, so $I_l \subseteq [a, b]$. By Lemma 1 and [[linearity of the integral|080RWVVSB6]], $z \mapsto m(S_z)$ is integrable on $[a, b]$ with integral $\sum_l \abs{P_l} (d_l - c_l) = m(S)$.
11. Let $T \supseteq E$ be a simple set, written as a disjoint union of nonempty boxes $P'_l \times [c'_l, d'_l)$. On $[a, b]$, the indicator of $[c'_l, d'_l)$ equals the indicator of the interval $[c'_l, d'_l) \cap [a, b]$, whose length is at most $d'_l - c'_l$.
12. By Lemma 1, Lemma 2 and linearity, $z \mapsto m(T_z)$ is integrable on $[a, b]$, with $\int_a^b m(T_z) \, dz \le \sum_l \abs{P'_l} (d'_l - c'_l) = m(T)$.
13. Let $z \in [a, b]$. Since $S_z \subseteq E_z \subseteq T_z$ and $S_z, T_z$ are simple, the definitions of inner and outer measure give $m(S_z) \le m_*(E_z) = A(z)$ and $A(z) = m^*(E_z) \le m(T_z)$.
14. Simple sets $S \subseteq E \subseteq T$ exist, since $E$ is bounded. Fix one such $T$. By step 13, $0 \le A(z) \le m(T_z) \le \sum_l \abs{P'_l}$, so $A$ is bounded on $[a, b]$.
15. Let $\underline{J}$ and $\overline{J}$ be the lower and upper Darboux integrals of $A$ on $[a, b]$. Let $\varphi \le A \le \psi$ with $\varphi, \psi$ integrable. Then each lower sum of $A$ is at least that of $\varphi$, and each upper sum of $A$ is at most that of $\psi$. So $\int_a^b \varphi \le \underline{J}$ and $\overline{J} \le \int_a^b \psi$.
16. By steps 10, 13 and 15, $m(S) \le \underline{J}$ for every simple $S \subseteq E$. Taking the supremum, $m_*(E) \le \underline{J}$.
17. By steps 12, 13 and 15, $\overline{J} \le m(T)$ for every simple $T \supseteq E$. Taking the infimum, $\overline{J} \le m^*(E)$.
18. Every lower sum is at most every upper sum, so $\underline{J} \le \overline{J}$. Since $E$ is Jordan measurable, $m_*(E) = m^*(E) = m(E)$. Steps 16 and 17 give $m(E) \le \underline{J} \le \overline{J} \le m(E)$.
19. So $\underline{J} = \overline{J} = m(E)$. By the agreement of Darboux and Riemann integrals, $A$ is integrable on $[a, b]$ and $\operatorname{vol}(E) = \int_a^b A(z) \, dz$.
20. If two such solids have $A(z)$ equal for each $z \in [a, b]$, the right sides agree. So the two solids have equal volume.

## Idea

For a finite union of boxes, the area of the cross-section at height $z$ is a step function of $z$, and its integral adds up the volumes of the boxes. A Jordan measurable solid is squeezed between such unions, from inside and outside. Their cross-sections squeeze the cross-sections of the solid, so the integral of $A(z)$ is squeezed to the volume.
