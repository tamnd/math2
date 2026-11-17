---
tag: 0V4QXPGJQK
kind: concept
name: Vacuous truth
msc: ["03B05", "03B10"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZNX6DQ3EJ, 0B88PQTJ66, 0ECVK59Y03]
sources:
  - url: https://en.wikipedia.org/wiki/Vacuous_truth
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
  - book: isbn:9781108439534
    locator: Section 2.2
same_as:
  wikidata: Q1096079
  wikipedia: Vacuous truth
---

## Summary

A statement is vacuously true when it is true only because its condition is satisfied by nothing.
There are two forms.
First, an [[implication|0ZNX6DQ3EJ]] $p \to q$ with a false antecedent $p$ is true, whatever the truth value of $q$, by the truth table of the [[material implication|0NMG7W7Q11]].
Second, a restricted universal statement $\forall x \in A \; P(x)$, which means $\forall x \, (x \in A \to P(x))$, is true when $A$ is the [[empty set|0ECVK59Y03]], whatever the [[predicate|0QHEWQD30B]] $P$ is, because each instance $a \in A \to P(a)$ has a false antecedent.
More generally, $\forall x \, (H(x) \to P(x))$ is vacuously true when no element of the domain satisfies $H$.
Vacuous truth lets general definitions and theorems hold without exceptions for empty sets and impossible cases, for example in the fact that the empty set is a [[subset|0BJR9QR08E]] of every set.

## Motivation

A universal statement is false exactly when it has a [[counterexample|0ED72CTBNP]].
A counterexample to "every element of $A$ has the property $P$" is an element of $A$ without the property $P$.
When $A$ is empty, there is no element of $A$ at all, so there is no counterexample, and the statement is true.

The same reasoning fixes the truth value of an implication with a false antecedent.
The theorem "for every integer $n$, if $4 \mid n$, then $n$ is even" is true, so each of its instances must be true.
The instances $n = 6$ and $n = 7$ have a false antecedent, and their consequents are true and false.
So both rows "F, T" and "F, F" of the truth table of $p \to q$ must give T, and this is the definition that logic uses.

A second reason is uniformity.
The theorem "if $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$" should hold for all sets, including $A = \varnothing$.
With vacuous truth it holds without a special case.

## Notation

Vacuous truth has no symbol of its own.
The two forms are the truth table rows $(\mathrm{F} \to q) = \mathrm{T}$ for both values of $q$, and the equivalence of $\forall x \in \varnothing \; P(x)$ with the constant true proposition, often written $\top$.
Authors say that such a statement is "vacuously true" or that it "holds vacuously".
Many books use the word "trivial" for a different case: they call an implication $p \to q$ trivial when its consequent $q$ is true, as in "if $n$ is prime, then $n = n$".
The reading of quantifiers in mathematical English is on the page [[quantifiers in mathematical writing|EGTZPA6QH3]].

## Remarks

### Examples

1. [[The empty set is a subset of every set|AF3SAHVDR4]]: the defining statement $\forall x \, (x \in \varnothing \to x \in B)$ has a false antecedent for each $x$.
2. [[Every prime number between 24 and 28 is even|1SWS4DH1KK]]: there is no prime number $n$ with $24 < n < 28$, so the statement is vacuously true.
3. "If $2 + 2 = 5$, then $7$ is even" is true, because its antecedent is false.
4. The empty function $f \colon \varnothing \to B$ is [[injective|09NWETVTNY]]: the condition "for all $a, b \in \varnothing$, if $f(a) = f(b)$, then $a = b$" ranges over the empty set.
5. Every real number $b$ is an upper bound of $\varnothing$, because "$x \le b$ for all $x \in \varnothing$" holds vacuously. For this reason the empty set has no [[supremum|0R3H5PANRQ]] in $\mathbb{R}$.

### Non-examples

1. [[An existential statement over the empty set is false|CHKD0587G6]]: "some element of $\varnothing$ is even" needs a witness, and there is none.
2. "If $2$ is even, then $4$ is even" is true, but not vacuously: its antecedent is true, and the consequent is checked.
3. "Every element of $\{0\}$ is even" is true, but not vacuously: the set has the element $0$, and $0 = 2 \cdot 0$ is even.

### Basic properties

