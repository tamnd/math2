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

Natural deduction is a proof system that copies the way mathematicians argue: assume something for a while, reason about an arbitrary object, give a witness a name.
Here is a complete derivation of $\forall x\, P(x) \to \exists x\, P(x)$ in it:
$$\dfrac{\dfrac{\dfrac{[\forall x\, P(x)]^1}{P(y)}\,{\forall}\mathrm{E}}{\exists x\, P(x)}\,{\exists}\mathrm{I}}{\forall x\, P(x) \to \exists x\, P(x)}\,{\to}\mathrm{I}^1$$
Read it from the top.
We assume $\forall x\, P(x)$ and give the assumption the label 1.
The rule ${\forall}\mathrm{E}$ instantiates it at the variable $y$, the rule ${\exists}\mathrm{I}$ turns $P(y)$ into $\exists x\, P(x)$, and ${\to}\mathrm{I}$ closes the assumption with label 1.
Check: no assumption stays open, so the formula is a theorem.

In general, a natural deduction derivation for [[first-order logic|086QKPF0A6]] is a finite tree of [[formulas|HYJ10AF6RT]].
The leaves are assumptions, and each other node follows from the nodes directly above it by one rule.
Each connective and quantifier has introduction rules, which prove a formula with that symbol, and elimination rules, which use such a formula.
The rules ${\to}\mathrm{I}$, ${\vee}\mathrm{E}$, ${\exists}\mathrm{E}$ and the classical rule RAA discharge assumptions, and the rules ${\forall}\mathrm{I}$ and ${\exists}\mathrm{E}$ carry an eigenvariable condition.
We write $\Gamma \vdash_{\mathsf{ND}} \varphi$ when some derivation has root $\varphi$ and all its open assumptions in $\Gamma$.
The [[definition|PAQ4ZX2TX1]] lists every rule with its conditions.

## Motivation

In a [[Hilbert-style calculus|N95HV0VWSM]] almost all the work is done by axioms, and a short argument becomes a long list of axiom instances.
Mathematicians do not argue like this.
To prove "if $\varphi$ then $\psi$" they assume $\varphi$ for a while and derive $\psi$.
To prove "for all $x$" they argue about an arbitrary $x$, and to use "there is an $x$" they give the witness a name.
Natural deduction turns each of these habits into a rule, so a formal derivation reads almost like the informal proof.

The pairing of rules also gives the system a clean structure.
A derivation that introduces a symbol and then at once eliminates it makes a detour, and detours can be removed.
This fact, normalization, leads to the [[Curry-Howard correspondence|A77FER1Q5H]], where derivations are programs.
The [[sequent calculus|W72CA3R9MP]] later in the sub-area records the open assumptions at every node, and the [[equivalence of proof systems|A9AAHN4BMH]] shows that all these calculi prove the same formulas.

## Notation

We write $[\varphi]^u$ for an assumption that a later step with label $u$ discharges, and $\Gamma \vdash_{\mathsf{ND}} \varphi$ for derivability.
Rules are named ${\to}\mathrm{I}$, ${\to}\mathrm{E}$, ${\forall}\mathrm{I}$ and so on; RAA is reductio ad absurdum, and ${\bot}\mathrm{E}$ is "ex falso".
Gentzen called the intuitionistic system NJ and the classical system NK.
Three layouts are common: Gentzen-Prawitz trees, [[Fitch-style natural deduction|2B6XC7XJA8]] with nested boxes, and the sequent-style form, which writes $\Gamma \vdash \varphi$ at each node.
Some books take $\neg$ as primitive, and others define $\neg \varphi$ as $\varphi \to \bot$, as we do.

## Remarks

### Arguing about an arbitrary object

