---
tag: MBYJP2GY8Z
kind: proof
name: Proof of Buss's witnessing theorem by bootstrapping and free-cut elimination
msc: ["03F30", "68Q15"]
topics: [RA380RWEC0]
audience: research
proves: RH4R7GTTAX
uses: [A2CFPP8JMN, YPQPC1WJMV, FMM44KFZQT, AYRZ98Y0NW, W72CA3R9MP, GVT2NKN37K, Z742YPHPNS]
methods: [0ASJVEFA9J, 12MQ2NJ29A, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Buss's witnessing theorem
  - url: https://en.wikipedia.org/wiki/Cobham%27s_thesis
    locator: lead section
---

## Proof

We prove part 2 for $i = 1$ in full, from four cited bootstrapping lemmas.
For part 1 we give the structure of Buss's argument and name the cited lemmas.
Part 3 then follows from parts 1 and 2.

**Cited facts.**

- **Cobham's theorem.** $\mathrm{FP}$ is the closure of the base functions $0$, $S(x)$, $\floor{x/2}$, $2x$, $\chi_\le(x, z)$ and $\mathrm{Choice}(x, y, z)$ under composition and limited iteration on notation. Here $\chi_\le(x, z) = 1$ if $x \le z$ and $0$ otherwise. $\mathrm{Choice}(x, y, z) = y$ if $x > 0$ and $z$ otherwise. Limited iteration on notation defines $f(\bar x, 0) = g(\bar x)$ and $f(\bar x, y) = h(\bar x, y, f(\bar x, \floor{y/2}))$ for $y > 0$, under a condition $\abs{f(\bar x, y)} \le q(\abs{\bar x}, \abs y)$ for a polynomial $q$.
- **L1 (monotonicity).** $S^1_2$ proves that $\le$ is a linear order and that each function symbol of the language is nondecreasing in each argument. So for every term $t$, $S^1_2 \vdash \bar a \le \bar b \to t(\bar a) \le t(\bar b)$. Also $\abs 0 = 0$, $\floor{u/2} \le u$, and $\abs{\floor{u/2}} + 1 = \abs u$ for $u \ge 1$.
- **L2 (Buss's Theorem 5).** A function $\Sigma^b_1$-defined in $S^1_2$ can be added to the language with its defining axiom. Each $\Sigma^b_1$ or $\Pi^b_1$ formula of the new language is $S^1_2$-provably equivalent to one of the old language. Polynomial induction stays valid for $\Sigma^b_1$ formulas of the new language.
- **L3 (sequences).** $S^1_2$ $\Sigma^b_1$-defines functions for sequence coding: the entry $\beta(j, w)$, the length $\mathrm{Len}(w)$, the append operation, and $\mathrm{MSP}(u, k) = \floor{u / 2^k}$. It proves their usual properties. There is a term $\mathrm{SqBd}(a, b)$: every sequence of length at most $\abs b + 1$ with entries at most $a$ has a code at most $\mathrm{SqBd}(a, b)$.
- **L4 (length induction).** $S^1_2$ proves $\Sigma^b_1$-$\mathrm{LIND}$: $A(0) \land \forall j \, (A(j) \to A(j + 1)) \to \forall x \, A(\abs x)$.

**Part 2 for $i = 1$: every $f \in \mathrm{FP}$ is $\Sigma^b_1$-definable in $S^1_2$.**
We prove a stronger claim by induction on a Cobham derivation of $f$.
The claim: there are a $\Sigma^b_1$ formula $A_f(\bar x, y)$ and a term $t_f(\bar x)$ such that

- (a) $A_f(\bar n, f(\bar n))$ is true for all $\bar n$;
- (b) $S^1_2 \vdash \forall \bar x \, \exists y \le t_f(\bar x) \, A_f(\bar x, y)$;
- (c) $S^1_2 \vdash A_f(\bar x, y) \land A_f(\bar x, y') \to y = y'$.

1. Base functions. Take $A_0 := (y = 0)$, $A_S := (y = Sx)$, $A_{\mathrm{half}} := (y = \floor{x/2})$ and $A_{\mathrm{dbl}} := (y = x + x)$.
2. Their bounds are $0$, $Sx$, $x$ and $x + x$. Here $\floor{x/2} \le x$ is from L1.
3. For $\chi_\le$ take $(x \le z \land y = S0) \lor (\neg x \le z \land y = 0)$, with bound $S0$.
4. For $\mathrm{Choice}$ take $(\neg x = 0 \land v = y) \lor (x = 0 \land v = z)$, with bound $y + z$.
5. These formulas are open, so they are $\Sigma^b_1$. Property (a) holds by the definitions of the functions.
6. Property (b) holds by pure logic, with $y + z$ bounding $y$ and $z$ by L1.
7. Property (c) uses only that $0 \ne S0$, a $\mathsf{BASIC}$ axiom.
8. Composition. Let $f(\bar x) = h(g_1(\bar x), \dots, g_m(\bar x))$, and assume the claim for $h$ and each $g_l$.
9. By L2, add symbols for $h$ and the $g_l$. By (b) and (c), $S^1_2 \vdash g_l(\bar x) \le t_{g_l}(\bar x)$ and $S^1_2 \vdash h(\bar u) \le t_h(\bar u)$.
10. Let $A_f(\bar x, y)$ be $y = h(g_1(\bar x), \dots, g_m(\bar x))$. By L2 it is equivalent to a $\Sigma^b_1$ formula of the base language.
11. Property (a) holds since the symbols denote $h$ and $g_l$. Property (c) is the transitivity of $=$.
12. Let $t_f := t_h(t_{g_1}(\bar x), \dots, t_{g_m}(\bar x))$. Step 9 and L1 give $h(g_1(\bar x), \dots) \le t_f(\bar x)$, so (b) holds.
13. Limited iteration. Let $f$ come from $g$ and $h$ with bound $q$, and assume the claim for $g$ and $h$. Add their symbols by L2.
14. Choose a term $T(\bar x, y)$ with $2^{q(\abs{\bar x}, \abs y)} \le T(\bar x, y)$ for all values. Let $s := x_1 + \dots + x_k + y + 2$, so $q(\abs{\bar x}, \abs y) \le c \abs s^d$ for some $c \ge 1$ and $d \ge 2$. Since $\abs{2^m} = m + 1$, nesting $d - 1$ smashes $s \# (s \# \cdots)$ gives a value at least $2^{\abs s^d}$. The product of $c$ copies of this term is $T$.
15. Since $v + 1 \le 2^{\abs v}$ for all $v$, the bound on $f$ gives $f(\bar n, m) < T(\bar n, m)$ for all $\bar n, m$.
16. For $u$ and $j \le \abs u$ write $u_j := \mathrm{MSP}(u, \abs u - j)$, the number formed by the first $j$ binary digits of $u$.
17. By L1 and L3, $S^1_2$ proves: $u_0 = 0$, $u_{\abs u} = u$, $u_j \le u$, and $u_j \ge 1$ for $j \ge 1$.
18. It also proves $\floor{u_j / 2} = u_{j - 1}$ for $1 \le j \le \abs u$. For $u \ge 1$ and $j < \abs u$ it proves $(\floor{u/2})_j = u_j$.
19. Let $\mathrm{Start}(\bar x, e)$ be $(g(\bar x) \le T(\bar x, 0) \land e = g(\bar x)) \lor (\neg g(\bar x) \le T(\bar x, 0) \land e = 0)$.
20. Let $\mathrm{Step}(\bar x, u, z, e)$ be $(h(\bar x, u, z) \le T(\bar x, u) \land e = h(\bar x, u, z)) \lor (\neg h(\bar x, u, z) \le T(\bar x, u) \land e = 0)$.
21. Each formula determines $e$ uniquely from the other arguments, and forces $e \le T(\bar x, 0)$ or $e \le T(\bar x, u)$.
22. Let $\mathrm{Comp}(w, \bar x, u)$ say: $\mathrm{Len}(w) = \abs u + 1$, $\mathrm{Start}(\bar x, \beta(1, w))$, and $\forall j < \abs u \; \mathrm{Step}(\bar x, u_{j + 1}, \beta(j + 1, w), \beta(j + 2, w))$.
23. The quantifier $\forall j < \abs u$ is sharply bounded. So $\mathrm{Comp}$ is $\Sigma^b_1$ after the translation of L2.
24. Truth. Fix $\bar n, m$, and let $e_j$ be the entries of a sequence $w$ with $\mathrm{Comp}(w, \bar n, m)$. We show $e_j = f(\bar n, m_j)$ by induction on $j$.
25. For $j = 0$: $g(\bar n) = f(\bar n, 0) < T(\bar n, 0)$ by step 15, so $\mathrm{Start}$ gives $e_0 = g(\bar n) = f(\bar n, m_0)$.
26. For $j \ge 1$: $m_j \ge 1$ and $\floor{m_j/2} = m_{j - 1}$, so $h(\bar n, m_j, e_{j - 1}) = f(\bar n, m_j)$.
27. This value is below $T(\bar n, m_j)$ by step 15, so $\mathrm{Step}$ gives $e_j = f(\bar n, m_j)$.
28. Define $A_f(\bar x, y, v) := \exists w \le \mathrm{SqBd}(T(\bar x, y), y) \, (\mathrm{Comp}(w, \bar x, y) \land v = \beta(\abs y + 1, w))$, and $t_f := T$.
29. Property (a). The sequence $\langle f(\bar n, m_0), \dots, f(\bar n, m_{\abs m}) \rangle$ satisfies $\mathrm{Comp}$, by the computation in steps 25 to 27.
30. Its entries are below $T(\bar n, m_j) \le T(\bar n, m)$, by step 15 and L1. So L3 bounds its code by $\mathrm{SqBd}$, and its last entry is $f(\bar n, m)$.
31. Property (b). Fix $\bar x, y$, and let $\Phi(u)$ be $\neg u \le y \lor \exists w \le \mathrm{SqBd}(T(\bar x, y), y) \, \mathrm{Comp}(w, \bar x, u)$. It is $\Sigma^b_1$.
32. $\Phi(0)$ holds: take the one-entry sequence $\langle e_0 \rangle$ with $\mathrm{Start}(\bar x, e_0)$. Then $e_0 \le T(\bar x, 0) \le T(\bar x, y)$.
33. For the step, let $u \ge 1$, $u \le y$, and assume $\Phi(\floor{u/2})$. Since $\floor{u/2} \le u \le y$, some $w'$ satisfies $\mathrm{Comp}(w', \bar x, \floor{u/2})$.
34. Then $\mathrm{Len}(w') = \abs u$ by L1. Let $e$ satisfy $\mathrm{Step}(\bar x, u, \beta(\abs u, w'), e)$, and let $w$ be $w'$ with $e$ appended.
35. The conditions of $\mathrm{Comp}(w, \bar x, u)$ for $j < \abs u - 1$ hold for $w'$, since $(\floor{u/2})_{j + 1} = u_{j + 1}$ by step 18.
36. The condition for $j = \abs u - 1$ is the choice of $e$, since $u_{\abs u} = u$.
37. Each entry of $w$ is at most $T(\bar x, u_j) \le T(\bar x, y)$, by step 21 and L1. The length is $\abs u + 1 \le \abs y + 1$.
38. So L3 gives $w \le \mathrm{SqBd}(T(\bar x, y), y)$, and $\Phi(u)$ holds. For $u = 0$ the step is trivial, and for $\neg u \le y$ it is trivial too.
39. $\Sigma^b_1$-$\mathrm{PIND}$ gives $\forall u \, \Phi(u)$. With $u := y$ we get $w$, and $v := \beta(\abs y + 1, w) \le T(\bar x, y)$ satisfies $A_f$.
40. Property (c). Let $w, w'$ both satisfy $\mathrm{Comp}(\cdot, \bar x, y)$. Let $\Psi(j)$ be $\forall j' \le \abs y \, (j' \le j \to \beta(j' + 1, w) = \beta(j' + 1, w'))$.
41. $\Psi$ is sharply bounded over open formulas, so it is $\Sigma^b_1$. $\Psi(0)$ holds since $\mathrm{Start}$ determines the first entry.
42. If $\Psi(j)$ holds, then $\Psi(j + 1)$ holds, since $\mathrm{Step}$ determines entry $j + 2$ from entry $j + 1$, by step 21.
43. L4 gives $\Psi(\abs y)$. So the last entries agree, and $v = v'$. This completes the induction and part 2 for $i = 1$.

