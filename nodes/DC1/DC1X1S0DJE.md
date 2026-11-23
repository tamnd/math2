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

Take the sentence $A = \forall x\, \neg (S x = 0)$, which says that $0$ is not a successor.
Its [[negative translation|QEZR7PZ2DD]] is
$$A^N = \forall x\, (\neg \neg (S x = 0) \to \bot).$$
In HA the formula $\neg \neg (S x = 0)$ is equivalent to $S x = 0$, because an equation between numbers is decidable.
So $A^N$ is equivalent to $\forall x\, (S x = 0 \to \bot)$, which is $A$ itself, and the translation changes nothing up to provable equivalence.

The same holds for a whole class of formulas.
Let PA and HA be [[Peano arithmetic|0QFT7Z76N5]] and [[Heyting arithmetic|RXHJPVMPJH]] in the same language, with atomic formulas $s = t$ and $\bot$.
Call a formula *negative* if it has no $\vee$ and no $\exists$.
We show that if $A$ is negative and $\mathsf{PA} \vdash A$, then $\mathsf{HA} \vdash A$.
So PA is conservative over HA for negative formulas, a [[conservation theorem|TNZ995J8AP]].

First we prove that $\mathsf{HA} \vdash A^N \leftrightarrow A$ for every negative formula $A$, by induction on $A$.

1. HA proves $s = t \vee \neg s = t$ for all terms $s$ and $t$, by induction on the variables.
2. For an atom $s = t$ we have $(s = t)^N = \neg \neg s = t$.
   The direction $s = t \to \neg \neg s = t$ holds in intuitionistic logic.
3. For the other direction, assume $\neg \neg s = t$.
   By step 1, either $s = t$, or $\neg s = t$, and the second case contradicts the assumption.
   So $s = t$.
4. For the atom $\bot$ we have $\bot^N = \bot$.
5. The translation commutes with $\wedge$, $\to$ and $\forall$, so the induction hypothesis for the parts gives the equivalence for $A \wedge B$, $A \to B$ and $\forall x\, A$.
6. These are all the cases, since $A$ has no $\vee$ and no $\exists$, and $\neg B$ is $B \to \bot$.

Now assume $\mathsf{PA} \vdash A$ with $A$ negative.
The [[Gödel-Gentzen translation theorem|WC4TDGEWZR]] gives $\mathsf{HA} \vdash A^N$, and the equivalence above gives $\mathsf{HA} \vdash A$.

## Remarks

With function symbols for all primitive recursive functions, every $\Pi^0_1$ sentence $\forall x\, \varphi(x)$ with $\varphi$ quantifier-free is negative.
So PA and HA prove the same $\Pi^0_1$ sentences, for example the same consistency statements.
The class of negative formulas is closed under $\neg$, so PA and HA also refute the same negative formulas.

The result fails as soon as $\vee$ appears.
With Kleene's predicate $T$, the sentence $\forall x\, (\exists y\, T(x, x, y) \vee \neg \exists y\, T(x, x, y))$ is a theorem of PA that HA does not prove.
For $\Pi^0_2$ sentences, which contain $\exists$, the negative translation alone does not suffice, and the [[A-translation|PY679V9MVR]] is needed.

## Explanations

### L1 human

Statements built only from equations, "and", "if-then" and "for all" carry no hidden claim that something exists.
For them, classical and intuitionistic arithmetic agree.
The reason is that double negations can be removed from equations between numbers, since each such equation can be checked by calculation.
For example, "every number $x$ satisfies $x + 0 = x$" is a theorem of both theories.

### L2 human

We run the argument on $A = \forall x\, \forall y\, (x + y = y + x)$, the commutativity of addition.
PA proves $A$, so HA proves $A^N = \forall x\, \forall y\, \neg \neg (x + y = y + x)$.
Step 3 removes the double negation, because HA proves $x + y = y + x \vee \neg (x + y = y + x)$.
So HA proves $A$, and we never had to find an intuitionistic proof of commutativity by hand.

The typical use is to transfer $\Pi^0_1$ theorems, such as consistency statements, from classical to intuitionistic arithmetic.
Watch out: the lemma fails for formulas with $\exists$, because $(\exists x\, B)^N = \neg \forall x\, \neg B^N$ is not equivalent to $\exists x\, B$ in HA.
