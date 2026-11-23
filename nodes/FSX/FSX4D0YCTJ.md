---
tag: FSX4D0YCTJ
kind: proof
name: Proof of the decidability of Presburger arithmetic by Cooper's quantifier elimination
aliases: [cooper-quantifier-elimination, proof-of-presburgers-theorem]
msc: ["03B25", "03C10"]
topics: [E4AVTNWE9E]
audience: grad
proves: 4W0E9G7PPV
methods: [12MQ2NJ29A, 0ASJVEFA9J, 0WCP0PVET6, 0J0XBKG64S, X5HG1RNWQX]
uses: [7FDDXV3JK7, 007NPQX34K, 0WAY5WX8NY, JS7BWX3HW3, HWC687ES0Q, W65B6BKZRY]
sources:
  - url: https://en.wikipedia.org/wiki/Presburger_arithmetic
    locator: Decidability of Presburger arithmetic
  - url: https://en.wikipedia.org/wiki/Quantifier_elimination
    locator: lead section
---

## Proof

We remove one existential quantifier at a time: we normalize the formula so that the variable has coefficient $1$, and then we replace the quantifier by a finite disjunction over test points.
We use the signature $L_{\mathbb{Z}}$ and the structure $\mathbb{Z}$ of the [[statement|4W0E9G7PPV]].
For an integer $m \ge 0$ and a term $t$, we write $m t$ for $t + \cdots + t$ with $m$ summands, $0$ when $m = 0$, and $-m t$ for $0 - m t$.
For an integer $i \ge 1$ we write $i$ also for the closed term $1 + \cdots + 1$.
We call a formula positive when it is built from atomic formulas with $\wedge$ and $\vee$ only.

### Linear forms and positive formulas

1. Every $L_{\mathbb{Z}}$-term $t(\vec{x})$ has the same value in $\mathbb{Z}$ as a linear form $a_1 x_1 + \cdots + a_k x_k + c$ with integers $a_i, c$, by induction on terms.
2. Conversely, each such linear form is the value of a term built with $+$, $-$ and $1$.
3. In $\mathbb{Z}$, $s < t \leftrightarrow 0 < t - s$, and $s = t \leftrightarrow (0 < t - s + 1 \wedge 0 < s - t + 1)$.
4. The second equivalence holds because the only integer $u$ with $-1 < u < 1$ is $0$.
5. So every atomic formula is equivalent to a positive formula with atoms of the forms $0 < t$ and $D_n(t)$.
6. In $\mathbb{Z}$, $\neg (0 < t) \leftrightarrow 0 < 1 - t$, because $t \le 0$ holds exactly when $1 - t \ge 1$.
7. In $\mathbb{Z}$, $\neg D_n(t) \leftrightarrow \bigvee_{r = 1}^{n - 1} D_n(t + r)$.
   This holds because $t$ is not divisible by $n$ exactly when $t \equiv -r \pmod{n}$ for some $r$ with $1 \le r \le n - 1$.
8. With the laws of De Morgan we move each negation down to the atoms, and steps 6 and 7 remove it.
   So every quantifier-free formula is equivalent to a positive formula.
9. It is enough to eliminate $\exists y$ from $\exists y \, \theta$ for a positive $\theta$.
   By [[structural induction|12MQ2NJ29A]] we remove the innermost quantifier first, and we write $\forall y \, \alpha$ as $\neg \exists y \, \neg \alpha$.

### Making the coefficient of the variable equal to one

10. Let $\theta(y, \vec{x})$ be positive.
    By step 1, each atom is $0 < a y + t$ or $D_n(a y + t)$, with an integer $a$ and a term $t$ without $y$.
11. If no atom has $a \ne 0$, then $\exists y \, \theta$ is equivalent to $\theta$, and we are done.
    Otherwise let $l$ be the [[least common multiple|007NPQX34K]] of the numbers $\lvert a \rvert$ with $a \ne 0$.
12. For an atom with $a \ne 0$, let $m = l / \lvert a \rvert$, a positive integer.
    Replace $0 < a y + t$ by $0 < m a y + m t$, which is equivalent since $m > 0$.
13. Replace $D_n(a y + t)$ by $D_{m n}(m a y + m t)$.
    This is equivalent because $n$ divides $u$ exactly when $m n$ divides $m u$.
