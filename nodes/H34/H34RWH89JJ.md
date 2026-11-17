---
tag: H34RWH89JJ
kind: example
name: Peano arithmetic interprets PA plus the inconsistency of PA
msc: ["03F25", "03F30", "03F40"]
topics: [8XY7JYZKFW]
audience: grad
instance_of: [8H03GRMDYG]
uses: [8H03GRMDYG, 0QFT7Z76N5, 4PZM5GJTR5, MFJXPAF0R0, NB2BCZR40F, 7CVJCQKY41, N238J43XNE, 9X08XK5RV2]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretability
    locator: Informal definition
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
  - book: isbn:9780521857840
---

## Example

Let PA be [[Peano arithmetic|0QFT7Z76N5]], with a fixed [[Gödel numbering|MFJXPAF0R0]] of formulas and derivations.
Let $\mathrm{Pr}(x)$ be the $\Sigma_1$ [[provability predicate|NB2BCZR40F]] of PA: "there is a derivation in PA of the formula with code $x$".
Let $\mathrm{Con}(\mathsf{PA})$ be the $\Pi_1$ sentence $\lnot\mathrm{Pr}(\ulcorner 0 = 1 \urcorner)$.
For a sentence $B$, let $\mathrm{Con}(\mathsf{PA} + B)$ be the sentence $\lnot\mathrm{Pr}(\ulcorner \lnot B \urcorner)$.
We show that PA [[interprets|8H03GRMDYG]] the theory $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$.
Feferman proved this fact first.

We use the following known facts.

- (F1) Orey-Hájek characterization: for a sentence $A$, $\mathsf{PA} \rhd \mathsf{PA} + A$ holds if and only if every $\Pi_1$ sentence provable in $\mathsf{PA} + A$ is provable in PA.
- (F2) Provable $\Sigma_1$-completeness: for each $\Sigma_1$ sentence $\sigma$, $\mathsf{PA} \vdash \sigma \to \mathrm{Pr}(\ulcorner \sigma \urcorner)$.
- (F3) Derivability conditions: if $\mathsf{PA} \vdash \varphi$, then $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \varphi \urcorner)$; and $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \varphi \to \psi \urcorner) \land \mathrm{Pr}(\ulcorner \varphi \urcorner) \to \mathrm{Pr}(\ulcorner \psi \urcorner)$.
- (F4) [[Gödel's second incompleteness theorem|4PZM5GJTR5]]: a consistent recursively axiomatized extension $U$ of PA does not prove $\mathrm{Con}(U)$.

By (F1), it is enough to show that $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$ is $\Pi_1$-conservative over PA.

1. Let $\pi$ be a $\Pi_1$ sentence with $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA}) \vdash \pi$. We must show $\mathsf{PA} \vdash \pi$.
2. By the [[deduction theorem|9X08XK5RV2]], $\mathsf{PA} \vdash \lnot\mathrm{Con}(\mathsf{PA}) \to \pi$. By contraposition, $\mathsf{PA} \vdash \lnot\pi \to \mathrm{Con}(\mathsf{PA})$.
3. The sentence $\lnot\pi$ is equivalent to a $\Sigma_1$ sentence, since $\pi$ is $\Pi_1$. By (F2), $\mathsf{PA} \vdash \lnot\pi \to \mathrm{Pr}(\ulcorner \lnot\pi \urcorner)$.
4. The formula $\pi \to (\lnot\pi \to 0 = 1)$ is a tautology, so PA proves it. Two uses of (F3) give $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \pi \urcorner) \land \mathrm{Pr}(\ulcorner \lnot\pi \urcorner) \to \mathrm{Pr}(\ulcorner 0 = 1 \urcorner)$.
5. We now argue in the theory $\mathsf{PA} + \lnot\pi$. By step 2 we have $\mathrm{Con}(\mathsf{PA})$, and by step 3 we have $\mathrm{Pr}(\ulcorner \lnot\pi \urcorner)$.
6. If $\mathrm{Pr}(\ulcorner \pi \urcorner)$ also held, step 4 would give $\mathrm{Pr}(\ulcorner 0 = 1 \urcorner)$, against $\mathrm{Con}(\mathsf{PA})$. So $\mathsf{PA} + \lnot\pi \vdash \lnot\mathrm{Pr}(\ulcorner \pi \urcorner)$.
7. The formula $\lnot\lnot\pi \leftrightarrow \pi$ is a tautology, so (F3) gives $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \lnot\lnot\pi \urcorner) \leftrightarrow \mathrm{Pr}(\ulcorner \pi \urcorner)$. So $\lnot\mathrm{Pr}(\ulcorner \pi \urcorner)$ is equivalent in PA to $\mathrm{Con}(\mathsf{PA} + \lnot\pi)$.
8. By steps 6 and 7, $\mathsf{PA} + \lnot\pi \vdash \mathrm{Con}(\mathsf{PA} + \lnot\pi)$.
9. The theory $\mathsf{PA} + \lnot\pi$ is a recursively axiomatized extension of PA. By step 8 and (F4), it is inconsistent.
10. So $\mathsf{PA} \vdash \pi$. This proves the $\Pi_1$-conservativity, and (F1) gives $\mathsf{PA} \rhd \mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$.

