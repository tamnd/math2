---
tag: AYYJXYNT01
kind: proof
name: Proof of the Cartan-Dieudonné theorem by induction on the dimension
msc: ["51F15", "15B10"]
topics: [AZS5BPF5H3]
audience: grad
proves: 0VMWGYY35Q
uses: [0VGSYBWHV2, 0717XXPWM6, 0R7VXTYHYZ, 025158VEYZ, 0Q8HZTJC7G, 079D68S3AW, 0SP7P0G7KQ, 0E2NYPVSP9, 0WGAXEK99E, F7M8ZXB4P7, FEER10D15S]
methods: [0ASJVEFA9J]
sources:
  - url: https://www.cis.upenn.edu/~cis6100/geombchap7.pdf
    locator: Lemma 7.1.3 and Theorem 7.2.1
---

## Proof

We first set up the reflections and their formula, then argue by induction on $n$: one reflection makes $T$ fix a vector $v$, and the rest lives on the hyperplane orthogonal to $v$.

**The reflections.**

1. Let $V$ be a real inner product space with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and norm $\norm{\cdot}$. For $u \in V$ with $u \neq 0$, set $H_u = \{ x \in V : \ip{x}{u} = 0 \}$. Over $\R$ the inner product is symmetric.
2. The set $H_u$ is the [[orthogonal complement|079D68S3AW]] of the line $\R u$. If $\dim V = n$, then $\dim H_u = n - 1$ by the [[dimension formula|0E2NYPVSP9]], so $H_u$ is a hyperplane.
3. We claim that the [[reflection|025158VEYZ]] in $H_u$ is $R_u(x) = x - 2\frac{\ip{x}{u}}{\ip{u}{u}}u$. For $x \in V$, set $c = \ip{x}{u} / \ip{u}{u}$ and $p = x - cu$.
4. Then $\ip{p}{u} = \ip{x}{u} - c\ip{u}{u} = 0$, so $p \in H_u$. For $h \in H_u$ we have $\ip{cu}{h} = c\ip{h}{u} = 0$, so $cu \in H_u^\perp$.
5. Since $x = p + cu$ and the [[decomposition|0SP7P0G7KQ]] $V = H_u \oplus H_u^\perp$ is unique, the [[orthogonal projection|0Q8HZTJC7G]] is $P_{H_u}(x) = p$. So the reflection $2P_{H_u} - \id$ sends $x$ to $2p - x = x - 2cu = R_u(x)$, which proves the claim.
6. In the notation of step 3, $R_u(x) = p - cu$. So $R_u(R_u(x)) = p + cu = x$, because $p \in H_u$ is fixed and the component $-cu$ is reversed. Hence $R_u \circ R_u = \id$.
7. A reflection keeps norms: since $p \perp u$, we get $\norm{p - cu}^2 = \norm{p}^2 + c^2\norm{u}^2 = \norm{p + cu}^2$.

**The induction.**

