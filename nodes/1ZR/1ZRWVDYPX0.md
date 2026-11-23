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

The modal logic $\mathsf{GL}$ proves exactly the laws of provability that $\mathsf{PA}$ proves about itself, and the logic $\mathsf{GLS}$ proves exactly the laws that are true.

We use the realizations $*$ of the [[definition of provability logic|61THBNS8WE]] for $T = \mathsf{PA}$, so $(\square \varphi)^* = \mathrm{Prov}_{\mathsf{PA}}(\ulcorner \varphi^* \urcorner)$.
Let $\mathsf{GLS}$ be the smallest set of modal formulas that contains every theorem of $\mathsf{GL}$ and every formula $\square \psi \to \psi$, and that is closed under modus ponens.
It is not closed under necessitation.
Let $\mathrm{Sub}(\varphi)$ be the set of subformulas of $\varphi$.

1. Arithmetical completeness.
   For every modal formula $\varphi$, $\mathsf{GL} \vdash \varphi$ if and only if $\mathsf{PA} \vdash \varphi^*$ for every realization $*$.
   In other words, $\mathrm{PL}(\mathsf{PA}) = \mathsf{GL}$.
2. Truth.
   For every modal formula $\varphi$, the following are equivalent.
   1. $\mathsf{GLS} \vdash \varphi$.
   2. $\mathsf{GL} \vdash \bigwedge \{ \square \psi \to \psi : \square \psi \in \mathrm{Sub}(\varphi) \} \to \varphi$.
   3. $\mathbb{N} \models \varphi^*$ for every realization $*$.
3. Part 1 holds with $\mathsf{PA}$ replaced by any theory $T$ in the language of arithmetic that contains $\mathsf{PA}$, has a decidable set of axioms, and is $\Sigma_1$-sound.
   Here $\Sigma_1$-sound means that every $\Sigma_1$ sentence provable in $T$ is true in $\mathbb{N}$.

