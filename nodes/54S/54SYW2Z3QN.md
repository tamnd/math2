---
tag: 54SYW2Z3QN
kind: proof
name: Proof of Parikh's theorem by cuts in a nonstandard model
msc: ["03F30", "03C62"]
topics: [RA380RWEC0]
audience: research
proves: YPQPC1WJMV
uses: [1NR3HAWG9D, WQ1ZE255SF, 676H7EGTKJ, GE43CSZTS9, 3K1AKGXF8A, 1QD0KDDGYJ, GJ9KW45F3C, 1QWN5CV4CG]
methods: [0J0XBKG64S, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: lead section
---

## Proof

We assume that no term bounds the witness, build a model in which the witness is too large, cut that model down to the part below the terms, and find a small witness in the cut.
We write $x \le y$ for $x < y \lor x = y$, and we use one standard fact without proof.

**Fact A.** $\mathsf{I}\Delta_0$ proves that $<$ is a discrete linear order with least element $0$, and that $x < Sx$.
It proves that $+$ and $\cdot$ are commutative, associative and monotone: $x \le y \to x + z \le y + z$ and $x \le y \to x \cdot z \le y \cdot z$.
Each law follows by open induction, as in [[the proof that addition commutes|GJ9KW45F3C]].

Let $T$ and $\varphi(\bar x, y)$ be as in the statement, with $\bar x = (x_1, \dots, x_m)$.
If $T$ is inconsistent, it proves every sentence, and the term $t = 0$ works.
So let $T$ be consistent.
Suppose, for a contradiction, that $T \nvdash \forall \bar x \, \exists y < t(\bar x) \, \varphi(\bar x, y)$ for every term $t(\bar x)$ of $L_A$.

### A model with no small witness

1. Add new constants $\bar c = (c_1, \dots, c_m)$ to $L_A$.
   Let $\Gamma$ be $T$ together with the sentences $\neg \exists y < t(\bar c) \, \varphi(\bar c, y)$, one for each term $t(\bar x)$ of $L_A$.
2. Let $\Gamma_0 \subseteq \Gamma$ be finite, so it contains the new sentences for finitely many terms $t_1, \dots, t_k$.
   Let $s = t_1 + \dots + t_k$, and let $s = 0$ when $k = 0$.
3. By the assumption, $T \nvdash \forall \bar x \, \exists y < s(\bar x) \, \varphi(\bar x, y)$.
   By the [[completeness theorem|WQ1ZE255SF]] there is a model $M' \models T$ with elements $\bar a'$ such that $M' \models \neg \exists y < s(\bar a') \, \varphi(\bar a', y)$.
4. By Fact A, $M' \models t_i(\bar a') \le s(\bar a')$ for each $i$.
   So every $y < t_i(\bar a')$ satisfies $y < s(\bar a')$, by transitivity, and so it fails $\varphi(\bar a', y)$.
5. So $M'$, with $c_j$ read as $a'_j$, is a model of $\Gamma_0$.
6. By steps 2 to 5, every finite subset of $\Gamma$ has a model.
   The [[compactness theorem|1NR3HAWG9D]] gives a model $M$ of $\Gamma$, and we let $\bar a$ be the values of $\bar c$ in $M$.

### The cut below the terms

7. Let $I = \{ b \in M : M \models b < t(\bar a) \text{ for some term } t(\bar x) \text{ of } L_A \}$.
8. The set $I$ is closed downward: if $d < b$ and $b < t(\bar a)$, then $d < t(\bar a)$ by transitivity, which is part of Fact A.
9. We have $0 \in I$, since $0 < S0$, and each $a_j \in I$, since $a_j < S a_j$ and $S x_j$ is a term.
10. The set $I$ is closed under $S$, $+$ and $\cdot$.
    Let $b < t(\bar a)$ and $b' < t'(\bar a)$.
    By Fact A, $Sb \le t(\bar a) < S t(\bar a)$, and $b + b' \le t(\bar a) + t'(\bar a) < S(t(\bar a) + t'(\bar a))$.
    In the same way, $b \cdot b' \le t(\bar a) \cdot t'(\bar a) < S(t(\bar a) \cdot t'(\bar a))$.
11. By steps 9 and 10, $I$ is the domain of a [[substructure|676H7EGTKJ]] of $M$ for $L_A$, with $<$ restricted to $I$, and we also call this substructure $I$.
    For every term $r$ and $\bar b \in I$, the value of $r(\bar b)$ is the same in $I$ and in $M$.

### Bounded formulas mean the same in the cut

12. We claim that for every $\Delta_0$ formula $\theta(\bar z)$ and every $\bar b \in I$, $I \models \theta(\bar b)$ if and only if $M \models \theta(\bar b)$.
    We prove the claim by [[structural induction|12MQ2NJ29A]] on $\theta$.
13. For an atomic $\theta$, the values of terms agree by step 11, and $<$ on $I$ is the restriction of $<$ on $M$.
14. For $\theta = \neg \theta_1$ or $\theta = \theta_1 \land \theta_2$, the claim for $\theta_1$ and $\theta_2$ gives the claim for $\theta$.
15. Let $\theta = \exists u < r(\bar z) \, \theta_1(u, \bar z)$, with $u$ not in $r$.
    The value $e = r(\bar b)$ lies in $I$ by step 11, and every $u \in M$ with $u < e$ lies in $I$ by step 8.
16. So the elements below $e$ are the same in $I$ and in $M$, and the claim for $\theta_1$, applied to each of them, gives the claim for $\theta$.
17. The case $\forall u < r(\bar z) \, \theta_1$ is equivalent to $\neg \exists u < r(\bar z) \, \neg \theta_1$, so steps 14 to 16 apply.

### The cut satisfies the axioms

18. Each axiom of [[$\mathsf{Q}$|3K1AKGXF8A]] follows logically from a $\Pi_1$ sentence that holds in $M$.
    The axioms for $S$, $+$ and $\cdot$, except $\mathsf{Q}3$, are already $\Pi_1$.
    The axiom $\mathsf{Q}3$, $x \ne 0 \to \exists y \, (x = Sy)$, follows from $\forall x \, (x \ne 0 \to \exists y < x \, (x = Sy))$.
    That sentence holds in $M$ by $\mathsf{Q}3$ and $y < Sy$.
19. The axiom $\mathsf{Q}8$, $x < y \leftrightarrow \exists v \, (v + Sx = y)$, follows from two $\Pi_1$ sentences.
    The first is $\forall x \, \forall y \, \forall v \, (v + Sx = y \to x < y)$.
    The second is $\forall x \, \forall y \, (x < y \to \exists v < Sy \, (v + Sx = y))$.
    Both hold in $M$, since $v \le v + Sx < S(v + Sx)$ by Fact A.
20. Let $\forall \bar w \, \chi(\bar w)$ be a $\Pi_1$ sentence true in $M$, with $\chi$ in $\Delta_0$.
    For $\bar b \in I$ we have $M \models \chi(\bar b)$, so $I \models \chi(\bar b)$ by step 12, and so $I \models \forall \bar w \, \chi(\bar w)$.
21. Steps 18 to 20 show that $I$ satisfies the axioms of $\mathsf{Q}$ and the extra $\Pi_1$ axioms of $T$.

### The cut satisfies induction

22. Let $\theta(x, \bar z)$ be $\Delta_0$ and let $\bar b \in I$.
    Assume $I \models \theta(0, \bar b)$ and $I \models \forall x \, (\theta(x, \bar b) \to \theta(Sx, \bar b))$, and suppose $I \models \neg \theta(a, \bar b)$ for some $a \in I$.
23. Let $\psi(x)$ be $x \le a \to \theta(x, \bar b)$, a $\Delta_0$ formula with parameters $a, \bar b$.
    Then $M \models \psi(0)$, by step 12.
24. Let $x \in M$ with $M \models \psi(x)$, and suppose $Sx \le a$.
    Then $x < Sx \le a$, so $x \in I$ by step 8, and $M \models \theta(x, \bar b)$ because $\psi(x)$ holds.
25. By step 12, $I \models \theta(x, \bar b)$, so the assumption of step 22 gives $I \models \theta(Sx, \bar b)$, and step 12 gives $M \models \theta(Sx, \bar b)$.
    If instead $Sx \not\le a$, then $\psi(Sx)$ holds because its premise is false.
26. So $M \models \forall x \, (\psi(x) \to \psi(Sx))$.
    Since $M \models \mathsf{I}\Delta_0$, we get $M \models \psi(a)$, and so $M \models \theta(a, \bar b)$.
27. By step 12, $I \models \theta(a, \bar b)$, which contradicts step 22, so $I \models \forall x \, \theta(x, \bar b)$.
28. By steps 21 to 27, $I \models T$.

### The contradiction

29. We have $T \vdash \forall \bar x \, \exists y \, \varphi(\bar x, y)$ and $I \models T$, with $\bar a \in I$ by step 9.
    So there is $b \in I$ with $I \models \varphi(\bar a, b)$.
30. By step 12, $M \models \varphi(\bar a, b)$, and by step 7, $b < t(\bar a)$ for some term $t$.
31. So $M \models \exists y < t(\bar c) \, \varphi(\bar c, y)$, which contradicts the sentence for $t$ in $\Gamma$, since $M \models \Gamma$.

So the assumption is false, and there is a term $t(\bar x)$ with $T \vdash \forall \bar x \, \exists y < t(\bar x) \, \varphi(\bar x, y)$.
This proves [[Parikh's theorem|YPQPC1WJMV]].

## Idea

Suppose that no term bounds the witness.
Compactness then gives a model $M$ and parameters $\bar a$ with no witness below any term in $\bar a$, so the parameters behave like huge, [[nonstandard|1QWN5CV4CG]] numbers.
Now throw away everything in $M$ above all the terms in $\bar a$.
What is left is a cut $I$, closed under the operations, and bounded formulas cannot tell $I$ from $M$, because their quantifiers never look above the cut.
So $I$ is again a model of $T$, it has a witness, and that witness lies below a term, which contradicts the choice of $M$.

## Variants

The proof-theoretic proof writes $T$ in a sequent calculus with an induction rule for $\Delta_0$ formulas.
Free-cut elimination, a form of the [[cut-elimination theorem|AYRZ98Y0NW]], gives a proof in which every formula is bounded, and an induction on that proof gives the bound term.
The same argument works for $S^i_2$ and $T^i_2$, and it is the route that leads on to Buss's witnessing theorem.

For a theory with universal axioms and an open formula $\varphi$, [[Herbrand's theorem|VZ21F10WRS]] gives a shorter route.
It yields terms $t_1, \dots, t_k$ with $T \vdash \varphi(\bar x, t_1) \lor \dots \lor \varphi(\bar x, t_k)$, and then $S(t_1 + \dots + t_k)$ is a bound.