14. Now each nonzero coefficient of $y$ is $l$ or $-l$.
    In divisibility atoms, the rule $D_k(u) \leftrightarrow D_k(-u)$ makes the coefficient $+l$.
15. So $\theta$ is equivalent to $\psi(l y, \vec{x})$, where $\psi(z, \vec{x})$ is positive and $z$ has coefficient $1$ or $-1$ in each atom that contains it.
16. In $\mathbb{Z}$, $\exists y \, \psi(l y, \vec{x}) \leftrightarrow \exists z \, (D_l(z) \wedge \psi(z, \vec{x}))$, because the values of $l y$ are exactly the multiples of $l$.
    For $l = 1$ we omit $D_l(z)$.
17. Let $\chi(z, \vec{x})$ be $D_l(z) \wedge \psi(z, \vec{x})$.
    It is positive, and each atom that contains $z$ has one of three forms.
18. Form (i) is a lower bound $0 < z - s$, that is $s < z$, and form (ii) is an upper bound $0 < u - z$, that is $z < u$.
19. Form (iii) is $D_n(z + t)$.
    Here $s$, $u$ and $t$ are terms without $z$.

### The test points

20. Let $s_1, \ldots, s_m$ be the terms of the lower bounds in $\chi$.
    Let $\delta$ be the least common multiple of the numbers $n$ in atoms of form (iii), or $\delta = 1$ if there are none.
21. Let $\chi_{-\infty}(z, \vec{x})$ be $\chi$ with each lower bound replaced by $0 < 0$ and each upper bound replaced by $0 < 1$.
22. Let $\rho(\vec{x})$ be the following quantifier-free formula:
    $$\rho = \bigvee_{i = 1}^{\delta} \chi_{-\infty}(i, \vec{x}) \vee \bigvee_{j = 1}^{m} \bigvee_{i = 1}^{\delta} \chi(s_j + i, \vec{x}).$$
23. We claim that $\mathbb{Z} \models \exists z \, \chi \leftrightarrow \rho$.
    We fix integer values of $\vec{x}$, so that the $s_j$, $u$ and $t$ become integers.
24. Lemma on positive formulas: if every atom of $\chi$ that is true at $z = c$ is also true at $z = d$, then $\chi(c)$ implies $\chi(d)$.
    This holds by induction on positive formulas.
25. Periodicity: $\chi_{-\infty}(c) \leftrightarrow \chi_{-\infty}(c - \delta)$ for every integer $c$.
    Only atoms of form (iii) depend on $z$ in $\chi_{-\infty}$, and each of their $n$ divides $\delta$.
26. Far to the left: if $c \le s_j$ for all $j$ and $c < u$ for all upper bounds $u$, then $\chi(c) \leftrightarrow \chi_{-\infty}(c)$.
27. Step 26 holds because at such a $c$ each lower bound is false, like $0 < 0$, and each upper bound is true, like $0 < 1$.

### Every test point gives a witness

28. Suppose that $\chi(s_j + i)$ holds.
    Then $z = s_j + i$ is a witness for $\exists z \, \chi$.
29. Suppose that $\chi_{-\infty}(i)$ holds.
    Choose $k \ge 0$ so that $c = i - k \delta$ satisfies the condition of step 26, which is possible since $\delta \ge 1$.
30. By step 25, applied $k$ times, $\chi_{-\infty}(c)$ holds.
    By step 26, $\chi(c)$ holds, so $c$ is a witness.

### A witness gives a test point

31. Let $\chi(c_0)$ hold.
    If some $\chi(s_j + i)$ holds with $1 \le i \le \delta$, then $\rho$ holds.
32. So assume that no $\chi(s_j + i)$ with $1 \le i \le \delta$ holds.
    We show that $\chi(c_0 - \delta)$ holds.
33. Atoms without $z$ do not change, and atoms of form (iii) keep their value for the reason of step 25.
34. An upper bound $c_0 < u$ that holds gives $c_0 - \delta < u$, since $\delta \ge 1$.
35. Let a lower bound $s_j < c_0$ hold, and suppose, for a contradiction, that $s_j < c_0 - \delta$ fails.
36. Then $s_j < c_0 \le s_j + \delta$, so $c_0 = s_j + i$ with $1 \le i \le \delta$.
37. Then $\chi(s_j + i)$ is $\chi(c_0)$, which holds, against the assumption of step 32.
    So $s_j < c_0 - \delta$ holds.
