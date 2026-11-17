---
tag: 025YZN3VJW
kind: concept
name: Conjunction
aliases: [logical-and]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_conjunction
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
  - book: isbn:9781108439534
    locator: Section 3.4
same_as:
  wikidata: Q191081
  wikipedia: Logical conjunction
---

## Summary

The conjunction of two [[propositions|0ZGC7ZESYN]] $p$ and $q$ is the proposition $p \land q$, read "$p$ and $q$", which is true when $p$ and $q$ are both true and false in the three other cases.
Conjunction is a [[logical connective|QS0XVAN9BG]] with two inputs; the precise definition and the truth table are on the page [[conjunction (definition)|0M28ASWG8T]].
To prove $p \land q$, we prove $p$ and we prove $q$; from $p \land q$, we may use $p$ and we may use $q$.
Conjunction is how mathematics lists several conditions at once, in definitions, in hypotheses and in chained inequalities.

## Motivation

Most definitions ask for several conditions together.
An integer $n$ is prime when $n > 1$ and the only positive divisors of $n$ are $1$ and $n$.
A function is a bijection when it is injective and surjective.
A theorem often has a list of hypotheses, and the list means that all of them hold.
To check such a definition or to use such a theorem, we must know exactly when a list of conditions holds: when each condition in the list holds.
The connective $\land$ states this rule for two conditions, and longer lists are repeated conjunctions.

## Notation

This sub-area writes $p \land q$.
Other notations are $p \,\&\, q$, $p \cdot q$ and $pq$; the last two come from the arithmetic of truth values, where $p \land q$ is the product of $p$ and $q$ in $\{0, 1\}$.
In programming, conjunction is often written `p && q`.
In English, conjunction is expressed by "and", "but", "both ... and", "although", "while" and by commas in a list of hypotheses.
The chain $a < b < c$ abbreviates $a < b \land b < c$.
"Neither $p$ nor $q$" is the conjunction $\neg p \land \neg q$.
In Lean's Mathlib, the conjunction of `a` and `b` is `And a b`, written `a ∧ b`.

## Remarks

### Examples

1. [[The chained inequality $1 < x < 4$ is a conjunction|~518b2b1d]]: it means "$1 < x$ and $x < 4$".
2. [[A natural-deduction proof that $p \land q$ implies $q \land p$|~1e3ca695]]: the rules of conjunction prove its commutativity.
3. "$6$ is even and $6$ is divisible by $3$" is true, because both parts are true.
4. [[The word "but" in "the absolute value is continuous but not differentiable at $0$"|HW5E2DSZH3]]: "but" is a conjunction with a contrast.
5. "$n$ is prime" means "$n > 1$ and $n$ has no positive divisor other than $1$ and $n$". For $n = 1$ the first part fails, so $1$ is not prime.

### Non-examples

1. [[The condition $x^2 = 4$ is a disjunction, not a conjunction|~92fe75b8]]: "the solutions are $2$ and $-2$" does not mean "$x = 2$ and $x = -2$".
2. [[In "$2$ and $3$ are coprime", the word "and" is not a connective|R4D9KAT2QH]]: it joins two numbers in one relation, not two propositions.
3. "Add $2$ and then multiply by $3$" is a command with an order of steps, not a proposition. A conjunction does not depend on the order of its parts.

### Rules of inference for conjunction

In [[natural deduction|6KT3BJZ7D1]], conjunction has one introduction rule and two elimination rules.

1. [[Conjunction introduction|FJN3XDRXAR]]: from $p$ and $q$, conclude $p \land q$. In Mathlib this rule is `And.intro`.
2. Conjunction elimination (left): from $p \land q$, conclude $p$. In Mathlib this rule is `And.left`.
3. Conjunction elimination (right): from $p \land q$, conclude $q$. In Mathlib this rule is `And.right`.

The proof method follows the rules: a proof of $p \land q$ has two parts, one for $p$ and one for $q$, and a hypothesis $p \land q$ gives two separate hypotheses $p$ and $q$.
These rules hold in [[intuitionistic logic|Q11N8X99FK]] as well as in classical logic.

