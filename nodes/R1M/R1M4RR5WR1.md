---
tag: R1M4RR5WR1
kind: example
name: The completeness schema is not a reflection principle
msc: ["03F40"]
topics: [HXHHWY3328]
audience: research
not_instance_of:
  - target: NB485KFXKV
    note: "The schema φ → Prov_T(⌜φ⌝) asserts completeness, not soundness; for a sound T its instance for the Gödel sentence is false in the standard model, while every instance of a reflection principle for a sound T is true."
uses: [NB485KFXKV, NB2BCZR40F, 3PRW76471J, X9WYNYE29C, F6H4STF9RG, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Truth of the Gödel sentence
---

## Example

Turn the arrow of a reflection principle around.
Instead of "if $T$ proves $\varphi$, then $\varphi$", say "if $\varphi$, then $T$ proves $\varphi$".
The two look alike, but the second claims that $T$ proves every truth, and we show that it fails.

Let $T$ be a theory in the language $\{ 0, S, +, \cdot \}$ that contains $\mathsf{PA}$, has a decidable set of axioms, and has all its axioms true in $\mathbb{N}$.
Let $\mathrm{Prov}_T$ be its standard [[provability predicate|NB2BCZR40F]].
The completeness schema $\mathrm{C}(T)$ is the set of all sentences
$$\varphi \to \mathrm{Prov}_T(\ulcorner \varphi \urcorner),$$
one for each sentence $\varphi$.
We show that every instance of the local [[reflection principle|NB485KFXKV]] $\mathrm{Rfn}(T)$ is true in $\mathbb{N}$, while some instance of $\mathrm{C}(T)$ is false.

1. Every theorem of $T$ is true in $\mathbb{N}$, by the [[soundness theorem|4A84VHDTHV]], because all axioms of $T$ are true in $\mathbb{N}$.
2. For each sentence $\varphi$, the sentence $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ is true in $\mathbb{N}$ exactly when $T \vdash \varphi$.
   This is what the formula $\mathrm{Prov}_T$ means under the coding.
3. Every instance $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$ of $\mathrm{Rfn}(T)$ is true in $\mathbb{N}$.
   If its antecedent is true, then $T \vdash \varphi$ by step 2, and $\varphi$ is true by step 1.
4. By the [[diagonal lemma|3PRW76471J]] there is a sentence $G$ with $T \vdash G \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$, the [[Gödel sentence|X9WYNYE29C]] of $T$.
5. $T$ does not prove $G$.
   If $T \vdash G$, then the [[derivability condition|F6H4STF9RG]] D1 gives $T \vdash \mathrm{Prov}_T(\ulcorner G \urcorner)$, and step 4 gives $T \vdash \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$.
   Then $T$ proves a sentence and its negation, and one of them is false, against step 1.
6. By steps 5 and 2, the sentence $\mathrm{Prov}_T(\ulcorner G \urcorner)$ is false in $\mathbb{N}$.
7. The equivalence of step 4 is a theorem of $T$, so it is true in $\mathbb{N}$ by step 1.
   With step 6 it shows that $G$ is true in $\mathbb{N}$.
8. So the instance $G \to \mathrm{Prov}_T(\ulcorner G \urcorner)$ of $\mathrm{C}(T)$ has a true antecedent (step 7) and a false consequent (step 6).
   It is false in $\mathbb{N}$.

Steps 3 and 8 show that $\mathrm{C}(T)$ does not express that the theorems of $T$ are true, which is the defining property of a reflection principle.

## Remarks

The direction of the arrow is the whole difference.
"Provable implies true" holds for every sound theory, and "true implies provable" fails for every sound theory of this kind, by the first incompleteness theorem.

For $\Sigma_1$ sentences the completeness direction does hold, and $T$ even proves it.
For each $\Sigma_1$ sentence $\sigma$, $T \vdash \sigma \to \mathrm{Prov}_T(\ulcorner \sigma \urcorner)$; this is formalized $\Sigma_1$-completeness, the principle behind the derivability condition D3.
So the completeness schema first fails at the level $\Pi_1$, and $G$ is indeed equivalent to a $\Pi_1$ sentence.

What happens if we add the false instance of step 8 to $T$?
With step 4, $G \to \mathrm{Prov}_T(\ulcorner G \urcorner)$ gives $G \to \neg G$, and so $\neg G$.
The new theory is $T + \neg G$, which is consistent because $T \nvdash G$ (step 5), but it proves the false sentence $\neg G$.

## Explanations

### L1 human

A reflection principle says "everything the theory proves is true".
The reverse, "everything true is proved by the theory", sounds similar but says something very different.
Gödel built a true statement that the theory cannot prove, so the reverse statement fails.
A good theory is like a careful witness: everything it says is true, but it does not say everything that is true.

### L2 human

Compare the two schemas on two sentences, for a sound theory $T \supseteq \mathsf{PA}$.
For $0 = S0$, the reflection instance $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner) \to 0 = S0$ is true, because $T$ does not prove $0 = S0$.
The completeness instance $0 = S0 \to \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$ is also true, because its antecedent is false.
For the Gödel sentence $G$, the reflection instance is true, because its antecedent is false (step 6), but the completeness instance is false (step 8).
So the false sentence does not separate the schemas, and the true unprovable sentence does.
Watch out: do not read $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ as a law; inside $T$ both directions hold only for the sentences that $T$ proves.