The rule ${\forall}\mathrm{I}$ says: if you derived $\varphi[y/x]$ and nothing you still assume mentions $y$, then you may conclude $\forall x\, \varphi$.
Take the hypotheses $\forall x\, (P(x) \to Q(x))$ and $\forall x\, P(x)$.
Two steps of ${\forall}\mathrm{E}$ with the term $y$ give $P(y) \to Q(y)$ and $P(y)$, and ${\to}\mathrm{E}$ gives $Q(y)$.
The only open assumptions are the two hypotheses, and $y$ is not free in them, so ${\forall}\mathrm{I}$ gives $\forall x\, Q(x)$.
The informal proof is "let $y$ be arbitrary"; the side condition is the formal meaning of "arbitrary".

The rule ${\exists}\mathrm{E}$ is the formal "let $u$ be such that".
[[A natural deduction derivation of a quantifier swap|Q0MPGREG1B]] uses both conditions in one tree, for $\exists x\, \forall y\, R(x, y) \to \forall y\, \exists x\, R(x, y)$.
It needs no classical rule, so it is also an intuitionistic derivation.

### Classical reasoning

Some valid formulas need the rule RAA: from a derivation of $\bot$ from $\neg \varphi$, conclude $\varphi$ and discharge $\neg \varphi$.
[[A classical natural deduction derivation of a quantifier law|TVB3CTGHQ4]] derives $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ with RAA twice.
No derivation without RAA exists, because the formula is not a theorem of [[intuitionistic logic|Q11N8X99FK]].
The propositional rules on their own already give many laws; [[a formal derivation of the transitivity of implication|DNRZJKRDZC]] uses only ${\to}\mathrm{I}$ and ${\to}\mathrm{E}$.

Equality has its own pair of rules.
${=}\mathrm{I}$ gives $s = s$ with no premise, and ${=}\mathrm{E}$ replaces $s$ by $t$ in a formula, given $s = t$.
With the formula $x = s$, the rule turns $s = t$ and $s = s$ into $t = s$, so symmetry is a two-step derivation.

### What is not a derivation

The tree with leaf $[P(y)]^1$, then $\forall x\, P(x)$ by ${\forall}\mathrm{I}$, then $P(y) \to \forall x\, P(x)$ by ${\to}\mathrm{I}^1$, is not a derivation.
The step ${\forall}\mathrm{I}$ fails its condition, because $y$ is free in the open assumption $P(y)$.
Its conclusion is false in the structure $\{0, 1\}$ with $P$ true of $0$ only, when $y$ is $0$.

[[A wrong existential elimination in natural deduction|51AN89Q48G]] ends with $\exists x\, P(x) \to \forall y\, P(y)$.
There the conclusion of ${\exists}\mathrm{E}$ contains the eigenvariable, so the name of the witness escapes its box.

Discharge is also local.
A step ${\to}\mathrm{I}^u$ closes only the leaves $\varphi$ that carry the label $u$.
If another leaf $\varphi$ in the tree has no label, the tree is still a derivation of $\varphi \to \psi$, but from $\{ \varphi \}$, not from the empty set.

### The rules you can rely on

Natural deduction is sound: if $\Gamma \vdash_{\mathsf{ND}} \varphi$, then $\Gamma \models \varphi$.
The proof is an induction on derivations, and the eigenvariable conditions are what make the cases ${\forall}\mathrm{I}$ and ${\exists}\mathrm{E}$ go through.
It is also complete: if $\Gamma \models \varphi$, then $\Gamma \vdash_{\mathsf{ND}} \varphi$, and it derives the same formulas as the other calculi by the [[equivalence of proof systems|A9AAHN4BMH]].

The [[deduction theorem|8M9ZFDR4DH]] is built in, since ${\to}\mathrm{I}$ turns a derivation of $\psi$ from $\Gamma \cup \{ \varphi \}$ into one of $\varphi \to \psi$ from $\Gamma$, with no side condition.
A rule is derived when one fixed tree of basic rules gives it, and modus tollens and double negation elimination are derived rules.
Every derivation can be brought to a normal form with no detours, by the [[normalization theorem|W33WAE1XTC]], and a normal derivation has the [[subformula property|Z2NXKDK06G]].

### Watch out

