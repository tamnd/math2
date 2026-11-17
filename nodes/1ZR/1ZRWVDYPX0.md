---
tag: 1ZRWVDYPX0
kind: statement
role: theorem
name: Solovay's arithmetical completeness theorem
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
uses: [61THBNS8WE, WJK0YA4GP2, QQ6PZFGGB3, 1DMFNR7FZT, HACXBCM7SS, NB2BCZR40F, F6H4STF9RG, 3HD30YG3DG, 3PRW76471J, 69234Z1V00, 4NBAX3VRQ7, Z0H1KA8ZHT]
about: [WJK0YA4GP2, HACXBCM7SS]
proofs: [PRK1NYS962]
history:
  first_stated: "Solovay, 1976, Provability interpretations of modal logic, Israel Journal of Mathematics 25"
  notes: "Arithmetical completeness of GL for PA, and of GLS for truth in the standard model."
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: History
  - book: isbn:9780521701464
---

## Statement

We use the realizations $*$ of the [[definition of provability logic|61THBNS8WE]] for $T = \mathsf{PA}$, so $(\square \varphi)^* = \mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi^* \urcorner)$.
Let $\mathsf{GLS}$ be the smallest set of modal formulas that contains every theorem of $\mathsf{GL}$ and every formula $\square \psi \to \psi$, and that is closed under modus ponens.
It is not closed under necessitation.

1. Arithmetical completeness. For every modal formula $\varphi$, $\mathsf{GL} \vdash \varphi$ if and only if $\mathsf{PA} \vdash \varphi^*$ for every realization $*$. In other words, $\mathrm{PL}(\mathsf{PA}) = \mathsf{GL}$.
2. Truth. For every modal formula $\varphi$, the following are equivalent.
   1. $\mathsf{GLS} \vdash \varphi$.
   2. $\mathsf{GL} \vdash \bigwedge \set{\square \psi \to \psi : \square \psi \in \mathrm{Sub}(\varphi)} \to \varphi$, where $\mathrm{Sub}(\varphi)$ is the set of subformulas of $\varphi$.
   3. $\N \models \varphi^*$ for every realization $*$.
3. Part 1 holds with $\mathsf{PA}$ replaced by any theory $T$ in the language of arithmetic that contains $\mathsf{PA}$, has a decidable set of axioms, and is $\Sigma_1$-sound, that is, every $\Sigma_1$ sentence provable in $T$ is true in $\N$.

The proof is in [[the proof of Solovay's theorem|PRK1NYS962]].
It uses the [[Kripke completeness of GL|1DMFNR7FZT]], the [[diagonal lemma|3PRW76471J]], and one lemma on the formalization of a finite computation in $\mathsf{PA}$, which it cites without proof.

## Remarks

### Why each hypothesis is needed

1. $\Sigma_1$-soundness in part 3. The theory $T = \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent, by Gödel's second incompleteness theorem, and it proves $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, since it proves that $\mathsf{PA}$, a part of $T$, is inconsistent. So $\square \bot \in \mathrm{PL}(T)$, but $\mathsf{GL} \nvdash \square \bot$.
2. The standard provability predicate. With the [[Rosser provability predicate|Z0H1KA8ZHT]] in place of $\mathrm{Prov}_{\mathsf{PA}}$, $\mathsf{PA}$ proves the realization of $\neg \square \bot$, which is not a theorem of $\mathsf{GL}$.
3. A decidable set of axioms. It makes $\mathrm{Prov}_T$ a $\Sigma_1$ formula, which gives the [[derivability conditions|F6H4STF9RG]] and the formalized $\Sigma_1$-completeness used in the proof.
4. No necessitation in $\mathsf{GLS}$. $\mathsf{GLS} \vdash \neg \square \bot$, but $\square \neg \square \bot$ realizes as "$\mathsf{PA}$ proves its own consistency", which is false.

### Consequences

1. $\mathrm{PL}(\mathsf{PA})$ and the set of modal formulas true under every realization are decidable, since $\mathsf{GL}$ is decidable by the [[Kripke completeness of GL|1DMFNR7FZT]].
2. Every scheme about provability that is not a theorem of $\mathsf{GL}$ has a counterexample in $\mathsf{PA}$. For instance, $\mathsf{GL} \nvdash \square \square \bot \to \square \bot$, so $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA}) \to \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner \neg \mathrm{Con}(\mathsf{PA}) \urcorner)$.
3. $\mathsf{GLS} \nvdash \square p \vee \square \neg p$. So for some sentence $\sigma$, neither $\sigma$ nor $\neg \sigma$ is provable, which is the first incompleteness theorem in modal form.

