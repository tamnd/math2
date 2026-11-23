---
tag: JHGJ6APMRF
kind: example
name: Consistency is equivalent to local reflection for Π1 sentences
msc: ["03F40", "03F30"]
topics: [HXHHWY3328]
audience: research
instance_of: [NB485KFXKV]
uses: [NB485KFXKV, 4NBAX3VRQ7, F6H4STF9RG, NB2BCZR40F, 7CVJCQKY41, 3K1AKGXF8A]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_principle
    locator: For arithmetic
---

## Example

Goldbach's conjecture says that every even number from $4$ on is a sum of two primes, and each single case can be checked by a finite search.
Suppose $\mathsf{PA}$ proved the conjecture but it were false.
Then some even number fails, $\mathsf{PA}$ can verify the failure by computation, and $\mathsf{PA}$ would prove both the conjecture and its negation.
So "if $\mathsf{PA}$ proves Goldbach, then Goldbach holds" follows from the consistency of $\mathsf{PA}$ alone.
We make this argument formal, for every sentence of the same shape.

Let $T$ be a consistent theory in the language $\{ 0, S, +, \cdot \}$ that contains $\mathsf{PA}$ and has a decidable set of axioms.
Let $\mathrm{Prov}_T$ be its standard [[provability predicate|NB2BCZR40F]] and $\mathrm{Con}(T) := \neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$.
A $\Pi_1$ sentence is a sentence $\forall x \, \theta(x)$ in which every quantifier of $\theta$ is bounded; a block of universal quantifiers can be contracted to one by coding tuples.
We show that, over $T$, the sentence $\mathrm{Con}(T)$ is equivalent to the schema $\mathrm{Rfn}_{\Pi_1}(T)$ of all sentences $\mathrm{Prov}_T(\ulcorner \pi \urcorner) \to \pi$ with $\pi$ a $\Pi_1$ sentence.

We use three facts about $\mathrm{Prov}_T$ that hold for $T \supseteq \mathsf{PA}$, from the [[derivability conditions|F6H4STF9RG]].

- (D1) If $T \vdash \varphi$, then $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \urcorner)$.
- (D2) $T \vdash \mathrm{Prov}_T(\ulcorner \varphi \to \psi \urcorner) \to (\mathrm{Prov}_T(\ulcorner \varphi \urcorner) \to \mathrm{Prov}_T(\ulcorner \psi \urcorner))$ for all sentences $\varphi$, $\psi$.
- (FΣ) Formalized $\Sigma_1$-completeness: $T \vdash \sigma \to \mathrm{Prov}_T(\ulcorner \sigma \urcorner)$ for every $\Sigma_1$ sentence $\sigma$.

**First direction: reflection gives consistency.**

1. The sentence $0 = S0$ has no unbounded quantifier, so it is a $\Pi_1$ sentence (put a vacuous $\forall x$ in front for the exact form).
2. So $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner) \to 0 = S0$ is an instance of $\mathrm{Rfn}_{\Pi_1}(T)$.
3. The axiom $\forall x \, \neg (Sx = 0)$ of [[Robinson arithmetic|3K1AKGXF8A]] gives $\neg (0 = S0)$, and this axiom is in $T$.
4. From $A \to B$ and $\neg B$ we get $\neg A$, so steps 2 and 3 give $\neg \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, which is $\mathrm{Con}(T)$.

**Second direction: consistency gives reflection.**
Fix a $\Pi_1$ sentence $\pi = \forall x \, \theta(x)$ with $\theta$ bounded.

5. Let $\sigma := \exists x \, \neg \theta(x)$.
   Since $\neg \theta$ is bounded, $\sigma$ is a $\Sigma_1$ sentence, and pure logic proves $\neg \pi \leftrightarrow \sigma$.
