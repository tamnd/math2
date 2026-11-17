---
tag: ~bc719aec
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

*Focusing* is a normal form for cut-free [[sequent calculus|W72CA3R9MP]] proofs, introduced by Andreoli for [[linear logic|2P2184B6HE]].
Connectives are split into negative ones, whose rules are invertible, and positive ones, whose rules involve choices.
A *focused proof* alternates two phases.
The inversion phase applies negative rules eagerly, in a fixed order.
The focus phase chooses one positive formula and decomposes it with positive rules, and it keeps the focus on its positive subformulas until it reaches a negative subformula or an atom.
Andreoli's theorem says that every provable sequent has a focused proof, so proof search may be restricted to focused proofs without loss.
Focusing cuts down the search space, and it gives a proof-theoretic basis for logic programming.

## Motivation

A cut-free sequent proof leaves many choices open: which formula to work on next, and in what order to apply rules that do not interact.
Many proofs differ only by the order of such independent steps, and a proof search procedure that tries all orders wastes time.
Some rules are invertible: their premises are provable whenever the conclusion is, so they can be applied at once without loss.
Other rules, such as ${\otimes}$ and ${\oplus}$, force a choice of how to split the context or which disjunct to keep.
Andreoli observed that after one such choice, the next choices on the subformulas of the same formula can be made at once, without loss of completeness.
This gives proofs with a clear structure of phases, and in logic programming the phases match goal reduction and backchaining.

## Notation

We use one-sided MALL, the multiplicative-additive fragment of [[linear logic|H408H4WHBA]], with formulas in negation normal form:
$$F ::= a \mid a^{\perp} \mid \mathbf{1} \mid \bot \mid \mathbf{0} \mid \top \mid F \otimes F \mid F \mathbin{\wp} F \mid F \oplus F \mid F \mathbin{\&} F .$$
Here $\mathbin{\wp}$ is par, the multiplicative disjunction.
The negative formulas are those whose main connective is $\mathbin{\wp}$, $\bot$, $\mathbin{\&}$ or $\top$, and the negated atoms $a^{\perp}$.
The positive formulas are those whose main connective is $\otimes$, $\mathbf{1}$, $\oplus$ or $\mathbf{0}$, and the atoms $a$.
The choice of polarity for atoms is a convention; other papers assign polarities to atoms in other ways.

The focused system has two kinds of sequents.
In $\vdash \Gamma \Uparrow L$, the multiset $\Gamma$ holds positive formulas and negated atoms, and $L$ is a list of formulas still to be inverted.
In $\vdash \Gamma \Downarrow F$, the formula $F$ is under focus.
The rules are as follows, each from the premises to the conclusion.

- Inversion: $[\bot]$ from $\vdash \Gamma \Uparrow L$ infer $\vdash \Gamma \Uparrow \bot, L$; $[\mathbin{\wp}]$ from $\vdash \Gamma \Uparrow A, B, L$ infer $\vdash \Gamma \Uparrow A \mathbin{\wp} B, L$.
- Inversion: $[\top]$ $\vdash \Gamma \Uparrow \top, L$ is an axiom; $[\mathbin{\&}]$ from $\vdash \Gamma \Uparrow A, L$ and $\vdash \Gamma \Uparrow B, L$ infer $\vdash \Gamma \Uparrow A \mathbin{\&} B, L$.
- Store: from $\vdash \Gamma, C \Uparrow L$ infer $\vdash \Gamma \Uparrow C, L$, when $C$ is positive or a negated atom.
- Focus: $[\mathbf{1}]$ $\vdash \cdot \Downarrow \mathbf{1}$ is an axiom; $[\otimes]$ from $\vdash \Gamma \Downarrow A$ and $\vdash \Delta \Downarrow B$ infer $\vdash \Gamma, \Delta \Downarrow A \otimes B$.
- Focus: $[\oplus_i]$ from $\vdash \Gamma \Downarrow A_i$ infer $\vdash \Gamma \Downarrow A_1 \oplus A_2$, for $i = 1, 2$.
- Identity: $[\mathrm{init}]$ $\vdash a^{\perp} \Downarrow a$ is an axiom.
- Release: from $\vdash \Gamma \Uparrow N$ infer $\vdash \Gamma \Downarrow N$, when $N$ is negative.
- Decide: from $\vdash \Gamma \Downarrow P$ infer $\vdash \Gamma, P \Uparrow \cdot$, when $P$ is positive.

There is no rule for $\mathbf{0}$, as in MALL, and the focused system has no cut.
Andreoli used the words *asynchronous* for negative and *synchronous* for positive.

## Remarks

### Examples

- The sequent $\vdash a^{\perp} \mathbin{\wp} b^{\perp}, a \otimes b$ has exactly one focused proof: one inversion phase, one decision on $a \otimes b$, and two initial sequents. The [[example of a multiplicative focused proof|~a15f32cb]] gives it.
- The sequent $\vdash a^{\perp} \mathbin{\&} b^{\perp}, b \oplus a$ has a focused proof in which the rule $\mathbin{\&}$ creates two branches, and each branch focuses on $b \oplus a$ with a different choice. The [[example of an additive focused proof|~0b3df90f]] gives it.
- A [[Horn clause|QR92EZDTKF]] program in Prolog: resolution with a clause $G \to A$ against a goal $A$ is a focus on that clause. The focus phase decomposes the clause until the head $A$ meets the goal, and then releases the body $G$ as a new goal.
- Hereditary Harrop formulas, the language of $\lambda$Prolog, allow implications and universal quantifiers in goals. Their goal-directed proofs are again focused proofs, with an inversion phase on the goal.
- Focusing also applies to [[LK|PZX9J3VEMT]] and LJ, as studied by Liang and Miller. There the uniform proofs are the focused proofs in which all atoms are given negative polarity.

