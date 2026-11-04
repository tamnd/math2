---
tag: 5FBS58NMAK
kind: proof
name: Proof of the fundamental theorem of algebra by Liouville's theorem
msc: [12D10]
proves: 0JP0W07Y9A
uses: [09FTAET5Z4, 0YMP521ZR5, 0DG0Z72CQD, 0D1C9Y1EXA, 0419794R0T, 0EHKVRF4J6, 03HF5PMY5T, 0V4DET59NW, 07PFYV65MB]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_algebra
    locator: Complex-analytic proofs
---

## Proof

We argue by contradiction.

1. Let $n \ge 1$, let $a_0, \dots, a_n$ be [[complex numbers|09FTAET5Z4]] with $a_n \ne 0$, and let $p(z) = \sum_{k=0}^{n} a_k z^k$.
2. Assume that $p(z) \ne 0$ for each $z \in \C$.
3. The polynomial $p$ is a power series with finitely many nonzero coefficients, so its radius of convergence is $\infty$. By [[power series are holomorphic|0YMP521ZR5]], $p$ is [[holomorphic|0DG0Z72CQD]] on $\C$.
4. Then $p$ is continuous: $p(z + h) - p(z) = h \cdot \frac{p(z + h) - p(z)}{h} \to 0 \cdot p'(z) = 0$ as $h \to 0$.
5. Let $g = 1/p$, defined on $\C$ by step 2. For $z \in \C$ and small $h \ne 0$, $$\frac{g(z + h) - g(z)}{h} = - \frac{p(z + h) - p(z)}{h} \cdot \frac{1}{p(z + h) \, p(z)}.$$
6. By steps 3 and 4, the right side of step 5 tends to $-p'(z)/p(z)^2$. So $g$ is [[complex differentiable|0D1C9Y1EXA]] at each point, and $g$ is [[entire|0419794R0T]].
7. Let $S = \sum_{k=0}^{n-1} \abs{a_k}$ and $R_0 = \max(1, 2S/\abs{a_n})$. Let $\abs{z} \ge R_0$.
8. By the [[triangle inequality|03HF5PMY5T]], $\abs{p(z)} \ge \abs{a_n} \abs{z}^n - \sum_{k=0}^{n-1} \abs{a_k} \abs{z}^k$.
9. Since $\abs{z} \ge 1$, we have $\abs{z}^k \le \abs{z}^{n-1}$ for $k \le n - 1$. So $\abs{p(z)} \ge \abs{z}^{n-1} (\abs{a_n} \abs{z} - S)$.
10. Since $\abs{z} \ge 2S/\abs{a_n}$, we have $S \le \abs{a_n} \abs{z} / 2$. So $\abs{p(z)} \ge \abs{a_n} \abs{z}^n / 2 \ge \abs{a_n}/2$.
11. The closed disc $K = \set{z : \abs{z} \le R_0}$ is closed and bounded, so it is compact by the [[Heine–Borel theorem|07PFYV65MB]].
12. The function $\abs{p}$ is continuous by step 4. It [[attains its minimum|0V4DET59NW]] $m$ on $K$, and $m > 0$ by step 2.
13. By steps 10 and 12, $\abs{g(z)} \le \max(1/m, 2/\abs{a_n})$ for each $z \in \C$. So $g$ is bounded.
14. By [[Liouville's theorem|0EHKVRF4J6]], $g$ is constant. Hence $p = 1/g$ is constant, and $\abs{p}$ is bounded on $\C$.
15. But step 10 gives $\abs{p(z)} \ge \abs{a_n} \abs{z}^n / 2$ for $\abs{z} \ge R_0$. Since $n \ge 1$, this tends to $\infty$ as $\abs{z} \to \infty$.
16. Steps 14 and 15 contradict each other. So assumption 2 is false, and there is $z_0 \in \C$ with $p(z_0) = 0$.

## Idea

If $p$ had no zero, then $1/p$ would be an entire function. It is small far away, because $\abs{p}$ grows like $\abs{z}^n$, and it is bounded on a large disc by compactness. Liouville's theorem then makes $1/p$ constant, which a nonconstant polynomial cannot be.
