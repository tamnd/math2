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

The theorem says that a first-order proof of prenex formulas can be split into a propositional part on top and a part below that only adds quantifiers.

Let $\Gamma \Rightarrow \Delta$ be a sequent of [[prenex formulas|CS82V969DE]] that is derivable in the first-order [[sequent calculus|PZX9J3VEMT]] LK.
Then $\Gamma \Rightarrow \Delta$ has a cut-free derivation that contains a sequent $M$, the *midsequent*, with these properties.

1. $M$ contains no quantifier.
2. Every rule above $M$ is a propositional rule or a structural rule.
3. Every rule below $M$ is a quantifier rule or a structural rule.

Here structural rules are weakening, contraction and exchange, and the axioms are $p \Rightarrow p$ with $p$ atomic.
Rules below $M$ have one premise, so the part below $M$ is a single chain of sequents from $M$ to $\Gamma \Rightarrow \Delta$.

## Remarks

### A midsequent in the drinker formula

Take the prenex sequent $\Rightarrow \exists x\, \forall y\, (P(x) \to P(y))$, which says that some $x$ has $P$ only if everyone has $P$.
With distinct variables $a$, $b$ and $c$, a derivation has the midsequent $M$ below.
$$M = \ \Rightarrow P(a) \to P(b),\ P(b) \to P(c)$$
Above $M$ the derivation starts from the axiom $P(b) \Rightarrow P(b)$ and uses WR, ${\to}$R, WL, XR, ${\to}$R and XR, all propositional or structural.
Below $M$ the chain reads as follows, with $E$ for the end formula.

1. ${\forall}$R with eigenvariable $c$ gives $\Rightarrow P(a) \to P(b), \forall y\, (P(b) \to P(y))$.
2. ${\exists}$R with the term $b$ gives $\Rightarrow P(a) \to P(b), E$.
3. XR, then ${\forall}$R with eigenvariable $b$, then ${\exists}$R with the term $a$ give $\Rightarrow E, E$.
4. CR gives $\Rightarrow E$.

The midsequent lists two instances of the matrix, and the chain only chooses terms for them.
The order matters: $b$ may serve as an eigenvariable in step 3 only because step 2 has already used it as a term and removed it.

### Why each hypothesis is needed

The formulas must be prenex.
Let $A = \forall x\, P(x)$ and consider the derivable sequent $\Rightarrow A \to A$.
In a derivation with a midsequent $M$, each formula of $M$ descends through the chain to a formula of the end sequent.
Below $M$, a structural rule keeps a formula, and a quantifier rule makes a formula that begins with a quantifier.
So a formula of $M$ descends to a quantifier-free formula or to one that begins with a quantifier.
The only end formula $A \to A$ is neither, so $M$ is the empty sequent, which is not derivable because LK is sound.

Cut-freeness is part of the conclusion, not a hypothesis, and the theorem is proved through the [[cut-elimination theorem|AYRZ98Y0NW]].
The proof needs a cut-free derivation, since a cut formula can be any formula, with quantifiers under connectives, even when the end sequent is prenex.

### What it gives you

The main consequence is [[Herbrand's theorem|VZ21F10WRS]] for existential sentences.
Let $B(x)$ be quantifier-free and let $\Rightarrow \exists x\, B(x)$ be derivable.
Below $M$ only ${\exists}$R and structural rules can occur, so $M$ is $\Rightarrow B(t_1), \dots, B(t_n)$ for some terms $t_1, \dots, t_n$.
It is derived by propositional rules, so $B(t_1) \vee \dots \vee B(t_n)$ is a propositional tautology.

More generally, a first-order proof of a prenex sequent separates into a propositional argument and a choice of instances, and the terms of the instances can be read off $M$.

### The converse

The chain can be read downward as a recipe.
If $B(t_1) \vee \dots \vee B(t_n)$ is a tautology, then $\Rightarrow B(t_1), \dots, B(t_n)$ is derivable by propositional rules, and $n$ steps of ${\exists}$R and $n - 1$ contractions give $\Rightarrow \exists x\, B(x)$.
This is the easy direction of Herbrand's theorem.
The midsequent is not unique: the same end sequent can have derivations with different midsequents and different numbers of instances.

### Generalizations

In LK every first-order formula is equivalent to a prenex formula, so the theorem applies to any sequent after this change.
The change uses classical equivalences, and versions of Herbrand's theorem for formulas that are not prenex use Skolem functions or Herbrand expansions instead.

### Watch out

The theorem does not say that the given derivation has a midsequent.
It says that some cut-free derivation does, and producing it requires moving rules around.
Also the number of instances in $M$ can be very large, since it is bounded only through the size of a cut-free derivation.

## History

Gerhard Gentzen proved the theorem in his paper *Untersuchungen über das logische Schließen*, published in 1934 and 1935, as a consequence of the Hauptsatz.
He called it the *verschärfter Hauptsatz*, the sharpened Hauptsatz.
It gave a proof of Herbrand's theorem inside the sequent calculus.

## Explanations

### L1 human

A proof of a statement with "for all" and "there exists" in front can be split into two parts.
The first part proves a statement about specific objects, with no quantifiers at all.
The second part only turns specific objects into "for all" and "there exists", one at a time.
The sequent between the two parts is the midsequent.

### L2 human

To find instances for $\Rightarrow \exists x\, B(x)$, look at the midsequent of a derivation: it is a list of instances $B(t_i)$ whose disjunction is a tautology.
In the drinker example two instances suffice, with the terms $a$ and $b$.
The typical use is this extraction of witnesses, which is why the theorem is the sequent calculus route to Herbrand's theorem.
A trap is the order of the quantifier rules, since ${\forall}$R on a variable must come after every ${\exists}$R that uses it as a term.

### L3 human

The theorem follows from cut elimination by moving quantifier rules below propositional rules in a cut-free derivation.
The number of instances in $M$ is bounded in terms of the cut-free derivation, so the cost of cut elimination passes to Herbrand disjunctions.
The proof uses that a propositional rule never has a quantified principal formula, and this is where prenex form enters.
