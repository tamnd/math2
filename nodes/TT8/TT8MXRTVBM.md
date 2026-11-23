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

Robinson arithmetic is the theory with the successor axioms and the recursion equations for $+$ and $\cdot$, and nothing else.
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

The axioms fall into three groups, and each group has a job.
Axioms $\mathsf{Q}1$ to $\mathsf{Q}3$ describe the successor: it never gives $0$, it never sends two numbers to one, and every nonzero number comes from it.
Axioms $\mathsf{Q}4$ to $\mathsf{Q}7$ are the recursion equations, so they compute $x + y$ and $x \cdot y$ by recursion on the right argument.
Axiom $\mathsf{Q}8$ only defines $<$.

Axioms $\mathsf{Q}1$ to $\mathsf{Q}7$ are Robinson's original axioms, in the language $\{0, S, +, \cdot\}$.
Adding $\mathsf{Q}8$ is an [[extension by definitions|GCK0NN60E4]], and such an extension is [[conservative|QSCE4HJEZ7]].
So the eight axioms prove the same sentences without $<$ as the seven original axioms.

$\mathsf{Q}$ is the first-order version of the [[Peano axioms|0QFT7Z76N5]] without induction, with $\mathsf{Q}3$ added.
Peano arithmetic proves $\mathsf{Q}3$ by induction, but without induction it must be an axiom.
The [[standard model|WXHVSE066S]] satisfies all eight axioms, while [[the integers|QXFENZWRWM]] break $\mathsf{Q}1$, since $S(-1) = 0$.
The [[concept of Robinson arithmetic|3K1AKGXF8A]] describes what $\mathsf{Q}$ proves and what it does not prove.

## Explanations

### L1 human

The definition gives eight rules.
Rules 1 to 3 say that zero is not a "next" number, that different numbers have different "next" numbers, and that every number except zero is a "next" number.
Rules 4 and 5 say how to add, by counting up one step at a time.
Rules 6 and 7 say how to multiply, by repeated addition.
Rule 8 says that $x$ is less than $y$ when $y$ is $x + 1$ plus something.

### L2 human

We prove $0 < \overline{1}$ in $\mathsf{Q}$, that is, $0 < S0$.
By $\mathsf{Q}8$, it suffices to find a $v$ with $v + S0 = S0$, and we try $v = 0$.
Axioms $\mathsf{Q}5$ and $\mathsf{Q}4$ give
$$0 + S0 = S(0 + 0) = S0.$$
So $\exists v\, (v + S0 = S0)$ follows by existential introduction, and $\mathsf{Q}8$ gives $0 < S0$.

The typical use of the definition is to check that a given structure is a model of $\mathsf{Q}$, one axiom at a time.
Watch out for the order of the summands in $\mathsf{Q}8$.
The form $v + S x = y$ lets $\mathsf{Q}5$ peel successors off $S x$, which is what the proofs about $<$ need.
The form $S x + v = y$ defines the same relation in $\mathbb{N}$, but it can define a different relation in non-standard models.
