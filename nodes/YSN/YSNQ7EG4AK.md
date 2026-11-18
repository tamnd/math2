---
tag: YSNQ7EG4AK
kind: proof
name: Proof of the realization theorem for S4
msc: ["03B45", "03F45"]
topics: [CQM9SRN8PM]
audience: research
proves: BP022FTWCP
uses: [5HKWCXEFG1, N60RVXSA5W, W72CA3R9MP, 6X2ABCND9X]
methods: [0ASJVEFA9J, 12MQ2NJ29A]
sources:
  - book: isbn:9781108424912
    locator: "Artemov and Fitting, Justification Logic: Reasoning with Reasons"
  - url: https://en.wikipedia.org/wiki/Sergei_N._Artemov
    locator: Research
---

## Proof

We prove both parts of [[the realization theorem|BP022FTWCP]].
Part 1 is proved in full; part 2 is proved by an induction whose last step cites Artemov's substitution argument.

Part 1: projection.

1. We use induction on a derivation of $\varphi$ in $\mathsf{LP}$ and show $\mathsf{S4} \vdash \varphi^\circ$ at each step.
2. A propositional axiom projects to a propositional tautology, an $\mathsf{S4}$ theorem.
3. The application axiom projects to $\square(\varphi \to \psi) \to (\square\varphi \to \square\psi)$, the axiom $\mathrm{K}$.
4. The sum axioms project to $\square\varphi \to \square\varphi$, a tautology.
5. The axiom $t{:}\varphi \to \varphi$ projects to $\square\varphi \to \varphi$, the axiom $\mathrm{T}$.
6. The axiom $t{:}\varphi \to {!t}{:}(t{:}\varphi)$ projects to $\square\varphi \to \square\square\varphi$, the axiom $\mathrm{4}$.
7. Axiom necessitation gives $c{:}A$ with $A$ an axiom. By steps 2 to 6, $\mathsf{S4} \vdash A^\circ$, and necessitation gives $\mathsf{S4} \vdash \square A^\circ$.
8. Modus ponens commutes with projection, since $(\varphi \to \psi)^\circ = \varphi^\circ \to \psi^\circ$.

Part 2: realization.

9. We use the lifting lemma of [[internalization|6X2ABCND9X]]: if $\vec{x}{:}\vec{B} \vdash_{\mathsf{LP}} F$, then $\vec{x}{:}\vec{B} \vdash_{\mathsf{LP}} t{:}F$ for a term $t(\vec{x})$.
10. The lemma is proved by induction on the derivation of $F$. An axiom $F$ gets a constant $c$, and a hypothesis $x_i{:}B_i$ gets ${!x_i}$ by the checker axiom.
11. Modus ponens from $s{:}(G \to F)$ and $u{:}G$ gives $(s \cdot u){:}F$ by the application axiom. A formula $c{:}A$ from axiom necessitation gets ${!c}$.
12. Let $\mathsf{S4} \vdash A$. By cut elimination for the [[sequent calculus|W72CA3R9MP]] of $\mathsf{S4}$, the sequent $\Rightarrow A$ has a cut-free derivation $D$.
13. Every formula in $D$ is a subformula of $A$, by the subformula property of cut-free derivations.
14. Each occurrence of $\square$ in $D$ is linked to the matching occurrence in the conclusion of each rule. The classes of linked occurrences are families, and each family has one polarity.
15. Each negative family gets a fresh proof variable. Each positive family gets a fresh provisional variable $u_i$.
16. By induction on $D$, from the leaves down, we build for each sequent $\Gamma \Rightarrow \Delta$ a derivation $\mathsf{LP} \vdash \bigwedge\Gamma^r \to \bigvee\Delta^r$.
17. Axioms and propositional rules go through, since $\mathsf{LP}$ contains classical propositional logic.
18. The left box rule passes from $\Gamma, B \Rightarrow \Delta$ to $\Gamma, \square B \Rightarrow \Delta$. The box gets the variable $s$ of its family, and $s{:}B^r \to B^r$ is an axiom.
19. The right box rule passes from $\square\Gamma \Rightarrow B$ to $\square\Gamma \Rightarrow \square B$. The induction hypothesis gives $\vec{x}{:}\vec{\Gamma}^r \vdash B^r$.
20. Step 9 gives a term $t_{i,k}$ with $\vec{x}{:}\vec{\Gamma}^r \vdash t_{i,k}{:}B^r$. Here $k$ counts the right box rules of family $i$.
21. Put $s_i := t_{i,1} + \dots + t_{i,n_i}$. The sum axioms give $t_{i,k}{:}B^r \to s_i{:}B^r$ for each $k$.
22. We substitute $s_i$ for $u_i$, one family at a time. $\mathsf{LP}$ is closed under substitution of terms for proof variables.
23. A term $t_{i,k}$ can contain other provisional variables. Artemov's substitution lemma shows that the substitutions can be ordered so that every step stays derivable; we cite this lemma.
24. After all substitutions, the last sequent gives $\mathsf{LP} \vdash A^r$.
25. Negative families got distinct variables in step 15 and are never substituted. So $r$ is a normal realization, which proves part 2.

## Idea

Part 1 is a check that each axiom of $\mathsf{LP}$ projects to an axiom of $\mathsf{S4}$.
Part 2 reads a cut-free $\mathsf{S4}$ proof as a recipe for building proofs.
Each right box rule says "from proofs of the hypotheses, build a proof of the conclusion", and the lifting lemma gives the term.
A positive box introduced several times collects all its terms with $+$.

## Variants

1. Fitting's semantic proof builds a canonical Fitting model for $\mathsf{LP}$ and shows that every $\mathsf{S4}$ theorem has a realization by an argument on the modal canonical model. It gives no explicit terms but works for many logics.
2. Proofs through nested sequents and hypersequents extend the method to $\mathsf{S5}$ and to other logics with cut-free calculi.
