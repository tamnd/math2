---
tag: 4ZW0SHW2RG
kind: concept
name: Deep inference
msc: ["03F05", "03F52"]
topics: [R10RMQCJQX]
audience: research
uses: [W72CA3R9MP, 09K9MWD2QQ, AYRZ98Y0NW]
sources:
  - url: https://en.wikipedia.org/wiki/Deep_inference
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Calculus_of_structures
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Calculus_of_structures
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Calculus_of_structures
    locator: SKSg
  - url: https://en.wikipedia.org/wiki/Calculus_of_structures
    locator: BV
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Locality
---

## Summary

Deep inference lets a proof rule rewrite a piece of a formula wherever that piece sits, instead of only at the top of a sequent.
With rules that reach inside formulas, identity, cut, weakening and contraction can all be cut down to steps on single atoms.
Exactly: every rule has the form $S\{A\} / S\{B\}$, which rewrites a subformula $A$ into $B$ inside a context $S\{\ \}$, a formula with one hole at any depth.
The hole must be in a positive position, so that $S\{A\} \to S\{B\}$ is valid whenever $A \to B$ is valid.
The *calculus of structures* of Guglielmi is the main formalism, and its system SKS for classical [[propositional logic|09K9MWD2QQ]] appears in the Notation below.
A derivation is a sequence of formulas, each obtained from the one before by one rule instance or by the equations, and a proof is a derivation from the unit $\mathsf{t}$.

## Motivation

Look at one step of the switch rule, from $A \wedge (B \vee C)$ to $(A \wedge B) \vee C$, used deep inside a formula:
$$a \vee \bigl(b \wedge (c \vee d)\bigr) \quad \text{to} \quad a \vee \bigl((b \wedge c) \vee d\bigr).$$
The context is $a \vee \{\ \}$, and the rule never touches $a$.
No rule of a [[sequent calculus|W72CA3R9MP]] can make this step, because sequent rules act only on the main connective of a formula in the sequent.

That shallowness has a cost.
Contraction and weakening in a sequent calculus act on a whole formula $A$, of any size, so checking one step can mean copying or comparing an unbounded amount of data.
When rules may act anywhere, these steps break into pieces that each touch a bounded amount of data, and this property is called *locality*.
Guglielmi also needed a proof system for a logic BV with a self-dual non-commutative connective, and no sequent calculus for it was known; deep rules gave one.

## Notation

Formulas of SKS are built from atoms $a, b, \dots$, their negations $\bar{a}, \bar{b}, \dots$, and the units $\mathsf{t}$ and $\mathsf{f}$, with $\vee$ and $\wedge$.
The negation of a compound formula is defined by the De Morgan laws, so negation sits only on atoms and every context is positive.
Formulas are taken modulo associativity and commutativity of $\vee$ and $\wedge$ and the unit equations $A \vee \mathsf{f} = A$, $A \wedge \mathsf{t} = A$, $\mathsf{t} \vee \mathsf{t} = \mathsf{t}$ and $\mathsf{f} \wedge \mathsf{f} = \mathsf{f}$.
Each rule below goes from premise to conclusion, inside any context, where $a$ is an atom or a negated atom.

- Atomic identity $\mathsf{ai}{\downarrow}$: $\mathsf{t}$ to $a \vee \bar{a}$. Atomic cut $\mathsf{ai}{\uparrow}$: $a \wedge \bar{a}$ to $\mathsf{f}$.
- Atomic weakening $\mathsf{aw}{\downarrow}$: $\mathsf{f}$ to $a$. Atomic coweakening $\mathsf{aw}{\uparrow}$: $a$ to $\mathsf{t}$.
- Atomic contraction $\mathsf{ac}{\downarrow}$: $a \vee a$ to $a$. Atomic cocontraction $\mathsf{ac}{\uparrow}$: $a$ to $a \wedge a$.
- Switch $\mathsf{s}$: $A \wedge (B \vee C)$ to $(A \wedge B) \vee C$. Medial $\mathsf{m}$: $(A \wedge B) \vee (C \wedge D)$ to $(A \vee C) \wedge (B \vee D)$.

The rules marked ${\downarrow}$ are the down rules, and each up rule ${\uparrow}$ is the dual of a down rule.
Some authors write $\top$ and $\bot$ for the units, and some write $[A, B]$ for $A \vee B$ and $(A, B)$ for $A \wedge B$.

## Remarks

### Identity from atoms

The identity $A \vee \bar{A}$ for a compound $A$ is not a rule of SKS, yet every instance is provable.
For $A = a \wedge b$ the formula is $(a \wedge b) \vee \bar{a} \vee \bar{b}$, and its [[proof|KWYR5E9XF3]] runs as follows.
Two atomic identities turn $\mathsf{t} = \mathsf{t} \wedge \mathsf{t}$ into $(a \vee \bar{a}) \wedge (b \vee \bar{b})$.
One switch gives $((a \vee \bar{a}) \wedge b) \vee \bar{b}$, and a second switch, inside the left disjunct, gives $((b \wedge a) \vee \bar{a}) \vee \bar{b}$.
The equations reorder this to the goal.
The same pattern, by induction on $A$, derives the general identity rule.

