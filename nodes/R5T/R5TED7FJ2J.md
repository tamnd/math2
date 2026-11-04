---
tag: R5TED7FJ2J
kind: proof
name: Proof of Goursat's theorem by repeated subdivision
msc: ["30E20"]
proves: 0BRG85WXYC
uses: [0DG0Z72CQD, 0D1C9Y1EXA, 00FWNP9TXY, 05RCDKHZM6, 0D37QFPEZE, 07PFYV65MB, 0EZBG8SKJM, 0YQ458D7PF, 0DJMGPN8K9, 0FJZMBX0ZZ]
sources:
  - url: https://math.iisc.ac.in/~vvdatar/courses/2020_Jan/Lecture_Notes/Lecture-7.pdf
    locator: Section 3
---

## Proof

We cut the rectangle into four, keep the worst quarter, and repeat. Near the limit point, $f$ is almost linear.

1. Since $f$ is [[holomorphic|0DG0Z72CQD]], it is [[complex differentiable|0D1C9Y1EXA]] at each $z_1 \in U$. So $f(z_1 + h) - f(z_1) = h \cdot \frac{f(z_1 + h) - f(z_1)}{h} \to 0 \cdot f'(z_1) = 0$. So $f$ is continuous on $U$.
2. For a closed rectangle $P = \set{x + iy : p_1 \le x \le q_1, \ p_2 \le y \le q_2} \subseteq U$ with $p_1 < q_1$ and $p_2 < q_2$, write $B(P) = \oint_{\partial P} f(z) \, dz$, the [[contour integral|00FWNP9TXY]] along $\partial P$ counterclockwise.
3. The bottom side is $s + i p_2$ with $s \in [p_1, q_1]$, and the right side is $q_1 + it$ with $t \in [p_2, q_2]$. The top and left sides are traversed backwards. Using [[additivity over intervals|05RCDKHZM6]] and the [[substitution|0D37QFPEZE]] $s \mapsto p_1 + q_1 - s$ for backward sides, we get the formula below.
   $$B(P) = \int_{p_1}^{q_1} f(s + i p_2) \, ds + i \int_{p_2}^{q_2} f(q_1 + it) \, dt - \int_{p_1}^{q_1} f(s + i q_2) \, ds - i \int_{p_2}^{q_2} f(p_1 + it) \, dt.$$
4. Cut $P$ by the lines $x = m_1$ and $y = m_2$, where $m_1 = (p_1 + q_1)/2$ and $m_2 = (p_2 + q_2)/2$. This gives four rectangles $P^{(1)}, \dots, P^{(4)}$.
5. Add the four formulas of step 3. Each inner half-segment appears twice with opposite signs, and the outer half-segments combine by additivity over intervals. So $B(P) = \sum_{k=1}^4 B(P^{(k)})$.
6. Let $\mathrm{p}(P)$ be the perimeter of $P$ and $d(P)$ its diagonal length. Any two points of $P$ are at distance at most $d(P)$. Each $P^{(k)}$ has perimeter $\mathrm{p}(P)/2$ and diagonal $d(P)/2$.
7. By step 5 and the [[triangle inequality|0FJZMBX0ZZ]], some $k$ has $\abs{B(P^{(k)})} \ge \abs{B(P)}/4$.
8. Put $Q_0 = Q$. Given $Q_n$, let $Q_{n+1}$ be a quarter of $Q_n$ chosen as in step 7. By induction, $\abs{B(Q)} \le 4^n \abs{B(Q_n)}$, $\mathrm{p}(Q_n) = 2^{-n} \mathrm{p}(Q)$ and $d(Q_n) = 2^{-n} d(Q)$.
9. Each $Q_n$ is closed and bounded, so it is [[compact|07PFYV65MB]]. The $Q_n$ are nonempty and nested. By [[Cantor's intersection theorem|0EZBG8SKJM]], there is a point $z_0 \in \bigcap_{n} Q_n$. Then $z_0 \in Q \subseteq U$.
10. Define $\psi(z) = \frac{f(z) - f(z_0)}{z - z_0} - f'(z_0)$ for $z \in U$, $z \ne z_0$, and $\psi(z_0) = 0$. Then $\psi(z) \to 0$ as $z \to z_0$.
11. Put $\ell(z) = f(z_0) + f'(z_0)(z - z_0)$. Then $f(z) = \ell(z) + \psi(z)(z - z_0)$ for all $z \in U$.
12. The function $\Phi(z) = f(z_0) z + f'(z_0) (z - z_0)^2/2$ satisfies $\Phi' = \ell$ on $\C$. Indeed $\frac{(z + h - z_0)^2 - (z - z_0)^2}{h} = 2(z - z_0) + h$.
13. Since $\partial Q_n$ is a closed path, the [[fundamental theorem of contour integration|0YQ458D7PF]] gives $\oint_{\partial Q_n} \ell(z) \, dz = 0$. By step 11, $B(Q_n) = \oint_{\partial Q_n} \psi(z)(z - z_0) \, dz$. The integrand $f - \ell$ is continuous.
14. Let $\varepsilon > 0$. By step 10 choose $\delta > 0$ with $\abs{\psi(z)} \le \varepsilon$ for $z \in U$, $\abs{z - z_0} < \delta$. Choose $n$ with $d(Q_n) < \delta$.
15. For $z \in \partial Q_n$, both $z$ and $z_0$ lie in $Q_n$. So $\abs{z - z_0} \le d(Q_n) < \delta$ and $\abs{\psi(z)(z - z_0)} \le \varepsilon \, d(Q_n)$.
16. The path $\partial Q_n$ has length $\mathrm{p}(Q_n)$. By the [[estimation lemma|0DJMGPN8K9]], $\abs{B(Q_n)} \le \varepsilon \, d(Q_n) \, \mathrm{p}(Q_n) = \varepsilon \, 4^{-n} d(Q) \, \mathrm{p}(Q)$.
17. By step 8, $\abs{B(Q)} \le 4^n \abs{B(Q_n)} \le \varepsilon \, d(Q) \, \mathrm{p}(Q)$.
18. Since $\varepsilon > 0$ is arbitrary, $B(Q) = 0$. That is, $\oint_{\partial Q} f(z) \, dz = 0$.

## Idea

Each subdivision loses at most a factor $4$ in the integral, while the product of diameter and perimeter also shrinks by a factor $4$. Near the limit point $f$ equals a linear function, whose integral vanishes, plus an error that is small compared to $\abs{z - z_0}$. So the error wins the race and the integral is $0$.
