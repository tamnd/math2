---
tag: AMMKNENT3R
kind: concept
name: Focusing
msc: ["03F52", "03F05", "68N17"]
topics: [R10RMQCJQX]
audience: research
uses: [W72CA3R9MP, 2P2184B6HE, H408H4WHBA, QR92EZDTKF, PZX9J3VEMT]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Connectives, duality, and polarity
  - url: https://en.wikipedia.org/wiki/Linear_logic
    locator: Sequent calculus presentation
  - url: https://en.wikipedia.org/wiki/Focused_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Focused_proof
    locator: Polarisation
  - url: https://en.wikipedia.org/wiki/Focused_proof
    locator: Uniform proofs
  - url: https://en.wikipedia.org/wiki/Harrop_formula
    locator: Hereditary Harrop formulae and logic programming
  - url: https://en.wikipedia.org/wiki/Logic_programming
    locator: Linear logic programming
---

## Summary

Focusing is a discipline for proof search: do every step that cannot go wrong first, and when a real choice must be made, commit to one formula and keep working on it until its choices run out.
Andreoli showed for [[linear logic|2P2184B6HE]] that this discipline loses no provable sequent, so a search may look only at focused proofs.
Exactly: the connectives split into *negative* ones, whose [[sequent calculus|W72CA3R9MP]] rules are invertible, and *positive* ones, whose rules make choices.
A *focused proof* alternates an inversion phase, which applies negative rules eagerly, and a focus phase, which picks one positive formula and decomposes it with positive rules until it reaches a negative subformula or an atom.
Andreoli's theorem says that every provable sequent has a focused proof.

## Motivation

Search for a proof of the one-sided linear sequent $\vdash a^{\perp} \mathbin{\wp} b^{\perp}, a \otimes b$, which says that $a \otimes b$ entails itself.
The rule for $\mathbin{\wp}$ is invertible: its premise $\vdash a^{\perp}, b^{\perp}, a \otimes b$ is provable whenever the conclusion is, so we may apply it at once.
The rule for $\otimes$ is not: it must split the other formulas between its two premises, and of the four splits only $a^{\perp} \mid b^{\perp}$ works.
A naive search would try ${\otimes}$ and ${\mathbin{\wp}}$ in both orders and every split, while focusing applies ${\mathbin{\wp}}$, then decides on $a \otimes b$, and closes both branches.
The [[worked search|36CHQ3S3Y6]] shows that this is the only focused proof.

Many cut-free proofs differ only by the order of independent steps, and a search that tries every order wastes its time.
Andreoli observed that after one choice on a positive formula, the next choices on its positive subformulas can be made at once, with no loss of completeness.
In logic programming the two phases match goal reduction and backchaining, which is why focusing became the proof theory of Prolog-like languages.

## Notation

We use one-sided MALL, the multiplicative-additive fragment of [[linear logic|H408H4WHBA]], with formulas in negation normal form:
$$F ::= a \mid a^{\perp} \mid \mathbf{1} \mid \bot \mid \mathbf{0} \mid \top \mid F \otimes F \mid F \mathbin{\wp} F \mid F \oplus F \mid F \mathbin{\&} F .$$
Here $\mathbin{\wp}$ is par, the multiplicative disjunction.
A formula is negative when its main connective is $\mathbin{\wp}$, $\bot$, $\mathbin{\&}$ or $\top$, or when it is a negated atom $a^{\perp}$.
It is positive when its main connective is $\otimes$, $\mathbf{1}$, $\oplus$ or $\mathbf{0}$, or when it is an atom $a$.
The polarity of atoms is a convention, and other papers assign it differently.
Andreoli used the words *asynchronous* for negative and *synchronous* for positive.

The focused system has two kinds of sequents.
In $\vdash \Gamma \Uparrow L$, the multiset $\Gamma$ holds positive formulas and negated atoms, and $L$ is a list of formulas still to be inverted.
In $\vdash \Gamma \Downarrow F$, the formula $F$ is under focus.

## Remarks

