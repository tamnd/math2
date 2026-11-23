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

We prove part 2 for $i = 1$ in full by writing each polynomial-time computation as a short sequence of values, and we give the structure of part 1 with its cited lemmas.
Part 3 then follows from parts 1 and 2.

### Cited facts

**Cobham's theorem.** $\mathrm{FP}$ is the closure of the projections and the base functions $0$, $S(x)$, $\lfloor x/2 \rfloor$, $2x$, $\chi_\le(x, z)$ and $\mathrm{Choice}(x, y, z)$ under composition and limited iteration on notation.
Here $\chi_\le(x, z) = 1$ if $x \le z$ and $0$ otherwise, and $\mathrm{Choice}(x, y, z) = y$ if $x > 0$ and $z$ otherwise.
Limited iteration on notation defines $f(\bar x, 0) = g(\bar x)$ and $f(\bar x, y) = h(\bar x, y, f(\bar x, \lfloor y/2 \rfloor))$ for $y > 0$.
It requires $\lvert f(\bar x, y) \rvert \le q(\lvert \bar x \rvert, \lvert y \rvert)$ for a polynomial $q$.

**L1 (monotonicity).** $S^1_2$ proves that $\le$ is a linear order and that each function symbol is nondecreasing in each argument.
So for every term $t$, $S^1_2 \vdash \bar a \le \bar b \to t(\bar a) \le t(\bar b)$.
It also proves $\lvert 0 \rvert = 0$, $\lfloor u/2 \rfloor \le u$, and $\lvert \lfloor u/2 \rfloor \rvert + 1 = \lvert u \rvert$ for $u \ge 1$.

**L2 (new symbols).** A function $\Sigma^b_1$-defined in $S^1_2$ can be added to the language with its defining axiom.
Each $\Sigma^b_1$ or $\Pi^b_1$ formula of the new language is $S^1_2$-provably equivalent to one of the old language.
Polynomial induction stays valid for $\Sigma^b_1$ formulas of the new language.

**L3 (sequences).** $S^1_2$ $\Sigma^b_1$-defines the entry $\beta(j, w)$, the length $\mathrm{Len}(w)$, appending an entry, and $\mathrm{MSP}(u, k) = \lfloor u / 2^k \rfloor$, and it proves their usual properties.
There is a term $\mathrm{SqBd}(a, b)$ such that every sequence of length at most $\lvert b \rvert + 1$ with entries at most $a$ has a code at most $\mathrm{SqBd}(a, b)$.

**L4 (length induction).** $S^1_2$ proves $\Sigma^b_1$-$\mathrm{LIND}$, the scheme $A(0) \land \forall j \, (A(j) \to A(j + 1)) \to \forall x \, A(\lvert x \rvert)$.

### Part 2: the claim and the base functions

