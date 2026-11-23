---
tag: 4T3MSP1SPK
kind: proof
name: Proof of the representability of recursive functions in Robinson arithmetic
msc: ["03F30", "03D20"]
topics: [QHCRN4JVG0]
audience: grad
proves: BJF29XET83
uses: [TT8MXRTVBM, 69234Z1V00, Y8X8D9YJF8, Y0JTZXBRT5, 4WCR2JXT4S, HJEZHW1YQ2, BM6P0C2AC2, 2X3BHXYR6D, HBK5QHC1GC]
methods: [0ASJVEFA9J, 0WCP0PVET6, 0NTF6DMVAP]
sources:
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - url: https://builds.openlogicproject.org/
    locator: Representability in Q
---

## Proof

We first write the graph of each recursive function as a $\Sigma_1$ formula, and then we change that formula so that $\mathsf{Q}$ can prove the output is unique.
Part A shows that the graph of every total recursive function is defined in $\mathfrak{N}$ by a $\Sigma_1$ formula.
It is an outline, and its main lemma, the [[β-function lemma|BM6P0C2AC2]], is proved separately.
Part B, given in full, turns any $\Sigma_1$ definition of the graph of a function into a $\Sigma_1$ formula that represents the function in $\mathsf{Q}$.
Parts 2 and 3 of the theorem follow at the end.
We write functions of one argument, and the case of $k$ arguments is the same with $\vec{x}$ in place of $x$.

We cite steps 1 to 4 of [[the proof of Σ1-completeness|Y8X8D9YJF8]] as N1 to N4.
N1 computes sums and products of numerals, N2 evaluates closed terms, and N3 proves $\overline{m} \ne \overline{n}$ for $m \ne n$.
N4 is $\mathsf{Q} \vdash \forall x\,(x < \overline{n} \leftrightarrow \bigvee_{i < n} x = \overline{i})$.

### Part A: basic functions and composition

1. Let $\beta(c, d, i)$ be the remainder of $c$ on division by $1 + (i + 1) d$.
   By [[this lemma|2X3BHXYR6D]], its graph is defined by the $\Delta_0$ formula below.
   By the β-function lemma, every finite sequence $a_0, \ldots, a_n$ equals $\beta(c, d, 0), \ldots, \beta(c, d, n)$ for some $c$ and $d$, and $\beta(c, d, i) \le c$.

$$B(c, d, i, v) := \exists q \le c\,\bigl(c = q \cdot (1 + (i + 1) \cdot d) + v \land v < 1 + (i + 1) \cdot d\bigr).$$

2. The zero, successor and projection functions have the $\Delta_0$ graphs $y = 0$, $y = S x$ and $y = x_j$.
3. For composition, let $h(x) = f(g(x))$, where $\Sigma_1$ formulas $F$ and $G$ define the graphs of $f$ and $g$.
   Then $\exists z\,(G(x, z) \land F(z, y))$ defines $y = h(x)$.
   We move the existential quantifiers of $G$ and $F$ to the front and [[merge them|4WCR2JXT4S]] into one, which gives a $\Sigma_1$ formula.
   Several inner functions are handled in the same way.

### Part A: primitive recursion and minimization

4. For primitive recursion, let $h(x, 0) = f(x)$ and $h(x, z + 1) = g(x, z, h(x, z))$, with $\Sigma_1$ graphs $F$ and $G$.
   Then $y = h(x, z)$ holds exactly when some $c, d$ satisfy $\beta(c, d, 0) = f(x)$, $\beta(c, d, i + 1) = g(x, i, \beta(c, d, i))$ for all $i < z$, and $\beta(c, d, z) = y$.
   From left to right, step 1 codes the sequence $h(x, 0), \ldots, h(x, z)$, and from right to left, induction on $i \le z$ gives $\beta(c, d, i) = h(x, i)$.
