---
tag: J1NTZCSPPM
kind: proof
name: Proof of Goodstein's theorem by ordinals below epsilon nought
msc: ["03F30", "03F15"]
topics: [T6FK1E7GJ1]
audience: grad
proves: XQMNJF241J
uses: [0YSCSX5YZC, 6GD30FGYDZ, KAEDCQ8RM6, KT50SMH3EC, 0ZHQMQ2C1N, 0F1D6PK9RZ, Z742YPHPNS, R6ZC4BJGXV, X8RKXQASR9]
methods: [0ASJVEFA9J, 0EFYCFHYFG, TP3GC5J08D, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: Proof of Goodstein's theorem
  - url: https://en.wikipedia.org/wiki/Goodstein's_theorem
    locator: Sequence length as a function of the starting value
---

## Proof

We use the notation of [[Goodstein's theorem|XQMNJF241J]]: hereditary base-$b$ notation, the map $B_b$ and the sequence $G_1 = m$, $G_{k+1} = B_{k+1}(G_k) - 1$.
Ordinals are compared through their [[Cantor normal form|6GD30FGYDZ]].
Two normal forms are compared at the largest exponent where their coefficients differ, and a missing term has coefficient $0$.

**The ordinal of a number.**
For $b \ge 2$ define $o_b(0) = 0$ and, for $n = b^{e_1} c_1 + \cdots + b^{e_r} c_r$ in base $b$ with $e_1 > \cdots > e_r$ and $0 < c_i < b$,
$$o_b(n) = \omega^{o_b(e_1)} c_1 + \cdots + \omega^{o_b(e_r)} c_r.$$
So $o_b(n)$ replaces every $b$ in the hereditary notation of $n$ by $\omega$.
This is a definition by strong induction on $n$, because each exponent satisfies $e_i < n$: indeed $b^{e_i} \le n$ and $b^{e} \ge 2^{e} > e$.

**Lemma 1: $o_b$ is strictly increasing.**

1. We prove by strong induction on $n$: for every $m < n$, $o_b(m) < o_b(n)$, and $o_b(n)$ as written is a Cantor normal form.
2. Write $m = \sum_j d_j b^j$ and $n = \sum_j d'_j b^j$ with digits $0 \le d_j, d'_j < b$. Every exponent $j$ with a nonzero digit is less than $n$.
3. By the induction hypothesis, $o_b$ is strictly increasing on $\set{0, 1, \dots, n - 1}$. So distinct exponents $j$ give distinct exponents $o_b(j)$, in the same order.
4. Hence $o_b(m)$ and $o_b(n)$ are Cantor normal forms, with the terms in decreasing order of the exponents.
5. Since $m < n$, the largest $j_0$ with $d_{j_0} \ne d'_{j_0}$ has $d_{j_0} < d'_{j_0}$. This is the comparison of numbers in base $b$.
6. By step 3, the largest exponent where the two normal forms differ is $o_b(j_0)$. There the coefficients are $d_{j_0} < d'_{j_0}$.
7. By the comparison rule for normal forms, $o_b(m) < o_b(n)$.
8. Since both orders are linear, Lemma 1 also gives the converse: $o_b(m) < o_b(n)$ implies $m < n$.

**Lemma 2: $o_b(n) < \varepsilon_0$.**

1. Recall that $\varepsilon_0 = \sup_j \omega_j$ with $\omega_0 = \omega$ and $\omega_{j+1} = \omega^{\omega_j}$, as on the page [[epsilon nought|KT50SMH3EC]].
2. If $\gamma < \varepsilon_0$, then $\gamma < \omega_j$ for some $j$, so $\omega^{\gamma} c < \omega^{\gamma + 1} \le \omega^{\omega_j} = \omega_{j+1}$ for every finite $c$.
3. A sum of finitely many ordinals below $\omega^{\delta}$ is below $\omega^{\delta}$. This is a rule of [[ordinal arithmetic|KAEDCQ8RM6]].
4. By strong induction on $n$, each exponent $o_b(e_i)$ is below $\varepsilon_0$, so steps 2 and 3 give $o_b(n) < \omega_{j+1}$ for a suitable $j$.

**Lemma 3: the base change keeps the ordinal.**
Let $n = b^{e_1} c_1 + \cdots + b^{e_r} c_r$ in hereditary base $b$.

1. We prove by strong induction on $n$: $B_b(n) = (b+1)^{B_b(e_1)} c_1 + \cdots + (b+1)^{B_b(e_r)} c_r$ is the hereditary base-$(b+1)$ notation of $B_b(n)$, and $o_{b+1}(B_b(n)) = o_b(n)$.
2. The first formula is the definition of $B_b$: it replaces $b$ by $b + 1$ at the top level and inside each exponent.
3. Each $e_i < n$, so the induction hypothesis gives $o_{b+1}(B_b(e_i)) = o_b(e_i)$.
4. Lemma 1 for base $b$ gives $o_b(e_1) > \cdots > o_b(e_r)$. By step 3 and Lemma 1 for base $b + 1$, $B_b(e_1) > \cdots > B_b(e_r)$.
5. The digits satisfy $0 < c_i < b < b + 1$. By uniqueness of base expansions, the formula of step 1 is the base-$(b+1)$ expansion of $B_b(n)$.
6. The exponents $B_b(e_i)$ are in hereditary base $b + 1$ by the induction hypothesis. So the whole expansion is the hereditary base-$(b+1)$ notation.
7. Replacing $b + 1$ by $\omega$ gives $\omega^{o_{b+1}(B_b(e_1))} c_1 + \cdots = \omega^{o_b(e_1)} c_1 + \cdots = o_b(n)$, by step 3.

**Part 1: every Goodstein sequence reaches $0$.**

1. Fix $m$ and let $\alpha_k = o_{k+1}(G_k)$ for every $k$ with $G_k$ defined. This is an [[ordinal|0YSCSX5YZC]] below $\varepsilon_0$ by Lemma 2.
2. Let $G_k > 0$. Then $G_{k+1} = B_{k+1}(G_k) - 1 < B_{k+1}(G_k)$.
3. Lemma 1 for base $k + 2$ gives $\alpha_{k+1} = o_{k+2}(G_{k+1}) < o_{k+2}(B_{k+1}(G_k))$.
4. Lemma 3 for $b = k + 1$ gives $o_{k+2}(B_{k+1}(G_k)) = o_{k+1}(G_k) = \alpha_k$. So $\alpha_{k+1} < \alpha_k$.
5. Suppose that $G_k > 0$ for every $k$. Then $\alpha_1 > \alpha_2 > \alpha_3 > \cdots$ is an infinite strictly decreasing sequence of ordinals.
6. This is impossible, because the ordinals are [[well-ordered|0F1D6PK9RZ]]: the set $\set{\alpha_k}$ would have no least element.
7. So $G_k = 0$ for some $k$, which is part 1 of the theorem.

**Part 3: a proof in $\mathsf{PA}$ plus transfinite induction up to $\varepsilon_0$.**

1. Code the ordinals below $\varepsilon_0$ by their Cantor normal forms, as finite trees of numbers. The comparison rule for normal forms is then primitive recursive.
2. The maps $o_b$, $B_b$ and the sequence $G_k$ are primitive recursive. Lemmas 1, 2 and 3 are proved by induction on numbers, so $\mathsf{PA}$ proves them.
3. Let $\varphi(\alpha)$ say: for all $m$ and $k$, if $G_k$ is defined for $m$ and $\alpha_k = \alpha$, then the sequence of $m$ reaches $0$.
4. If $\varphi(\beta)$ holds for all $\beta < \alpha$, then $\varphi(\alpha)$ holds. Indeed $G_k = 0$ already, or $\alpha_{k+1} < \alpha$ by Part 1, step 4.
5. [[Transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$ for the arithmetic formula $\varphi$ gives $\varphi(\alpha)$ for all $\alpha < \varepsilon_0$.
6. Apply it with $k = 1$ and $\alpha = o_2(m)$. This proves part 1, in $\mathsf{PA}$ plus this instance of transfinite induction.
7. The ordinal $\varepsilon_0$ is well-ordered in $\mathsf{ZFC}$, so $\mathsf{ZFC}$ also proves part 1.

**Part 2: $\mathsf{PA}$ does not prove part 1.**
This part uses two lemmas that we cite without proof.

1. Let $L(m)$ be the least $k$ with $G_k = 0$ for the sequence of $m$. The relation $L(m) = k$ is primitive recursive.
2. Suppose $\mathsf{PA}$ proves $\forall m\, \exists k\, G_k = 0$. Then $\mathsf{PA}$ proves $\forall m\, \exists k\, L(m) = k$, by the least number principle of $\mathsf{PA}$.
3. So $L$ is a [[provably total function|Z742YPHPNS]] of $\mathsf{PA}$.
4. **Cited lemma A** (Wainer 1970, after Kreisel). For every function $g$ that $\mathsf{PA}$ proves total, there is $\alpha < \varepsilon_0$ with $g(x) < f_\alpha(x)$ for all large $x$, where $f_\alpha$ is the [[fast-growing hierarchy|R6ZC4BJGXV]].
5. The [[Hardy hierarchy|X8RKXQASR9]] satisfies $f_\alpha = H_{\omega^\alpha}$, with $\omega^\alpha < \varepsilon_0$. So lemma A gives $L(m) < H_{\omega^\alpha}(m)$ for all large $m$.
6. **Cited lemma B** (Kirby and Paris 1982). For every $\beta < \varepsilon_0$, $L(m) > H_\beta(m)$ for all large $m$.
7. Take $\beta = \omega^\alpha$ in lemma B. Then $L(m) > H_{\omega^\alpha}(m)$ for all large $m$, which contradicts step 5.
8. So $\mathsf{PA}$ does not prove part 1. This is part 2 of the theorem.

**The length of the sequence.**
This computation explains lemma B, and it is the start of Cichon's proof.

1. For $x \in \N$ and a limit $\lambda < \varepsilon_0$, the standard fundamental sequence $\lambda[x]$ is defined on the page [[fast-growing hierarchy|R6ZC4BJGXV]]. Define $P_x(\alpha + 1) = \alpha$ and $P_x(\lambda) = P_x(\lambda[x])$.
2. **Cited lemma C** (Cichon 1983). For $b \ge 2$ and $n \ge 1$, $o_b(n - 1) = P_b(o_b(n))$.
3. With Lemma 3, lemma C gives $\alpha_{k+1} = o_{k+2}(B_{k+1}(G_k) - 1) = P_{k+2}(\alpha_k)$.
4. For $\alpha > 0$ and $x \ge 1$, the [[Hardy functions|X8RKXQASR9]] satisfy $H_\alpha(x) = H_{P_x(\alpha)}(x + 1)$. For $\alpha = \beta + 1$ this is the definition $H_{\beta+1}(x) = H_\beta(x+1)$.
5. For a limit $\lambda$ and $x \ge 1$ we have $\lambda[x] > 0$, and $H_\lambda(x) = H_{\lambda[x]}(x) = H_{P_x(\lambda[x])}(x + 1) = H_{P_x(\lambda)}(x+1)$, by induction on the ordinal.
6. Steps 3 and 4 give $H_{\alpha_1}(3) = H_{\alpha_2}(4) = \cdots = H_{\alpha_k}(k + 2)$ while $G_k$ is defined.
7. At $k = L(m)$ we have $\alpha_k = 0$ and $H_0(k+2) = k + 2$. So $L(m) = H_{o_2(m)}(3) - 2$.
8. Check for $m = 3$: $o_2(3) = \omega + 1$, and $H_{\omega+1}(3) = H_\omega(4) = H_4(4) = 8$. So $L(3) = 6$, as in the sequence $3, 3, 3, 2, 1, 0$.
9. Check for $m = 4$: $o_2(4) = \omega^\omega$ and $H_{\omega^\omega}(3) = f_\omega(3) = f_3(3) = 3 \cdot 2^{402653211}$.

## Idea

Replace the base by $\omega$ in each term of the sequence.
The base change does not move this ordinal, and the subtraction of $1$ makes it smaller, so the ordinals strictly decrease below $\varepsilon_0$ and the sequence stops.
For the unprovability, the length of the sequence is a Hardy function along $\varepsilon_0$, and it grows faster than every function that $\mathsf{PA}$ proves total.

## Variants

- Kirby and Paris proved part 2 with non-standard models of $\mathsf{PA}$. In a non-standard model they build an initial segment that is a model of $\mathsf{PA}$ in which some Goodstein sequence does not end.
- Cichon gave the proof through lemma C and the Hardy hierarchy, with the [[provably total functions|Z742YPHPNS]] of $\mathsf{PA}$ in place of models.
- A third route uses Gentzen's [[consistency proof|QPV0HNP22S]]. It needs only that no primitive recursive sequence of ordinals below $\varepsilon_0$ strictly decreases for ever. Such a sequence can be slowed down to the ordinals of a Goodstein sequence, so Goodstein's theorem excludes it.