The proof is in [[the proof of Solovay's theorem|PRK1NYS962]].
It uses the [[Kripke completeness of GL|1DMFNR7FZT]], the [[diagonal lemma|3PRW76471J]], and one lemma on the formalization of a finite computation in $\mathsf{PA}$, which it cites without proof.

## Remarks

### A first use

Does $\mathsf{PA}$ prove that if it is consistent, then it does not prove its own inconsistency?
In symbols, the question is whether $\mathsf{PA} \vdash \mathrm{Con}(\mathsf{PA}) \to \neg \mathrm{Prov}_{\mathsf{PA}}(\ulcorner \neg \mathrm{Con}(\mathsf{PA}) \urcorner)$.
The modal form is $\varphi = \neg \square \bot \to \neg \square \square \bot$, since $\mathrm{Con}(\mathsf{PA})$ is $\neg \square \bot$ under every realization.
Take worlds $1$ and $2$ with $1 R 2$ only.
World $2$ has no successors, so $2 \models \square \bot$, and then $1 \models \square \square \bot$ while $1 \not\models \square \bot$.
So $\varphi$ fails at $1$, and $\mathsf{GL} \nvdash \varphi$.
By part 1, some realization $*$ has $\mathsf{PA} \nvdash \varphi^*$, and since $\varphi$ has no variables, $\varphi^*$ is the sentence of the question.
The answer is no.

### Why each hypothesis is needed

$\Sigma_1$-soundness is needed in part 3.
The theory $T = \mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$ is consistent, by Gödel's second incompleteness theorem.
It proves $\mathrm{Prov}_T(\ulcorner 0 = S0 \urcorner)$, since it proves that $\mathsf{PA}$, a part of $T$, is inconsistent.
So $\square \bot \in \mathrm{PL}(T)$, but $\mathsf{GL} \nvdash \square \bot$.

The standard provability predicate is needed.
With the [[Rosser provability predicate|Z0H1KA8ZHT]] in place of $\mathrm{Prov}_{\mathsf{PA}}$, $\mathsf{PA}$ proves the realization of $\neg \square \bot$, which is not a theorem of $\mathsf{GL}$.
A decidable set of axioms makes $\mathrm{Prov}_T$ a $\Sigma_1$ formula, and that gives the [[derivability conditions|F6H4STF9RG]] and the formalized $\Sigma_1$-completeness used in the proof.

### Watch out

$\mathsf{GLS}$ is not closed under necessitation, and it must not be.
$\mathsf{GLS} \vdash \neg \square \bot$, but $\square \neg \square \bot$ realizes as "$\mathsf{PA}$ proves its own consistency", which is false.
In the same way, part 1 is about provability in $\mathsf{PA}$, so a formula such as $\neg \square \bot$ has true realizations that are not provable.

### What it gives you

$\mathrm{PL}(\mathsf{PA})$ and the set of modal formulas true under every realization are decidable, since $\mathsf{GL}$ is decidable by the [[Kripke completeness of GL|1DMFNR7FZT]].
Every scheme about provability that is not a theorem of $\mathsf{GL}$ has a counterexample in $\mathsf{PA}$, as the first use above shows.

The truth part gives the first incompleteness theorem in modal form.
Take the frame with a root $0$ that sees two worlds $1$ and $2$, with $p$ true at $1$ only.
At $0$, both $\square p$ and $\square \neg p$ fail, so $\square p \to p$ and $\square \neg p \to \neg p$ hold and $\square p \vee \square \neg p$ fails.
So $\mathsf{GLS} \nvdash \square p \vee \square \neg p$ by part 2, and some sentence $\sigma$ has neither $\sigma$ nor $\neg \sigma$ provable.

### The converse

The direction from $\mathsf{GL} \vdash \varphi$ to $\mathsf{PA} \vdash \varphi^*$ is arithmetical soundness.
It uses only the derivability conditions and the formalized [[Löb's theorem|3HD30YG3DG]].
The other direction is the completeness, and it needs the construction of the proof.

### Generalizations

Part 3 covers theories such as $\mathsf{ZF}$ through their interpretation of arithmetic, when they are $\Sigma_1$-sound.
The proof of part 2 works for every $T$ as in part 3 whose theorems are all true in $\mathbb{N}$.
For several provability operators, [[Japaridze's polymodal logic GLP|3EDRQJJHMT]] has an arithmetical completeness theorem of the same kind.
For first-order modal formulas the analogue fails, since the [[quantified provability logic|5K9J8R8SCP]] of $\mathsf{PA}$ is not recursively axiomatizable.

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

We decide whether $\mathsf{PA}$ proves every instance of $\square(\square p \to p) \vee \square \neg p$.
To refute the first disjunct at a world, we need a successor where $\square p$ is true and $p$ is false.
A world $v$ with no successors and $p$ false does this, since every boxed formula is true at $v$.
To refute the second disjunct, we need a successor where $p$ is true, so add a world $w$ with no successors and $p$ true.
Take a root $0$ with $0 R v$ and $0 R w$ only.
Check: at $0$, the formula $\square p \to p$ fails at $v$ and $\neg p$ fails at $w$, so both disjuncts fail at $0$.
The frame is finite, transitive and irreflexive, so $\mathsf{GL}$ does not prove the formula.
By part 1, some instance is not provable in $\mathsf{PA}$.
This is the typical use: search for a finite countermodel, and Solovay's theorem turns it into a failure in arithmetic.

### L3 human

Soundness is the easy half, and completeness is the deep half.
Solovay's proof embeds a finite Kripke countermodel into arithmetic.
A self-referential computable function walks along the frame, and the sentence "the walk ends at world $i$" plays the role of world $i$.
The proof uses only the [[derivability conditions|F6H4STF9RG]], provable [[Σ1-completeness|69234Z1V00]] and the [[diagonal lemma|3PRW76471J]], so it works for all $\Sigma_1$-sound theories with these properties.
Combined with the translation of [[Grzegorczyk logic|2Q8E4GQF3B]] into $\mathsf{GL}$, it gives an arithmetical completeness theorem for the reading "true and provable".
A refinement of the method gives one for [[GLP|3EDRQJJHMT]].
