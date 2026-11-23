---
tag: 81ZNY1XKYJ
kind: statement
role: theorem
name: Completeness theorem for propositional logic
aliases: [completeness-of-propositional-logic, completeness-of-the-hilbert-system-l]
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
about: [1MGMQX43B8, 09K9MWD2QQ]
uses: [1MGMQX43B8, H31CS3HK5P, 1HK0VYWTV7, 05006AJ7DZ, VM8TQ70CVJ, QN7M1JCGT9, XD629S54CS, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Completeness_(logic)
    locator: Semantic completeness
  - url: https://en.wikipedia.org/wiki/Paul_Bernays
    locator: Mathematical work
  - url: https://en.wikipedia.org/wiki/Emil_Leon_Post
    locator: Early work
  - book: isbn:9781482237726
    locator: Chapter 1
history:
  first_stated: "1918, Paul Bernays (habilitation thesis)"
  notes: "Emil Post proved the completeness of the propositional calculus of Principia Mathematica independently, in his 1920 Columbia thesis, published in 1921."
---

## Statement

Every formula that is true under all truth assignments has a derivation in L, so truth tables and derivations pick out the same formulas.

Let $P$ be a set of propositional variables, and let $L$ be the [[Hilbert system|1MGMQX43B8]] with the axiom schemas A1, A2, A3 and the rule modus ponens.
Write $\Gamma \vdash \varphi$ when $\varphi$ has a derivation in $L$ from $\Gamma$.
Write $\Gamma \models \varphi$ for [[logical consequence|1HK0VYWTV7]]: every [[truth assignment|H31CS3HK5P]] that makes all members of $\Gamma$ true makes $\varphi$ true.

1. Weak form: for every formula $\varphi$, if $\models \varphi$, that is, if $\varphi$ is a [[tautology|05006AJ7DZ]], then $\vdash \varphi$.
2. Strong form: for every set of formulas $\Gamma$ and every formula $\varphi$, if $\Gamma \models \varphi$, then $\Gamma \vdash \varphi$.
3. With the [[soundness theorem|XD629S54CS]]: $\Gamma \vdash \varphi$ if and only if $\Gamma \models \varphi$.
4. Decidability: there is an algorithm that decides, for a formula $\varphi$, whether $\vdash \varphi$.
   It computes the [[truth table|05RSK4Q657]] of $\varphi$ and checks that every row gives $1$.

## Remarks

### Two proofs

[[Kalmár's proof|KD3Q8XH8A3]] gives the weak form, and the strong form for finite $\Gamma$, by turning each row of a truth table into a derivation.
[[The proof by maximal consistent sets|GNPVCQC55C]] gives the strong form, by building a truth assignment from a consistent set.

### Why each hypothesis is needed

The theorem needs all three axiom schemas.
Without A3, the tautology $\neg \neg p_0 \to p_0$ has no derivation.
To see this, read $\neg x$ as the constant $1$: then A1 and A2 are always true and MP keeps truth, but $\neg \neg p_0 \to p_0$ is false when $v(p_0) = 0$.

The weak form is not enough for an infinite $\Gamma$, since there is no formula "$\Gamma \to \varphi$".
For a finite $\Gamma = \{ \gamma_1, \dots, \gamma_n \}$, the weak form applied to $\gamma_1 \to (\gamma_2 \to \cdots \to (\gamma_n \to \varphi))$ gives the strong form.
For an infinite $\Gamma$, the proof needs either the [[compactness theorem|4X9126SEMM]] or the construction of a maximal consistent set.

For an uncountable set $P$, that construction uses [[Zorn's lemma|04RXTQA5ZA]].
In ZF without choice, the strong form for an arbitrary $P$ is equivalent to the compactness theorem, and so to the [[Boolean prime ideal theorem|STPBXBKSZP]].
The weak form and the countable case need no choice.

### What it gives you

A set of formulas is [[consistent|VM8TQ70CVJ]] if and only if it is [[satisfiable|QN7M1JCGT9]]: soundness gives one direction, and the strong form gives the other.
Every tautology has a derivation; for example, $\vdash (p_0 \to p_1) \to (\neg p_1 \to \neg p_0)$, because its four-row truth table has only the value $1$.
The set of theorems of $L$ is decidable by part 4, and the truth table of a formula with $k$ variables has $2^k$ rows.

The strong form and soundness give the compactness theorem.
Suppose every finite subset of $\Gamma$ is satisfiable but $\Gamma$ is not.
Then $\Gamma \models \neg (p_0 \to p_0)$, so $\Gamma \vdash \neg (p_0 \to p_0)$.
The derivation uses only a finite $\Gamma_0 \subseteq \Gamma$, and soundness gives $\Gamma_0 \models \neg (p_0 \to p_0)$, so $\Gamma_0$ has no model, a contradiction.

### Post completeness

$L$ is [[complete in the sense of Post|WK2P0E82B4]]: adding any non-tautology $\varphi$ as a new axiom schema makes $L$ inconsistent.
Take $v$ with $v(\varphi) = 0$.
Replace each variable $p$ of $\varphi$ by $p_0 \to p_0$ when $v(p) = 1$, and by $\neg (p_0 \to p_0)$ when $v(p) = 0$.
The resulting instance $\varphi'$ is false under every assignment, so $\neg \varphi'$ is a tautology and $\vdash \neg \varphi'$ by the weak form.
The new schema gives $\vdash \varphi'$, so the extended system derives a formula and its negation.

### The converse

The converse of the strong form is the soundness theorem: if $\Gamma \vdash \varphi$, then $\Gamma \models \varphi$.
It is true, and its proof is a short induction on derivations.

### Generalizations

[[Gödel's completeness theorem|WQ1ZE255SF]] is the same statement for first-order logic, and its proof by [[model existence|G0DTR159RN]] extends the second proof, with witnesses for the existential formulas.
Other proof systems for propositional logic are complete too, for example [[natural deduction|6KT3BJZ7D1]] and the sequent calculus.
[[Resolution|ZDW6N1PGJ7]] is refutation complete: a set of clauses is unsatisfiable exactly when resolution derives the empty clause; see [[soundness and completeness of resolution|DH1P95R390]].
[[Intuitionistic logic|Q11N8X99FK]] is complete for Kripke models and for Heyting algebras, but not for the two-valued truth tables.

## History

Paul Bernays gave the first known proof of the completeness of propositional logic, in his habilitation thesis of 1918 under David Hilbert.
Emil Post proved it independently in his doctoral thesis at Columbia University, published in 1921, for the propositional calculus of Principia Mathematica.
The proof by maximal consistent sets follows the method that Leon Henkin used for first-order logic.

## Explanations

### L1 human

There are two ways to show that a formula is always true.
The first way is to fill in its truth table and check every row.
The second way is to write a proof with fixed axioms and the rule "from $A$ and if $A$ then $B$, get $B$".
The completeness theorem says that the second way can prove every formula that passes the first test.
For example, "if $p$ then $p$" is true in both rows of its truth table, so it has a proof from the axioms.
Together with soundness, the two ways give exactly the same formulas.

### L2 human

We decide whether $\vdash (\neg p \to p) \to p$ in $L$.
The formula has one variable $p$, so its truth table has two rows.
In the row $v(p) = 1$ the consequent $p$ is true, so the whole implication has the value $1$.
In the row $v(p) = 0$ we get
$$v(\neg p) = 1, \qquad v(\neg p \to p) = 1 \to 0 = 0, \qquad v((\neg p \to p) \to p) = 0 \to 0 = 1.$$
Both rows give $1$, so the formula is a tautology, and the weak form gives $\vdash (\neg p \to p) \to p$.

The typical use is this one: a truth table, which is mechanical, proves that a derivation exists.
Kalmár's proof even turns the truth table into a derivation.
Watch out: do not expect a short derivation, since the derivation from Kalmár's proof grows with the $2^k$ rows of the table.

### L3 human

The second proof has an algebraic form.
The formulas modulo provable equivalence form the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]], a Boolean algebra.
A maximal consistent set is an ultrafilter of this algebra, and a truth assignment is a homomorphism onto $\{ 0, 1 \}$.
So completeness is the statement that the Boolean algebra has enough ultrafilters, which is a case of the Stone representation theorem.

Gödel's completeness theorem for first-order logic and the completeness of modal and intuitionistic logics for their Kripke models use the same plan: build a canonical model from maximal consistent sets.
The length of derivations is the subject of [[proof complexity|1Q046J0AW2]].
Some propositional proof system has derivations of polynomial size for all tautologies if and only if NP equals coNP.