We show that every $f \in \mathrm{FP}$ is $\Sigma^b_1$-definable in $S^1_2$, by induction on a Cobham derivation of $f$.
The stronger claim is that there are a $\Sigma^b_1$ formula $A_f(\bar x, y)$ and a term $t_f(\bar x)$ with three properties.
(a) $A_f(\bar n, f(\bar n))$ is true for all $\bar n$.
(b) $S^1_2 \vdash \forall \bar x \, \exists y \le t_f(\bar x) \, A_f(\bar x, y)$.
(c) $S^1_2 \vdash A_f(\bar x, y) \land A_f(\bar x, y') \to y = y'$.

1. For the base functions take $y = 0$, $y = Sx$, $y = \lfloor x/2 \rfloor$ and $y = x + x$, and for a projection take $y = x_j$.
   Their bounds are $0$, $Sx$, $x$, $x + x$ and $x_j$, where $\lfloor x/2 \rfloor \le x$ is from L1.
2. For $\chi_\le$ take $(x \le z \land y = S0) \lor (\neg x \le z \land y = 0)$, with bound $S0$.
3. For $\mathrm{Choice}$ take $(\neg x = 0 \land v = y) \lor (x = 0 \land v = z)$, with bound $y + z$.
4. These formulas are open, so they are $\Sigma^b_1$, and property (a) holds by the definitions of the functions.
5. Property (b) holds by pure logic, with $y + z$ bounding both $y$ and $z$ by L1.
6. Property (c) uses only $0 \ne S0$, an axiom of $\mathsf{BASIC}$.

### Part 2: composition

7. Let $f(\bar x) = h(g_1(\bar x), \dots, g_m(\bar x))$, and assume the claim for $h$ and each $g_l$.
8. By L2 we add symbols for $h$ and the $g_l$.
   By (b) and (c), $S^1_2 \vdash g_l(\bar x) \le t_{g_l}(\bar x)$ and $S^1_2 \vdash h(\bar u) \le t_h(\bar u)$.
9. Let $A_f(\bar x, y)$ be $y = h(g_1(\bar x), \dots, g_m(\bar x))$, which L2 turns into a $\Sigma^b_1$ formula of the base language.
10. Property (a) holds since the symbols denote $h$ and the $g_l$, and property (c) is the transitivity of $=$.
11. Let $t_f := t_h(t_{g_1}(\bar x), \dots, t_{g_m}(\bar x))$.
    Step 8 and L1 give $h(g_1(\bar x), \dots) \le t_f(\bar x)$, so (b) holds.

### Part 2: limited iteration and its trace

12. Let $f$ come from $g$ and $h$ by limited iteration with bound $q$, and assume the claim for $g$ and $h$.
    We add their symbols by L2.
13. We choose a term $T(\bar x, y)$ with $2^{q(\lvert \bar x \rvert, \lvert y \rvert)} \le T(\bar x, y)$ for all values.
    Let $s := x_1 + \dots + x_k + y + 2$, so $q(\lvert \bar x \rvert, \lvert y \rvert) \le c \lvert s \rvert^d$ for some $c \ge 1$ and $d \ge 2$.
14. Since $\lvert 2^m \rvert = m + 1$, nesting $d - 1$ smashes $s \# (s \# \cdots)$ gives a value at least $2^{\lvert s \rvert^d}$.
    The product of $c$ copies of this term is $T$.
15. Since $v + 1 \le 2^{\lvert v \rvert}$ for all $v$, the bound on $f$ gives $f(\bar n, m) < T(\bar n, m)$ for all $\bar n, m$.
16. For $u$ and $j \le \lvert u \rvert$ we write $u_j := \mathrm{MSP}(u, \lvert u \rvert - j)$, the number formed by the first $j$ binary digits of $u$.
17. By L1 and L3, $S^1_2$ proves $u_0 = 0$, $u_{\lvert u \rvert} = u$, $u_j \le u$, and $u_j \ge 1$ for $j \ge 1$.
18. It also proves $\lfloor u_j / 2 \rfloor = u_{j - 1}$ for $1 \le j \le \lvert u \rvert$, and $(\lfloor u/2 \rfloor)_j = u_j$ for $u \ge 1$ and $j < \lvert u \rvert$.
### Part 2: the trace formula

19. Let $\mathrm{Start}(\bar x, e)$ be $(g(\bar x) \le T(\bar x, 0) \land e = g(\bar x)) \lor (\neg g(\bar x) \le T(\bar x, 0) \land e = 0)$.
20. Let $\mathrm{Step}(\bar x, u, z, e)$ be the formula $(h(\bar x, u, z) \le T(\bar x, u) \land e = h(\bar x, u, z)) \lor (\neg h(\bar x, u, z) \le T(\bar x, u) \land e = 0)$.
21. Each of the two formulas determines $e$ from the other arguments, and forces $e \le T(\bar x, 0)$ or $e \le T(\bar x, u)$.
22. Let $\mathrm{Comp}(w, \bar x, u)$ say three things: $\mathrm{Len}(w) = \lvert u \rvert + 1$, then $\mathrm{Start}(\bar x, \beta(1, w))$, and then the condition below.
    $$\forall j < \lvert u \rvert \; \mathrm{Step}(\bar x, u_{j + 1}, \beta(j + 1, w), \beta(j + 2, w)).$$
23. The quantifier $\forall j < \lvert u \rvert$ is sharply bounded, so $\mathrm{Comp}$ is $\Sigma^b_1$ after the translation of L2.
24. We define $t_f := T$ and the formula below.
    $$A_f(\bar x, y, v) := \exists w \le \mathrm{SqBd}(T(\bar x, y), y) \, (\mathrm{Comp}(w, \bar x, y) \land v = \beta(\lvert y \rvert + 1, w)).$$

### Part 2: the trace is correct

25. Fix $\bar n, m$, and let $e_j = \beta(j + 1, w)$ be the entries of a $w$ with $\mathrm{Comp}(w, \bar n, m)$.
    We show $e_j = f(\bar n, m_j)$ by induction on $j$.
26. For $j = 0$ we have $g(\bar n) = f(\bar n, 0) < T(\bar n, 0)$ by step 15, so $\mathrm{Start}$ gives $e_0 = g(\bar n) = f(\bar n, m_0)$.
27. For $j \ge 1$ we have $m_j \ge 1$ and $\lfloor m_j/2 \rfloor = m_{j - 1}$, so $h(\bar n, m_j, e_{j - 1}) = f(\bar n, m_j)$.
    This value is below $T(\bar n, m_j)$ by step 15, so $\mathrm{Step}$ gives $e_j = f(\bar n, m_j)$.
28. For property (a), the sequence $\langle f(\bar n, m_0), \dots, f(\bar n, m_{\lvert m \rvert}) \rangle$ satisfies $\mathrm{Comp}$, by the computation in steps 26 and 27.
29. Its entries are below $T(\bar n, m_j) \le T(\bar n, m)$, by step 15 and L1.
    So L3 bounds its code by $\mathrm{SqBd}$, and its last entry is $f(\bar n, m)$.

### Part 2: the trace exists

30. For property (b), fix $\bar x, y$, and let $\Phi(u)$ be $\neg u \le y \lor \exists w \le \mathrm{SqBd}(T(\bar x, y), y) \, \mathrm{Comp}(w, \bar x, u)$, a $\Sigma^b_1$ formula.
31. $\Phi(0)$ holds: take the one-entry sequence $\langle e_0 \rangle$ with $\mathrm{Start}(\bar x, e_0)$, so that $e_0 \le T(\bar x, 0) \le T(\bar x, y)$.
32. For the step, let $1 \le u \le y$ and assume $\Phi(\lfloor u/2 \rfloor)$.
    Since $\lfloor u/2 \rfloor \le u \le y$, some $w'$ satisfies $\mathrm{Comp}(w', \bar x, \lfloor u/2 \rfloor)$.
