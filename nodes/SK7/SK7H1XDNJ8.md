---
tag: SK7H1XDNJ8
kind: proof
name: Proof of the Casorati–Weierstrass theorem by Riemann's theorem
msc: [30D30]
proves: 02HHNPC8ED
uses: [0DG0Z72CQD, 0YKDJBV26S, 0BSQDZWF34, 0P18JC72RE, 0WPQYW8MTE, 0D1C9Y1EXA]
sources:
  - url: https://en.wikipedia.org/wiki/Casorati%E2%80%93Weierstrass_theorem
    locator: Proof of the theorem
---

## Proof

We argue by contradiction.

1. Let $c$, $r$ and $f$ be as in the statement, with $c$ an [[essential singularity|0YKDJBV26S]] of $f$. Fix $\delta \in (0, r)$ and let $P = \set{z : 0 < \abs{z - c} < \delta}$.
2. Assume that $f(P)$ is not dense in $\C$. Then there are $w_0 \in \C$ and $\varepsilon > 0$ with $\abs{f(z) - w_0} \ge \varepsilon$ for each $z \in P$.
3. Let $g(z) = 1/(f(z) - w_0)$ on $P$. It is [[holomorphic|0DG0Z72CQD]] on $P$, as $f - w_0$ is holomorphic and nonzero there, and $\abs{g} \le 1/\varepsilon$.
4. By [[Riemann's theorem on removable singularities|0BSQDZWF34]], $g$ extends to a holomorphic function $G$ on $\set{z : \abs{z - c} < \delta}$. Also $G(z) \ne 0$ for $z \in P$.
5. Case $G(c) \ne 0$. By continuity, $G \ne 0$ on a disc $\abs{z - c} < \delta'$, so $w_0 + 1/G$ is holomorphic there. It equals $f$ for $0 < \abs{z - c} < \delta'$.
6. Define $F = f$ on $0 < \abs{z - c} < r$ and $F(c) = w_0 + 1/G(c)$. Near $c$, $F = w_0 + 1/G$, so $F$ is [[complex differentiable|0D1C9Y1EXA]] at $c$.
7. So $F$ is holomorphic on $\abs{z - c} < r$ and equals $f$ off $c$. Thus $c$ is a [[removable singularity|0P18JC72RE]] of $f$, which contradicts step 1.
8. Case $G(c) = 0$. By continuity, $G(z) \to 0$ as $z \to c$. Since $\abs{f(z)} \ge \abs{f(z) - w_0} - \abs{w_0} = 1/\abs{G(z)} - \abs{w_0}$ on $P$, we get $\abs{f(z)} \to \infty$.
9. So $c$ is a [[pole|0WPQYW8MTE]] of $f$, which also contradicts step 1.
10. Both cases are impossible, so $f(P)$ is dense in $\C$.
11. Let $w \in \C$. For each $n \ge 1$, apply step 10 with $\delta_n = \min(\delta, 1/n)$. It gives $z_n$ with $0 < \abs{z_n - c} < 1/n$ and $\abs{f(z_n) - w} < 1/n$.
12. Then $z_n \ne c$, $z_n \to c$ and $f(z_n) \to w$.

## Idea

If $f$ stayed away from a value $w_0$ near $c$, then $1/(f - w_0)$ would be bounded near $c$. Riemann's theorem removes its singularity. Turning back to $f$, the singularity of $f$ is removable or a pole, depending on whether this extension vanishes at $c$.
