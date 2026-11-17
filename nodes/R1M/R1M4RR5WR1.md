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

Let $T$ be a theory in the language $\set{0, S, +, \cdot}$ that contains $\mathsf{PA}$, has a decidable set of axioms, and whose axioms are all true in the standard model $\N$.
Let $\mathrm{Prov}_T$ be its standard [[provability predicate|NB2BCZR40F]].
The completeness schema $\mathrm{C}(T)$ is the set of all sentences $\varphi \to \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$, one for each sentence $\varphi$.
It reverses the arrow of the local [[reflection principle|NB485KFXKV]] $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$.
We show that $\mathrm{C}(T)$ is not a reflection principle: it has an instance that is false in $\N$, while every instance of $\mathrm{Rfn}(T)$ is true in $\N$.

1. Every theorem of $T$ is true in $\N$, by the [[soundness theorem|4A84VHDTHV]] of first-order logic, because all axioms of $T$ are true in $\N$.
2. For each sentence $\varphi$, the sentence $\mathrm{Prov}_T(\ulcorner \varphi \urcorner)$ is true in $\N$ exactly when $T \vdash \varphi$. This is the meaning of the formula $\mathrm{Prov}_T$ under the coding.
3. Every instance $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \varphi$ of $\mathrm{Rfn}(T)$ is true in $\N$. If its antecedent is true, then $T \vdash \varphi$ by step 2, and $\varphi$ is true by step 1.
4. By the [[diagonal lemma|3PRW76471J]] there is a sentence $G$ with $T \vdash G \leftrightarrow \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$, the [[Gödel sentence|X9WYNYE29C]] of $T$.
5. $T$ does not prove $G$. If $T \vdash G$, then the [[derivability condition|F6H4STF9RG]] D1 gives $T \vdash \mathrm{Prov}_T(\ulcorner G \urcorner)$, and step 4 gives $T \vdash \neg \mathrm{Prov}_T(\ulcorner G \urcorner)$. Then $T$ proves a sentence and its negation, which contradicts step 1, because a contradiction is not true in $\N$.
6. By steps 5 and 2, the sentence $\mathrm{Prov}_T(\ulcorner G \urcorner)$ is false in $\N$.
7. By step 1, the equivalence of step 4 is true in $\N$. With step 6 it gives that $G$ is true in $\N$.
8. So the instance $G \to \mathrm{Prov}_T(\ulcorner G \urcorner)$ of $\mathrm{C}(T)$ has a true antecedent (step 7) and a false consequent (step 6), and it is false in $\N$.
9. Steps 3 and 8 show that $\mathrm{C}(T)$ does not have the defining property of a reflection principle for a sound theory: it does not express that the theorems of $T$ are true.

## Remarks

The example shows that the direction of the arrow matters.
Reflection says "provable implies true", and it is true for a sound theory; the completeness schema says "true implies provable", and it fails for every sound theory of this kind, by the first incompleteness theorem.
For a $\Sigma_1$ sentence $\sigma$, the instance $\sigma \to \mathrm{Prov}_T(\ulcorner \sigma \urcorner)$ is provable in $T$; this is formalized $\Sigma_1$-completeness, one of the [[derivability conditions|F6H4STF9RG]].
So the completeness schema fails first at the level $\Pi_1$, and $G$ is (equivalent to) a $\Pi_1$ sentence.
Adding the instance of step 8 to $T$ gives a theory that proves $\neg G$, because $G \to \mathrm{Prov}_T(\ulcorner G \urcorner)$ and step 4 give $G \to \neg G$.
That theory is consistent, by step 5, but it proves the false sentence $\neg G$.

## Explanations

### L1 human

A reflection principle says "everything the theory proves is true".
The opposite statement, "everything true is proved by the theory", sounds similar but is very different.
Gödel built a true statement that the theory cannot prove, so the opposite statement is false for it.
A good theory is like a careful witness: everything it says is true, but it does not say everything that is true.

### L2 human

We compare the two schemas on two sentences, for a sound theory $T \supseteq \mathsf{PA}$.

1. For $\varphi := (0 = S0)$: the reflection instance $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner) \to 0 = S0$ is true, because $T$ does not prove $0 = S0$. The completeness instance $0 = S0 \to \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$ is also true, because its antecedent is false.
2. For the Gödel sentence $G$: the reflection instance is true, because its antecedent is false (step 6). The completeness instance is false (step 8).

The typical use of this comparison is to keep the two directions apart: formalized $\Sigma_1$-completeness is the completeness direction for $\Sigma_1$ sentences, and it is provable, while reflection goes the other way and is not.
A trap is to read $\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ as a law; only the instances for provable $\varphi$ hold in both directions inside $T$.
