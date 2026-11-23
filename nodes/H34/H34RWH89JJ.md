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

### The claim and the tools

Let PA be [[Peano arithmetic|0QFT7Z76N5]], with a fixed [[Gödel numbering|MFJXPAF0R0]] of formulas and derivations.
Let $\mathrm{Pr}(x)$ be the $\Sigma_1$ [[provability predicate|NB2BCZR40F]] of PA, "some derivation in PA proves the formula with code $x$".
Let $\mathrm{Con}(\mathsf{PA})$ be the $\Pi_1$ sentence $\lnot \mathrm{Pr}(\ulcorner 0 = 1 \urcorner)$, and for a sentence $B$ let $\mathrm{Con}(\mathsf{PA} + B)$ be $\lnot \mathrm{Pr}(\ulcorner \lnot B \urcorner)$.
We show that PA [[interprets|8H03GRMDYG]] the theory $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$, a fact first proved by Feferman.

We use four known facts.

- (F1) Orey-Hájek characterization: for a sentence $A$, $\mathsf{PA} \rhd \mathsf{PA} + A$ holds if and only if every $\Pi_1$ sentence provable in $\mathsf{PA} + A$ is provable in PA.
- (F2) Provable $\Sigma_1$-completeness: for each $\Sigma_1$ sentence $\sigma$, $\mathsf{PA} \vdash \sigma \to \mathrm{Pr}(\ulcorner \sigma \urcorner)$.
- (F3) Derivability conditions: if $\mathsf{PA} \vdash \varphi$, then $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \varphi \urcorner)$; and $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \varphi \to \psi \urcorner) \land \mathrm{Pr}(\ulcorner \varphi \urcorner) \to \mathrm{Pr}(\ulcorner \psi \urcorner)$.
- (F4) [[Gödel's second incompleteness theorem|4PZM5GJTR5]]: a consistent recursively axiomatized extension $U$ of PA does not prove $\mathrm{Con}(U)$.

By (F1), it is enough to show that $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$ is $\Pi_1$-conservative over PA.

### The proof of Π1-conservativity

1. Let $\pi$ be a $\Pi_1$ sentence with $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA}) \vdash \pi$.
   We must show that $\mathsf{PA} \vdash \pi$.
2. By the [[deduction theorem|9X08XK5RV2]], $\mathsf{PA} \vdash \lnot \mathrm{Con}(\mathsf{PA}) \to \pi$.
   By contraposition, $\mathsf{PA} \vdash \lnot \pi \to \mathrm{Con}(\mathsf{PA})$.
3. The sentence $\lnot \pi$ is equivalent to a $\Sigma_1$ sentence, since $\pi$ is $\Pi_1$.
   So (F2) gives $\mathsf{PA} \vdash \lnot \pi \to \mathrm{Pr}(\ulcorner \lnot \pi \urcorner)$.
4. PA proves the tautology $\pi \to (\lnot \pi \to 0 = 1)$.
   Two uses of (F3) give $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \pi \urcorner) \land \mathrm{Pr}(\ulcorner \lnot \pi \urcorner) \to \mathrm{Pr}(\ulcorner 0 = 1 \urcorner)$.
5. We now argue in $\mathsf{PA} + \lnot \pi$.
   Step 2 gives $\mathrm{Con}(\mathsf{PA})$, and step 3 gives $\mathrm{Pr}(\ulcorner \lnot \pi \urcorner)$.
6. If $\mathrm{Pr}(\ulcorner \pi \urcorner)$ also held, step 4 would give $\mathrm{Pr}(\ulcorner 0 = 1 \urcorner)$, against $\mathrm{Con}(\mathsf{PA})$.
   So $\mathsf{PA} + \lnot \pi \vdash \lnot \mathrm{Pr}(\ulcorner \pi \urcorner)$.
7. PA proves the tautology $\lnot \lnot \pi \leftrightarrow \pi$, so (F3) gives $\mathsf{PA} \vdash \mathrm{Pr}(\ulcorner \lnot \lnot \pi \urcorner) \leftrightarrow \mathrm{Pr}(\ulcorner \pi \urcorner)$.
   So $\lnot \mathrm{Pr}(\ulcorner \pi \urcorner)$ is equivalent in PA to $\mathrm{Con}(\mathsf{PA} + \lnot \pi)$.