5. Written with $B$ and $G$, the middle clause is $\forall i < z\, \exists u \le c\, \exists u' \le c\,\bigl(B(c, d, i, u) \land B(c, d, i + 1, u') \land G(x, i, u, u')\bigr)$.
   The existential quantifier of $G$ moves in front of $\exists u \le c\, \exists u' \le c$ by logic.
   The result is $\forall i < z$ in front of a $\Sigma_1$ formula, which is $\Sigma_1$ in $\mathfrak{N}$ by [[collection of witnesses|HJEZHW1YQ2]].
   With the outer $\exists c\, \exists d$ and step 3, the graph of $h$ is $\Sigma_1$.
6. For minimization, let $h(x)$ be the least $z$ with $g(x, z) = 0$, where such a $z$ exists for every $x$, and let $G$ define the graph of $g$.
   Then $G(x, y, 0) \land \forall z < y\, \exists u\,(G(x, z, u) \land u \ne 0)$ defines $y = h(x)$, since $g$ is total.
   By collection again, this formula is $\Sigma_1$ in $\mathfrak{N}$.
7. A total [[recursive function|HBK5QHC1GC]] is built from the basic functions by composition, primitive recursion and minimization.
   By induction on this construction, steps 2 to 6 show that its graph is defined in $\mathfrak{N}$ by a $\Sigma_1$ formula.
   Merging the existential quantifiers, we write this formula as $\exists w\, \delta(x, y, w)$ with $\delta$ in $\Delta_0$.

### Part B: trichotomy

Let $f : \mathbb{N} \to \mathbb{N}$, and let $\exists w\, \delta(x, y, w)$ with $\delta$ in $\Delta_0$ define the graph of $f$ in $\mathfrak{N}$.

8. We first show $\mathsf{Q} \vdash \forall u\,(S u + \overline{m} = S(u + \overline{m}))$ for each $m$, by induction on $m$ outside the theory.
   For $m = 0$ both sides equal $S u$ by $\mathsf{Q}4$.
   For the step, $\mathsf{Q}5$, the hypothesis and $\mathsf{Q}5$ give $S u + S\overline{m} = S(S u + \overline{m}) = S S(u + \overline{m}) = S(u + S\overline{m})$.
9. Next we show trichotomy, $\mathsf{Q} \vdash \forall x\,(x < \overline{n} \lor x = \overline{n} \lor \overline{n} < x)$, by induction on $n$ outside the theory.
   For $n = 0$, $\mathsf{Q}3$ gives $x = 0$ or $x = S y$.
   In the second case $y + S 0 = S(y + 0) = S y = x$ by $\mathsf{Q}5$ and $\mathsf{Q}4$, so $0 < x$ by $\mathsf{Q}8$.
10. For $n + 1$, we use the three cases for $\overline{n}$.
    If $x < \overline{n}$ or $x = \overline{n}$, then $x = \overline{i}$ for some $i \le n$, and $\overline{i} < \overline{n + 1}$, both by N4.
    If $\overline{n} < x$, then $v + S\overline{n} = x$ for some $v$, and $\mathsf{Q}3$ gives $v = 0$ or $v = S u$.
    If $v = 0$, then $x = 0 + \overline{n + 1} = \overline{n + 1}$ by N1.
    If $v = S u$, then step 8 and $\mathsf{Q}5$ give $x = S u + S\overline{n} = S(u + S\overline{n}) = u + S S\overline{n}$, so $\overline{n + 1} < x$ by $\mathsf{Q}8$.

### Part B: the representing formula

11. We define the $\Delta_0$ formula $\delta^*(x, y, w) := y \le w \land \exists w'' \le w\; \delta(x, y, w'')$.
    We also define the $\Delta_0$ formula $\theta(x, y, w) := \delta^*(x, y, w) \land \forall y' \le w\; \forall w' \le w\,\bigl(\delta^*(x, y', w') \to y' = y\bigr)$.
    Our candidate is the $\Sigma_1$ formula $\varphi(x, y) := \exists w\; \theta(x, y, w)$.
12. Fix $n$ and put $m = f(n)$.
    In $\mathbb{N}$, $\delta^*(n, y', w')$ implies $\delta(n, y', w'')$ for some $w''$, so $y' = m$.
    Choose $w_0$ with $\delta(n, m, w_0)$ true, and put $c = \max(m, w_0)$.
    Then $\delta^*(n, m, c)$ is true, and so is $\theta(n, m, c)$.
13. By Part 1 of [[Σ1-completeness|69234Z1V00]], $\mathsf{Q} \vdash \theta(\overline{n}, \overline{m}, \overline{c})$ and $\mathsf{Q} \vdash \delta^*(\overline{n}, \overline{m}, \overline{c})$.
    Hence $\mathsf{Q} \vdash \varphi(\overline{n}, \overline{m})$, which gives $\mathsf{Q} \vdash \forall y\,(y = \overline{m} \to \varphi(\overline{n}, y))$.

### Part B: uniqueness

14. For the other direction we reason in $\mathsf{Q}$.
    We assume $\theta(\overline{n}, y, w)$ and show $y = \overline{m}$, in the cases $w \le \overline{c}$ and $\neg(w \le \overline{c})$.
15. In the case $w \le \overline{c}$, N4 gives $w = \overline{j}$ for some $j \le c$.
    The first conjunct of $\theta$ gives $y \le \overline{j}$, so $y = \overline{i}$ for some $i \le j$, by N4.
    If $\theta(n, i, j)$ is true in $\mathbb{N}$, then $\delta^*(n, i, j)$ is true, so $i = m$ by step 12.
    If it is false, then $\mathsf{Q} \vdash \neg \theta(\overline{n}, \overline{i}, \overline{j})$ by Σ1-completeness, against the assumption.
    So $y = \overline{m}$ in every subcase.
16. In the case $\neg(w \le \overline{c})$, trichotomy for $\overline{c}$ gives $\overline{c} < w$.
    Trichotomy for $\overline{m}$ gives $w < \overline{m}$, $w = \overline{m}$ or $\overline{m} < w$.
    In the first two cases N4 gives $w = \overline{j}$ with $j \le m \le c$, so $w \le \overline{c}$, against the case.
    So $\overline{m} < w$.
17. We apply the second conjunct of $\theta(\overline{n}, y, w)$ with $y' = \overline{m}$ and $w' = \overline{c}$.
    Its hypotheses $\overline{m} \le w$, $\overline{c} \le w$ and $\delta^*(\overline{n}, \overline{m}, \overline{c})$ hold by steps 16 and 13, so $\overline{m} = y$.
18. Steps 14 to 17 give $\mathsf{Q} \vdash \forall y\,(\varphi(\overline{n}, y) \to y = \overline{m})$.
    With step 13, the $\Sigma_1$ formula $\varphi$ represents $f$ in $\mathsf{Q}$, and every extension of $\mathsf{Q}$ proves the same sentences.
    This proves Part 1.

### Parts 2 and 3

19. For Part 2, let $R$ be recursive, and let $\varphi$ represent its recursive characteristic function $\chi_R$.
    Put $\psi(x) := \varphi(x, \overline{1})$.
    If $n \in R$, then $\mathsf{Q} \vdash \varphi(\overline{n}, \overline{1})$.
    If $n \notin R$, then $\mathsf{Q} \vdash \forall y\,(\varphi(\overline{n}, y) \leftrightarrow y = 0)$ and $\mathsf{Q} \vdash \overline{1} \ne 0$ by $\mathsf{Q}1$, so $\mathsf{Q} \vdash \neg \psi(\overline{n})$.
20. For Part 3, let $T$ be consistent with a recursive set of axioms, so that a computable procedure lists its theorems.
    If $\psi$ represents $R$ in $T$, then on input $n$ we list the theorems of $T$ until $\psi(\overline{n})$ or $\neg \psi(\overline{n})$ appears.
    One of them appears by representability, and not both by consistency, so the answer is correct and $R$ is recursive.
21. If $\varphi$ represents $f$ in $T$, then on input $n$ we list the theorems of $T$ until $\varphi(\overline{n}, \overline{m})$ appears for some $m$.
    It appears for $m = f(n)$.
    For $m \ne f(n)$ the theory proves $\neg \varphi(\overline{n}, \overline{m})$ by N3, so by consistency it does not prove $\varphi(\overline{n}, \overline{m})$.
    Hence $f$ is recursive.

## Idea

The graph of a computable function says "there is a computation with this output", which is a $\Sigma_1$ statement, and the β function lets one number code the whole computation.
A $\Sigma_1$ definition of the graph is not yet a representation, since $\mathsf{Q}$ may not prove that the output is unique.
Part B builds uniqueness into the formula: $\theta$ says that $y$ is the only output with a witness below $w$.
Then $\mathsf{Q}$ checks all small candidates by Σ1-completeness, and it compares large ones with numerals by trichotomy.

## Variants

If the language has a symbol for every primitive recursive function, as in primitive recursive arithmetic, Part A needs no β function.
Gödel's paper of 1931 represented the primitive recursive relations in his system, which is enough for the incompleteness theorems, and the step to all recursive functions adds minimization.
Part B uses only N1 to N4 and trichotomy, so the same argument works in every theory that proves these facts, for example the theory $\mathsf{R}$.
