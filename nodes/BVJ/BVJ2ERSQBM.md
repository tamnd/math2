---
tag: BVJ2ERSQBM
kind: definition
name: Bloch–Wigner function
msc: ["33B30", "11G55"]
defines: Q8K5MWEXB9
uses: [G0X0NWSDB7, 02QGGD5G87]
sources:
  - url: https://en.wikipedia.org/wiki/Polylogarithm
---

## Definition

Let $\operatorname{Li}_2$ be the [[dilogarithm|G0X0NWSDB7]], taken as its principal branch on $\C \setminus [1, \infty)$.
For $z \in \C \setminus [1, \infty)$, let $\arg(1 - z) \in (-\pi, \pi)$ be the principal argument of $1 - z$, as for the [[complex logarithm|02QGGD5G87]].
The *Bloch–Wigner function* is
$$D(z) = \operatorname{Im}\big(\operatorname{Li}_2(z)\big) + \arg(1 - z) \, \log \abs{z}, \qquad z \in \C \setminus \big(\set{0} \cup [1, \infty)\big),$$
extended to all of $\C$ by continuity, with $D(0) = D(1) = 0$.

## Remarks

The function is real-analytic on $\C \setminus \set{0, 1}$ and continuous on $\C$.
Across $(1, \infty)$ the term $\operatorname{Im} \operatorname{Li}_2$ jumps by $2\pi \log x$ at the point $x$, and the term $\arg(1 - z) \log \abs{z}$ jumps by $-2\pi \log x$, so the extension is well defined.

Example: for $z = e^{i\theta}$ one has $\log \abs{z} = 0$, so $D(e^{i\theta}) = \operatorname{Im} \operatorname{Li}_2(e^{i\theta}) = \operatorname{Cl}_2(\theta)$, the [[Clausen function|AVS6G54711]].
In particular $D(e^{i\pi/3}) = \operatorname{Cl}_2(\pi/3) \approx 1.01494$.

Non-example: the function $\operatorname{Im} \operatorname{Li}_2(z)$ alone does not extend continuously across $(1, \infty)$, because of the jump $2\pi \log x$ described above.

Symmetries: $D(\bar z) = -D(z)$, and
$$D(z) = D\left(1 - \tfrac1z\right) = D\left(\tfrac{1}{1-z}\right) = -D\left(\tfrac1z\right) = -D(1 - z) = -D\left(\tfrac{z}{z-1}\right).$$
For $\operatorname{Im} z > 0$, $D(z)$ is the hyperbolic volume of the ideal tetrahedron with vertices $0, 1, \infty, z$.
