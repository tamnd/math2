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

1. Modal formulas are built from propositional variables and $\bot$ with $\to$ and $\square$. The other connectives and $\lozenge \varphi := \neg \square \neg \varphi$ are abbreviations.
2. The logic $\mathsf{GL}$ is the smallest set of modal formulas that contains all tautologies, the axiom $\square(p \to q) \to (\square p \to \square q)$ and Löb's axiom $\square(\square p \to p) \to \square p$, and that is closed under modus ponens, the [[necessitation rule|G989VP2NGP]] and uniform substitution.
3. Let $T$ be a theory that contains [[Peano arithmetic|HACXBCM7SS]], with a decidable set of axioms and standard [[provability predicate|NB2BCZR40F]] $\mathrm{Prov}_T$. An arithmetical realization $*$ maps each propositional variable to a sentence of arithmetic. It extends to all formulas by $\bot^* = (0 = S0)$, $(\varphi \to \psi)^* = (\varphi^* \to \psi^*)$ and $(\square \varphi)^* = \mathrm{Prov}_T(\ulcorner \varphi^* \urcorner)$, where $\ulcorner \cdot \urcorner$ is a [[Gödel numbering|MFJXPAF0R0]].
4. The provability logic of $T$ is $\mathrm{PL}(T) = \set{\varphi : T \vdash \varphi^* \text{ for every realization } *}$.

## Remarks

Solovay's theorem (1976) says that $\mathrm{PL}(\mathsf{PA}) = \mathsf{GL}$; see [[Solovay's arithmetical completeness theorem|1ZRWVDYPX0]].

Example: $\square p \to \square\square p$ is in $\mathsf{GL}$, by part 1 of [[Löb's axiom in provability logic|QQ6PZFGGB3]].
Its realizations are instances of the third derivability condition: if $\sigma$ is provable, then it is provable that $\sigma$ is provable.

Non-example: $\square p \to p$ is not in $\mathsf{GL}$.
Under the realization with $p^* = (0 = S0)$, it becomes the consistency statement of $\mathsf{PA}$, which $\mathsf{PA}$ does not prove by Gödel's second incompleteness theorem.

On Kripke frames, $\mathsf{GL}$ is the logic of the finite transitive irreflexive frames; see the [[Kripke completeness of GL|1DMFNR7FZT]].
The name "provability logic" also covers related systems for other theories and other notions of provability.

## Explanations

### L1 human

The system $\mathsf{GL}$ is named after Gödel and Löb.
Its one extra axiom is the modal form of [[Löb's theorem|3HD30YG3DG]].
It captures every general law of provability that Peano arithmetic can prove about itself.
For example, it contains "if $p$ is provable, then it is provable that $p$ is provable".

### L2 human

1. Take the formula $\square \bot \to \bot$.
2. Under every realization it becomes $\mathrm{Prov}_{\mathsf{PA}}(\ulcorner 0 = S0 \urcorner) \to 0 = S0$, which is equivalent in $\mathsf{PA}$ to $\mathrm{Con}(\mathsf{PA})$.
3. $\mathsf{PA}$ does not prove $\mathrm{Con}(\mathsf{PA})$, so $\square \bot \to \bot$ is not in $\mathrm{PL}(\mathsf{PA})$.

A trap: $\mathrm{PL}(T)$ asks for provability in $T$ of every realization, not for truth; the formula of step 1 is true under every realization.