Three slips cause most wrong derivations.
The first is to break an eigenvariable condition, as in the two trees above.
The second is to use a formula from inside a discharged part of the tree after the discharge: each formula may rest only on assumptions above it.
The third is to use RAA in a proof that must be intuitionistic, where $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ is not derivable.

Watch out also for the opening derivation in the empty structure.
There $\forall x\, P(x)$ is true and $\exists x\, P(x)$ is false.
The derivation is sound only because the usual semantics of first-order logic requires a nonempty domain, so the variable $y$ always denotes something.

### History

Gentzen introduced natural deduction, together with the sequent calculus, in his paper "Untersuchungen über das logische Schließen" of 1934 to 1935.
Jaśkowski published a system of suppositional proofs independently in 1934.
Prawitz proved the normalization theorem in his monograph *Natural Deduction* of 1965.
Fitch's book *Symbolic Logic* of 1952 made the layout with nested subproofs popular.

### Try it

First, derive $\forall x\, (P(x) \wedge Q(x)) \to \forall x\, Q(x)$.
Assume the antecedent with label 1, use ${\forall}\mathrm{E}$ with $y$ and ${\wedge}\mathrm{E}$ to get $Q(y)$, apply ${\forall}\mathrm{I}$ ($y$ is not free in assumption 1), and close with ${\to}\mathrm{I}^1$.

Second, say why $P(y) \vdash_{\mathsf{ND}} \forall x\, P(x)$ fails.
Any final step ${\forall}\mathrm{I}$ on $y$ would have the open assumption $P(y)$, which contains $y$; and the claim is false in $\{0, 1\}$ with $P = \{ 0 \}$ and $y = 0$.

## Explanations

### L1 human

Natural deduction is a set of rules for writing proofs the way people argue.
To prove "if it rains, the street is wet", we assume that it rains and show that the street is wet.
To prove "every square has four sides", we take an arbitrary square, about which we know nothing else, and show that it has four sides.
To use "some student failed", we give the student a name, Sam, and argue about Sam, but the final conclusion must not mention Sam.
A proof is drawn as a tree, with the assumptions at the top and the conclusion at the bottom.

### L2 human

We derive $\forall x\, \forall y\, R(x, y) \to \forall y\, \forall x\, R(x, y)$, the law that two universal quantifiers commute.
Write $A$ for the antecedent and assume $[A]^1$.
Two steps of ${\forall}\mathrm{E}$, with the terms $u$ and then $v$, give
$$\forall y\, R(u, y) \quad \text{and then} \quad R(u, v).$$
Now ${\forall}\mathrm{I}$ on $u$ gives $\forall x\, R(x, v)$, because $u$ is not free in $A$ or in $\forall x\, R(x, v)$.
Then ${\forall}\mathrm{I}$ on $v$ gives $\forall y\, \forall x\, R(x, y)$, because $v$ is not free in $A$ or in the result.
Finally ${\to}\mathrm{I}^1$ discharges $A$.
Check: the two eigenvariables are fresh, and the only open assumption before the last step is the sentence $A$.
The typical use is to formalize a short informal proof, one sentence of it for each one or two rules, as in [[proof strategies by logical form|872K5XB580]].
The trap is the order: you can only generalize a variable after every assumption that mentions it is closed.

### L3 human

The introduction rules can be read as the meaning of the logical symbols, and the elimination rules are then justified by them.
This is the idea of proof-theoretic semantics, with Prawitz's inversion principle.
A detour, an introduction followed at once by the matching elimination, can be removed, and the removal is $\beta$-reduction of lambda terms under the [[Curry-Howard correspondence|A77FER1Q5H]].
The intuitionistic system NJ fits this view best, and RAA breaks the balance between introduction and elimination, which is one reason why proof theorists study [[intuitionistic logic|Q11N8X99FK]].
The [[sequent calculus|W72CA3R9MP]] makes the bookkeeping of open assumptions explicit, and normalization of natural deduction corresponds to [[cut elimination|AYRZ98Y0NW]] there.
