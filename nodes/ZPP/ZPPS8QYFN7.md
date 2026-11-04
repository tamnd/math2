---
tag: ZPPS8QYFN7
kind: proof
name: Proof of Hurwitz's theorem by Rouché's theorem
msc: [30C15]
proves: 0SSKBQN58M
uses: [097KNJFJ7V, 0DG0Z72CQD, 0431RN0R1N, 064N002TX4, 0YBVKMYX0W, 0K83KEJ43P, 07PFYV65MB, 0V4DET59NW, 0D430QR02W]
sources:
  - url: https://en.wikipedia.org/wiki/Hurwitz%27s_theorem_(complex_analysis)
    locator: Proof
---

## Proof

1. Let $G$, $(f_k)$, $f$, $m$ and $z_0$ be as in the statement. By [[uniform limits of holomorphic functions are holomorphic|0431RN0R1N]], $f$ is [[holomorphic|0DG0Z72CQD]] on $G$.
2. The function $f$ is not identically zero on any disc around $z_0$. Otherwise the [[identity theorem|0YBVKMYX0W]] on the [[domain|097KNJFJ7V]] $G$ would give $f = 0$ on $G$. So the [[order|064N002TX4]] $m$ of $f$ at $z_0$ is finite.
3. By step 2 and the [[isolated zeros theorem|0K83KEJ43P]], case 2 holds at $z_0$. Choose $\rho_0 > 0$ with $\set{z : \abs{z - z_0} \le \rho_0} \subseteq G$ and $f(z) \ne 0$ for $0 < \abs{z - z_0} \le \rho_0$.
4. Let $0 < \rho \le \rho_0$. This is the meaning of "sufficiently small" below. Let $C$ be the circle $\abs{z - z_0} = \rho$.
5. The circle $C$ is compact by the [[Heine–Borel theorem|07PFYV65MB]], and $f \ne 0$ on $C$. By [[attainment of bounds|0V4DET59NW]], $\abs{f}$ has a minimum $\delta > 0$ on $C$.
6. Since $f_k \to f$ uniformly on the compact set $C$, there is $N$ with $\abs{f_k(z) - f(z)} < \delta$ for each $k \ge N$ and $z \in C$.
7. Fix $k \ge N$ and let $g = f_k - f$. It is holomorphic on $G$, an open set containing the closed disc $\abs{z - z_0} \le \rho$.
8. On $C$, $\abs{g} < \delta \le \abs{f}$. By [[Rouché's theorem|0D430QR02W]], $f$ and $f + g = f_k$ have the same number of zeros in $\abs{z - z_0} < \rho$, counted with order.
9. In this disc, $f$ has only the zero $z_0$, by step 3, and its order is $m$. So $f_k$ has exactly $m$ zeros in $\abs{z - z_0} < \rho$, counted with order, for each $k \ge N$.

## Idea

Choose a small circle around $z_0$ on which $f$ has no zeros, so $\abs{f}$ is at least some $\delta > 0$ there. For large $k$, $f_k$ differs from $f$ by less than $\delta$ on the circle. Rouché's theorem then says that $f_k$ and $f$ have the same number of zeros inside, which is $m$.
