---
tag: 644XCQAC8C
kind: example
name: Single axioms for propositional logic
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
instance_of: [1MGMQX43B8]
uses: [1MGMQX43B8, 1NNYWRN6B8, 0Y0MQYST0M, 05006AJ7DZ, ZMVBAY7ZZD]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_axiomatic_systems_in_logic
    locator: Sheffer's stroke
  - url: https://en.wikipedia.org/wiki/List_of_axiomatic_systems_in_logic
    locator: Implication and negation
  - url: https://en.wikipedia.org/wiki/Implicational_propositional_calculus
    locator: Axiom system
  - url: https://en.wikipedia.org/wiki/Minimal_axioms_for_Boolean_algebra
    locator: lead section
---

## Example

A [[Hilbert system|1MGMQX43B8]] can have a single axiom schema, if the schema is long and chosen with care.
We describe three such systems and check that each axiom is a [[tautology|05006AJ7DZ]] and each rule preserves truth.
In each system the letters $A, B, C, D, E$ stand for arbitrary formulas.

**Nicod's system.** The only connective is the [[Sheffer stroke|1NNYWRN6B8]] $A \mid B$, read "not both $A$ and $B$", so $A \mid B$ is false exactly when $A$ and $B$ are both true.
The single axiom schema is
$$(A \mid (B \mid C)) \mid [(E \mid (E \mid E)) \mid ((D \mid B) \mid [(A \mid D) \mid (A \mid D)])].$$
The only rule, Nicod's modus ponens, infers $C$ from $A$ and $A \mid (B \mid C)$.

**Meredith's system.** The connectives are $\neg$ and $\to$, the rule is [[modus ponens|0Y0MQYST0M]], and the single axiom schema is
$$((((A \to B) \to (\neg C \to \neg D)) \to C) \to E) \to ((E \to A) \to (D \to A)).$$

**Łukasiewicz's implicational system.** The only connective is $\to$, the rule is modus ponens, and the single axiom schema is
$$((A \to B) \to C) \to ((C \to A) \to (D \to A)).$$

We check the three systems.

1. In Nicod's axiom, $E \mid E$ is $\neg E$, so $E \mid (E \mid E)$ is $\neg (E \land \neg E)$, which is always true.
2. For any $X$, the formula $1 \mid X$ is $\neg X$.
   Also $(A \mid D) \mid (A \mid D)$ is $A \land D$, and $(D \mid B) \mid (A \land D)$ is $\neg (\neg (D \land B) \land A \land D)$, which is $(A \land D) \to B$.
3. The formula $A \mid (B \mid C)$ is $\neg (A \land \neg (B \land C))$, which is $A \to (B \land C)$.
4. Since $P \mid \neg X$ is $P \to X$, steps 1 to 3 show that Nicod's axiom has the truth table of $(A \to (B \land C)) \to ((A \land D) \to B)$.
5. This formula is a tautology: if $A \to (B \land C)$ and $A \land D$ are true, then $A$ is true, so $B \land C$ is true, so $B$ is true.
6. Nicod's rule preserves truth: if $A$ and $A \to (B \land C)$ are true, then $B \land C$ is true, so $C$ is true.
7. Meredith's axiom is a tautology, and we show it by contradiction.
   Suppose that it is false under some assignment.
   Then $E \to A$ and $D$ are true, $A$ is false, and the antecedent $X \to E$ is true, where $X$ is $((A \to B) \to (\neg C \to \neg D)) \to C$.
8. As $A$ is false and $E \to A$ is true, $E$ is false.
   As $X \to E$ is true, $X$ is false, so $C$ is false and $(A \to B) \to (\neg C \to \neg D)$ is true.
9. But $A \to B$ is true because $A$ is false, and $\neg C \to \neg D$ is false because $\neg C$ is true and $\neg D$ is false.
   So $(A \to B) \to (\neg C \to \neg D)$ is false, a contradiction.
10. Łukasiewicz's axiom is a tautology.
    If it were false, then $C \to A$ and $D$ would be true, $A$ false, and $(A \to B) \to C$ true.
    As $A$ is false, $A \to B$ is true, so $C$ is true, and then $C \to A$ is false, a contradiction.
11. A full truth table check, over the $2^5 = 32$ assignments of values to $A, \dots, E$, gives the same results as steps 5, 7 and 10.

## Remarks

### Sound, and also complete

Each of the three systems is sound by the checks above, and each is also complete for its language.
Nicod's and Meredith's systems derive every tautology in their connectives.
Łukasiewicz's system has the same theorems as the [[implicational propositional calculus|ZMVBAY7ZZD]].
Completeness is the hard part, and it is not proved here.

### Nicod's rule is not modus ponens

The major premise of Nicod's rule is $A \mid (B \mid C)$, which means $A \to (B \land C)$, and the rule keeps only the part $C$ of the conclusion.
With $B = C$ the premise means $A \to C$, and the rule becomes ordinary modus ponens.
So a single axiom in the stroke needs a stronger rule to make up for the missing connectives.

### History

Nicod gave his single axiom for the Sheffer stroke in 1917.
Łukasiewicz found his single axiom for the implicational calculus in 1948.
Wolfram found the single equational axiom $((a \mid b) \mid c) \mid (a \mid ((a \mid c) \mid a)) = c$ for Boolean algebra by a search of short identities in the Sheffer stroke.
McCune and coauthors proved, by automated theorem proving, that it is a single axiom for Boolean algebra.

### Watch out

A long axiom copied with a bracket in the wrong place is often not a tautology.
Move one bracket in Łukasiewicz's axiom and you get $((A \to B) \to C) \to (((C \to A) \to D) \to A)$.
At $A = 0$ and $C = 1$ we get
$$(A \to B) \to C = 1 \to 1 = 1, \qquad ((C \to A) \to D) \to A = (0 \to D) \to 0 = 1 \to 0 = 0,$$
so the whole formula is $1 \to 0 = 0$, and it is not a tautology.
Check each copy with a full truth table before you use it.

## Explanations

### L1 human

The usual Hilbert systems have three or more axiom patterns.
These systems show that one pattern is enough, if it is long and chosen with care.
Each pattern here is always true, so the system proves only true formulas.
The hard fact, which takes long proofs, is that the one pattern and the one rule prove every always-true formula.

### L2 human

We check one instance of Nicod's rule with small formulas.

1. Take $A := p$, $B := q$, $C := q$, so the premises are $p$ and $p \mid (q \mid q)$.
2. The formula $q \mid q$ is $\neg q$, so $p \mid (q \mid q)$ is $\neg (p \land \neg q)$, that is, $p \to q$.
3. The rule gives $q$ from $p$ and $p \to q$, which is ordinary modus ponens.

So Nicod's rule includes modus ponens as the case $B = C$.
The typical use of single axioms is in the study of axiom systems: their length, their independence, and the search for short systems.
