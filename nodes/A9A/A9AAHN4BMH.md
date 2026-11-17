---
tag: A9AAHN4BMH
kind: statement
role: theorem
name: Equivalence of proof systems
aliases: [equivalence-of-proof-systems]
msc: ["03F03", "03B10"]
topics: [TTCRX3NFNY]
audience: ug2
about: [N95HV0VWSM, 6KT3BJZ7D1, W72CA3R9MP, WGWBBVE8GX]
uses: [2B00FE6K5W, PAQ4ZX2TX1, PZX9J3VEMT, WGWBBVE8GX, 1HK0VYWTV7, 4A84VHDTHV]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Deductive systems
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Relation to analytic tableaux
  - book: isbn:9780122384523
    locator: Section 2.4
---

## Statement

Let $L$ be a countable first-order language without equality, whose logical symbols are $\neg$, $\to$ and $\forall$.
Let $\Gamma$ be a set of sentences of $L$ and $\varphi$ a sentence of $L$.
Then the following five conditions are equivalent.

1. $\Gamma \vdash_{\mathsf{H}} \varphi$ in the [[Hilbert-style predicate calculus|2B00FE6K5W]], without the equality axioms.
2. $\Gamma \vdash_{\mathsf{ND}} \varphi$ in [[natural deduction|PAQ4ZX2TX1]] with the rules for $\to$, $\forall$ and $\bot$, RAA, and the rules for $\neg$ below.
3. $\Gamma \vdash_{\mathsf{LK}} \varphi$: some sequent $\Gamma_0 \Rightarrow \varphi$, with $\Gamma_0$ a finite list of members of $\Gamma$, has a derivation in the [[sequent calculus|PZX9J3VEMT]] LK.
4. $\Gamma \vdash_{\mathsf{T}} \varphi$: some [[semantic tableau|WGWBBVE8GX]] for $\Gamma \cup \{\neg \varphi\}$ is closed.
5. $\Gamma \models \varphi$: every model of $\Gamma$ is a model of $\varphi$, as on the page [[logical consequence|1HK0VYWTV7]].

In condition 2, the rule ${\neg}\mathrm{I}$ infers $\neg \psi$ from a derivation of $\bot$ from the assumption $[\psi]$, which it discharges, and ${\neg}\mathrm{E}$ infers $\bot$ from $\psi$ and $\neg \psi$.
These are the rules ${\to}\mathrm{I}$ and ${\to}\mathrm{E}$ for $\psi \to \bot$.
Every formula in a derivation is a formula of $L$ or the formula $\bot$.
The [[proof|27ZX7V7AB2]] goes around the cycle $2 \Rightarrow 1 \Rightarrow 5 \Rightarrow 4 \Rightarrow 3 \Rightarrow 2$.

## Remarks

### Why each hypothesis is needed

- The language is countable because the completeness of systematic tableaux lists the closed terms and the members of $\Gamma$. The theorem holds for every language, but the proof of $5 \Rightarrow 4$ then uses the axiom of choice, for example through Zorn's lemma.
- Equality is left out because the tableau rules and LK of these pages have no rules for $=$. With the equality axioms of each system, the theorem holds again; see [[rules for equality|Y90Z13AXY8]].
- $\Gamma$ and $\varphi$ are sentences because the systems read free variables in different ways. In $\mathsf{H}_G$, $\{P(x)\} \vdash \forall x\, P(x)$, but in $\mathsf{H}$ and in natural deduction this fails.
- The condition "some finite list $\Gamma_0$" in 3 is needed because a sequent is finite. For an infinite $\Gamma$, no sequent has all of $\Gamma$ on the left.

### Consequences