### The focused rules

Each rule goes from the premises to the conclusion.

- Inversion of $\bot$ and $\mathbin{\wp}$: $[\bot]$ from $\vdash \Gamma \Uparrow L$ infer $\vdash \Gamma \Uparrow \bot, L$; $[\mathbin{\wp}]$ from $\vdash \Gamma \Uparrow A, B, L$ infer $\vdash \Gamma \Uparrow A \mathbin{\wp} B, L$.
  Inversion of $\top$ and $\mathbin{\&}$: $[\top]$ is the axiom $\vdash \Gamma \Uparrow \top, L$; $[\mathbin{\&}]$ from $\vdash \Gamma \Uparrow A, L$ and $\vdash \Gamma \Uparrow B, L$ infer $\vdash \Gamma \Uparrow A \mathbin{\&} B, L$.
- Store: from $\vdash \Gamma, C \Uparrow L$ infer $\vdash \Gamma \Uparrow C, L$, when $C$ is positive or a negated atom.
- Focus: $[\mathbf{1}]$ is the axiom $\vdash \cdot \Downarrow \mathbf{1}$; $[\otimes]$ from $\vdash \Gamma \Downarrow A$ and $\vdash \Delta \Downarrow B$ infer $\vdash \Gamma, \Delta \Downarrow A \otimes B$.
  Also $[\oplus_i]$ from $\vdash \Gamma \Downarrow A_i$ infer $\vdash \Gamma \Downarrow A_1 \oplus A_2$, and $[\mathrm{init}]$ is the axiom $\vdash a^{\perp} \Downarrow a$.
- Release: from $\vdash \Gamma \Uparrow N$ infer $\vdash \Gamma \Downarrow N$, when $N$ is negative.
  Decide: from $\vdash \Gamma \Downarrow P$ infer $\vdash \Gamma, P \Uparrow \cdot$, when $P$ is positive.

There is no rule for $\mathbf{0}$, as in MALL, and there is no cut.

### Two searches, one with branching

The multiplicative search of the Motivation has one inversion phase and one focus phase.
The [[additive example|RTRXJYNPE7]], $\vdash a^{\perp} \mathbin{\&} b^{\perp}, b \oplus a$, shows why inversion must come first.
The rule $[\mathbin{\&}]$ creates two branches, one holding $a^{\perp}$ and one holding $b^{\perp}$.
Each branch then focuses on $b \oplus a$ and picks the disjunct that matches its atom.
Had we chosen a disjunct before the case split, one of the two branches would have failed.

### What is not focused

The MALL proof of $\vdash a \otimes b, a^{\perp}, b^{\perp} \mathbin{\wp} \bot$ that applies ${\otimes}$ last, at the bottom, is a correct proof but not a focused one.
It makes the positive choice while the negative formula $b^{\perp} \mathbin{\wp} \bot$ is still unprocessed, and the [[non-example|C4S1DYMAQP]] permutes it into focused form.

In intuitionistic logic, $p \vee q \Rightarrow q \vee p$ is provable but has no uniform proof.
A uniform proof must end with ${\vee}$R, and neither $p \vee q \Rightarrow q$ nor $p \vee q \Rightarrow p$ is provable.
So a language whose programs may contain disjunctions is not an abstract logic programming language.

### Why focusing is complete

**Theorem (Andreoli).** A sequent $\vdash \Gamma$ is provable in MALL if and only if $\vdash \cdot \Uparrow \Gamma$ is provable in the focused system.

Soundness is direct: erase the arrows, and each focused rule becomes a MALL rule or a bookkeeping step.
Completeness rests on three facts, which we cite.
The negative rules of MALL are invertible.
Rules acting on different formulas permute with each other.
And a focalization lemma shows that, in a sequent with no negative formula left, some positive formula can be decomposed first with its whole positive phase.
For full linear logic the sequents get one more zone, for formulas $?A$ that may be used many times.

### Logic programming

