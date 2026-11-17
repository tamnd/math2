---
tag: TT8MXRTVBM
kind: definition
name: Robinson arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: grad
defines: 3K1AKGXF8A
uses: [329ZG1Z0G5, 92SWXST1ZM, WDVVEYD6AT, 0QFT7Z76N5, GCK0NN60E4, QSCE4HJEZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
---

## Definition

Let $L_A$ be the [[language of arithmetic|329ZG1Z0G5]], with the constant symbol $0$, the unary function symbol $S$, the binary function symbols $+$ and $\cdot$, and the binary relation symbol $<$.
*Robinson arithmetic* $\mathsf{Q}$ is the first-order [[theory|92SWXST1ZM]] in $L_A$ whose axioms are the universal closures of these eight formulas:

1. $\mathsf{Q}1$: $S x \ne 0$;
2. $\mathsf{Q}2$: $S x = S y \to x = y$;
3. $\mathsf{Q}3$: $x \ne 0 \to \exists y\, (x = S y)$;
4. $\mathsf{Q}4$: $x + 0 = x$;
5. $\mathsf{Q}5$: $x + S y = S(x + y)$;
6. $\mathsf{Q}6$: $x \cdot 0 = 0$;
7. $\mathsf{Q}7$: $x \cdot S y = (x \cdot y) + x$;
8. $\mathsf{Q}8$: $x < y \leftrightarrow \exists v\, (v + S x = y)$.

## Notation

The theorems of $\mathsf{Q}$ are written $\mathsf{Q} \vdash \varphi$.
A theory $T$ in $L_A$ extends $\mathsf{Q}$ when $T \vdash \varphi$ for every axiom $\varphi$ of $\mathsf{Q}$.

## Remarks

Axioms $\mathsf{Q}1$ to $\mathsf{Q}7$ are Robinson's original axioms, in the language $\set{0, S, +, \cdot}$.
Axiom $\mathsf{Q}8$ defines $<$ from $+$, so adding it is an [[extension by definitions|GCK0NN60E4]].
Such an extension is [[conservative|QSCE4HJEZ7]], so the eight axioms prove the same sentences without $<$ as the seven original axioms.
$\mathsf{Q}$ is the first-order version of the [[Peano axioms|0QFT7Z76N5]] without induction, with $\mathsf{Q}3$ added.
Peano arithmetic proves $\mathsf{Q}3$ by induction, but $\mathsf{Q}$ needs it as an axiom.
The [[standard model|WXHVSE066S]] satisfies all eight axioms, while [[the integers|QXFENZWRWM]] violate $\mathsf{Q}1$.
The [[concept page|3K1AKGXF8A]] describes what $\mathsf{Q}$ proves and what it does not prove.

## Explanations

### L1 human

The definition gives eight rules.
Rules 1 to 3 say: zero is not a "next" number, different numbers have different "next" numbers, and every number except zero is a "next" number.
Rules 4 and 5 tell how to add, by counting up one step at a time.
Rules 6 and 7 tell how to multiply, by repeated addition.
Rule 8 says that $x$ is less than $y$ when $y$ is $x + 1$ plus something.

### L2 human

We show that $\mathsf{Q} \vdash 0 < S 0$, the statement $0 < \overline{1}$.

1. By $\mathsf{Q}8$, it suffices to find $v$ with $v + S 0 = S 0$.
2. Take $v = 0$. By $\mathsf{Q}5$, $0 + S 0 = S(0 + 0)$.
3. By $\mathsf{Q}4$, $0 + 0 = 0$, so $S(0 + 0) = S 0$.
4. So $0 + S 0 = S 0$, and $\exists v\, (v + S 0 = S 0)$ follows by existential introduction.

The typical use of the definition is to check that a given structure is a model of $\mathsf{Q}$, axiom by axiom.
A trap is $\mathsf{Q}8$ in the other order: with $S x + v = y$ in place of $v + S x = y$, the defined relation can differ in non-standard models.