- Soundness and completeness hold for each of the four systems, because each is equivalent to $\Gamma \models \varphi$. So [[Gödel's completeness theorem|WQ1ZE255SF]] holds for the Hilbert-style calculus, natural deduction and LK at once.
- Every derivation in one system can be turned into a derivation in each other system. Four of the five arrows are explicit translations of proofs; only $5 \Rightarrow 4$ is a search.
- Compactness: if $\Gamma \models \varphi$, then $\Gamma_0 \models \varphi$ for a finite $\Gamma_0 \subseteq \Gamma$, because each derivation uses finitely many members of $\Gamma$.
- A different translation of tableaux into a one-sided form of LK uses no cut. With it, the cycle shows that LK without cut is complete for sequents of sentences. This is a semantic proof of the [[cut-elimination theorem|AYRZ98Y0NW]], with no bound on size.

### Converse

Each condition implies each other one, so the converse of every implication between two of them is part of the theorem.
For formulas with free variables the converse can fail between systems: $\{P(x)\} \vdash_{\mathsf{H}_G} \forall x\, P(x)$, but $\{P(x)\} \nvdash_{\mathsf{H}} \forall x\, P(x)$.

### Generalizations

- The cost of the translations differs. In propositional logic, Hilbert-style systems and natural deduction simulate each other with a polynomial increase in length (Cook and Reckhow).
- Cut-free LK and tableaux need much longer proofs for some sentences: eliminating cut can cause an increase in size that no tower of exponentials bounds (Statman, Orevkov).
- For [[intuitionistic logic|Q11N8X99FK]], natural deduction without RAA, LJ and an intuitionistic Hilbert-style calculus are again equivalent, with Kripke models in place of structures.
- With the equality symbol, the equivalence holds when each system gets its rules for equality.

## History

Gentzen proved in 1934 to 1935 that his natural deduction calculi, his sequent calculi and a Hilbert-style calculus derive the same formulas, for classical and for intuitionistic logic.
Beth and Hintikka introduced tableaux in 1955 and proved their completeness through models.

## Explanations

### L1 human

Logicians use several kinds of formal proof: long lists of lines, trees of assumptions, trees of claims, and searches for a counterexample.
The theorem says that all of them prove exactly the same things.
They also prove exactly the statements that are true in every situation where the assumptions are true.
For example, "if everybody likes cake, then Ann likes cake" can be proved in each system, and "if Ann likes cake, then everybody likes cake" in none.

### L2 human

We follow the sentence $\forall x\, P(x) \to P(c)$ around the cycle.

1. In $\mathsf{H}$ it is an axiom of group 2, so $\vdash_{\mathsf{H}} \forall x\, P(x) \to P(c)$.
2. By soundness it is valid.
3. The tableau for $\neg(\forall x\, P(x) \to P(c))$ adds $\forall x\, P(x)$ and $\neg P(c)$ by $\alpha$, then $P(c)$ by $\gamma$, and closes.
4. LK derives $P(c) \Rightarrow P(c)$, then $\forall x\, P(x) \Rightarrow P(c)$ by ${\forall}$L, then $\Rightarrow \forall x\, P(x) \to P(c)$ by ${\to}$R.
5. Natural deduction derives $P(c)$ from $[\forall x\, P(x)]^1$ by ${\forall}\mathrm{E}$ and then the implication by ${\to}\mathrm{I}^1$.

The typical use of the theorem is to choose the system that suits the task: natural deduction to write a proof, LK or tableaux to search for one, and $\mathsf{H}$ to prove facts about all proofs.
A trap is to compare systems on formulas with free variables, where the systems differ.

### L3 human

The theorem is a statement about one consequence relation with several presentations, in the same way that a group can have several presentations by generators and relations.
The semantic step $5 \Rightarrow 4$ is the hard part, and the syntactic translations are inductions on derivations; the translations between natural deduction and LK are the basis of the correspondence between normalization and cut elimination.
In proof complexity the systems are compared by the length of the shortest proofs, and there the systems are different: cut-free systems can need non-elementarily longer proofs than systems with cut.
For theories, the same equivalence holds with $\Gamma$ the set of axioms, so the choice of proof system does not change the theorems of a theory such as Peano arithmetic.
