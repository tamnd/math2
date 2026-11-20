---
tag: XRXMHP9Z76
kind: proof
name: Proof of Witt's theorem
msc: ["11E04", "15A63"]
topics: [DYAK7YMK7B]
audience: grad
proves: CCB8VNQCV0
methods: [0ASJVEFA9J, 01XM7JEKHY]
uses: [43VKGAA2H7, M2JH84VEY9, 0AXZNE5XNH, 0M4SXE5WW3, MZHFGPV1YT]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Statement
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Proof

Let $\operatorname{char} F \neq 2$, and let $B$ be nondegenerate and [[symmetric|0AXZNE5XNH]] on $V$.
For a subspace $X$, $X^\perp = \{v : B(x, v) = 0 \text{ for all } x \in X\}$, and $\operatorname{rad}(X) = X \cap X^\perp$ is the radical of $B$ on $X$.

Part 1, by induction on $d = \dim \operatorname{rad}(U)$, for all $U$, $W$ and $\sigma$ at once.

1. Let $d = 0$. Then $B$ is nondegenerate on $U$. $W$ is isometric to $U$ through $\sigma$, so $B$ is nondegenerate on $W$. Part 3 of the [[reflection lemma|43VKGAA2H7]] gives $\tau$.
2. Let $d \geq 1$. Take $r \in \operatorname{rad}(U)$ with $r \neq 0$. [[Extend|0M4SXE5WW3]] $r$ to a basis of $U$, and let $U_1$ be the span of the other basis vectors. Then $U = U_1 \oplus Fr$.
3. $B$ is nondegenerate and symmetric, hence reflexive. So $(U_1^\perp)^\perp = U_1$, by part 4 of the [[dimension statement for orthogonal complements|M2JH84VEY9]].
4. $r \notin U_1$, so $r \notin (U_1^\perp)^\perp$. So there is $s_0 \in U_1^\perp$ with $B(s_0, r) \neq 0$. After scaling, $B(s_0, r) = 1$.
5. $r \in \operatorname{rad}(U)$, so $B(r, x) = 0$ for all $x \in U$. In particular $r \in U_1^\perp$ and $B(r, r) = 0$.
6. Put $s = s_0 - \frac{B(s_0, s_0)}{2} r$. Then $s \in U_1^\perp$ by steps 4 and 5, and $B(r, s) = 1$ since $B(r, r) = 0$.
7. $B(s, s) = B(s_0, s_0) - B(s_0, s_0) B(r, s_0) + \frac{B(s_0, s_0)^2}{4} B(r, r) = 0$, by symmetry and step 5. So $s$ is [[isotropic|MZHFGPV1YT]].
8. Put $r' = \sigma(r)$ and $W_1 = \sigma(U_1)$. Then $W = W_1 \oplus F r'$, and $B(r', \sigma x) = B(r, x) = 0$ for $x \in U$. So $r' \in \operatorname{rad}(W)$, and $r' \neq 0$.
9. Steps 3 to 7, applied to $W_1$ and $r'$, give $s' \in W_1^\perp$ with $B(r', s') = 1$ and $B(s', s') = 0$.
10. $s \notin U$, since $B(r, s) = 1$ but $B(r, U) = 0$. So $\tilde U = U \oplus Fs$ has dimension $\dim U + 1$. In the same way, $\tilde W = W \oplus F s'$ has dimension $\dim W + 1$.
11. Define $\tilde \sigma \colon \tilde U \to \tilde W$ by $\tilde \sigma(x + c s) = \sigma(x) + c s'$ for $x \in U$, $c \in F$. It is a linear bijection.
12. $\tilde \sigma$ keeps $B$ on pairs of elements of $U$, since $\sigma$ does.
13. For $x_1 \in U_1$: $B(x_1, s) = 0 = B(\sigma x_1, s')$, since $s \in U_1^\perp$ and $s' \in W_1^\perp$.
14. $B(r, s) = 1 = B(r', s')$ and $B(s, s) = 0 = B(s', s')$. With $U = U_1 \oplus Fr$, steps 12 to 14 and bilinearity show that $\tilde \sigma$ is an isometry.
15. Let $z = x + c s \in \operatorname{rad}(\tilde U)$, with $x \in U$. Then $0 = B(r, z) = B(r, x) + c B(r, s) = c$. So $z = x \in U$.
16. $z$ is orthogonal to $\tilde U \supseteq U$, so $z \in \operatorname{rad}(U)$. Also $r \in \operatorname{rad}(U)$, but $r \notin \operatorname{rad}(\tilde U)$, since $B(r, s) = 1$.
17. So $\operatorname{rad}(\tilde U) \subsetneq \operatorname{rad}(U)$, and $\dim \operatorname{rad}(\tilde U) < d$.
18. By the induction hypothesis, $\tilde \sigma$ extends to an isometry $\tau$ of $V$. Then $\tau$ also extends $\sigma$, since $\tilde \sigma$ agrees with $\sigma$ on $U$.

Part 2.

19. Take bases $(a_1, \dots, a_k)$ of $W_1$ and $(b_1, \dots, b_k)$ of $W_2$. Let $\sigma \colon W_1 \to W_2$ be the linear bijection with $\sigma(a_i) = b_i$.
20. $B$ is zero on $W_1$ and on $W_2$, so $B(\sigma x, \sigma y) = 0 = B(x, y)$ for $x, y \in W_1$. So $\sigma$ is an isometry.
21. By part 1, $\sigma$ extends to an isometry $\tau$ of $V$, and $\tau(W_1) = \sigma(W_1) = W_2$. $\blacksquare$

## Idea

A degenerate subspace $U$ has radical vectors $r$, which pair to zero with all of $U$.
Each such $r$ gets an isotropic partner $s$ outside $U$, and the image $\sigma(r)$ gets a partner $s'$ in the same way.
Adding $s$ and $s'$ removes one dimension of the radical, and the nondegenerate case is the reflection lemma.

## Variants

One can also prove part 1 by induction on $\dim U$ alone, with reflections in each step.
This is the usual proof in many books, and it needs extra care when $U$ is degenerate.
