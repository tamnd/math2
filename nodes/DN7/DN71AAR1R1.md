---
tag: DN71AAR1R1
kind: example
name: The liar in the Kripke-Feferman theory
aliases: [liar-in-kf, kf-liar]
msc: ["03F25", "03A05"]
topics: [6Q4JJ2MMV8]
audience: research
instance_of: [2F15E76R0Z]
illustrates: [2F15E76R0Z]
uses: [VQG258JQAD, SFPSB6JPTC, KBYY281V8T]
sources:
  - url: https://plato.stanford.edu/entries/truth-axiomatic/
    locator: "Axiomatic Theories of Truth, 4.4 The Kripke-Feferman theory"
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.3.4 Quasi-classical compositionality: the closed-off Kripke construction"
---

## Example

We use the axioms 1 to 14 of [[the Kripke-Feferman theory|VQG258JQAD]] and its notation.
Let $\lambda := \exists y\, (D(\underline{k}, y) \wedge \neg T(y))$ be the liar sentence from the [[proof of the diagonal lemma|SFPSB6JPTC]], with $\varphi(y) := \neg T(y)$.
We show three facts.
First, $\mathsf{KF} \vdash T\ulcorner \lambda \urcorner \leftrightarrow T\ulcorner \neg \lambda \urcorner$.
Second, $\mathsf{KF} + \mathsf{Cons}$ proves $\lambda$ and $\neg T\ulcorner \lambda \urcorner$.
Third, $\mathsf{KF} + \mathsf{Compl}$ proves $\neg \lambda$ and $T\ulcorner \lambda \urcorner$.

1. The proof of the diagonal lemma gives $\mathsf{PA} \vdash \forall y\, (D(\underline{k}, y) \leftrightarrow y = \ulcorner \lambda \urcorner)$ and $\mathsf{PA} \vdash \lambda \leftrightarrow \neg T\ulcorner \lambda \urcorner$.
2. *Arithmetical lemma.* For each arithmetical formula $\psi(\bar y)$, $\mathsf{KF}$ proves $\forall \bar y\, (T\ulcorner \psi(\dot{\bar y}) \urcorner \leftrightarrow \psi(\bar y))$ and $\forall \bar y\, (T\ulcorner \neg \psi(\dot{\bar y}) \urcorner \leftrightarrow \neg \psi(\bar y))$.
3. We prove step 2 by induction on $\psi$, for both claims together. Atomic formulas use axioms 2 and 3.
4. For $\psi = \neg \chi$, the first claim is the second claim for $\chi$. The second claim uses axiom 6 and the first claim for $\chi$.
5. Conjunction and disjunction use axioms 7 to 10. Quantifiers use axioms 11 to 14.
6. Axiom 13 gives $T\ulcorner \lambda \urcorner \leftrightarrow \exists m\, T\ulcorner D(\underline{k}, \dot m) \wedge \neg T(\dot m) \urcorner$.
7. Axiom 7 turns the right side into $\exists m\, (T\ulcorner D(\underline{k}, \dot m) \urcorner \wedge T\ulcorner \neg T(\dot m) \urcorner)$.
8. Step 2 for $D$ turns it into $\exists m\, (D(\underline{k}, m) \wedge T\ulcorner \neg T(\dot m) \urcorner)$.
9. By step 1, the only such $m$ is the code of $\lambda$. So $T\ulcorner \lambda \urcorner \leftrightarrow T\ulcorner \neg T\ulcorner \lambda \urcorner \urcorner$.
10. Axiom 5 with $A := \ulcorner \lambda \urcorner$ gives $T\ulcorner \neg T\ulcorner \lambda \urcorner \urcorner \leftrightarrow T\ulcorner \neg \lambda \urcorner$.
11. Steps 9 and 10 give $\mathsf{KF} \vdash T\ulcorner \lambda \urcorner \leftrightarrow T\ulcorner \neg \lambda \urcorner$. This is the first fact.
12. *With $\mathsf{Cons}$.* The axiom gives $\neg (T\ulcorner \lambda \urcorner \wedge T\ulcorner \neg \lambda \urcorner)$. With step 11, this gives $\neg T\ulcorner \lambda \urcorner$.
13. Step 1 then gives $\lambda$. This is the second fact.
14. *With $\mathsf{Compl}$.* The axiom gives $T\ulcorner \lambda \urcorner \vee T\ulcorner \neg \lambda \urcorner$. With step 11, this gives $T\ulcorner \lambda \urcorner$.
15. Step 1 then gives $\neg \lambda$. This is the third fact.

## Remarks

The example shows that $\mathsf{KF}$ describes a notion of truth that is not classical, although its logic is classical.
By step 11, either $\lambda$ and its negation are both true, or neither is true.
So truth in $\mathsf{KF}$ is paracomplete (a [[truth-value gap|4CBCWZQZ12]]) or paraconsistent (a [[truth-value glut|WH94DG6D3Q]]) at the liar.
The SEP entry on the liar says that $\mathsf{KF}$ alone is silent about the liar.
Its two extensions treat it in opposite ways: $\mathsf{KF} + \mathsf{Cons}$ proves the liar and calls it untrue, and $\mathsf{KF} + \mathsf{Compl}$ refutes it and calls it true.
The theory $\mathsf{KF} + \mathsf{Cons}$ proves $\lambda$ but not $T\ulcorner \lambda \urcorner$, so it is not closed under the rule "from $\varphi$ infer $T\ulcorner \varphi \urcorner$".
If we replace axiom 5 by the classical negation axiom, step 9 and that axiom give $T\ulcorner \lambda \urcorner \leftrightarrow \neg T\ulcorner T\ulcorner \lambda \urcorner \urcorner$.
Axiom 4 then gives $T\ulcorner \lambda \urcorner \leftrightarrow \neg T\ulcorner \lambda \urcorner$, a contradiction.
This is the inconsistency of iteration with the negation axiom.

## Explanations

### L1 human

The liar says "I am not true".
The Kripke-Feferman theory cannot decide whether the liar is true.
It can prove only one thing: the liar is true exactly when its negation is true.
So either both are true, or neither is true.
If we add the rule "no sentence is true together with its negation", the theory proves that the liar is not true.
Then, since the liar says exactly that, the theory also proves the liar itself.

### L2 human

1. In arithmetic, $\lambda \leftrightarrow \neg T\ulcorner \lambda \urcorner$.
2. The truth axioms of $\mathsf{KF}$ take $T\ulcorner \lambda \urcorner$ through the parts of $\lambda$ and give $T\ulcorner \neg T\ulcorner \lambda \urcorner \urcorner$.
3. The axiom for negated truth sentences gives $T\ulcorner \neg \lambda \urcorner$.
4. So $T\ulcorner \lambda \urcorner \leftrightarrow T\ulcorner \neg \lambda \urcorner$.
5. With $\mathsf{Cons}$, both cannot hold, so neither holds. In particular $\neg T\ulcorner \lambda \urcorner$, which is $\lambda$ by step 1.

The typical use of this example is to compare type-free truth theories by their verdict on the liar.
The trap is step 5: $\mathsf{KF} + \mathsf{Cons}$ asserts $\lambda$ and also asserts that $\lambda$ is not true.
