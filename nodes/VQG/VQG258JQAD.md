---
tag: VQG258JQAD
kind: definition
name: Kripke-Feferman theory
aliases: [kf-axioms, kripke-feferman-axioms]
msc: ["03F25", "03A05"]
topics: [6Q4JJ2MMV8]
audience: research
defines: 2F15E76R0Z
uses: [HACXBCM7SS, 1QD0KDDGYJ, MFJXPAF0R0, ES71QTSTNV]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 4.4 The Kripke-Feferman theory"
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 2.2 Notational conventions"
  - book: isbn:9780521115810
---

## Definition

Let $\mathcal{L}_0$ be arithmetic with $0$, $S$, $=$, predicates for addition and multiplication, and $\neg$, $\wedge$, $\vee$, $\forall$, $\exists$.
Let $\mathcal{L}_T$ be $\mathcal{L}_0$ with a new unary predicate $T$, and fix a [[Gödel numbering|MFJXPAF0R0]].
In the axioms, $A$ and $B$ range over codes of sentences of $\mathcal{L}_T$.
$A(v)$ ranges over codes of formulas with at most the variable $v$ free.
$A(\dot x)$ is the result of putting the numeral of $x$ for $v$.
$\mathrm{AtSent}(A)$ says that $A$ is an atomic sentence of $\mathcal{L}_0$, and $\mathrm{Tr}_0$ is the arithmetical truth predicate for these sentences.
The *Kripke-Feferman theory* $\mathsf{KF}$ is the classical first-order theory in $\mathcal{L}_T$ with the following axioms.

1. The axioms of [[Peano arithmetic|HACXBCM7SS]], with the [[induction schema|1QD0KDDGYJ]] for all formulas of $\mathcal{L}_T$.
2. $\forall A\, (\mathrm{AtSent}(A) \to (TA \leftrightarrow \mathrm{Tr}_0(A)))$.
3. $\forall A\, (\mathrm{AtSent}(A) \to (T[\neg A] \leftrightarrow \neg \mathrm{Tr}_0(A)))$.
4. $\forall A\, (T[T\dot A] \leftrightarrow TA)$.
5. $\forall A\, (T[\neg T\dot A] \leftrightarrow T[\neg A])$.
6. $\forall A\, (T[\neg \neg A] \leftrightarrow TA)$.
7. $\forall A\, \forall B\, (T[A \wedge B] \leftrightarrow (TA \wedge TB))$.
8. $\forall A\, \forall B\, (T[\neg (A \wedge B)] \leftrightarrow (T[\neg A] \vee T[\neg B]))$.
9. $\forall A\, \forall B\, (T[A \vee B] \leftrightarrow (TA \vee TB))$.
10. $\forall A\, \forall B\, (T[\neg (A \vee B)] \leftrightarrow (T[\neg A] \wedge T[\neg B]))$.
11. $\forall A(v)\, (T[\forall v\, A(v)] \leftrightarrow \forall x\, T[A(\dot x)])$.
12. $\forall A(v)\, (T[\neg \forall v\, A(v)] \leftrightarrow \exists x\, T[\neg A(\dot x)])$.
13. $\forall A(v)\, (T[\exists v\, A(v)] \leftrightarrow \exists x\, T[A(\dot x)])$.
14. $\forall A(v)\, (T[\neg \exists v\, A(v)] \leftrightarrow \forall x\, T[\neg A(\dot x)])$.

Axioms 2 to 14 are the thirteen truth axioms.

## Notation

1. Square brackets mark a syntactic operation that arithmetic expresses. For example, $T[\neg A]$ says that $T$ holds of the code of the negation of $A$.
2. $T\dot A$ is the sentence $T(\underline{n})$, where $n$ is the code $A$ and $\underline{n}$ is its numeral.
3. For a fixed sentence $\varphi$, $T\ulcorner \varphi \urcorner$ is $T$ applied to the numeral of the code of $\varphi$.
4. $\mathsf{KF} + \mathsf{Cons}$ adds $\forall A\, \neg (TA \wedge T[\neg A])$. $\mathsf{KF} + \mathsf{Compl}$ adds $\forall A\, (TA \vee T[\neg A])$.
5. Some authors add $\forall x\, (Tx \to \mathrm{Sent}(x))$, and some use a second predicate $F$ for falsity. The SEP entry notes that several variants exist.

## Remarks

### Examples

1. [[The liar in KF|DN71AAR1R1]]: $\mathsf{KF}$ proves $T\ulcorner \lambda \urcorner \leftrightarrow T\ulcorner \neg \lambda \urcorner$, and its two extensions decide the liar in opposite ways.
2. [[A Kripke fixed point is a model of KF|Z1HBM98428]]: the extension of any strong Kleene fixed point satisfies all fourteen axiom groups.

### Non-examples

1. The [[Friedman-Sheard theory|G062SH2PS0]] is not a version of $\mathsf{KF}$: FS and $\mathsf{KF}$ together are inconsistent.
2. The theory with axioms 1 to 14 and the classical negation axiom is inconsistent, so it is not a version of $\mathsf{KF}$.

### Why the negated clauses

The truth axioms describe the [[strong Kleene fixed points|ES71QTSTNV]] of Kripke.
Each axiom is a clause of the jump, for a sentence or for its negation.

1. Axiom 4 is the iteration axiom. With it, the classical negation axiom $T[\neg A] \leftrightarrow \neg TA$ would be inconsistent, as the SEP entry states.
2. So the negation of a complex sentence needs its own clause. Axioms 3, 5, 6, 8, 10, 12 and 14 give these clauses.
3. Each negated clause is the De Morgan dual of a positive clause. Axiom 5 says that $\neg T\dot A$ is true when the negation of $A$ is true.
4. Axioms 2 and 3 together give the classical negation clause for atomic sentences of $\mathcal{L}_0$. So truth is classical on $\mathcal{L}_0$.

### Relation to the concept page

The page [[Kripke-Feferman theory|2F15E76R0Z]] describes the motivation, the strength, the history and the common errors.
This page gives the exact axioms.

## Explanations

### L1 human

The theory has fourteen groups of axioms.
The first group is ordinary arithmetic.
The others say when a sentence is true, and when its negation is true, from the parts of the sentence.
For example, "$A$ and $B$" is true when both are true, and its negation is true when one of the negations is true.

### L2 human

We prove $\mathsf{KF} \vdash T\ulcorner \neg (0 = 1 \wedge 0 = 0) \urcorner$.

1. Axiom 3 applies to the atomic sentence $0 = 1$, which is false. So $T\ulcorner \neg\, 0 = 1 \urcorner$.
2. Axiom 8 gives $T\ulcorner \neg (0 = 1 \wedge 0 = 0) \urcorner \leftrightarrow (T\ulcorner \neg\, 0 = 1 \urcorner \vee T\ulcorner \neg\, 0 = 0 \urcorner)$.
3. The right side holds by step 1. So $T\ulcorner \neg (0 = 1 \wedge 0 = 0) \urcorner$.

The typical use of the axiom list is to check that a given model, such as a Kripke fixed point, satisfies $\mathsf{KF}$.
The trap is axiom 5: it is not $T[\neg T\dot A] \leftrightarrow \neg TA$, which is false for the liar in the least fixed point.

### L3 human

Each truth axiom of $\mathsf{KF}$ corresponds to one clause of Kripke's jump operator for strong Kleene logic.
A positive inductive definition gives the least fixed point; the axioms say only that $T$ is closed under the clauses in both directions.
So every fixed point, and not only the least one, gives a model.
This is the axiomatic counterpart of the semantic fact that the jump has many fixed points.