6. By (FΣ), $T \vdash \sigma \to \mathrm{Prov}_T(\ulcorner \sigma \urcorner)$.
7. Pure logic proves $\sigma \to \neg \pi$, so (D1) and (D2) give $T \vdash \mathrm{Prov}_T(\ulcorner \sigma \urcorner) \to \mathrm{Prov}_T(\ulcorner \neg \pi \urcorner)$.
8. The tautology $\pi \to (\neg \pi \to 0 = S0)$, with (D1) and two uses of (D2), gives $T \vdash \mathrm{Prov}_T(\ulcorner \pi \urcorner) \to (\mathrm{Prov}_T(\ulcorner \neg \pi \urcorner) \to \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner))$.
9. Chaining steps 6, 7 and 8 gives $T \vdash (\sigma \wedge \mathrm{Prov}_T(\ulcorner \pi \urcorner)) \to \mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$.
10. By contraposition, $T \vdash \mathrm{Con}(T) \to (\mathrm{Prov}_T(\ulcorner \pi \urcorner) \to \neg \sigma)$.
11. Since $\neg \sigma$ is equivalent to $\pi$ (step 5), $T \vdash \mathrm{Con}(T) \to (\mathrm{Prov}_T(\ulcorner \pi \urcorner) \to \pi)$.

Step 11 holds for every $\Pi_1$ sentence $\pi$.
With step 4, it shows that $T + \mathrm{Con}(T)$ and $T + \mathrm{Rfn}_{\Pi_1}(T)$ have the same theorems.

## Remarks

The example shows that $\mathrm{Con}(T)$ is a [[reflection principle|NB485KFXKV]] in disguise, and that it carries the full strength of reflection for $\Pi_1$ sentences.
With a free variable in $\pi$ and the uniform form of (FΣ), the same steps show that $\mathrm{Con}(T)$ is also equivalent to the uniform schema $\mathrm{RFN}_{\Pi_1}(T)$.
The hypothesis $T \supseteq \mathsf{PA}$ is used only for (D1), (D2) and (FΣ), and the theory $\mathsf{I\Sigma}_1$ already proves these, so $T \supseteq \mathsf{I\Sigma}_1$ is enough.

The equivalence stops at $\Pi_1$, and step 6 shows why.
It needs the negation of $\pi$ to be $\Sigma_1$, so that (FΣ) applies.
For a $\Sigma_1$ sentence the negation is $\Pi_1$, and (FΣ) says nothing about it.
Indeed, for the $\Sigma_1$ sentence $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, the reflection instance is equivalent in $T + \mathrm{Con}(T)$ to $\mathrm{Con}(T + \mathrm{Con}(T))$, which $T + \mathrm{Con}(T)$ does not prove when it is consistent.

## Explanations

### L1 human

A theory "reflects" on a statement when it says "if I prove this statement, then it is true".
Consistency says "I do not prove $0 = 1$", which is the reflection for the false statement $0 = 1$.
For statements of the simplest checkable kind, like Goldbach's conjecture, consistency already gives the reflection.
If such a statement were false, a counterexample could be checked by hand, and the theory would prove the statement false.
If the theory also proved it true, it would contradict itself.

### L2 human

Follow the second direction for the true $\Pi_1$ sentence $\pi = \forall x \, (0 + x = x)$.
Its negation is equivalent to the $\Sigma_1$ sentence $\sigma = \exists x \, \neg (0 + x = x)$.
Reason inside $T + \mathrm{Con}(T)$, and assume both $\mathrm{Prov}_T(\ulcorner \pi \urcorner)$ and $\sigma$.
From $\sigma$, formalized $\Sigma_1$-completeness gives $\mathrm{Prov}_T(\ulcorner \sigma \urcorner)$, and so $\mathrm{Prov}_T(\ulcorner \neg \pi \urcorner)$.
Together with $\mathrm{Prov}_T(\ulcorner \pi \urcorner)$ this gives $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, which contradicts $\mathrm{Con}(T)$.
So, still inside $T + \mathrm{Con}(T)$, we conclude $\mathrm{Prov}_T(\ulcorner \pi \urcorner) \to \pi$.
The typical use is to replace the whole $\Pi_1$ reflection schema by the single sentence $\mathrm{Con}(T)$.
Watch out: the same argument for a $\Sigma_1$ sentence breaks at the use of $\Sigma_1$-completeness, because the negation is then $\Pi_1$.
