---
tag: 6KT3BJZ7D1
kind: concept
name: Natural deduction
msc: ["03F03", "03B10", "03B05"]
topics: [TTCRX3NFNY]
audience: ug2
uses: [086QKPF0A6, HYJ10AF6RT, NCDZ969V7X, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: Gentzen-style inference rules
  - book: isbn:9781447145578
    locator: Chapter 3
same_as:
  wikidata: Q1572108
  wikipedia: Natural deduction
---

## Summary

Natural deduction is a proof system for [[first-order logic|086QKPF0A6]] in which a derivation is a finite tree of formulas.
The leaves of the tree are assumptions, and each inner node follows from the nodes directly above it by one rule.
Each connective and quantifier has introduction rules, which prove a formula with it, and elimination rules, which use such a formula.
Some rules (${\to}\mathrm{I}$, ${\vee}\mathrm{E}$, ${\exists}\mathrm{E}$ and the classical rule RAA) discharge assumptions.
The quantifier rules ${\forall}\mathrm{I}$ and ${\exists}\mathrm{E}$ carry an eigenvariable condition.
$\Gamma \vdash_{\mathsf{ND}} \varphi$ means that some derivation has root $\varphi$ and all its open assumptions in $\Gamma$.
The [[definition|PAQ4ZX2TX1]] lists the rules and their conditions.
The system matters because its derivations follow the structure of ordinary mathematical arguments, and it is the basis of normalization and of the [[Curry-Howard correspondence|A77FER1Q5H]].

## Motivation

In a [[Hilbert-style calculus|~4ea8b834]] almost all the work is done by axioms, and short arguments become long lists of axiom instances.
Mathematicians do not argue like this.
To prove "if $\varphi$ then $\psi$" they assume $\varphi$ for a while and derive $\psi$.
To prove "for all $x$" they argue about an arbitrary $x$, and to use "there is an $x$" they give the witness a name.
Natural deduction turns each of these habits into a rule.
Each logical symbol gets one rule that says how to prove it and one rule that says how to use it, so a reader can see which step uses which symbol.

## Notation

We write $[\varphi]^u$ for an assumption that a later step with label $u$ discharges, and $\Gamma \vdash_{\mathsf{ND}} \varphi$ for derivability.
Rules are named ${\to}\mathrm{I}$, ${\to}\mathrm{E}$, ${\forall}\mathrm{I}$ and so on; RAA is reductio ad absurdum, and ${\bot}\mathrm{E}$ is "ex falso".
Gentzen called the intuitionistic system NJ and the classical system NK.
There are three common layouts: Gentzen-Prawitz trees, [[Fitch-style natural deduction|~1528beb9]] with boxes, and the sequent-style form, which writes $\Gamma \vdash \varphi$ at each node.
Some books take $\neg$ as primitive, and others define $\neg \varphi$ as $\varphi \to \bot$, as we do.

## Remarks

### Examples

- [[A natural deduction derivation of a quantifier swap|~923aadff]]: $\vdash_{\mathsf{ND}} \exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$. It uses each quantifier rule once and no classical rule.
- [[A classical natural deduction derivation of a quantifier law|~0d459855]]: $\vdash_{\mathsf{ND}} \neg \forall x\, P(x) \to \exists x\, \neg P(x)$. It uses RAA twice, and no intuitionistic derivation exists.
- [[A formal derivation of the transitivity of implication|DNRZJKRDZC]]: $(P \to Q) \to ((Q \to R) \to (P \to R))$ with ${\to}\mathrm{I}$ and ${\to}\mathrm{E}$ only. It shows the propositional part.
- From $\forall x\, (P(x) \to Q(x))$ and $\forall x\, P(x)$: ${\forall}\mathrm{E}$ twice gives $P(y) \to Q(y)$ and $P(y)$, ${\to}\mathrm{E}$ gives $Q(y)$, and ${\forall}\mathrm{I}$ gives $\forall x\, Q(x)$. The step is correct because both open assumptions are sentences.
- Symmetry of equality: ${=}\mathrm{I}$ gives $s = s$, and ${=}\mathrm{E}$ with $\varphi = (x = s)$ turns $s = t$ and $s = s$ into $t = s$.

### Non-examples

- [[A wrong existential elimination in natural deduction|~b3ac11e8]]: a tree that ends with $\exists x\, P(x) \to \forall y\, P(y)$. The condition that fails: the conclusion of ${\exists}\mathrm{E}$ contains the eigenvariable.
- The tree $[P(y)]^1$, $\forall x\, P(x)$, $P(y) \to \forall x\, P(x)$. The condition that fails: ${\forall}\mathrm{I}$ is applied while $y$ is free in the open assumption $P(y)$.
- A tree that ends with $\varphi \to \psi$ by ${\to}\mathrm{I}$ but keeps $\varphi$ open elsewhere is a derivation, but it is a derivation from $\{\varphi\}$, not from the empty set. Only the leaves marked with the label of the step are discharged.

### Basic properties

- Soundness: if $\Gamma \vdash_{\mathsf{ND}} \varphi$, then $\Gamma \models \varphi$. The proof is an induction on derivations, and the eigenvariable conditions are used in the cases ${\forall}\mathrm{I}$ and ${\exists}\mathrm{E}$.
- Completeness: if $\Gamma \models \varphi$, then $\Gamma \vdash_{\mathsf{ND}} \varphi$. Natural deduction derives the same formulas as the Hilbert-style calculus, the sequent calculus and tableaux; see [[equivalence of proof systems|~c9d242a1]].
- The [[deduction theorem|8M9ZFDR4DH]] is built in: ${\to}\mathrm{I}$ is the rule $\Gamma \cup \{\varphi\} \vdash \psi \Rightarrow \Gamma \vdash \varphi \to \psi$, with no condition.
- Derived rules: a rule is derived when one fixed tree of basic rules gives it. Modus tollens (from $\varphi \to \psi$ and $\neg \psi$ infer $\neg \varphi$) and double negation elimination (from $\neg \neg \varphi$ infer $\varphi$, by RAA) are derived rules.
- Normalization: every derivation can be turned into a normal derivation, in which no introduction rule is directly followed by the elimination rule of the same symbol. Normal derivations have the subformula property.

### History

Gentzen introduced natural deduction in his paper "Investigations into logical deduction" of 1934 to 1935, together with the sequent calculus.
Jaśkowski published a system of suppositional proofs independently in 1934.
Prawitz proved the normalization theorem in his monograph *Natural Deduction* of 1965.
Fitch's book *Symbolic Logic* of 1952 popularized the layout with nested subproofs.

### Common errors

- To break the eigenvariable condition of ${\forall}\mathrm{I}$ or ${\exists}\mathrm{E}$. Both errors derive invalid formulas, as the non-examples show.
- To use a formula from inside a discharged part of the tree after the discharge. Each formula may use only the assumptions above it in the tree.
- To use RAA in a proof that must be intuitionistic. Many standard quantifier laws then fail, for example $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$.

## Explanations

### L1 human

Natural deduction is a set of rules for writing proofs the way people argue.
To prove "if it rains, the street is wet", we assume that it rains and show that the street is wet.
To prove "every square has four sides", we take an arbitrary square, about which we know nothing else, and show that it has four sides.
To use "some student failed", we give the student a name, Sam, and argue about Sam, but the final conclusion must not mention Sam.
A proof is drawn as a tree: the assumptions are at the top and the conclusion is at the bottom.

### L2 human

We derive $\forall x\, (P(x) \wedge Q(x)) \to \forall x\, P(x)$.

1. $[\forall x\, (P(x) \wedge Q(x))]^1$: assumption with label 1.
2. $P(y) \wedge Q(y)$: ${\forall}\mathrm{E}$ from line 1 with $t = y$.
3. $P(y)$: ${\wedge}\mathrm{E}$ from line 2.
4. $\forall x\, P(x)$: ${\forall}\mathrm{I}$ from line 3; $y$ is not free in assumption 1 or in $\forall x\, P(x)$.
5. $\forall x\, (P(x) \wedge Q(x)) \to \forall x\, P(x)$: ${\to}\mathrm{I}$, which discharges label 1.

The typical use is to formalize a short informal proof: each sentence of the informal proof becomes one or two rules, as on the page [[proof strategies by logical form|872K5XB580]].
A trap is to treat the eigenvariable $y$ as a fixed object after ${\forall}\mathrm{I}$, or to reuse an eigenvariable that appears in an open assumption.

### L3 human

The introduction rules can be read as the meaning of the logical symbols, and the elimination rules are then justified by them: this is the idea of proof-theoretic semantics, with Prawitz's inversion principle.
A detour, an introduction followed at once by the matching elimination, can be removed, and the removal is $\beta$-reduction of lambda terms under the [[Curry-Howard correspondence|A77FER1Q5H]].
The intuitionistic system NJ is the natural one from this view, and RAA breaks the symmetry between introduction and elimination; this is one reason why [[intuitionistic logic|Q11N8X99FK]] is studied by proof theorists.
The [[sequent calculus|W72CA3R9MP]] makes the bookkeeping of open assumptions explicit, and normalization of natural deduction corresponds to [[cut elimination|AYRZ98Y0NW]] there.
