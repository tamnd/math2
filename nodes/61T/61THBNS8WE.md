---
tag: 61THBNS8WE
kind: definition
name: Provability logic
msc: ["03F45", "03B45"]
topics: [3E7M66WW6Q]
audience: research
defines: WJK0YA4GP2
uses: [C3RZY20ETK, G989VP2NGP, HACXBCM7SS, NB2BCZR40F, MFJXPAF0R0]
sources:
  - url: https://en.wikipedia.org/wiki/Provability_logic
    locator: lead section
---

## Definition

The provability logic of a theory is the set of modal formulas that the theory proves under every reading of $\square$ as its own provability predicate.

1. Modal formulas are built from propositional variables and $\bot$ with $\to$ and $\square$.
   The other connectives and $\lozenge \varphi := \neg \square \neg \varphi$ are abbreviations.
2. The logic $\mathsf{GL}$ is the smallest set of modal formulas that contains all tautologies, the axiom K and Löb's axiom.
   It is closed under modus ponens, the [[necessitation rule|G989VP2NGP]] and uniform substitution.
   The two modal axioms are K, $\square(p \to q) \to (\square p \to \square q)$, and L, $\square(\square p \to p) \to \square p$.
3. Let $T$ be a theory that contains [[Peano arithmetic|HACXBCM7SS]], with a decidable set of axioms and standard [[provability predicate|NB2BCZR40F]] $\mathrm{Prov}_T$.
   An arithmetical realization $*$ maps each propositional variable to a sentence of arithmetic.
   It extends to all formulas by $\bot^* = (0 = S0)$, $(\varphi \to \psi)^* = (\varphi^* \to \psi^*)$ and $(\square \varphi)^* = \mathrm{Prov}_T(\ulcorner \varphi^* \urcorner)$.
   Here $\ulcorner \cdot \urcorner$ is a [[Gödel numbering|MFJXPAF0R0]].
4. The provability logic of $T$ is the following set:
   $$\mathrm{PL}(T) = \{ \varphi : T \vdash \varphi^* \text{ for every realization } * \}.$$

## Notation

We write $\mathrm{PL}(T)$ or $\mathsf{PL}_T$ for the provability logic of $T$, and $*$ for a realization.
Some books call $\mathsf{GL}$ by the names $\mathsf{L}$, $\mathsf{G}$ or $\mathsf{K4W}$.

## Remarks

Each clause of the realization has a job.
The clause for $\bot$ fixes a false sentence, so that $\neg \square \bot$ becomes the consistency statement.
The clause for $\to$ makes the realization commute with the propositional connectives, so every tautology goes to a tautology.
The clause for $\square$ is the only place where arithmetic enters, and it must use the standard predicate of $T$ itself.
The quantifier "for every realization" is what makes $\mathrm{PL}(T)$ a logic: it is closed under uniform substitution, because a substitution instance of $\varphi$ realized by $*$ is $\varphi$ realized by another realization.

A small example: $\square p \to \square\square p$ is in $\mathsf{GL}$, by the derivation from [[Löb's axiom|QQ6PZFGGB3]].
Its realizations are instances of the third derivability condition: if $\sigma$ is provable, then it is provable that $\sigma$ is provable.
A formula that fails is $\square p \to p$.
Under the realization with $p^* = (0 = S0)$, it becomes the consistency statement of $\mathsf{PA}$, which $\mathsf{PA}$ does not prove by Gödel's second incompleteness theorem.

The main theorem about the definition is Solovay's theorem of 1976, $\mathrm{PL}(\mathsf{PA}) = \mathsf{GL}$, given in [[Solovay's arithmetical completeness theorem|1ZRWVDYPX0]].
On Kripke frames, $\mathsf{GL}$ is the logic of the finite transitive irreflexive frames, by the [[Kripke completeness of GL|1DMFNR7FZT]].
The [[concept page|WJK0YA4GP2]] tells the story of the subject, and the name "provability logic" also covers related systems for other theories and other notions of provability.

## Explanations

### L1 human

The system $\mathsf{GL}$ is named after Gödel and Löb.
Its one extra axiom is the modal form of [[Löb's theorem|3HD30YG3DG]].
It captures every general law of provability that Peano arithmetic can prove about itself.
For example, it contains "if $p$ is provable, then it is provable that $p$ is provable".

### L2 human

Take the formula $\square \bot \to \bot$ and ask whether it is in $\mathrm{PL}(\mathsf{PA})$.
Under every realization it becomes the following sentence:
$$\mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner) \to 0 = S0.$$
This sentence is equivalent in $\mathsf{PA}$ to $\mathrm{Con}(\mathsf{PA})$.
$\mathsf{PA}$ does not prove $\mathrm{Con}(\mathsf{PA})$, so $\square \bot \to \bot$ is not in $\mathrm{PL}(\mathsf{PA})$.
Watch out: the sentence is true in $\mathbb{N}$, so the formula is true under every realization.
$\mathrm{PL}(T)$ asks for provability in $T$ of every realization, not for truth.
