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

Fix $c, d, i \in \N$, and put $m = 1 + (i + 1) d$ and $r = \beta(c, d, i)$, so that $m \ge 1$.
Steps 2 and 4 of [[the proof of Σ1-completeness|Y8X8D9YJF8]] are cited as N2 (closed terms equal their numerals in $\mathsf{Q}$) and N4 ($\mathsf{Q} \vdash \forall x\,(x < \overline{k} \leftrightarrow \bigvee_{j < k} x = \overline{j})$).

1. Part 1, shape. Every quantifier of $B$ is the bounded quantifier $\exists q \le c$, and $q$ does not occur in the bound $c$. So $B$ is $\Delta_0$ by the [[definition|Y0JTZXBRT5]].
2. Part 1, from left to right. If $\mathfrak{N} \models B(c, d, i, v)$ with witness $q$, then $c = q m + v$ and $0 \le v < m$. By the uniqueness of division with remainder, $v = r$.
3. Part 1, from right to left. Division with remainder gives $c = q m + r$ with $r < m$. Since $m \ge 1$, $q \le q m \le c$. So $q$ is a witness for $B(c, d, i, r)$.
4. Part 2, one direction. By step 3, $B(\overline{c}, \overline{d}, \overline{i}, \overline{r})$ is a true $\Delta_0$ sentence. By Part 1 of [[Σ1-completeness|69234Z1V00]], $\mathsf{Q}$ proves it. So $\mathsf{Q} \vdash \forall v\,(v = \overline{r} \to B(\overline{c}, \overline{d}, \overline{i}, v))$.
5. Part 2, other direction. Reason in $\mathsf{Q}$, and assume $B(\overline{c}, \overline{d}, \overline{i}, v)$. Take a witness $q$; the second conjunct of the matrix gives $v < 1 + (\overline{i} + 1) \cdot \overline{d}$. The bound is a closed term with value $m$, so by N2 it equals $\overline{m}$, and $v < \overline{m}$.
6. By N4, $v = \overline{j}$ for some $j < m$. Consider each such $j$.
7. If $j = r$, then $v = \overline{r}$.
8. If $j \ne r$, then $B(c, d, i, j)$ is false in $\mathfrak{N}$ by step 2. It is a $\Delta_0$ sentence, so $\mathsf{Q} \vdash \neg B(\overline{c}, \overline{d}, \overline{i}, \overline{j})$ by Part 1 of Σ1-completeness. This contradicts the assumption with $v = \overline{j}$, so $v = \overline{r}$ holds in this case as well.
9. Hence $\mathsf{Q} \vdash \forall v\,(B(\overline{c}, \overline{d}, \overline{i}, v) \to v = \overline{r})$. With step 4 this proves Part 2.

## Idea

The formula $B$ bounds its output $v$ by the modulus, so $\mathsf{Q}$ can list all candidate outputs below a numeral.
Each wrong candidate gives a false $\Delta_0$ sentence, which $\mathsf{Q}$ refutes, and only the true remainder is left.

## Variants

For a general $\Sigma_1$ graph the output is not bounded inside the formula, and the [[proof of the representability theorem|4T3MSP1SPK]] needs trichotomy for numerals to compare an unknown output with a numeral.
