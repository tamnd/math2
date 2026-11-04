---
tag: 5D4H3BBXSS
kind: proof
name: Proof of the Schwarz lemma by the maximum modulus principle
msc: [30C80]
proves: 0MB48XDBY3
uses: [0DG0Z72CQD, 0826SGV3R0, 045EWAXY9P, 0YMP521ZR5, 07PFYV65MB, 0V4DET59NW, 048F2P90WR]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz_lemma
    locator: Proof of the classical Schwarz lemma
---

## Proof

1. Let $\mathbb{D}$ and $f$ be as in the statement. By [[holomorphic functions are analytic|0826SGV3R0]] with $c = 0$ and radius $1$, $f(z) = \sum_{n \ge 0} a_n z^n$ for each $z \in \mathbb{D}$.
2. We have $a_0 = f(0) = 0$. By [[power series are holomorphic|0YMP521ZR5]], differentiating term by term at $0$ gives $f'(0) = a_1$.
3. The series $\sum_{n \ge 1} a_n z^{n-1}$ converges at each $z \in \mathbb{D}$: for $z \ne 0$ its partial sums are $1/z$ times those of the series for $f(z)$.
4. A power series that converges at $w$ has bounded terms there. So, by the definition of the [[radius of convergence|045EWAXY9P]], the series of step 3 has radius at least $1$.
5. Let $g(z) = \sum_{n \ge 1} a_n z^{n-1}$ on $\mathbb{D}$. By [[power series are holomorphic|0YMP521ZR5]], $g$ is [[holomorphic|0DG0Z72CQD]] on $\mathbb{D}$, hence continuous.
6. By steps 2 and 3, $g(z) = f(z)/z$ for $z \ne 0$, and $g(0) = a_1 = f'(0)$.
7. Claim: for $0 < r < 1$ and $\abs{z} \le r$, $\abs{g(z)} \le 1/r$. The disc $K_r = \set{z : \abs{z} \le r}$ is compact by the [[Heine–Borel theorem|07PFYV65MB]].
8. By [[attainment of bounds|0V4DET59NW]], $\abs{g}$ has a maximum on $K_r$ at some $z^*$.
9. If $\abs{z^*} < r$, then $\abs{g}$ has a local maximum at $z^*$ in the domain $\mathbb{D}$. By the [[maximum modulus principle|048F2P90WR]], $g$ is constant, so the maximum is also attained on $\abs{z} = r$.
10. So in all cases the maximum of $\abs{g}$ on $K_r$ is attained at a point $z'$ with $\abs{z'} = r$. There $\abs{g(z')} = \abs{f(z')}/r < 1/r$, since $f$ maps into $\mathbb{D}$. This proves the claim.
11. Fix $z \in \mathbb{D}$. Step 7 holds for every $r$ with $\abs{z} \le r < 1$. Letting $r \to 1$ gives $\abs{g(z)} \le 1$.
12. For $z \ne 0$, step 11 gives $\abs{f(z)} \le \abs{z}$, and this also holds at $z = 0$. At $z = 0$ it gives $\abs{f'(0)} \le 1$.
13. Now assume $\abs{f(z_0)} = \abs{z_0}$ for some $z_0 \ne 0$, or $\abs{f'(0)} = 1$. Then $\abs{g(z_0)} = 1$ or $\abs{g(0)} = 1$.
14. By step 11, $\abs{g} \le 1$ on $\mathbb{D}$. So $\abs{g}$ has a local maximum at an interior point of $\mathbb{D}$.
15. By the maximum modulus principle, $g$ is a constant $a$. By step 13, $\abs{a} = 1$.
16. Then $f(z) = z g(z) = a z$ for $z \ne 0$, and also for $z = 0$ since $f(0) = 0$.

## Idea

Dividing by $z$ removes the zero at the origin and gives a holomorphic $g$ with $g(0) = f'(0)$. On the circle $\abs{z} = r$ we have $\abs{g} < 1/r$, and the maximum modulus principle carries this bound inside. Letting $r \to 1$ gives $\abs{g} \le 1$, and equality at one interior point forces $g$ to be a constant of modulus one.
