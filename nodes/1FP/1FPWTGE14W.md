---
tag: 1FPWTGE14W
kind: statement
role: theorem
name: Midsequent theorem
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
uses: [PZX9J3VEMT, AYRZ98Y0NW, CS82V969DE]
about: [W72CA3R9MP, VZ21F10WRS]
proofs: [JQ335K7K2S]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand%27s_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Cut-elimination in the sequent calculus
history:
  first_stated: "1934 to 1935"
  notes: "Gentzen proved the theorem in the paper of the Hauptsatz and called it the sharpened Hauptsatz."
---

## Statement

Let $\Gamma \Rightarrow \Delta$ be a sequent of [[prenex formulas|CS82V969DE]] that is derivable in the first-order [[sequent calculus|PZX9J3VEMT]] LK.
Then $\Gamma \Rightarrow \Delta$ has a cut-free derivation that contains a sequent $M$, the *midsequent*, with these properties.

1. $M$ contains no quantifier.
2. Every rule above $M$ is a propositional rule or a structural rule.
3. Every rule below $M$ is a quantifier rule or a structural rule.

Here structural rules are weakening, contraction and exchange, and the axioms are $p \Rightarrow p$ with $p$ atomic.
Rules below $M$ have one premise, so the part below $M$ is a single chain of sequents from $M$ to $\Gamma \Rightarrow \Delta$.

## Remarks

### Why each hypothesis is needed

The formulas must be prenex.
Let $A = \forall x\, P(x)$ and consider the derivable sequent $\Rightarrow A \to A$.
In a derivation with a midsequent $M$, every formula of $M$ descends to a formula of the end sequent through rules below $M$.
Below $M$, a structural rule keeps a formula, and a quantifier rule makes a formula that begins with a quantifier.
So a quantifier-free formula of $M$ descends to a quantifier-free formula or to one that begins with a quantifier.
The only end formula is $A \to A$, which has a quantifier and does not begin with one, so no formula of $M$ descends to it.
So $M$ is the empty sequent, which has no cut-free derivation.

### Consequences

- **[[Herbrand's theorem|VZ21F10WRS]].** Let $B(x)$ be quantifier-free and let $\Rightarrow \exists x\, B(x)$ be derivable. Then for some terms $t_1, \dots, t_n$, the disjunction $B(t_1) \vee \dots \vee B(t_n)$ is a propositional tautology.
- The reason is that below $M$ only ${\exists}$R and structural rules can occur, so $M$ is $\Rightarrow B(t_1), \dots, B(t_n)$. It is derived by propositional rules, so it is a tautology.
- **Separation of the two layers.** A first-order proof of a prenex sequent splits into a propositional part and a part that only chooses instances. The terms of the instances are explicit in $M$.

### Converse

Every derivation with a midsequent is a derivation of LK, so the converse is immediate.
The useful converse reads the chain upwards: a quantifier-free sequent $M$ that is a tautology, followed by quantifier and structural rules, gives a valid sequent.
This is the easy direction of Herbrand's theorem.

### Generalizations

Every first-order formula is equivalent in LK to a prenex formula, so the theorem applies to any sequent after this change.
Herbrand's theorem for formulas that are not prenex uses Herbrand disjunctions with Skolem functions instead.

## History

Gerhard Gentzen proved the theorem in his paper *Untersuchungen über das logische Schließen*, published in 1934 and 1935, as a consequence of the Hauptsatz.
He called it the *verschärfter Hauptsatz*, the sharpened Hauptsatz.
It gives a proof of Herbrand's theorem within the sequent calculus.

## Explanations

### L1 human

A proof of a statement with "for all" and "there exists" in front can be split into two parts.
The first part proves a statement about specific objects, with no quantifiers at all.
The second part only turns specific objects into "for all" and "there exists", one at a time.
The sequent between the two parts is the midsequent.

### L2 human

Take the prenex sequent $\Rightarrow \exists x\, \forall y\, (P(x) \to P(y))$, with distinct variables $a$, $b$ and $c$.

1. The midsequent is $M = {} \Rightarrow P(a) \to P(b), P(b) \to P(c)$.
2. Above $M$: from the axiom $P(b) \Rightarrow P(b)$, use WR, ${\to}$R, WL, XR, ${\to}$R and XR.
3. ${\forall}$R with eigenvariable $c$ gives $\Rightarrow P(a) \to P(b), \forall y\, (P(b) \to P(y))$.
4. ${\exists}$R with the term $b$ gives $\Rightarrow P(a) \to P(b), \exists x\, \forall y\, (P(x) \to P(y))$.
5. XR, then ${\forall}$R with eigenvariable $b$, then ${\exists}$R with the term $a$ give two copies of the end formula.
6. CR gives the end sequent.

The typical use is to read off the instances: here $M$ is a disjunction of two instances.
A trap is the order of quantifier rules: ${\forall}$R on $b$ must come after the ${\exists}$R that uses $b$.

### L3 human

The theorem follows from cut elimination by permuting quantifier rules below propositional rules in a cut-free derivation.
The number of instances in $M$ is bounded in terms of the cut-free derivation, so the cost of cut elimination passes to Herbrand disjunctions.
The proof uses that a propositional rule never has a quantified principal formula, which is where prenex form enters.