38. By steps 33 to 37 and the lemma of step 24, $\chi(c_0 - \delta)$ holds.
39. The assumption of step 32 does not depend on $c_0$.
    So by [[induction|0ASJVEFA9J]] on $k$, $\chi(c_0 - k \delta)$ holds for every $k \ge 0$.
40. Choose $k$ so that $c = c_0 - k \delta$ satisfies the condition of step 26.
    Then $\chi_{-\infty}(c)$ holds.
41. Let $i \in \{ 1, \ldots, \delta \}$ with $i \equiv c \pmod{\delta}$.
    By step 25, $\chi_{-\infty}(i)$ holds, so $\rho$ holds.
42. This proves the claim of step 23.
    With steps 9 and 16, it proves part 1 of the statement.
43. Each step is an explicit rewriting of formulas, so $\psi$ is computed from $\varphi$.

### Decidability over the integers

44. Let $\sigma$ be an $L_{\mathbb{Z}}$-sentence.
    Part 1 computes a quantifier-free sentence $\sigma'$ with $\mathbb{Z} \models \sigma \leftrightarrow \sigma'$.
45. The atoms of $\sigma'$ contain only closed terms, and we compute the integer value of each.
46. Each atom $0 < c$ or $D_n(c)$ with an integer $c$ is checked by a comparison or a division.
    So the truth of $\sigma$ in $\mathbb{Z}$ is computed, and this proves part 2.

### From the integers to the natural numbers

47. For part 3, let $\sigma$ be a sentence in the symbols $0, 1, +$.
48. Let $\sigma^{\mathbb{N}}$ replace each $\exists x \, \alpha$ by $\exists x \, (0 < x + 1 \wedge \alpha)$ and each $\forall x \, \alpha$ by $\forall x \, (0 < x + 1 \to \alpha)$.
49. In $\mathbb{Z}$, $0 < x + 1$ holds exactly for $x \in \mathbb{N}$.
50. The set $\mathbb{N}$ contains $0$ and $1$ and is closed under $+$.
    So $(\mathbb{N}, 0, 1, +)$ is a [[substructure|JS7BWX3HW3]] of $(\mathbb{Z}, 0, 1, +)$.
51. By induction on formulas, $(\mathbb{N}, 0, 1, +) \models \alpha(\vec{a})$ exactly when $\mathbb{Z} \models \alpha^{\mathbb{N}}(\vec{a})$, for all $\vec{a}$ in $\mathbb{N}$.
52. In step 51, atoms agree because $\mathbb{N}$ is a substructure, and each quantifier ranges over $\mathbb{N}$ by step 49.
53. So $\sigma$ is in $\operatorname{Th}(\mathbb{N}, 0, 1, +)$ exactly when $\mathbb{Z} \models \sigma^{\mathbb{N}}$, and part 2 decides this.
54. Therefore $\operatorname{Th}(\mathbb{N}, 0, 1, +)$ is a [[decidable theory|HWC687ES0Q]].

## Idea

After the normalization, every atom in the variable $z$ is a lower bound, an upper bound or a congruence condition, and $z$ has coefficient $1$ everywhere.
If a witness exists, then either some witness lies just above a lower bound, within one period $\delta$ of the congruences, or the formula holds arbitrarily far to the left.
Far to the left only the congruences matter, and they repeat with period $\delta$, so finitely many test points are enough.
Replacing the quantifier by the disjunction over these test points removes it.

## Variants

Many textbook proofs first bring the matrix into disjunctive normal form and then eliminate the quantifier from each conjunction of bounds and congruences, with the Chinese remainder theorem.
Cooper's method avoids the normal form, which can be exponentially longer.

The automata proof writes numbers in binary, least significant digit first, and a [[finite automaton|W65B6BKZRY]] with one carry bit checks $x + y = z$ on the tuple of digit strings.
Then $\wedge$ is a product of automata, $\neg$ is complementation of a deterministic automaton, and $\exists$ is projection, which needs a subset construction and care with padding zeros.
A sentence is true exactly when its automaton accepts the empty word, and this is checked by an algorithm.
The same proof works for [[Büchi arithmetic|NSTECGT93D]], as in [[the proof that its definable relations are automatic|WX2B2GTGJX]].

Model-theoretic proofs show quantifier elimination for the theory of $\mathbb{Z}$-groups by a test that eliminates one existential quantifier in front of a conjunction of atoms.