33. Then $\mathrm{Len}(w') = \lvert u \rvert$ by L1.
    Let $e$ satisfy $\mathrm{Step}(\bar x, u, \beta(\lvert u \rvert, w'), e)$, and let $w$ be $w'$ with $e$ appended.
34. The conditions of $\mathrm{Comp}(w, \bar x, u)$ for $j < \lvert u \rvert - 1$ hold because they hold for $w'$, since $(\lfloor u/2 \rfloor)_{j + 1} = u_{j + 1}$ by step 18.
35. The condition for $j = \lvert u \rvert - 1$ is the choice of $e$, since $u_{\lvert u \rvert} = u$.
36. Each entry of $w$ is at most $T(\bar x, u_j) \le T(\bar x, y)$, by step 21 and L1, and the length is $\lvert u \rvert + 1 \le \lvert y \rvert + 1$.
37. So L3 gives $w \le \mathrm{SqBd}(T(\bar x, y), y)$, and $\Phi(u)$ holds.
    For $u = 0$ the step holds because $\Phi(0)$ holds, and for $\neg u \le y$ it holds because the first disjunct is true.
38. $\Sigma^b_1$-$\mathrm{PIND}$ gives $\forall u \, \Phi(u)$.
    With $u := y$ we get a $w$, and $v := \beta(\lvert y \rvert + 1, w) \le T(\bar x, y)$ satisfies $A_f$.

### Part 2: the trace is unique

39. For property (c), let $w$ and $w'$ both satisfy $\mathrm{Comp}(\cdot, \bar x, y)$.
    Let $\Psi(j)$ be $\forall j' \le \lvert y \rvert \, (j' \le j \to \beta(j' + 1, w) = \beta(j' + 1, w'))$.
40. $\Psi$ is a sharply bounded quantifier over an open formula, so it is $\Sigma^b_1$, and $\Psi(0)$ holds since $\mathrm{Start}$ determines the first entry.
41. Assume $\Psi(j)$.
    If $j < \lvert y \rvert$, then $\Psi(j + 1)$ holds, since $\mathrm{Step}$ determines entry $j + 2$ from entry $j + 1$, by step 21.
    If $j \ge \lvert y \rvert$, then $\Psi(j + 1)$ says no more than $\Psi(j)$.
42. L4 gives $\Psi(\lvert y \rvert)$, so the last entries agree and $v = v'$.
    This completes the induction and part 2 for $i = 1$.

Part 2 for $i \ge 2$ is cited from Buss.
The proof is the same induction, with oracle queries to $\Sigma^p_{i-1}$ sets expressed by $\Sigma^b_{i-1}$ formulas.

### Part 1: a proof in which every formula is bounded

43. Assume $S^i_2 \vdash \forall \bar x \, \exists y \, A(\bar x, y)$ with $A \in \Sigma^b_i$, and let $\bar c$ be new free variables.
44. Parikh's theorem for $S^i_2$, the analogue of [[Parikh's theorem|YPQPC1WJMV]] for this language, gives a term $t$ with $S^i_2 \vdash \exists y \le t(\bar c) \, A(\bar c, y)$.
45. We write $S^i_2$ in the [[sequent calculus|W72CA3R9MP]] with $\mathsf{BASIC}$ initial sequents and the rule $\Sigma^b_i$-$\mathrm{PIND}$.
    From $B(\lfloor a/2 \rfloor), \Gamma \to \Delta, B(a)$ the rule infers $B(0), \Gamma \to \Delta, B(t)$.
46. Free-cut elimination, which is cited, gives a proof $P^*$ of the sequent $\to \exists y \le t \, A(\bar c, y)$ in which every formula is $\Sigma^b_i$.
47. For $B \in \Sigma^b_i$, a formula $\mathrm{Witness}_B(w, \bar a)$ is defined by recursion on $B$, as cited from Buss.
    For $B \in \Sigma^b_{i-1} \cup \Pi^b_{i-1}$ it is $B$ itself.
48. For $(\exists x \le s) C$ it is $\beta(1, w) \le s \land \mathrm{Witness}_C(\beta(2, w), \bar a, \beta(1, w))$.
    Conjunction, disjunction and sharply bounded $\forall$ use the entries of $w$ in the same way.
49. Then $S^i_2 \vdash B \leftrightarrow \exists w \le t_B \, \mathrm{Witness}_B(w, \bar a)$ and $S^i_2 \vdash \mathrm{Witness}_B(w, \bar a) \to B(\bar a)$, by induction on $B$.
50. Also, $\mathrm{Witness}_B$ is a $\Delta^p_i$ predicate, and it is $\Delta^b_i$ in $S^i_2$.

### Part 1: the main lemma

51. The main lemma, cited from Buss, is about a sequent $\Gamma \to \Delta$ that has a proof in which all formulas are $\Sigma^b_i$, with free variables $\bar c$.
    It says that some $f \in \square^p_i$, $\Sigma^b_i$-defined in $S^i_2$, satisfies the following.
    $$S^i_2 \vdash \mathrm{Witness}_{\bigwedge \Gamma}(w, \bar c) \to \mathrm{Witness}_{\bigvee \Delta}(f(w, \bar c), \bar c).$$
52. The proof is by induction on the number of inferences.
    Cut and the logical rules compose or pair witness functions, and we cite these cases.
53. We give the $\mathrm{PIND}$ case without side formulas, where the premise is $B(\lfloor a/2 \rfloor) \to B(a)$ and the conclusion is $B(0) \to B(t)$.
54. The induction hypothesis gives $g \le t_B(a, \bar c)$ with $\mathrm{Witness}_{B(\lfloor a/2 \rfloor)}(w, a, \bar c) \to \mathrm{Witness}_{B(a)}(g(w, a, \bar c), a, \bar c)$.
55. We define $f$ by limited iteration: $f(w, 0, \bar c) = g(w, 0, \bar c)$ and $f(w, a, \bar c) = g(f(w, \lfloor a/2 \rfloor, \bar c), a, \bar c)$ for $a > 0$.
56. Its values are at most $t_B$, so $f \in \square^p_i$.
    For $i = 1$, steps 12 to 42 with $T := t_B$ define $f$, and since the truncation to $0$ never applies there, $S^1_2$ proves the recursion equations.
57. The formula $\mathrm{Witness}_{B(0)}(w, \bar c) \to \mathrm{Witness}_{B(a)}(f(w, a, \bar c), a, \bar c)$ is $S^i_2$-equivalent to a $\Sigma^b_i$ formula.
    This uses step 50, with $f$ replaced by its $\Sigma^b_i$ definition under a bounded $\exists$, as in L2.
58. The formula holds at $a = 0$, by step 54 with $a = 0$, since $\lfloor 0/2 \rfloor = 0$.
59. If it holds at $\lfloor a/2 \rfloor$, then step 54 and the recursion equation give it at $a$.
    So $\Sigma^b_i$-$\mathrm{PIND}$ in $a$ gives it for all $a$.
60. Substituting $t$ for $a$ gives the witness function $w \mapsto f(w, t, \bar c)$ for $B(0) \to B(t)$.

### Part 1: the conclusion

61. We apply the main lemma to $P^*$.
    The antecedent is empty, so its witness predicate is the empty conjunction, which is true.
62. So some $\Sigma^b_i$-defined $g \in \square^p_i$ satisfies $S^i_2 \vdash \mathrm{Witness}_{\exists y \le t \, A}(g(\bar c), \bar c)$.
63. By the clause for $\exists y \le t$, we get $\beta(1, g(\bar c)) \le t$ and $\mathrm{Witness}_A(\beta(2, g(\bar c)), \bar c, \beta(1, g(\bar c)))$.
64. Step 49 gives $S^i_2 \vdash A(\bar c, \beta(1, g(\bar c)))$.
65. Let $f(\bar x) := \beta(1, g(\bar x))$, which is in $\square^p_i$ since $\square^p_i$ is closed under composition.
66. The formula $y = \beta(1, g(\bar x))$, translated by L2, is a $\Sigma^b_i$ definition of $f$ in $S^i_2$.
67. So $S^i_2 \vdash \forall \bar x \, A(\bar x, f(\bar x))$, and $A(\bar n, f(\bar n))$ is true since $\mathbb{N}$ is a model of $S^i_2$.
    This proves part 1.

### Part 3

68. Let $A \in \Sigma^b_i$ and $B \in \Pi^b_i$ with $S^i_2 \vdash A \leftrightarrow B$.
    Let $C(\bar x, y)$ be $(y = 1 \land A(\bar x)) \lor (y = 0 \land \neg B(\bar x))$.
69. Since $\neg B$ is $\Sigma^b_i$, the formula $C$ is $\Sigma^b_i$.
    Also $S^i_2 \vdash \forall \bar x \, \exists y \, C$: if $A$ holds take $y = 1$, and if $A$ fails then $B$ fails, so take $y = 0$.
70. Part 1 gives $f \in \square^p_i$ with $C(\bar n, f(\bar n))$ true for all $\bar n$.
71. If $f(\bar n) = 1$, the first disjunct holds, so $A(\bar n)$ is true.
    Otherwise $f(\bar n) = 0$ and the second disjunct holds, so $B(\bar n)$ fails, and so does $A(\bar n)$.
72. So $A(\bar n)$ holds if and only if $f(\bar n) = 1$, and this test is in $\Delta^p_i = \mathrm{P}^{\Sigma^p_{i-1}}$.
73. Conversely, let $Q \in \Delta^p_i$.
    Its characteristic function $\chi_Q$ is in $\square^p_i$, so part 2 gives a definition $A_\chi$ and a term $t$.
74. Then $\exists y \le t \, (A_\chi(\bar x, y) \land y = 1)$ is $\Sigma^b_i$, and $\forall y \le t \, (A_\chi(\bar x, y) \to y = 1)$ is $\Pi^b_i$.
75. Existence and uniqueness make the two formulas $S^i_2$-provably equivalent, and both define $Q$.

## Idea

The easy direction translates programs into formulas.
A polynomial-time computation is a short sequence of values, one for each binary digit of the input, and polynomial induction proves that this sequence exists.
The hard direction runs the other way.
Free-cut elimination makes every formula in the proof $\Sigma^b_i$, and then each inference becomes a step of a $\square^p_i$ algorithm that transforms witnesses.
Polynomial induction becomes limited iteration on notation, and that is why the class is exactly polynomial time.

## Variants

Part 2 can also be proved through [[Cook's theory PV|FMM44KFZQT]].
Each $\mathsf{PV}$ symbol receives a $\Sigma^b_1$ definition in $S^1_2$, the $\mathsf{PV}$ rules become provable, and the uniqueness rule plays the role of step 42.

Proofs by realizability and by functional interpretation replace free-cut elimination by an interpretation of each formula.
For $T^1_2$ the same main-lemma method, with $\Sigma^b_1$-$\mathrm{IND}$ in place of $\mathrm{PIND}$, produces polynomial local search problems instead of limited iteration.
