---
tag: Y3VNY93EXZ
kind: proof
name: Proof of the Witt decomposition
msc: ["15A63", "11E04"]
topics: [DYAK7YMK7B]
audience: grad
proves: BPMRSPB6GD
methods: [0ASJVEFA9J, 0J0XBKG64S, 01XM7JEKHY]
uses: [SN50886T80, 43VKGAA2H7, M2JH84VEY9, 1X5PZSK44P, MZHFGPV1YT, 0W4FSW1TVB]
sources:
  - url: https://en.wikipedia.org/wiki/Witt's_theorem
    locator: Witt's decomposition theorem
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Proof

We split off hyperbolic planes while isotropic vectors remain, cancel common planes to get uniqueness, and build planes around a totally isotropic subspace to get the Witt index.
Let $\operatorname{char} F \neq 2$, and let $B$ be nondegenerate and symmetric on $V$, with $\dim V = n$.
For subspaces, $X \perp Y$ means $X \oplus Y$ with $B(x, y) = 0$ for all $x \in X$ and $y \in Y$.

Part 1, by induction on $n$.

1. If $V$ is [[anisotropic|MZHFGPV1YT]], which includes the case $n = 0$, we take $m = 0$ and $V_{\mathrm{an}} = V$.
2. Otherwise there is an isotropic vector $u$. By the [[hyperbolic plane statement|SN50886T80]], $u$ lies in a [[hyperbolic plane|1X5PZSK44P]] $H_1$, and $V = H_1 \oplus H_1^\perp$ with $B$ nondegenerate on $H_1^\perp$.
3. By the definition of $H_1^\perp$, $B(H_1, H_1^\perp) = 0$. So $V = H_1 \perp H_1^\perp$.
4. Since $\dim H_1^\perp = n - 2 < n$, the induction hypothesis gives $H_1^\perp = H_2 \perp \dots \perp H_m \perp V_{\mathrm{an}}$.
5. Steps 3 and 4 give $V = H_1 \perp H_2 \perp \dots \perp H_m \perp V_{\mathrm{an}}$.

Part 2.

6. Each hyperbolic plane has a basis with the matrix $\begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$. So any two hyperbolic planes are isometric, and so are any two orthogonal sums of $k$ hyperbolic planes. We write $kH$ for such a sum.
7. Let $V \cong mH \perp A \cong m'H \perp A'$ with $A, A'$ anisotropic. The roles are symmetric, so we may assume $m \leq m'$.
8. Then $mH \perp A \cong mH \perp \bigl( (m' - m)H \perp A' \bigr)$.
9. All these summands are nondegenerate: a hyperbolic plane has an invertible matrix, an anisotropic space has no nonzero radical vector, and an orthogonal sum of nondegenerate spaces is nondegenerate.
10. By [[Witt cancellation|43VKGAA2H7]], applied $m$ times, $A \cong (m' - m)H \perp A'$.
11. Suppose that $m' > m$. Then the right side contains a nonzero isotropic vector of a hyperbolic plane, and the isometry carries it to a nonzero isotropic vector of $A$. This contradicts that $A$ is anisotropic.
12. So $m = m'$, and step 10 gives $A \cong A'$.

Part 3.

13. Let $W$ be a totally isotropic subspace with basis $w_1, \dots, w_k$. Define $\varphi \colon V \to F^k$ by $\varphi(v) = (B(w_1, v), \dots, B(w_k, v))$.
14. The kernel of $\varphi$ is $W^\perp$, which has dimension $n - k$ by part 2 of the [[dimension statement for orthogonal complements|M2JH84VEY9]]. By the [[rank-nullity theorem|0W4FSW1TVB]], $\varphi$ has rank $k$, so it is onto.
15. So there is $z_1$ with $B(w_1, z_1) = 1$ and $B(w_j, z_1) = 0$ for $j \geq 2$. Put $c = B(z_1, z_1)$ and $v_1 = z_1 - \tfrac{c}{2} w_1$.
16. Then $B(w_1, v_1) = 1$, and $B(w_j, v_1) = 0$ for $j \geq 2$, since $B(w_j, w_1) = 0$. By symmetry, $B(v_1, v_1) = c - 2 \cdot \tfrac{c}{2} B(w_1, z_1) + \tfrac{c^2}{4} B(w_1, w_1) = c - c + 0 = 0$.
17. So $P_1 = \operatorname{span}(w_1, v_1)$ is a hyperbolic plane, and by the hyperbolic plane statement $V = P_1 \perp V_1$ with $V_1 = P_1^\perp$ nondegenerate.
18. By step 16 and $B(w_j, w_1) = 0$, the vectors $w_2, \dots, w_k$ lie in $V_1$, and they span a totally isotropic subspace of $V_1$.
19. Induction on $k$, with steps 13 to 18 applied in $V_1$, gives $V = P_1 \perp \dots \perp P_k \perp V'$, with each $P_i$ hyperbolic, $w_i \in P_i$ and $V'$ nondegenerate.
20. Now let $W$ be maximal, and suppose that $V'$ has a nonzero isotropic vector $z$. Then $B(w_i, z) = 0$ for each $i$, since $z \in V'$, and $B(z, z) = 0$.
21. Also $z \notin W$, since the sum in step 19 is direct and $W \subseteq P_1 \perp \dots \perp P_k$. So $W + Fz$ is totally isotropic of dimension $k + 1$, which contradicts maximality.
22. So $V'$ is anisotropic, and step 19 is a decomposition as in part 1 with $k$ planes. By part 2, $k = m$.

Part 4.

23. The subspace $H_1 \perp \dots \perp H_m$ has dimension $2m$ and lies in $V$, so $2m \leq n$.
24. If $m = 0$, then $V = V_{\mathrm{an}}$ is anisotropic. If $m \geq 1$, then $H_1$ contains a nonzero isotropic vector, so $V$ is not anisotropic. $\blacksquare$

## Idea

Each isotropic vector has a partner, and the pair spans a hyperbolic plane that splits off with a nondegenerate complement.
Repeat until no isotropic vector is left, and what remains is the anisotropic part.
Cancellation shows that the number of planes and the remaining part do not depend on the choices, because a leftover hyperbolic plane would put an isotropic vector into an anisotropic space.
For the index, every basis vector of a totally isotropic subspace gets its own partner, so a maximal one fills exactly the hyperbolic part.

## Variants

Part 3 also follows from [[Witt's theorem|CCB8VNQCV0]]: an isometry between two totally isotropic subspaces of the same dimension extends to $V$, so all maximal ones look alike.
The argument above avoids Witt's theorem and uses only cancellation, which is the special case of Witt's theorem for nondegenerate subspaces.