8. For $n \ge 0$, let $P(n)$ say: every linear isometry of an $n$-dimensional real inner product space is a composition of at most $n$ reflections in hyperplanes. Let $V$ have dimension $n$, and let $T \colon V \to V$ be a [[linear isometry|0717XXPWM6]].
9. If $T = \id$, then $T$ is the composition of zero reflections. This covers $n = 0$, where $V = \{ 0 \}$. Now let $n \ge 1$, assume $P(n - 1)$, and let $T \neq \id$.
10. Choose $v \in V$ with $T(v) \neq v$, and set $u = T(v) - v \neq 0$. By [[preservation of inner products|0R7VXTYHYZ]], $\ip{T(v)}{T(v)} = \ip{v}{v}$. Write $a = \ip{v}{v}$ and $b = \ip{T(v)}{v}$.
11. Then $\ip{u}{u} = a - 2b + a = 2(a - b)$ and $\ip{T(v)}{u} = a - b$. Since $u \neq 0$, we have $a - b \neq 0$.
12. By the formula of step 3,
$$R_u(T(v)) = T(v) - 2\frac{a - b}{2(a - b)}u = T(v) - u = v.$$
13. Let $S = R_u \circ T$. By step 7, $S$ is a linear isometry, and $S(v) = v$ by step 12.
14. Since $T(0) = 0$, we have $v \neq 0$. Let $E = H_v$, a hyperplane by step 2. For $x \in E$, preservation of inner products by $S$ gives $\ip{S(x)}{v} = \ip{S(x)}{S(v)} = \ip{x}{v} = 0$. So $S(E) \subseteq E$.
15. The restriction $S|_E \colon E \to E$ is a linear isometry of the real inner product space $E$, which has dimension $n - 1$.
16. By $P(n - 1)$, $S|_E = R'_1 \circ \cdots \circ R'_k$ with $k \le n - 1$, where $R'_j$ is the reflection of $E$ in a hyperplane $G_j$ of $E$.
17. Fix $j$. The orthogonal complement of $G_j$ in $E$ has dimension $(n - 1) - (n - 2) = 1$ by the dimension formula. Choose $w_j \neq 0$ in it.
18. Then $G_j \subseteq G'_j = \{ x \in E : \ip{x}{w_j} = 0 \}$, and $\dim G'_j = n - 2$ by step 2 applied in $E$. A [[subspace of full dimension|0WGAXEK99E]] is the whole space, so $G_j = G'_j$.
19. By steps 3 to 5 applied in $E$, $R'_j(x) = x - 2\frac{\ip{x}{w_j}}{\ip{w_j}{w_j}}w_j$ for $x \in E$.
20. Let $R_j = R_{w_j}$ be the reflection of $V$ in $H_{w_j}$, a hyperplane of $V$. By steps 3 and 19, $R_j(x) = R'_j(x)$ for $x \in E$. Also $R_j(v) = v$, since $\ip{v}{w_j} = 0$.
21. Each $R_j$ maps $E$ into $E$. So $R_1 \circ \cdots \circ R_k$ agrees with $S$ on $E$, and both maps fix $v$.
22. By the [[decomposition|0SP7P0G7KQ]] for the line $\R v$, each $x \in V$ is $tv + e$ with $t \in \R$ and $e \in E$, as $E = (\R v)^\perp$. Two linear maps that agree on $v$ and on $E$ are therefore equal.
23. Hence $S = R_1 \circ \cdots \circ R_k$. By step 6, $T = R_u \circ R_u \circ T = R_u \circ S = R_u \circ R_1 \circ \cdots \circ R_k$.
24. This is a composition of $k + 1 \le n$ reflections in hyperplanes of $V$. This proves $P(n)$, and part 1 follows by induction.

**The matrix form.**

25. Let $Q \in O(n)$. By [[the equivalent conditions|F7M8ZXB4P7]], $x \mapsto Qx$ is a linear isometry of $\R^n$ with the dot product.
26. By part 1, $Q$ is a product of at most $n$ reflections $R_u$. We may scale each $u$ to length $1$, because $R_{cu} = R_u$ for $c \neq 0$, and then the matrix of $R_u$ is $I_n - 2uu^{\mathsf{T}}$ by part 4 of [[the reflection theorem|FEER10D15S]]. $\blacksquare$

## Idea

If $T$ moves a vector $v$, then $T(v)$ and $v$ have the same length, so the reflection in the hyperplane orthogonal to $T(v) - v$ swaps them.
After that reflection we have an isometry $S$ that fixes $v$.
An isometry that fixes $v$ also maps the hyperplane orthogonal to $v$ to itself, and the induction hypothesis on that hyperplane gives at most $n - 1$ more reflections.
Each of them extends to $V$ by fixing $v$, and the count is at most $1 + (n - 1) = n$.

## Variants

[[The proof of the reflection theorem|CWPWRR6NQA]] runs the same induction with matrices: it sends $Qe_n$ to $e_n$ by one reflection and uses the block form of the result.
For a nondegenerate symmetric bilinear form $B$, the vector $u = T(v) - v$ can have $B(u, u) = 0$, and then the reflection in $u$ is not defined.
The general proof of part 3 must treat this case separately, for example by choosing $v$ with more care or by using $T(v) + v$ in place of $T(v) - v$.