### Contraction from atoms

Contraction on $a \wedge b$ takes $(a \wedge b) \vee (a \wedge b)$ to $a \wedge b$.
Medial, with $A = C = a$ and $B = D = b$, regroups the premise as $(a \vee a) \wedge (b \vee b)$, and two atomic contractions finish.
The [[worked derivation|7G6PJ1F0JQ]] checks each step and gives the induction for every formula.
Medial moves the four atom occurrences without copying or deleting any of them, and that is what makes contraction local.

### What it is not

A step inside a negation is not a deep inference step.
Switch under $\neg\{\ \}$ goes from a true formula to a false one when $A$ and $B$ are false and $C$ is true, as the [[non-example|D1DXH3Q469]] checks.
The context $\neg\{\ \}$ reverses implications, which is why SKS puts negation only on atoms.

A rule of [[LK|PZX9J3VEMT]], such as ${\wedge}$R, is a shallow rule: it builds the main connective of a formula in the sequent and cannot act inside a subformula.
Distributivity, from $A \wedge (B \vee C)$ to $(A \wedge B) \vee (A \wedge C)$, is valid but is not an SKS rule, because it copies $A$ and so is not local.

### The rules you can use

Each SKS rule is a valid implication, and every context is positive, so every derivation is sound.
The down fragment $\{\mathsf{ai}{\downarrow}, \mathsf{aw}{\downarrow}, \mathsf{ac}{\downarrow}, \mathsf{s}, \mathsf{m}\}$ already proves every tautology.
So all up rules, atomic cut included, are admissible; this is the deep inference form of the [[cut-elimination theorem|AYRZ98Y0NW]], and we cite it without proof.
The calculus has a top-down symmetry: read a derivation upside down and negate every formula, and you get a derivation with the dual rules.

### Watch out

The first slip is to apply a rule inside a negated subformula, as above.
The second is to confuse switch with distributivity.
Switch keeps one copy of $A$ and moves it next to $B$, while distributivity makes two copies.
The third is to apply switch backwards: from $(A \wedge B) \vee C$ to $A \wedge (B \vee C)$ fails when $A$ is false and $C$ is true.

### Try it

First, apply switch to $a \wedge (b \vee \bar{a})$ in the empty context.
The result is $(a \wedge b) \vee \bar{a}$, with $A = a$, $B = b$ and $C = \bar{a}$.

Second, use medial and atomic contraction to derive $\bar{a} \wedge b$ from $(\bar{a} \wedge b) \vee (\bar{a} \wedge b)$.
Medial gives $(\bar{a} \vee \bar{a}) \wedge (b \vee b)$, and $\mathsf{ac}{\downarrow}$ applies to the negated atom $\bar{a}$ as well as to $b$.

### History

Alessio Guglielmi introduced the calculus of structures in the paper "A System of Interaction and Structure", to give a proof system for the logic BV.
Kai Brünnler and Alwen Tiu then gave the system SKS for classical propositional logic, in which identity, cut, weakening and contraction act on atoms only.
Guglielmi and Tom Gundersen later introduced atomic flows, graphs that track atom occurrences through a derivation, to control normalization.

## Explanations

### L1 human

In most proof systems, a rule looks only at the outermost symbol of a formula.
Deep inference lets a rule rewrite any part of a formula, even a part deep inside.
In "$a$ or ($b$ and ($c$ or $d$))", a rule can rewrite the inner part "$b$ and ($c$ or $d$)" and leave $a$ alone.
Because rules can act anywhere, big steps split into very small steps on single letters.
So each step of a proof does only a small, fixed amount of work.

### L2 human

Here is contraction on a three-atom formula, $(a \wedge (b \vee c)) \vee (a \wedge (b \vee c))$.
Medial with $A = C = a$ and $B = D = b \vee c$ gives
$$(a \vee a) \wedge \bigl((b \vee c) \vee (b \vee c)\bigr).$$
Associativity and commutativity rewrite the right part as $(b \vee b) \vee (c \vee c)$.
Three atomic contractions then give $a \wedge (b \vee c)$.
Check: medial was used once, for the one $\wedge$, and atomic contraction once for each of the three atoms.
This shows how deep inference handles a big contraction: one medial for each conjunction, equations for each disjunction, and atomic steps at the leaves.

### L3 human

Deep inference treats a proof as a rewriting system on formulas, and the context $S\{\ \}$ takes the place that the sequent holds in Gentzen systems.
Up and down rules are dual, so a derivation can be read in either direction.
Deep inference systems exist for classical, linear and modal logics, and for BV with its non-commutative connective.
For BV the depth is essential: Alwen Tiu showed that no shallow sequent system presents it.
Atomic flows and [[proof nets|HN6WN1VE39]] both serve to study when two proofs are the same up to rule permutations, the [[identity of proofs|G7B4XWMS7Q]] problem.
With [[display calculi|2Q62W689SC]] and [[hypersequent calculi|73J7F0FN4A]], deep inference is one of the main proof formats beyond the plain sequent.
