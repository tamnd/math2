---
tag: AYYJXYNT01
kind: proof
name: Proof of the Cartan–Dieudonné theorem by induction on the dimension
msc: [51F15, 15B10]
proves: 0VMWGYY35Q
uses: [0VGSYBWHV2, 0717XXPWM6, 0R7VXTYHYZ, 025158VEYZ, 0Q8HZTJC7G, 079D68S3AW, 0SP7P0G7KQ, 0E2NYPVSP9, 0WGAXEK99E]
sources:
  - url: https://www.cis.upenn.edu/~cis6100/geombchap7.pdf
    locator: Lemma 7.1.3 and Theorem 7.2.1
---

## Proof

We argue by induction on $n$. A hyperplane of $V$ is a subspace of dimension $n - 1$.

1. Let $V$ be a real inner product space with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and norm $\norm{\cdot}$. For $u \in V$ with $u \ne 0$, set $H_u = \set{x \in V : \ip{x}{u} = 0}$. Over $\R$, the inner product is symmetric.
2. $H_u$ is the [[orthogonal complement|079D68S3AW]] of the line $\R u$. If $\dim V = n$, then $\dim H_u = n - 1$ by the [[dimension formula|0E2NYPVSP9]]. So $H_u$ is a hyperplane.
3. Claim: the [[reflection|025158VEYZ]] in $H_u$ is $R_u(x) = x - 2 \frac{\ip{x}{u}}{\ip{u}{u}} u$. Set $c = \ip{x}{u} / \ip{u}{u}$ and $p = x - c u$.
4. Then $\ip{p}{u} = \ip{x}{u} - c \ip{u}{u} = 0$, so $p \in H_u$. For $h \in H_u$, $\ip{c u}{h} = c \ip{h}{u} = 0$, so $c u \in H_u^\perp$.
5. Since $x = p + c u$ and the [[decomposition|0SP7P0G7KQ]] $V = H_u \oplus H_u^\perp$ is unique, the [[orthogonal projection|0Q8HZTJC7G]] is $P_{H_u}(x) = p$. So the reflection is $2p - x = x - 2 c u = R_u(x)$.
6. From step 3, $R_u(u) = -u$ and $R_u(h) = h$ for $h \in H_u$. Since $x = p + cu$, we get $R_u(R_u(x)) = R_u(p - cu) = p + cu = x$. So $R_u \circ R_u = \id$.
7. For $n \ge 0$, let $P(n)$ say: every linear isometry of an $n$-dimensional real inner product space is a composition of at most $n$ reflections in hyperplanes. Let $V$ have dimension $n$ and let $T \colon V \to V$ be a [[linear isometry|0717XXPWM6]].
8. If $T = \id$, then $T$ is the composition of zero reflections. This covers $n = 0$, where $V = \set{0}$. Now let $n \ge 1$, assume $P(n - 1)$, and let $T \ne \id$.
9. Choose $v \in V$ with $T(v) \ne v$, and set $u = T(v) - v \ne 0$. By [[preservation of inner products|0R7VXTYHYZ]], $\ip{T(v)}{T(v)} = \ip{v}{v}$. Write $a = \ip{v}{v}$ and $b = \ip{T(v)}{v}$.
10. Then $\ip{u}{u} = a - 2b + a = 2(a - b)$ and $\ip{T(v)}{u} = a - b$. Since $u \ne 0$, $a - b \ne 0$.
11. By step 3, $R_u(T(v)) = T(v) - 2 \frac{a - b}{2(a - b)} u = T(v) - u = v$.
12. Let $S = R_u \circ T$. A reflection keeps norms, since $\norm{p - cu}^2 = \norm{p}^2 + c^2 \norm{u}^2 = \norm{p + cu}^2$ when $p \perp u$. So $S$ is a linear isometry with $S(v) = v$.
13. Since $T(0) = 0$, we have $v \ne 0$. Let $E = H_v$, a hyperplane by step 2. For $x \in E$, preservation of inner products by $S$ gives $\ip{S(x)}{v} = \ip{S(x)}{S(v)} = \ip{x}{v} = 0$. So $S(E) \subseteq E$.
14. The restriction $S|_E \colon E \to E$ is a linear isometry of the real inner product space $E$, of dimension $n - 1$.
15. By $P(n-1)$, $S|_E = R'_1 \circ \cdots \circ R'_k$ with $k \le n - 1$, where $R'_j$ is the reflection of $E$ in a hyperplane $G_j$ of $E$.
16. Fix $j$. The orthogonal complement of $G_j$ in $E$ has dimension $(n - 1) - (n - 2) = 1$ by the dimension formula. Choose $w_j \ne 0$ in it.
17. Then $G_j \subseteq G'_j = \set{x \in E : \ip{x}{w_j} = 0}$, and $\dim G'_j = n - 2$ by step 2 in $E$. A [[subspace of full dimension|0WGAXEK99E]] is the whole space, so $G_j = G'_j$.
18. By steps 3 to 5 applied in $E$, $R'_j(x) = x - 2 \frac{\ip{x}{w_j}}{\ip{w_j}{w_j}} w_j$ for $x \in E$.
19. Let $R_j = R_{w_j}$ be the reflection of $V$ in $H_{w_j}$, a hyperplane of $V$. By step 3 and step 18, $R_j(x) = R'_j(x)$ for $x \in E$. Also $R_j(v) = v$, since $\ip{v}{w_j} = 0$.
20. Each $R_j$ maps $E$ into $E$. So $R_1 \circ \cdots \circ R_k$ agrees with $S$ on $E$, and both fix $v$.
21. By the [[decomposition|0SP7P0G7KQ]] for the line $\R v$, each $x \in V$ is $t v + e$ with $t \in \R$ and $e \in E$, as $E = (\R v)^\perp$. Two linear maps that agree on $v$ and on $E$ are equal.
22. Hence $S = R_1 \circ \cdots \circ R_k$. By step 6, $T = R_u \circ R_u \circ T = R_u \circ S = R_u \circ R_1 \circ \cdots \circ R_k$.
23. This is a composition of $k + 1 \le n$ reflections in hyperplanes of $V$. This proves $P(n)$, and the theorem follows by induction.

## Idea

If $T$ moves a vector $v$, the reflection in the hyperplane orthogonal to $T(v) - v$ swaps $T(v)$ and $v$, because they have the same length. Composing with it gives an isometry that fixes $v$, and hence maps the hyperplane orthogonal to $v$ to itself. Induction on that hyperplane gives at most $n - 1$ more reflections.