A [[Horn clause|QR92EZDTKF]] program shows the phases at work.
Resolution of a goal $A$ against a clause $G \to A$ is a focus on that clause.
The focus phase decomposes the clause until its head $A$ meets the goal, and then releases the body $G$ as the new goal.
Miller, Nadathur, Pfenning and Scedrov called a cut-free intuitionistic proof *uniform* when every sequent with a compound succedent is the conclusion of a right rule.
Horn clauses and hereditary Harrop formulas, the language of $\lambda$Prolog, have uniform proofs for every provable sequent.
Liang and Miller extended focusing to [[LK and LJ|PZX9J3VEMT]]; there, with negative atoms the focused proofs from Horn clauses do backward chaining, and with positive atoms forward chaining.

### Watch out

The first slip is to release the focus on a positive subformula.
In $\vdash a^{\perp} \Downarrow a \otimes \mathbf{1}$ the focus must go on into $a$ and $\mathbf{1}$, and release is only for negative subformulas.
The second slip is to decide on a negative formula; negative formulas are inverted at once, and only positive ones wait for a decision.
The third is to expect focusing to remove all choices.
The split in $[\otimes]$, the disjunct in $[\oplus_i]$ and the formula to decide on remain choices.

### Try it

First, which phase handles $a \mathbin{\&} \top$, and with which rules?
It is negative, so the inversion phase applies $[\mathbin{\&}]$, and the branch with $\top$ closes at once by $[\top]$.

Second, why does $\vdash a^{\perp}, b^{\perp} \Downarrow a \oplus b$ fail?
Both $[\oplus_i]$ leave a focused atom with two formulas in the context, and $[\mathrm{init}]$ needs exactly one.

### History

Jean-Marc Andreoli introduced focusing in 1992, in the paper "Logic programming with focusing proofs in linear logic" in the Journal of Logic and Computation.
Miller, Nadathur, Pfenning and Scedrov introduced uniform proofs and abstract logic programming languages in 1991, in the Annals of Pure and Applied Logic.
Focusing has since been extended to intuitionistic and classical logic.

## Explanations

### L1 human

When we search for a proof, many steps can be done in any order, and the order does not matter.
Focusing tells the search to do all the safe steps first, those that can never lead to a dead end.
Then it picks one formula with a real choice and stays on that formula while choices remain.
To prove "$a$ and $b$" from "$a$" and "$b$", the search picks "$a$ and $b$" and splits it into $a$ and $b$ at once.
The search tries far fewer orders of steps and still finds a proof whenever one exists.

### L2 human

Count how much focusing saves on $\vdash a^{\perp} \mathbin{\wp} b^{\perp}, a \otimes b$.
Without focusing, the last rule can be ${\mathbin{\wp}}$ or ${\otimes}$, and if it is ${\otimes}$, the formula $a^{\perp} \mathbin{\wp} b^{\perp}$ must go whole to one premise, which fails.
Focusing forces ${\mathbin{\wp}}$ and three Store steps, leaving one Decide on $a \otimes b$.
The split of $a^{\perp}, b^{\perp}$ in $[\otimes]$ has four options, and only one closes both premises by $[\mathrm{init}]$.
Check: $2^2 = 4$ splits, since each of the two stored atoms goes left or right.
So all the work is in one choice, and the rest of the search is forced.
This is the general shape: inversion is deterministic, and choices sit only in the focus phase.

### L3 human

Focusing shows that a cut-free proof is built from large synthetic rules: a positive phase followed by a negative phase acts as one rule on the stored formulas.
One reading of polarity comes from [[proof-theoretic semantics|K97KZB5R7N]]: a positive connective is fixed by its introduction rules, a negative one by its elimination rules.
The polarities chosen for atoms and for the connectives of classical and intuitionistic logic change the shape of focused proofs, but not provability.
Focused proofs remove many permutations of independent rules, so they bear on the [[identity of proofs|G7B4XWMS7Q]].
Compared with [[deep inference|4ZW0SHW2RG]], focusing keeps the sequent calculus and restricts proofs to a normal form, instead of changing the formalism.
