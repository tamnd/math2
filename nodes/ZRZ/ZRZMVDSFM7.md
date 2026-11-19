---
tag: ZRZMVDSFM7
kind: example
name: Double negation elimination is not an admissible rule of IPC
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: research
not_instance_of:
  - target: C5K35H0R4Y
    note: the rule from not not p to p is not admissible in IPC, since a substitution makes its premise a theorem and its conclusion a non-theorem
uses: [C5K35H0R4Y, B9M3P61ZVA, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Admissible_rule
    locator: Definitions
  - url: https://en.wikipedia.org/wiki/Intuitionistic_logic
    locator: Double negations
---

## Example

We show that the rule $\neg \neg p / p$ is not admissible in $\mathsf{IPC}$; see [[admissible rules|C5K35H0R4Y]].

1. Let $\sigma p = q \vee \neg q$.
2. The premise becomes $\neg \neg (q \vee \neg q)$, which is a theorem of $\mathsf{IPC}$.
3. To check step 2, assume $\neg (q \vee \neg q)$. From $q$ we get $q \vee \neg q$ and a contradiction, so $\neg q$.
4. Then $q \vee \neg q$ follows from $\neg q$, which contradicts the assumption. So $\neg \neg (q \vee \neg q)$ is a theorem.
5. The conclusion becomes $q \vee \neg q$, which is not a theorem of $\mathsf{IPC}$, as the [[law of excluded middle|0RYYK8PG4S]] fails intuitionistically.
6. So the rule maps a theorem to a non-theorem, and it is not admissible.

## Remarks

The identity substitution does not refute admissibility, since $\neg \neg p$ is not a theorem.
The definition quantifies over all substitutions, and one bad substitution is enough.
By [[Glivenko's theorem|B9M3P61ZVA]], $\neg \neg A$ is a theorem of $\mathsf{IPC}$ whenever $A$ is a classical tautology.
So every substitution instance of a classical tautology that is not an intuitionistic theorem refutes the rule.

## Explanations

### L1 human

"It is not refutable that $p$" does not give a proof of $p$ in intuitionistic logic.
Even as a rule between theorems it fails: "$q$ or not $q$" is not refutable, but it is not provable either.

### L2 human

1. To refute admissibility, search for a substitution that makes the premise provable.
2. Classical tautologies are good candidates, by Glivenko's theorem.
3. Then check that the conclusion is not provable, for instance with a Kripke countermodel.

The typical use is to see the difference between admissible rules and classically valid rules.
A trap: the rule is valid classically, and the identity substitution gives no counterexample.