### Converse

The direction from $\mathsf{GL} \vdash \varphi$ to $\mathsf{PA} \vdash \varphi^*$ is arithmetical soundness.
It uses only the derivability conditions and the formalized [[Löb's theorem|3HD30YG3DG]].
The other direction is the completeness, and it needs the construction of the proof.

### Generalizations

1. Part 3 covers theories such as $\mathsf{ZF}$ through their interpretation of arithmetic, when they are $\Sigma_1$-sound.
2. The proof of part 2 works for every $T$ as in part 3 whose theorems are all true in $\N$.
3. For several provability operators, [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] has an arithmetical completeness theorem of the same kind.
4. For first-order modal formulas the analogue fails; the [[quantified provability logic|5K9J8R8SCP]] of $\mathsf{PA}$ is not recursively axiomatizable.

## History

Robert Solovay proved the theorem in "Provability interpretations of modal logic", Israel Journal of Mathematics 25 (1976).
It answered the question of which modal laws $\mathsf{PA}$ proves about its own provability predicate.

## Explanations

### L1 human

Write $\square p$ for "$p$ can be proved in Peano arithmetic".
Solovay's theorem says that the modal system $\mathsf{GL}$ lists all the general laws of $\square$ that Peano arithmetic itself can prove.
If a law is missing from $\mathsf{GL}$, then some choice of arithmetic sentences makes it unprovable.
A second part lists the general laws that are true, which is a larger set, since "if $p$ is provable, then $p$" is true but not provable.

### L2 human

We show that $\mathsf{PA} \nvdash \mathrm{Con}(\mathsf{PA}) \to \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner \neg \mathrm{Con}(\mathsf{PA}) \urcorner)$.

1. The modal form is $\varphi = \neg \square \bot \to \neg \square \square \bot$, since $\mathrm{Con}(\mathsf{PA})$ is $\neg \square \bot$ under every realization.
2. Take worlds $1$, $2$ with $1 R 2$ only. At $2$ there are no successors, so $2 \models \square \bot$. At $1$, $\square \bot$ fails, since $1$ sees $2$, and $\square \square \bot$ holds.
3. So $\varphi$ fails at $1$, and $\mathsf{GL} \nvdash \varphi$.
4. By part 1, some realization $*$ has $\mathsf{PA} \nvdash \varphi^*$. The formula has no variables, so $\varphi^*$ is the sentence above.

The typical use: refute a scheme about provability on a finite frame, then apply part 1.
A trap: part 1 is about provability in $\mathsf{PA}$; a formula such as $\neg \square \bot$ has a true realization that is not provable.

### L3 human

Soundness is easy; completeness is the deep half.
Solovay's proof embeds a finite Kripke countermodel into arithmetic: a self-referential computable function walks along the frame, and the sentence "the walk ends at world $i$" plays the role of world $i$.
The proof uses only the [[derivability conditions|F6H4STF9RG]], provable [[Σ1-completeness|69234Z1V00]] and the [[diagonal lemma|3PRW76471J]], so it works for all $\Sigma_1$-sound theories with these properties.
Combined with the translation of [[Grzegorczyk logic|2Q8E4GQF3B]] into $\mathsf{GL}$, it gives an arithmetical completeness theorem for the reading "true and provable", and a refinement of the method gives one for [[GLP|3EDRQJJHMT]].
