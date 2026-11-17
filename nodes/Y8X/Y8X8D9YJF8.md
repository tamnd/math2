---
tag: Y8X8D9YJF8
kind: proof
name: Proof of the Σ1-completeness of Robinson arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
proves: 69234Z1V00
uses: [TT8MXRTVBM, Y0JTZXBRT5, 329ZG1Z0G5, WP27CABPA4]
methods: [0ASJVEFA9J, 12MQ2NJ29A, 0WCP0PVET6]
sources:
  - book: isbn:9780521857840
  - book: isbn:9780521701464
  - url: https://builds.openlogicproject.org/
    locator: Representability in Q
---

## Proof

We use the axioms $\mathsf{Q}1$ to $\mathsf{Q}8$ of [[Robinson arithmetic|TT8MXRTVBM]], with $\overline{n}$ for the numeral $S \cdots S 0$ with $n$ symbols $S$.
For a closed term $t$, $t^{\mathfrak{N}}$ is its value in $\N$.
Steps 1 to 4 are lemmas about numerals, steps 5 to 9 prove Part 1, and step 10 proves Part 2.

1. For all $k, m \in \N$, $\mathsf{Q} \vdash \overline{k} + \overline{m} = \overline{k + m}$ and $\mathsf{Q} \vdash \overline{k} \cdot \overline{m} = \overline{k m}$. For $+$ we use induction on $m$: $\overline{k} + 0 = \overline{k}$ is $\mathsf{Q}4$, and $\overline{k} + S\overline{m} = S(\overline{k} + \overline{m}) = S\overline{k + m}$ by $\mathsf{Q}5$ and the induction hypothesis. For $\cdot$ we use induction on $m$: $\overline{k} \cdot 0 = 0$ is $\mathsf{Q}6$, and $\overline{k} \cdot S\overline{m} = \overline{k} \cdot \overline{m} + \overline{k} = \overline{k m} + \overline{k} = \overline{k m + k}$ by $\mathsf{Q}7$, the induction hypothesis and the case of $+$.
2. For every closed term $t$, $\mathsf{Q} \vdash t = \overline{t^{\mathfrak{N}}}$. This follows by induction on $t$: the case $0$ is immediate, the case $S u$ follows from the hypothesis for $u$ by the equality axioms, and the cases $u + v$ and $u \cdot v$ follow from the hypotheses for $u$ and $v$ and step 1.
3. If $n \ne m$ then $\mathsf{Q} \vdash \overline{n} \ne \overline{m}$. We use induction on $\min(n, m)$. If $n = 0$ and $m = j + 1$, then $\overline{m} = S\overline{j} \ne 0$ by $\mathsf{Q}1$, and the case $m = 0$ is symmetric. If $n = n' + 1$ and $m = m' + 1$, then $\mathsf{Q} \vdash \overline{n'} \ne \overline{m'}$ by the induction hypothesis, and $\mathsf{Q}2$ gives $S\overline{n'} \ne S\overline{m'}$.
4. For every $n$, $\mathsf{Q} \vdash \forall x\,(x < \overline{n} \leftrightarrow x = \overline{0} \lor \cdots \lor x = \overline{n - 1})$, where the empty disjunction for $n = 0$ is a false sentence such as $0 \ne 0$. For the direction from right to left, let $i < n$. Then $\overline{n - 1 - i} + S\overline{i} = \overline{n}$ by step 1, so $\overline{i} < \overline{n}$ by $\mathsf{Q}8$. For the direction from left to right we use induction on $n$, reasoning in $\mathsf{Q}$ with $x$ arbitrary:
   - Case $n = 0$: if $x < 0$, then $v + S x = 0$ for some $v$ by $\mathsf{Q}8$. But $v + S x = S(v + x)$ by $\mathsf{Q}5$, and $S(v + x) \ne 0$ by $\mathsf{Q}1$. So $\neg(x < 0)$.
   - Case $n + 1$: suppose $v + S x = S\overline{n}$. By $\mathsf{Q}3$, $x = 0$ or $x = S y$ for some $y$. If $x = 0$, then $x = \overline{0}$ is a disjunct. If $x = S y$, then $S(v + S y) = v + S S y = S\overline{n}$ by $\mathsf{Q}5$, so $v + S y = \overline{n}$ by $\mathsf{Q}2$, and $y < \overline{n}$ by $\mathsf{Q}8$. By the induction hypothesis $y = \overline{i}$ for some $i < n$, so $x = \overline{i + 1}$ with $i + 1 < n + 1$.
