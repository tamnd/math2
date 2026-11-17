---
tag: DC1X1S0DJE
kind: example
name: Peano arithmetic is conservative over Heyting arithmetic for negative formulas
msc: ["03F25", "03F30", "03F55"]
topics: [8XY7JYZKFW]
audience: grad
instance_of: [TNZ995J8AP]
uses: [TNZ995J8AP, QEZR7PZ2DD, WC4TDGEWZR, RXHJPVMPJH, 0QFT7Z76N5]
sources:
  - url: https://en.wikipedia.org/wiki/Double-negation_translation
    locator: Arithmetic
  - url: https://en.wikipedia.org/wiki/Heyting_arithmetic
    locator: Conservativity
---

## Example

Let PA and HA be [[Peano arithmetic|0QFT7Z76N5]] and [[Heyting arithmetic|RXHJPVMPJH]] in the same language, with atomic formulas $s = t$ and $\bot$.
Call a formula *negative* if it has no $\vee$ and no $\exists$.
We show: if $A$ is negative and $\mathsf{PA} \vdash A$, then $\mathsf{HA} \vdash A$.
So PA is conservative over HA for negative formulas, a [[conservation theorem|TNZ995J8AP]].

**Lemma.** For every negative formula $A$, $\mathsf{HA} \vdash A^N \leftrightarrow A$, where $A^N$ is the [[negative translation|QEZR7PZ2DD]].

1. HA proves $s = t \vee \neg s = t$ for all terms $s$ and $t$, by induction on the variables.
2. Atom $s = t$: $(s = t)^N = \neg \neg s = t$. The direction $s = t \to \neg \neg s = t$ is intuitionistic logic.
3. For the other direction, assume $\neg \neg s = t$. By step 1, either $s = t$, or $\neg s = t$, which contradicts the assumption. So $s = t$.
4. Atom $\bot$: $\bot^N = \bot$.
5. $A \wedge B$: $(A \wedge B)^N = A^N \wedge B^N$, which is equivalent to $A \wedge B$ by the induction hypothesis for $A$ and $B$.
6. $A \to B$: $(A \to B)^N = A^N \to B^N$, which is equivalent to $A \to B$ by the induction hypothesis.
7. $\forall x\, A$: $(\forall x\, A)^N = \forall x\, A^N$, which is equivalent to $\forall x\, A$ by the induction hypothesis.
8. These are all the cases, since $A$ has no $\vee$ and no $\exists$, and $\neg B$ is $B \to \bot$.

**Conservativity.**

9. Assume $\mathsf{PA} \vdash A$ with $A$ negative.
10. By the [[Gödel-Gentzen translation theorem|WC4TDGEWZR]], $\mathsf{HA} \vdash A^N$.
11. By the lemma, $\mathsf{HA} \vdash A$.

## Remarks

With function symbols for all primitive recursive functions, every $\Pi^0_1$ sentence $\forall x\, \varphi(x)$ with $\varphi$ quantifier-free is negative.
So PA and HA prove the same $\Pi^0_1$ sentences, for example the same consistency statements.
The class of negative formulas is closed under $\neg$, so PA and HA also refute the same negative formulas.
The result fails for $\vee$: $\forall x\, (\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y))$ is a theorem of PA that HA does not prove.
For $\Pi^0_2$ sentences, which contain $\exists$, the [[A-translation|PY679V9MVR]] is needed.

## Explanations

### L1 human

Statements built only from equations, "and", "if-then" and "for all" carry no hidden existence claim.
For them, classical and intuitionistic arithmetic agree.
The reason is that double negations can be removed from equations between numbers, since each such equation is decidable.
For example, "every number $x$ satisfies $x + 0 = x$" has the same proofs in both theories.

### L2 human

We apply the lemma to $A = \forall x\, \neg (S x = 0)$.

1. $A^N = \forall x\, (\neg \neg (S x = 0) \to \bot)$.
2. By step 3 of the lemma, $\neg \neg (S x = 0)$ is equivalent to $S x = 0$ in HA.
3. So $A^N$ is equivalent to $\forall x\, (S x = 0 \to \bot)$, which is $A$.

The typical use is to transfer $\Pi^0_1$ theorems, such as consistency statements, from classical to intuitionistic arithmetic.
A trap is to apply the lemma to formulas with $\exists$: the translation of $\exists$ is not equivalent to $\exists$ in HA.