## Remarks

The theory $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$ is consistent, because PA does not prove $\mathrm{Con}(\mathsf{PA})$ by (F4).
It is not sound: PA is consistent, so $\mathrm{Con}(\mathsf{PA})$ is true in the standard model $\N$, and the axiom $\lnot\mathrm{Con}(\mathsf{PA})$ is a false $\Sigma_1$ sentence.
So an interpretation preserves consistency, but it does not preserve truth.

The interpretation works in every model of PA, also in $\N$.
So $\N$ defines a model $\N^I$ of $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$, and this model is not isomorphic to $\N$.

The proof also works for each consistent recursively axiomatized extension $T$ of PA in the language of PA: $T \rhd T + \lnot\mathrm{Con}(T)$.
It fails for the opposite sentence: PA does not interpret $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, see [[the non-example|NN7696NJR6]].

A second proof gives the interpretation directly.
PA proves $\mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA}))$, by the formalized second incompleteness theorem.
Under the hypothesis $\mathrm{Con}(\mathsf{PA})$, the arithmetized completeness theorem gives a definable model of $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$.
Under the hypothesis $\lnot\mathrm{Con}(\mathsf{PA})$, the identity interpretation already works.
The interpretation is defined by cases on $\mathrm{Con}(\mathsf{PA})$.

## Explanations

### L1 human

Peano arithmetic is a list of rules about whole numbers, and it cannot prove that it is free of contradictions.
We can add the false rule "Peano arithmetic contains a contradiction" and still get a list with no contradiction.
This example shows more: the old rules can imitate the new list.
They define a kind of "numbers" in which every rule of the new list holds, including the false one.
These "numbers" contain extra, infinitely large elements, and one of them plays the part of a proof of a contradiction.

### L2 human

We follow what the interpretation does inside the standard numbers $\N$.

1. $\N$ is a model of PA, so the interpretation $I$ gives a structure $\N^I$, defined in $\N$ by formulas of arithmetic.
2. By the lemma on interpretations, $\N^I$ is a model of $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$.
3. So $\N^I$ has an element $p$ with "$p$ codes a derivation of $0 = 1$ in PA".
4. Suppose that $\N^I$ were isomorphic to $\N$. Then $p$ would correspond to a standard number that codes a real derivation of $0 = 1$, and PA would be inconsistent.
5. PA is consistent, so $\N^I$ is a nonstandard model, and its element $p$ is a nonstandard number.

The typical use of the example is as a warning: interpretability is decided by $\Pi_1$-conservativity, not by truth.
A trap is to read "PA interprets $\mathsf{PA} + \lnot\mathrm{Con}(\mathsf{PA})$" as "PA is inconsistent"; the false sentence holds only in the interpreted structure.