### Non-examples

- The MALL proof of $\vdash a \otimes b, a^{\perp}, b^{\perp} \mathbin{\wp} \bot$ that applies ${\otimes}$ last is not focused: it applies a positive rule while a negative formula is still present. The [[non-example|~a387e4a9]] shows this and gives the focused proof.
- The intuitionistic sequent $p \vee q \Rightarrow q \vee p$ is provable but has no uniform proof. A uniform proof must end with ${\vee}$R, and neither $p \vee q \Rightarrow q$ nor $p \vee q \Rightarrow p$ is provable. So programs with disjunctions are not an abstract logic programming language.

### Basic properties

- **Theorem (Andreoli).** A sequent $\vdash \Gamma$ is provable in MALL if and only if $\vdash \cdot \Uparrow \Gamma$ is provable in the focused system.
- Soundness of the focused system is direct: erasing the arrows turns each focused rule into a MALL rule, a structural bookkeeping step, or nothing.
- Completeness uses three facts. The negative rules of MALL are invertible. The rules permute with each other when they act on different formulas. A focalization lemma shows that a positive formula in a sequent with no negative formulas can be decomposed first, with its whole positive phase. We cite the proof.
- For full linear logic the sequents get an extra unbounded zone for formulas $?A$, which can be used many times.
- Uniform proofs (Miller, Nadathur, Pfenning and Scedrov): a cut-free intuitionistic proof is uniform if every sequent with a non-atomic succedent is the conclusion of a right rule. Horn clauses and hereditary Harrop formulas have the property that every provable sequent has a uniform proof.

### History

Andreoli introduced focusing in his 1992 paper "Logic programming with focusing proofs in linear logic" in the Journal of Logic and Computation.
Miller, Nadathur, Pfenning and Scedrov introduced uniform proofs and abstract logic programming languages in 1991, in the Annals of Pure and Applied Logic.
Focusing was later extended to intuitionistic and classical logic, and it is used in the design of logic programming languages and proof assistants.

### Common errors

- Releasing the focus on a positive subformula. The focus must continue on positive subformulas, and release happens only on negative ones.
- Deciding on a negative formula. Only positive formulas are stored for later decisions; negative formulas are inverted at once.
- Expecting focusing to remove all choices. The context split in $[\otimes]$, the choice in $[\oplus_i]$ and the choice of the decided formula remain.

## Explanations

### L1 human

When we search for a proof, many steps can be done in any order and do not matter.
Focusing tells the search to do all the "safe" steps first, those that can never lead to a dead end.
Then it picks one formula with a real choice and keeps working on that same formula as long as choices remain.
For example, to prove "$a$ and $b$" from "$a$" and "$b$", the search picks the formula "$a$ and $b$" and splits it into $a$ and $b$ at once.
This way, the search tries far fewer orders of steps and still finds a proof whenever one exists.

### L2 human

We find a focused proof of $\vdash a^{\perp} \mathbin{\wp} b^{\perp}, a \otimes b$.

1. Inversion: $[\mathbin{\wp}]$ turns $\vdash \cdot \Uparrow a^{\perp} \mathbin{\wp} b^{\perp}, a \otimes b$ into $\vdash \cdot \Uparrow a^{\perp}, b^{\perp}, a \otimes b$.
2. Store moves $a^{\perp}$, $b^{\perp}$ and $a \otimes b$ to the left, giving $\vdash a^{\perp}, b^{\perp}, a \otimes b \Uparrow \cdot$.
3. Decide on the only positive formula $a \otimes b$: $\vdash a^{\perp}, b^{\perp} \Downarrow a \otimes b$.
4. $[\otimes]$ with the split $a^{\perp} \mid b^{\perp}$ gives $\vdash a^{\perp} \Downarrow a$ and $\vdash b^{\perp} \Downarrow b$.
5. Both are instances of $[\mathrm{init}]$.

The typical use of focusing is to design proof search: the inversion phase is deterministic, and choices happen only in the focus phase.
A trap is step 4: the other context splits leave a sequent such as $\vdash \cdot \Downarrow a$, which has no proof, so the split must match the atoms.

### L3 human

Focusing reveals that a cut-free proof is built from large synthetic rules: one positive phase followed by one negative phase acts as a single rule on the stored formulas.
One reading of polarity comes from [[proof-theoretic semantics|~50806e9d]]: a positive connective is determined by its introduction rules, and a negative one by its elimination rules.
The choice of polarity for atoms and for the connectives of classical and intuitionistic logic changes the shape of focused proofs.
Focusing connects with game semantics, where phases are moves of the two players, and with the study of [[identity of proofs|~8cb6c275]], since focused proofs remove many permutations of independent rules.
Compared with [[deep inference|~110b1691]], focusing restricts proofs to a normal form rather than changing the formalism.
