---
tag: C87Q6P0QVB
kind: proof
name: Proof of the open mapping theorem by the maximum modulus principle
msc: [30A99]
proves: 03YEM7JEDN
uses: [097KNJFJ7V, 0DG0Z72CQD, 0YBVKMYX0W, 0K83KEJ43P, 07PFYV65MB, 0V4DET59NW, 0C9S13WKMF, 048F2P90WR]
sources:
  - url: https://en.wikipedia.org/wiki/Open_mapping_theorem_(complex_analysis)
    locator: Proof
---

## Proof

1. Let $D$ and $f$ be as in the statement, let $V \subseteq D$ be open, and let $w_0 \in f(V)$, say $w_0 = f(z_0)$ with $z_0 \in V$. We find a disc around $w_0$ inside $f(V)$.
2. The function $f - w_0$ does not vanish on any open disc with center $z_0$. Otherwise the [[identity theorem|0YBVKMYX0W]], applied to $f$ and the constant $w_0$, would make $f$ constant on the [[domain|097KNJFJ7V]] $D$.
3. By step 2 and the [[isolated zeros theorem|0K83KEJ43P]], case 2 holds for $f - w_0$ at $z_0$. Choose $\rho > 0$ so that $K = \set{z : \abs{z - z_0} \le \rho} \subseteq V$ and $f(z) \ne w_0$ for $0 < \abs{z - z_0} \le \rho$.
4. The circle $C = \set{z : \abs{z - z_0} = \rho}$ is compact by the [[Heine–Borel theorem|07PFYV65MB]]. By [[attainment of bounds|0V4DET59NW]], $\abs{f - w_0}$ has a minimum $\delta$ on $C$, and $\delta > 0$ by step 3.
5. Let $w \in \C$ with $\abs{w - w_0} < \delta/2$. Let $g = f - w$, which is [[holomorphic|0DG0Z72CQD]] on $D$.
6. On $C$, the [[reverse triangle inequality|0C9S13WKMF]] gives $\abs{g(z)} \ge \abs{f(z) - w_0} - \abs{w - w_0} > \delta - \delta/2 = \delta/2$.
7. At the center, $\abs{g(z_0)} = \abs{w_0 - w} < \delta/2$.
8. The set $K$ is compact. So $\abs{g}$ attains its minimum on $K$ at some $z_1 \in K$. By steps 6 and 7, $z_1 \notin C$, so $\abs{z_1 - z_0} < \rho$.
9. Assume that $g(z_1) \ne 0$. Then $\abs{g(z)} \ge \abs{g(z_1)} > 0$ for each $z \in K$, so $1/g$ is holomorphic on the open disc $B = \set{z : \abs{z - z_0} < \rho}$.
10. For each $z \in B$, $\abs{1/g(z)} \le \abs{1/g(z_1)}$. So $\abs{1/g}$ has a local maximum at $z_1$ in the domain $B$.
11. By the [[maximum modulus principle|048F2P90WR]], $1/g$ is constant on $B$. Then $f = g + w$ is constant on $B$.
12. By the identity theorem, $f$ would then be constant on $D$, which is false. So the assumption of step 9 fails, and $g(z_1) = 0$.
13. Thus $f(z_1) = w$ with $z_1 \in B \subseteq V$, so $w \in f(V)$.
14. By steps 5 and 13, the disc $\abs{w - w_0} < \delta/2$ lies in $f(V)$. Since $w_0 \in f(V)$ was arbitrary, $f(V)$ is open.

## Idea

Around a point $z_0$, the values of $f$ on a small circle stay at distance at least $\delta$ from $w_0 = f(z_0)$. For $w$ close to $w_0$, $\abs{f - w}$ is then smaller at the center than anywhere on the circle, so it has an interior minimum. By the maximum modulus principle applied to $1/(f - w)$, this minimum must be a zero, so $w$ is a value of $f$.
