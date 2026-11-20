---
tag: WMK89ZW2WZ
kind: proof
name: Proof of the reflection lemma and Witt cancellation
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
proves: 43VKGAA2H7
methods: [0NTF6DMVAP, 0WCP0PVET6, 0ASJVEFA9J]
uses: [0AXZNE5XNH, 0KAN330PAH, 0F6ES3BRYP, M2JH84VEY9, 05Q4JD6XEH]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Witt's cancellation theorem
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Proof

Let $\operatorname{char} F \neq 2$, and let $B$ be a [[nondegenerate|0KAN330PAH]] [[symmetric|0AXZNE5XNH]] form on $V$, with $\dim V = n$.

Part 1.
Let $q = B(w, w) \neq 0$.

1. $\tau_w$ is linear, because $x \mapsto B(x, w)$ is linear.
2. For $x, y \in V$, put $a = 2B(x, w) / q$ and $b = 2B(y, w) / q$. By bilinearity and symmetry, $B(\tau_w x, \tau_w y) = B(x, y) - b B(x, w) - a B(w, y) + ab\, q$.
3. Put $X = B(x, w) B(y, w) / q$. Then $b B(x, w) = 2X$, $a B(w, y) = 2X$ and $ab\, q = 4X$. So the last three terms sum to $-2X - 2X + 4X = 0$, and $B(\tau_w x, \tau_w y) = B(x, y)$.
4. $\tau_w(w) = w - 2w = -w$. For $x \in w^\perp$, $B(x, w) = 0$, so $\tau_w(x) = x$.
5. $\tau_w(\tau_w x) = \tau_w(x) - a\, \tau_w(w) = x - a w + a w = x$. So $\tau_w$ is its own inverse, hence bijective, and it is an isometry.

Part 2.
Let $B(x, x) = B(y, y) = c \neq 0$.

6. By bilinearity and symmetry, $B(x - y, x - y) + B(x + y, x + y) = 2B(x, x) + 2B(y, y) = 4c$.
7. $4c \neq 0$, since $\operatorname{char} F \neq 2$ and $c \neq 0$. So $B(x - y, x - y) \neq 0$ or $B(x + y, x + y) \neq 0$.
8. Case $w = x - y$ with $B(w, w) \neq 0$. Then $B(x, w) = c - B(x, y)$ and $B(w, w) = 2c - 2B(x, y) = 2B(x, w)$. So $\tau_w(x) = x - w = y$.
9. Case $w = x + y$ with $B(w, w) \neq 0$. Then $B(x, w) = c + B(x, y)$ and $B(w, w) = 2B(x, w)$. So $\tau_w(x) = x - w = -y$.
10. In case 9, $\tau_y(-y) = y$ by step 4, since $B(y, y) = c \neq 0$. So $\tau = \tau_y \circ \tau_{x + y}$ sends $x$ to $y$. By part 1, $\tau$ is an isometry.

Part 3, by induction on $k = \dim U$.
For $k = 0$, the identity of $V$ extends $\sigma$.

11. Let $k \geq 1$. If $B(u, u) = 0$ for all $u \in U$, then $2B(u, u') = B(u + u', u + u') - B(u, u) - B(u', u') = 0$ for all $u, u' \in U$. So $B$ is zero on $U \neq \{0\}$, which contradicts nondegeneracy on $U$.
12. So there is $u \in U$ with $B(u, u) \neq 0$. Put $y = \sigma(u)$. Then $B(y, y) = B(u, u)$, since $\sigma$ keeps $B$.
13. By part 2, there is an isometry $\rho$ of $V$ with $\rho(u) = y$. Put $\sigma' = \rho^{-1} \circ \sigma$. It is an isometry from $U$ onto $\rho^{-1}(U')$, with $\sigma'(u) = u$.
14. Let $V_0 = u^\perp$ and $U_0 = U \cap u^\perp$. $B$ is nondegenerate on $\operatorname{span}(u)$, so $V = \operatorname{span}(u) \oplus V_0$, by part 3 of the [[dimension statement for orthogonal complements|M2JH84VEY9]]. The same part, applied in the space $U$, gives $U = \operatorname{span}(u) \oplus U_0$.
15. $B$ is nondegenerate on $V_0$. If $z \in V_0$ and $B(z, V_0) = 0$, then also $B(z, u) = 0$, so $B(z, V) = 0$ and $z = 0$. In the same way, $B$ is nondegenerate on $U_0$.
16. For $z \in U_0$, $B(\sigma' z, u) = B(\sigma' z, \sigma' u) = B(z, u) = 0$. So $\sigma'$ maps $U_0$ into $V_0$, and $\sigma'(U_0)$ is nondegenerate, being isometric to $U_0$.
17. $\dim U_0 = k - 1$. By the induction hypothesis in the space $V_0$, $\sigma'|_{U_0}$ extends to an isometry $\tau_0$ of $V_0$.
18. Define $\tau'$ on $V = \operatorname{span}(u) \oplus V_0$ by $\tau'(a u + z) = a u + \tau_0(z)$. It is a linear bijection.
19. $B(\tau'(a u + z), \tau'(a' u + z')) = a a' B(u, u) + B(\tau_0 z, \tau_0 z') = B(a u + z, a' u + z')$, since the cross terms vanish on both sides. So $\tau'$ is an isometry.
20. $\tau'$ agrees with $\sigma'$ on $u$ and on $U_0$, hence on $U$. So $\tau = \rho \circ \tau'$ is an isometry of $V$ that agrees with $\rho \circ \sigma' = \sigma$ on $U$.

Part 4.

21. Let $f \colon V_1 \perp V_2 \to V_1 \perp V_3 =: W$ be an isometry. $W$ is nondegenerate, as an orthogonal sum of nondegenerate spaces.
22. In $W$, put $U = f(V_1)$ and $U' = V_1$. Both are nondegenerate, and $\sigma = f|_{V_1}$, read as a map $U' \to U$, gives an isometry $U' \to U$.
23. By part 3, $\sigma$ extends to an isometry $\tau$ of $W$, so $\tau(V_1) = f(V_1)$.
24. A bijective isometry maps the [[orthogonal complement|05Q4JD6XEH]] of a subspace onto the complement of its image, because $B(\tau x, \tau z) = B(x, z)$. So $\tau$ maps $V_1^\perp = V_3$ onto $f(V_1)^\perp$.
25. In the same way, $f$ maps $V_2 = V_1^\perp$, taken in $V_1 \perp V_2$, onto $f(V_1)^\perp$, taken in $W$.
26. So $\tau^{-1} \circ f$ maps $V_2$ isometrically onto $V_3$. $\blacksquare$

## Idea

A reflection moves one anisotropic vector to another vector of the same value $B(v, v)$.
After this move, the problem lives in the orthogonal complement of the vector, which has smaller dimension.
Cancellation follows, because an isometry that matches $V_1$ with $V_1$ must match their complements.

## Variants

In step 11 one can also take an orthogonal basis of $U$, and extend $\sigma$ one basis vector at a time.
