---
tag: SGQ76R2WJY
kind: proof
name: Proof of the structural completeness of Medvedev's logic by a universal valuation
msc: ["03B55", "03B22"]
topics: [38EQ20GR7M]
audience: research
proves: TWCP5X6PGQ
uses: [R2FD01J3PC, 5GTQ69W47T, 480TCT5CJ9, B9M3P61ZVA, 9X08XK5RV2]
methods: [0NTF6DMVAP, 0J0XBKG64S, 12MQ2NJ29A]
sources:
  - arxiv: 2404.04349v1
    locator: pages 1 to 3
---

## Proof

We prove the contrapositive: if $\varphi \to \psi \notin \mathsf{ML}$, there is a substitution $\sigma$ with $\sigma(\varphi) \in \mathsf{ML}$ and $\sigma(\psi) \notin \mathsf{ML}$.
Worlds of $M_n$ are nonempty $K \subseteq \set{1, \dots, n}$, and $K \leq L$ iff $L \subseteq K$; see [[Medvedev's logic|R2FD01J3PC]].

*Part A: pairwise inconsistent formulas.* Fix $n \geq 1$.

1. Choose $m \geq 0$ with $2^m \geq n$, and let $S = \set{0, 1}^m$. Choose distinct $s_1, \dots, s_{n-1} \in S$, let $T = S \setminus \set{s_1, \dots, s_{n-1}}$, and fix $t_0 \in T$. $T$ is nonempty since $|S| \geq n$.
2. Fix atoms $q_1, \dots, q_m$. For $s \in S$, let $\beta_s$ be the conjunction of the literals $q_j$ for $s_j = 1$ and $\neg q_j$ for $s_j = 0$. For $m = 0$, $\beta_s$ is $\bot \to \bot$.
3. Put $\alpha_i = \beta_{s_i}$ for $i < n$, and $\alpha_n = \bigvee_{t \in T} \beta_t$.
4. (i) $\neg(\alpha_i \wedge \alpha_j) \in \mathsf{IPC}$ for $i \neq j$. For $s \neq t$, $\beta_s \wedge \beta_t$ contains $q_j$ and $\neg q_j$ for some $j$, and $\neg(q_j \wedge \neg q_j) \in \mathsf{IPC}$. For $\alpha_n$, use $\neg(\gamma \wedge (\delta_1 \vee \delta_2)) \leftrightarrow \neg(\gamma \wedge \delta_1) \wedge \neg(\gamma \wedge \delta_2)$ in $\mathsf{IPC}$.
5. (ii) $\neg \neg(\alpha_1 \vee \dots \vee \alpha_n) \in \mathsf{IPC}$. The disjunction contains every $\beta_s$, $s \in S$, so it is a classical tautology: each truth assignment makes $\beta_s$ true for its own vector $s$. By [[Glivenko's theorem|B9M3P61ZVA]], its double negation is in $\mathsf{IPC}$.
6. Put $s'_k = s_k$ for $k < n$ and $s'_n = t_0$. Define a valuation $u$ on $M_n$ by $u(q_j) = \set{K : (s'_k)_j = 1 \text{ for all } k \in K}$. It is an up-set, since $L \subseteq K$ for $L \geq K$.
7. At a maximal world $\set{k}$, $q_j$ holds iff $(s'_k)_j = 1$, and $\neg q_j$ holds iff $q_j$ fails. So $\beta_s$ holds at $\set{k}$ iff $s = s'_k$.
8. (iii) Hence $\alpha_i$ holds at $\set{k}$ iff $k = i$. For $i < n$ this is because the $s'_k$ are distinct. For $i = n$ it is because $s'_k \in T$ iff $k = n$.
9. Lemma: in a finite frame, $w \Vdash \neg \neg \chi$ iff every maximal world above $w$ forces $\chi$. If a maximal $z \geq w$ fails $\chi$, then $z \Vdash \neg \chi$ and $w \nVdash \neg \neg \chi$. Conversely, every world above $w$ lies below a maximal world, which forces $\chi$, so no world above $w$ forces $\neg \chi$.
10. For nonempty $I \subseteq \set{1, \dots, n}$, put $\alpha_I = \neg \neg \bigvee_{i \in I} \alpha_i$. The maximal worlds above $K$ are the $\set{k}$, $k \in K$. By steps 8 and 9, $K \Vdash_u \alpha_I$ iff $K \subseteq I$.

*Part B: the universal valuation.*

11. Let $v$ be any valuation on $M_n$. Define $\sigma(p) = \bigvee \set{\alpha_I : I \in v(p)}$ for each atom $p$, with the empty disjunction read as $\bot$.
12. $K \Vdash_u \sigma(p)$ iff $K \subseteq I$ for some $I \in v(p)$, by step 10. This holds iff $K \in v(p)$: if $K \subseteq I \in v(p)$ then $K \geq I$ and $v(p)$ is an up-set; conversely take $I = K$.
13. Substitution lemma: for a valuation $w$ on any frame, let $w^\sigma(p)$ be the set of worlds forcing $\sigma(p)$ under $w$. It is an up-set by persistence, and $x \Vdash_w \sigma(\chi)$ iff $x \Vdash_{w^\sigma} \chi$, by induction on $\chi$, since $\sigma$ commutes with the connectives.
14. By step 12, $u^\sigma = v$. So $K \Vdash_u \sigma(\chi)$ iff $K \Vdash_v \chi$, for every formula $\chi$.

*Part C: the main argument.*

15. Suppose $\varphi \to \psi \notin \mathsf{ML}$. Then some $M_n$, valuation $v$ and world $K$ satisfy $K \Vdash_v \varphi$ and $K \nVdash_v \psi$, by the clause for implication in [[Kripke semantics|5GTQ69W47T]].
16. The worlds above $K$ form $M(K)$, which is isomorphic to $M_{|K|}$, and forcing in this up-set is computed inside it. So we may assume that $K$ is the root of $M_n$. By persistence, $\varphi$ then holds at every world of $M_n$ under $v$.
17. Take the formulas of Part A and $\sigma$ of Part B for this $n$ and $v$. By step 14, the root fails $\sigma(\psi)$ under $u$, so $\sigma(\psi) \notin \mathsf{ML}$.
18. Suppose, for a contradiction, that $\sigma(\varphi) \notin \mathsf{ML}$: some $M_r$, valuation $w$ and world $J_0$ satisfy $J_0 \nVdash_w \sigma(\varphi)$.
19. By soundness in [[the completeness theorem|480TCT5CJ9]], the formulas of steps 4 and 5 hold at every world under $w$.
20. For $k \in \set{1, \dots, r}$, let $g(k)$ be the unique $i$ with $\set{k} \Vdash_w \alpha_i$. It exists by step 5 and step 9 at the maximal world $\set{k}$. It is unique by step 4.
21. Define $f \colon M_r \to M_n$ by $f(J) = g[J]$, a nonempty set. If $J \leq J'$, then $J' \subseteq J$, so $f(J') \subseteq f(J)$ and $f(J) \leq f(J')$.
22. Back condition: let $f(J) \leq L$, so $L \subseteq g[J]$. Put $J' = J \cap g^{-1}[L]$. It is nonempty, $J \leq J'$, and $g[J'] = L$, since each $l \in L$ has a preimage in $J$.
23. For $J \in M_r$ and nonempty $I$: $J \Vdash_w \alpha_I$ iff every $\set{k}$ with $k \in J$ forces $\bigvee_{i \in I} \alpha_i$, by step 9. By step 20 this holds iff $g(k) \in I$ for all $k \in J$, that is, iff $f(J) \subseteq I$. By step 10 this is iff $f(J) \Vdash_u \alpha_I$.
24. Let $W = w^\sigma$. Each $\sigma(p)$ is a disjunction of formulas $\alpha_I$, so step 23 gives $J \Vdash_w \sigma(p)$ iff $f(J) \Vdash_u \sigma(p)$. By step 12, $J \in W(p)$ iff $f(J) \in v(p)$.
25. Claim: $J \Vdash_W \chi$ iff $f(J) \Vdash_v \chi$, for every $\chi$. Induction on $\chi$: atoms by step 24; $\bot$, $\wedge$, $\vee$ directly.
26. Implication, forward: let $f(J) \Vdash_v \chi_1 \to \chi_2$ and $J' \geq J$ with $J' \Vdash_W \chi_1$. Then $f(J') \geq f(J)$ by step 21, $f(J') \Vdash_v \chi_1$, so $f(J') \Vdash_v \chi_2$ and $J' \Vdash_W \chi_2$.
27. Implication, backward: let $J \Vdash_W \chi_1 \to \chi_2$ and $L \geq f(J)$ with $L \Vdash_v \chi_1$. Step 22 gives $J' \geq J$ with $f(J') = L$. Then $J' \Vdash_W \chi_1$, so $J' \Vdash_W \chi_2$ and $L \Vdash_v \chi_2$.
28. By steps 18 and 13, $J_0 \nVdash_W \varphi$. By step 25, $f(J_0) \nVdash_v \varphi$. This contradicts step 16.
29. So $\sigma(\varphi) \in \mathsf{ML}$ and $\sigma(\psi) \notin \mathsf{ML}$, and the rule $\varphi / \psi$ is not admissible.

By contraposition, every admissible rule $\varphi / \psi$ has $\varphi \to \psi \in \mathsf{ML}$, so it is derivable.

## Idea

On $M_n$ there is one valuation $u$ from which every valuation $v$ arises by a substitution $\sigma$.
If $v$ refutes $\varphi \to \psi$ with $\varphi$ true everywhere, then $\sigma(\psi)$ is refuted by $u$.
Any countermodel to $\sigma(\varphi)$ on some $M_r$ would map onto $M_n$ by a p-morphism, and would refute $\varphi$ under $v$.

## Variants

The proof above is Skvortsov's, as retold by Přenosil.
Prucnal's original proof of 1976 is not reproduced here.
The same universal valuation and the Kreisel-Putnam rank of formulas give Maksimova's theorem that $\mathsf{ML}$ is the largest extension of the weak Kreisel-Putnam logic with the disjunction property.
