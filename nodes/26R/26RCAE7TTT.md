---
tag: 26RCAE7TTT
kind: example
name: A natural-deduction proof that p ∧ q implies q ∧ p
msc: ["03B05", "03F03"]
topics: [PM1AYWABA7]
audience: school
instance_of: [025YZN3VJW]
uses: [025YZN3VJW, 6KT3BJZ7D1, FJN3XDRXAR]
sources:
  - url: https://en.wikipedia.org/wiki/Conjunction_introduction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Conjunction_elimination
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.4
---

## Example

If you know "it is cold and it is windy", you also know "it is windy and it is cold".
We prove the general form $(p \land q) \to (q \land p)$ with the rules of [[conjunction|025YZN3VJW]] in [[natural deduction|6KT3BJZ7D1]].
Each line gives a formula and the rule that justifies it.

1. $p \land q$, an assumption, to be discharged in line 5.
2. $q$, by conjunction elimination (right) from line 1.
3. $p$, by conjunction elimination (left) from line 1.
4. $q \land p$, by [[conjunction introduction|FJN3XDRXAR]] from lines 2 and 3.
5. $(p \land q) \to (q \land p)$, by implication introduction, since line 4 was derived from the assumption in line 1.

## Remarks

The derivation uses all three rules of conjunction and proves one direction of commutativity.
The other direction, $(q \land p) \to (p \land q)$, has the same proof with $p$ and $q$ exchanged, and together they give $p \land q \equiv q \land p$.

The truth table gives the same fact: $p \land q$ and $q \land p$ are both T in the row TT and both F in the other three rows.
The derivation has one advantage over the table: it uses only the rules of conjunction and implication, so it is valid in [[intuitionistic logic|Q11N8X99FK]] too.

In Lean's Mathlib the derivation is the term `fun h => And.intro (And.right h) (And.left h)`.
It is a function that takes a proof `h` of `p ∧ q` and builds a proof of `q ∧ p`.

## Explanations

### L1 human

Suppose we know two facts together: "it is cold and it is windy".
Then we know "it is cold" by itself, and we know "it is windy" by itself.
Putting them back together in the other order gives "it is windy and it is cold".
The proof above writes these three moves as three rules.

### L2 human

Prove associativity in one direction, $((p \land q) \land r) \to (p \land (q \land r))$.

1. $(p \land q) \land r$, an assumption.
2. $p \land q$, by elimination (left) from line 1.
3. $r$, by elimination (right) from line 1.
4. $p$, by elimination (left) from line 2.
5. $q$, by elimination (right) from line 2.
6. $q \land r$, by introduction from lines 5 and 3.
7. $p \land (q \land r)$, by introduction from lines 4 and 6.
8. The implication, by implication introduction, discharging line 1.

Derivations like this show that a law follows from the rules alone, without truth values.
Watch out: an elimination rule applies only to the main connective of a line.
Line 1 does not give $q$ in one step, because its main connective joins $p \land q$ and $r$, so line 2 must come first.