5. We now prove Part 1 by induction on the number of connectives and quantifiers of the $\Delta_0$ sentence $\delta$. Substituting a numeral for a variable does not change this number, so the induction hypothesis applies to every instance of a shorter formula.
6. Atomic sentences. Let $\delta$ be $s = t$ with $s, t$ closed, and put $k = s^{\mathfrak{N}}$ and $m = t^{\mathfrak{N}}$. By step 2, $\mathsf{Q} \vdash s = \overline{k}$ and $\mathsf{Q} \vdash t = \overline{m}$. If $k = m$, then $\mathsf{Q} \vdash s = t$. If $k \ne m$, then step 3 gives $\mathsf{Q} \vdash \neg(s = t)$. Let $\delta$ be $s < t$. By step 2 it suffices to decide $\overline{k} < \overline{m}$. By step 4, $\mathsf{Q} \vdash \overline{k} < \overline{m} \leftrightarrow \bigvee_{i < m} \overline{k} = \overline{i}$. If $k < m$, the disjunct $\overline{k} = \overline{k}$ is provable. If $k \ge m$, every disjunct is refutable by step 3, so $\mathsf{Q} \vdash \neg(\overline{k} < \overline{m})$.
7. Connectives. If $\delta$ is $\neg \alpha$, $\alpha \land \beta$, $\alpha \lor \beta$ or $\alpha \to \beta$, the induction hypothesis gives, for $\alpha$ and $\beta$, a proof of the sentence or of its negation according to its truth value. Propositional logic then gives a proof of $\delta$ or of $\neg \delta$ according to the truth value of $\delta$.
8. Bounded quantifiers with $<$. Let $\delta$ be $\forall x < t\; \alpha(x)$ with $t$ closed, and let $n = t^{\mathfrak{N}}$. By steps 2 and 4, $\mathsf{Q} \vdash \forall x\,(x < t \leftrightarrow \bigvee_{i < n} x = \overline{i})$, so $\mathsf{Q} \vdash \delta \leftrightarrow \bigwedge_{i < n} \alpha(\overline{i})$. Each $\alpha(\overline{i})$ is shorter than $\delta$, so by the induction hypothesis $\mathsf{Q}$ proves the conjunction if every $\alpha(i)$ is true, and refutes one conjunct otherwise. The case $\exists x < t\; \alpha(x)$ is the same with $\bigvee_{i < n} \alpha(\overline{i})$.
9. Bounded quantifiers with $\le$. Since $x \le t$ abbreviates $x < t \lor x = t$, steps 2 and 4 give $\mathsf{Q} \vdash \forall x\,(x \le t \leftrightarrow \bigvee_{i \le n} x = \overline{i})$. The rest is as in step 8, with $i \le n$ in place of $i < n$. This completes the proof of Part 1.
10. Part 2. Let $\varphi = \exists x_1 \cdots \exists x_k\, \delta(x_1, \ldots, x_k)$ with $\delta \in \Delta_0$, and suppose $\mathfrak{N} \models \varphi$. Choose $n_1, \ldots, n_k \in \N$ with $\mathfrak{N} \models \delta(n_1, \ldots, n_k)$. By Part 1, $\mathsf{Q} \vdash \delta(\overline{n_1}, \ldots, \overline{n_k})$, and $k$ applications of existential generalization give $\mathsf{Q} \vdash \varphi$.

## Idea

A true $\Sigma_1$ sentence has a numerical witness, so it reduces to a true $\Delta_0$ sentence.
A $\Delta_0$ sentence is a finite combination of numerical equations and inequalities, and $\mathsf{Q}$ can compute closed terms, separate distinct numerals, and list the numbers below a numeral.
These three facts are steps 2, 3 and 4, and they are all that the induction needs.

## Variants

Step 4 is the only place where $\mathsf{Q}3$ is used.
Without $<$ in the language, as in Robinson's original axioms, $s < t$ is an abbreviation for $\exists v\,(v + S s = t)$, and the proof is the same, with the bounded quantifier $\forall x < t$ read as $\forall x\,(\exists v\,(v + S x = t) \to \ldots)$.
Some textbooks, such as Boolos, Burgess and Jeffrey, prove the result for a larger class of formulas.
That class is closed under $\land$, $\lor$, bounded quantifiers and $\exists$, and the proof adds one case for $\exists$, handled as in step 10.
