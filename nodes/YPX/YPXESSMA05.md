---
tag: YPXESSMA05
kind: proof
name: Proof that the β function is represented in Robinson arithmetic by a Δ0 formula
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
proves: 2X3BHXYR6D
uses: [Y0JTZXBRT5, 69234Z1V00, Y8X8D9YJF8, TT8MXRTVBM]
methods: [0NTF6DMVAP, 0WCP0PVET6]
sources:
  - book: isbn:9780521857840
  - url: https://builds.openlogicproject.org/
    locator: Representability in Q
---

## Proof

We prove Part 1 by division with remainder, and Part 2 by letting $\mathsf{Q}$ list all candidate outputs below the modulus and refute the wrong ones.
Fix $c, d, i \in \mathbb{N}$, and put $m = 1 + (i + 1) d$ and $r = \beta(c, d, i)$, so that $m \ge 1$.
From [[the proof of Σ1-completeness|Y8X8D9YJF8]] we use two facts.
The first, fact N2, says that $\mathsf{Q}$ proves each closed term equal to its numeral.
The second, fact N4, says that $\mathsf{Q} \vdash \forall x\,(x < \overline{k} \leftrightarrow \bigvee_{j < k} x = \overline{j})$ for each $k$.

### Part 1: the formula defines the remainder

1. The only quantifier of $B$ is the bounded quantifier $\exists q \le c$, and $q$ does not occur in the bound $c$.
   So $B$ is $\Delta_0$ by the [[definition of the classes|Y0JTZXBRT5]].
2. Suppose that $\mathfrak{N} \models B(c, d, i, v)$ with the witness $q$.
   Then $c = q m + v$ and $0 \le v < m$, so $v = r$ by the uniqueness of division with remainder.
3. Conversely, division with remainder gives $c = q m + r$ with $r < m$.
   Since $m \ge 1$, $q \le q m \le c$, so $q$ is a witness for $B(c, d, i, r)$.
   With step 2, this proves Part 1.

### Part 2: Q picks out the remainder

4. By step 3, $B(\overline{c}, \overline{d}, \overline{i}, \overline{r})$ is a true $\Delta_0$ sentence, so $\mathsf{Q}$ proves it by Part 1 of [[Σ1-completeness|69234Z1V00]].
   Hence $\mathsf{Q} \vdash \forall v\,(v = \overline{r} \to B(\overline{c}, \overline{d}, \overline{i}, v))$.
5. For the other direction we reason in $\mathsf{Q}$ and assume $B(\overline{c}, \overline{d}, \overline{i}, v)$.
   Take a witness $q$; the second conjunct gives $v < 1 + (\overline{i} + 1) \cdot \overline{d}$.
   The bound is a closed term with the value $m$, so by fact N2 it equals $\overline{m}$, and $v < \overline{m}$.
6. By fact N4, $v = \overline{j}$ for some $j < m$, and we consider each such $j$ in turn.
7. If $j = r$, then $v = \overline{r}$.
8. If $j \ne r$, then $B(c, d, i, j)$ is false in $\mathfrak{N}$ by step 2.
   It is a $\Delta_0$ sentence, so $\mathsf{Q} \vdash \neg B(\overline{c}, \overline{d}, \overline{i}, \overline{j})$ by Part 1 of Σ1-completeness.
   This contradicts the assumption with $v = \overline{j}$, so $v = \overline{r}$ holds in this case as well.
9. Hence $\mathsf{Q} \vdash \forall v\,(B(\overline{c}, \overline{d}, \overline{i}, v) \to v = \overline{r})$.
   With step 4, this proves Part 2.

## Idea

The formula $B$ bounds its output $v$ by the modulus, so $\mathsf{Q}$ can list all candidate outputs below a numeral.
For $c = 27001$, $d = 6$ and $i = 0$, the modulus is $7$ and the candidates are $0, 1, \ldots, 6$.
Each wrong candidate gives a false $\Delta_0$ sentence, which $\mathsf{Q}$ refutes, and only the true remainder $2$ is left.

## Variants

For a general $\Sigma_1$ graph the output is not bounded inside the formula.
Then the [[proof of representability|4T3MSP1SPK]] needs trichotomy for numerals, so that $\mathsf{Q}$ can compare an unknown output with a numeral.
