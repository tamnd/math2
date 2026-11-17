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

We prove $(p \land q) \to (q \land p)$ with the rules of [[conjunction|025YZN3VJW]] in [[natural deduction|6KT3BJZ7D1]].
Each line gives a formula and the rule that justifies it.

1. $p \land q$. Assumption, to be discharged in line 5.
2. $q$. Conjunction elimination (right), from line 1.
3. $p$. Conjunction elimination (left), from line 1.
4. $q \land p$. [[Conjunction introduction|FJN3XDRXAR]], from lines 2 and 3.
5. $(p \land q) \to (q \land p)$. Implication introduction, from the derivation of line 4 from the assumption in line 1.

## Remarks

The example shows the three rules of conjunction at work, and it proves one direction of commutativity.
The other direction, $(q \land p) \to (p \land q)$, has the same proof with $p$ and $q$ exchanged.
Together they give $p \land q \equiv q \land p$.

The same fact follows from the truth table: $p \land q$ and $q \land p$ are both T in the row TT and both F in the other three rows.
The derivation has an advantage over the table: it uses only the rules of conjunction and implication, so it is also valid in [[intuitionistic logic|Q11N8X99FK]].

In Lean's Mathlib, the derivation is the term `fun h => And.intro (And.right h) (And.left h)`: the function takes a proof `h` of `p ∧ q` and builds a proof of `q ∧ p`.

For a mathematical instance, take $p$: "$n$ is even" and $q$: "$n$ is divisible by $3$".
From "$n$ is even and divisible by $3$" the derivation gives "$n$ is divisible by $3$ and even", with no arithmetic.

## Explanations

### L1 human

Suppose we know two facts together: "it is cold and it is windy".
Then we know "it is cold" by itself, and we know "it is windy" by itself.
Putting them back together in the other order gives "it is windy and it is cold".
The proof above writes these three moves as three rules.

### L2 human

We prove associativity in one direction: $((p \land q) \land r) \to (p \land (q \land r))$.

1. $(p \land q) \land r$. Assumption.
2. $p \land q$. Conjunction elimination (left), from line 1.
3. $r$. Conjunction elimination (right), from line 1.
4. $p$. Conjunction elimination (left), from line 2.
5. $q$. Conjunction elimination (right), from line 2.
6. $q \land r$. Conjunction introduction, from lines 5 and 3.
7. $p \land (q \land r)$. Conjunction introduction, from lines 4 and 6.
8. $((p \land q) \land r) \to (p \land (q \land r))$. Implication introduction, discharging line 1.

The typical use of such derivations is to show that a law holds from the rules alone, without truth values.

A trap: the elimination rules apply to the main connective of a line only.
From line 1 we cannot get $q$ in one step, because the main connective of line 1 joins $p \land q$ and $r$; we first need line 2.