**Part 2 for $i \ge 2$** is cited (Buss's Theorem 7).
The proof is the same induction, with oracle queries to $\Sigma^p_{i-1}$ sets expressed by $\Sigma^b_{i-1}$ formulas.

**Part 1: structure of the witnessing argument.**

44. Assume $S^i_2 \vdash \forall \bar x \, \exists y \, A(\bar x, y)$ with $A \in \Sigma^b_i$, and let $\bar c$ be new free variables.
45. Parikh's theorem for $S^i_2$ (cited) gives a term $t$ with $S^i_2 \vdash \exists y \le t(\bar c) \, A(\bar c, y)$. It is the analogue of [[Parikh's theorem|YPQPC1WJMV]] for this language.
46. Formulate $S^i_2$ in the [[sequent calculus|W72CA3R9MP]] with $\mathsf{BASIC}$ initial sequents and the rule $\Sigma^b_i$-$\mathrm{PIND}$: from $B(\floor{a/2}), \Gamma \to \Delta, B(a)$ infer $B(0), \Gamma \to \Delta, B(t)$.
47. **Free-cut elimination** (cited, Buss's Theorem 13, after Gentzen and Takeuti). The sequent $\to \exists y \le t \, A(\bar c, y)$ has a proof $P^*$ in which every formula is $\Sigma^b_i$.
48. **Witness predicate** (cited, Buss's Lemma 14). For $B \in \Sigma^b_i$ a formula $\mathrm{Witness}_B(w, \bar a)$ is defined by recursion on $B$.
49. For $B \in \Sigma^b_{i-1} \cup \Pi^b_{i-1}$ it is $B$ itself. For $(\exists x \le s) C$ it is $\beta(1, w) \le s \land \mathrm{Witness}_C(\beta(2, w), \bar a, \beta(1, w))$. Conjunction, disjunction and sharply bounded $\forall$ use the entries of $w$.
50. Lemma 14 gives $S^i_2 \vdash B \leftrightarrow \exists w \le t_B \, \mathrm{Witness}_B(w, \bar a)$. Its proof, by induction on $B$, also gives $S^i_2 \vdash \mathrm{Witness}_B(w, \bar a) \to B(\bar a)$ for all $w$.
51. It also gives: $\mathrm{Witness}_B$ is a $\Delta^p_i$ predicate, and it is $\Delta^b_i$ in $S^i_2$.
52. **Main Lemma** (Buss's Lemma 15). Let $\Gamma \to \Delta$ have a proof in which all formulas are $\Sigma^b_i$, with free variables $\bar c$.
53. Then some $f \in \square^p_i$, $\Sigma^b_i$-defined in $S^i_2$, satisfies $S^i_2 \vdash \mathrm{Witness}_{\bigwedge \Gamma}(w, \bar c) \to \mathrm{Witness}_{\bigvee \Delta}(f(w, \bar c), \bar c)$.
54. The proof is by induction on the number of inferences. Cut and the logical rules compose or pair witness functions; these cases are cited.
55. The $\mathrm{PIND}$ case, without side formulas: the premise is $B(\floor{a/2}) \to B(a)$, and the conclusion is $B(0) \to B(t)$.
56. The induction hypothesis gives $g$ with $\mathrm{Witness}_{B(\floor{a/2})}(w, a, \bar c) \to \mathrm{Witness}_{B(a)}(g(w, a, \bar c), a, \bar c)$ and $g \le t_B(a, \bar c)$.
57. Define $f$ by limited iteration: $f(w, 0, \bar c) = g(w, 0, \bar c)$ and $f(w, a, \bar c) = g(f(w, \floor{a/2}, \bar c), a, \bar c)$ for $a > 0$.
58. Its values are at most $t_B$, so $f \in \square^p_i$. For $i = 1$, steps 13 to 43 with $T := t_B$ define $f$. There the truncation never applies, so $S^1_2$ proves the recursion equations.
59. The formula $\mathrm{Witness}_{B(0)}(w, \bar c) \to \mathrm{Witness}_{B(a)}(f(w, a, \bar c), a, \bar c)$ is $S^i_2$-equivalent to a $\Sigma^b_i$ formula. This uses step 51, and replaces $f$ by its $\Sigma^b_i$ definition under a bounded $\exists$, as in L2.
60. It holds at $a = 0$, by step 56 with $a = 0$, since $\floor{0/2} = 0$.
61. If it holds at $\floor{a/2}$, step 56 and the recursion equation give it at $a$. $\Sigma^b_i$-$\mathrm{PIND}$ in $a$ gives it for all $a$.
62. Substituting $t$ for $a$ gives the witness function $w \mapsto f(w, t, \bar c)$ for $B(0) \to B(t)$.
63. **Conclusion.** Apply the Main Lemma to $P^*$. The antecedent is empty, so its witness predicate is the empty conjunction, which is true.
64. So some $\Sigma^b_i$-defined $g \in \square^p_i$ satisfies $S^i_2 \vdash \mathrm{Witness}_{\exists y \le t \, A}(g(\bar c), \bar c)$.
65. By the clause for $\exists y \le t$, $\beta(1, g(\bar c)) \le t$ and $\mathrm{Witness}_A(\beta(2, g(\bar c)), \bar c, \beta(1, g(\bar c)))$.
66. Step 50 gives $S^i_2 \vdash A(\bar c, \beta(1, g(\bar c)))$.
67. Let $f(\bar x) := \beta(1, g(\bar x))$. It is in $\square^p_i$, since $\square^p_i$ is closed under composition.
68. The formula $y = \beta(1, g(\bar x))$, translated by L2, is a $\Sigma^b_i$ definition of $f$ in $S^i_2$.
69. $S^i_2 \vdash \forall \bar x \, A(\bar x, f(\bar x))$, and $A(\bar n, f(\bar n))$ is true since $\N$ is a model of $S^i_2$. This proves part 1.

**Part 3.**

70. Let $A \in \Sigma^b_i$, $B \in \Pi^b_i$ and $S^i_2 \vdash A \leftrightarrow B$. Let $C(\bar x, y)$ be $(y = 1 \land A(\bar x)) \lor (y = 0 \land \neg B(\bar x))$.
71. $\neg B$ is $\Sigma^b_i$, so $C$ is $\Sigma^b_i$. $S^i_2 \vdash \forall \bar x \, \exists y \, C$: if $A$, take $y = 1$; if $\neg A$, then $\neg B$, so take $y = 0$.
72. Part 1 gives $f \in \square^p_i$ with $C(\bar n, f(\bar n))$ true for all $\bar n$.
73. If $f(\bar n) = 1$, the first disjunct holds, so $A(\bar n)$ is true. Otherwise the second holds, so $B(\bar n)$ fails, and so does $A(\bar n)$.
74. So $A(\bar n)$ holds if and only if $f(\bar n) = 1$, and this test is in $\Delta^p_i = \mathrm{P}^{\Sigma^p_{i-1}}$.
75. Conversely, let $Q \in \Delta^p_i$. Its characteristic function $\chi_Q$ is in $\square^p_i$, so part 2 gives $A_\chi$ and a term $t$.
76. Then $\exists y \le t \, (A_\chi(\bar x, y) \land y = 1)$ is $\Sigma^b_i$, and $\forall y \le t \, (A_\chi(\bar x, y) \to y = 1)$ is $\Pi^b_i$.
77. Existence and uniqueness make the two formulas $S^i_2$-provably equivalent, and both define $Q$. $\blacksquare$

## Idea

The easy direction is a translation of programs into formulas: a polynomial-time computation is a short sequence of values, and polynomial induction proves that this sequence exists.
The hard direction runs the other way.
Free-cut elimination makes every formula in the proof $\Sigma^b_i$, and then each inference becomes a step of a $\square^p_i$ algorithm that transforms witnesses.
Polynomial induction becomes limited iteration on notation, which is why the class is exactly polynomial time.

## Variants

- Part 2 can also be proved through [[Cook's theory PV|FMM44KFZQT]]: each $\mathsf{PV}$ symbol receives a $\Sigma^b_1$ definition in $S^1_2$, and the $\mathsf{PV}$ rules become provable. The uniqueness rule then plays the role of step 43.
- Proofs by realizability and by functional interpretation replace free-cut elimination by an interpretation of each formula.
- For $T^1_2$ the same Main Lemma method, with $\Sigma^b_1$-$\mathrm{IND}$ in place of $\mathrm{PIND}$, produces polynomial local search problems instead of limited iteration.