1. For each predicate $P$, both $\forall x \in \varnothing \; P(x)$ and $\forall x \in \varnothing \; \neg P(x)$ are true. This is not a contradiction: the negation of $\forall x \in \varnothing \; P(x)$ is $\exists x \in \varnothing \; \neg P(x)$, by the [[negation of a universal statement|0P3A06QNDP]], and that statement is false.
2. The implication from $\forall x \in A \; P(x)$ to $\exists x \in A \; P(x)$ holds for every predicate $P$ exactly when $A$ is nonempty. For $A = \varnothing$ the first statement is true and the second is false.
3. The formula $\neg p \to (p \to q)$ is a [[tautology|05006AJ7DZ]]. It is valid in [[intuitionistic logic|Q11N8X99FK]] too, because it follows from [[explosion|TTKZGJEEK7]]. In Lean, a proof of an implication with a false hypothesis uses `absurd` or the elimination of `False`.
4. A vacuously true statement gives no information about its consequent. From "if $1 = 2$, then $q$" we cannot conclude anything about $q$.
5. If $A \subseteq B$ and $\forall x \in B \; P(x)$, then $\forall x \in A \; P(x)$. With $A = \varnothing$ this is a vacuous case, and the general rule needs no exception.

### History

Philo of Megara proposed the truth condition of the material conditional, under which a conditional with a false antecedent is true.
In the traditional logic that follows Aristotle, "every $A$ is $B$" was often read as implying that some $A$ exists.
Modern logic, from Frege's Begriffsschrift of 1879 on, reads "every $A$ is $B$" as $\forall x \, (A(x) \to B(x))$, which is true when nothing is an $A$.

### Common errors

1. A student thinks that "every element of $\varnothing$ is even" is false or meaningless. It is true, because there is no counterexample.
2. A student concludes "$S$ has a positive element" from "every element of $S$ is positive" without checking that $S$ is nonempty.
3. A student uses a vacuous implication as evidence for its consequent. "If $0 = 1$, then the Riemann hypothesis holds" is true and says nothing about the Riemann hypothesis.

## Explanations

### L1 human

"All the unicorns in this room are blue" is true when the room has no unicorns.
To break the claim, someone would have to show a unicorn in the room that is not blue.
No such unicorn exists, so the claim cannot be broken, and it counts as true.
In the same way, "every whole number between $24$ and $28$ that is prime is even" is true, because $25$, $26$ and $27$ are not prime.
A promise "if it snows in July here, I will pay you $100$" is not broken in a year without snow in July.

### L2 human

We decide whether "every real solution of $x^2 + 1 = 0$ is greater than $100$" is true.

1. Write the statement as $\forall x \in S \; (x > 100)$, where $S = \{x \in \mathbb{R} \mid x^2 + 1 = 0\}$.
2. For each real $x$, $x^2 \ge 0$, so $x^2 + 1 \ge 1 > 0$. So $S = \varnothing$.
3. The statement means $\forall x \in \mathbb{R} \; (x \in S \to x > 100)$. For each real $x$, the antecedent $x \in S$ is false, so the implication is true.
4. So the statement is vacuously true.

The same steps show that "every real solution of $x^2 + 1 = 0$ is less than $0$" is true.
The typical use of vacuous truth is at the edges of a general argument: an empty set, a base case with no elements, or a case that the hypotheses exclude.
A trap is to combine the two true statements of this example into "some real number is greater than $100$ and less than $0$"; this would need an element of $S$, and $S$ is empty.

### L3 human

In a [[Boolean algebra|0XADJKM699]] the least element $0$ satisfies $0 \le b$ for each $b$, and the implication $0 \to b = \neg 0 \lor b$ is the greatest element $1$.
A universal quantifier is a meet over the domain, and the meet of the empty family is $1$; an existential quantifier is a join, and the join of the empty family is $0$.
The same convention gives the empty sum $0$, the empty product $1$ and the empty intersection of subsets of $X$ equal to $X$.
In set theory and category theory, the empty set is an initial object: there is exactly one function from $\varnothing$ to each set, the empty function.

Classical first-order logic assumes that the domain is nonempty, so $\forall x \, P(x) \to \exists x \, P(x)$ is valid there, while the restricted form over a set $A$ keeps vacuous truth for $A = \varnothing$.
Free and inclusive logics allow empty domains and drop this validity.
The relevance logics reject vacuous implications such as $\neg p \to (p \to q)$, which are among the [[paradoxes of material implication|3T7ZJFC9QF]].