### Basic properties

The symbol $\equiv$ means [[logical equivalence|0JMR2HM2N2]], and $\top$ and $\bot$ stand for a true and a false proposition.

1. Commutativity: $p \land q \equiv q \land p$.
2. Associativity: $(p \land q) \land r \equiv p \land (q \land r)$, so we may write $p \land q \land r$ without brackets. It is true exactly when all three parts are true.
3. Idempotence: $p \land p \equiv p$.
4. Identity and domination: $p \land \top \equiv p$ and $p \land \bot \equiv \bot$.
5. Distributivity: $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$, with [[disjunction|0F72FK8EKB]].
6. Negation: $\neg(p \land q) \equiv \neg p \lor \neg q$, by [[De Morgan's laws|09PKJKA6J0]].
7. Sets: $x \in A \cap B$ means $x \in A \land x \in B$, so conjunction corresponds to [[intersection|0ZNMMA9TF5]].

The full list is on the page [[laws of propositional logic|~5fa904ea]].

### History

George Boole wrote the conjunction of two classes as a product $xy$ in his algebra of logic of 1847 and 1854.
Gottlob Frege, in his Begriffsschrift of 1879, used negation and the conditional as the only basic connectives and expressed "$p$ and $q$" as $\neg(p \to \neg q)$.
The introduction and elimination rules come from Gerhard Gentzen's natural deduction of the 1930s.

### Common errors

1. A student reads "the solutions are $2$ and $-2$" as "$x = 2$ and $x = -2$". No number is equal to both, so the correct form is "$x = 2$ or $x = -2$".
2. A student proves only one part of a conjunction. A proof of "$f$ is a bijection" needs a proof of injectivity and a proof of surjectivity.
3. A student negates "$p$ and $q$" as "not $p$ and not $q$". The negation is "not $p$ or not $q$".

## Explanations

### L1 human

A claim with "and" is true only when both parts are true.
"$10$ is even and $10$ is bigger than $5$" is true, because both parts are true.
"$10$ is even and $10$ is bigger than $50$" is false, because the second part is false.
One false part is enough to make the whole claim false.
The order of the parts does not matter: "$10$ is bigger than $5$ and $10$ is even" says the same thing.

### L2 human

We prove that for every integer $n$, if $n$ is divisible by $6$, then $n$ is even and $n$ is divisible by $3$.

1. Assume $n$ is divisible by $6$, so $n = 6k$ for an integer $k$.
2. The goal is a conjunction, so we prove its two parts separately.
3. First part: $n = 2(3k)$, so $n$ is even.
4. Second part: $n = 3(2k)$, so $n$ is divisible by $3$.
5. By conjunction introduction, $n$ is even and $n$ is divisible by $3$.

The typical use of conjunction in proofs is this split of the goal, and the matching split of a hypothesis into its parts.

A trap: the converse also holds here, but its proof is not a conjunction elimination.
From "$n$ is even and divisible by $3$" we get $n = 2a$ and $3 \mid 2a$, and since $3$ does not divide $2$, the prime $3$ divides $a$; so $6 \mid n$.
The rules of conjunction only split and join the parts; the arithmetic must come from elsewhere.

### L3 human

With truth values $0$ and $1$, conjunction is the minimum, and also the product, of its inputs.
In a [[Boolean algebra|0XADJKM699]] or a lattice, conjunction is the meet, the greatest lower bound; in the algebra of sets it is the intersection.
In hardware, conjunction is the AND [[logic gate|AMH914MF2A]].
A universal statement over a finite domain $\{a_1, \ldots, a_n\}$ is the conjunction $P(a_1) \land \cdots \land P(a_n)$, so the [[universal quantifier|0GHS47PDAQ]] generalizes conjunction to arbitrary domains.
In type theory, a proof of $p \land q$ is a pair of a proof of $p$ and a proof of $q$; Mathlib's `And` is a structure with the two fields `left` and `right`, so conjunction is a product type.
In category theory, the same pattern is the product: $p \land q$ is the product of $p$ and $q$ in the poset of propositions ordered by implication.