8. By steps 6 and 7, $\mathsf{PA} + \lnot \pi \vdash \mathrm{Con}(\mathsf{PA} + \lnot \pi)$.
9. The theory $\mathsf{PA} + \lnot \pi$ is a recursively axiomatized extension of PA, so by step 8 and (F4) it is inconsistent.
10. So $\mathsf{PA} \vdash \pi$.
    This proves the $\Pi_1$-conservativity, and (F1) gives $\mathsf{PA} \rhd \mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$.

## Remarks

### Consistent but false

The theory $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$ is consistent, because PA does not prove $\mathrm{Con}(\mathsf{PA})$, by (F4).
It is not sound: PA is consistent, so $\mathrm{Con}(\mathsf{PA})$ is true in $\mathbb{N}$, and the new axiom is a false $\Sigma_1$ sentence.
So an interpretation preserves consistency, but it does not preserve truth.
It does not give conservation either: the interpreted theory proves the $\Sigma_1$ sentence $\lnot \mathrm{Con}(\mathsf{PA})$, which PA does not prove.

### What changes with the theory and the sentence

The proof works for each consistent recursively axiomatized extension $T$ of PA in the language of PA, and gives $T \rhd T + \lnot \mathrm{Con}(T)$.
It fails for the opposite sentence: PA does not interpret $\mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, by the [[non-example|NN7696NJR6]].
The difference lies in the class of the new axiom.
The axiom $\mathrm{Con}(\mathsf{PA})$ is itself a $\Pi_1$ sentence that PA does not prove, so it breaks $\Pi_1$-conservativity at once.
The axiom $\lnot \mathrm{Con}(\mathsf{PA})$ is $\Sigma_1$, and steps 2 to 10 show that it adds no $\Pi_1$ theorems.

### A direct construction

A second proof builds the interpretation directly.
PA proves $\mathrm{Con}(\mathsf{PA}) \to \mathrm{Con}(\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA}))$, by the formalized second incompleteness theorem.
Under the hypothesis $\mathrm{Con}(\mathsf{PA})$, the arithmetized completeness theorem gives a definable model of $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$.
Under the hypothesis $\lnot \mathrm{Con}(\mathsf{PA})$, the identity interpretation already works.
The interpretation is defined by cases on $\mathrm{Con}(\mathsf{PA})$.

## Explanations

### L1 human

Peano arithmetic is a list of rules about whole numbers, and it cannot prove that it is free of contradictions.
We can add the false rule "Peano arithmetic contains a contradiction" and still get a list with no contradiction.
The example shows more: the old rules can imitate the new list.
They define a kind of "numbers" in which every rule of the new list holds, including the false one.
These "numbers" contain extra, infinitely large elements, and one of them plays the part of a proof of a contradiction.

### L2 human

We follow what the interpretation does inside the standard numbers $\mathbb{N}$.
Since $\mathbb{N}$ is a model of PA, the interpretation $I$ gives a structure $\mathbb{N}^I$, defined in $\mathbb{N}$ by formulas of arithmetic.
By the lemma on interpretations, $\mathbb{N}^I$ is a model of $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$, so it has an element $p$ that "codes a derivation of $0 = 1$ in PA".

Suppose that $\mathbb{N}^I$ were isomorphic to $\mathbb{N}$.
Then $p$ would correspond to a standard number that codes a real derivation of $0 = 1$, and PA would be inconsistent.
PA is consistent, so $\mathbb{N}^I$ is a non-standard model, and $p$ is a non-standard number.

The typical use of the example is as a warning: interpretability is decided by $\Pi_1$-conservativity, not by truth.
Watch out: "PA interprets $\mathsf{PA} + \lnot \mathrm{Con}(\mathsf{PA})$" does not mean that PA is inconsistent, since the false sentence holds only in the interpreted structure.
