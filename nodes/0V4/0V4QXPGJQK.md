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

A statement is vacuously true when it is true only because nothing satisfies its condition.
"Every prime number between 24 and 28 is even" is true, because $25$, $26$ and $27$ are not prime, so there is no prime there to break the claim.
Vacuous truth has two forms.
An [[implication|0ZNX6DQ3EJ]] $p \to q$ with a false antecedent $p$ is true whatever $q$ is, by the truth table of [[material implication|0NMG7W7Q11]].
A restricted universal statement $\forall x \in A \; P(x)$, which means $\forall x \, (x \in A \to P(x))$, is true when $A$ is the [[empty set|0ECVK59Y03]], whatever the [[predicate|0QHEWQD30B]] $P$ is.
More generally, $\forall x \, (H(x) \to P(x))$ is vacuously true when no element of the domain satisfies $H$.

## Motivation

A universal statement is false exactly when it has a [[counterexample|0ED72CTBNP]].
A counterexample to "every element of $A$ has property $P$" is an element of $A$ without property $P$.
When $A$ is empty there is no element of $A$ at all, so there is no counterexample, and the statement is true.

The same reasoning fixes the truth value of an implication with a false antecedent.
The theorem "for every integer $n$, if $4 \mid n$, then $n$ is even" is true, so each of its instances must be true.
For $n = 6$ the antecedent is false and the consequent is true, and for $n = 7$ both are false.
So the rows "F, T" and "F, F" of the truth table of $p \to q$ must both give T, and that is the definition logic uses.

The convention also keeps theorems free of exceptions.
"If $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$" should hold for all sets, including $A = \varnothing$, and with vacuous truth it does.
The fact that the empty set is a [[subset|0BJR9QR08E]] of every set is the best known case.

## Notation

Vacuous truth has no symbol of its own.
Its two forms are the truth table rows $(\mathrm{F} \to q) = \mathrm{T}$ for both values of $q$, and the equivalence of $\forall x \in \varnothing \; P(x)$ with the constant true proposition, often written $\top$.
Authors say that such a statement is "vacuously true" or that it "holds vacuously".
Many books use the word "trivial" for a different case, an implication $p \to q$ whose consequent $q$ is true, as in "if $n$ is prime, then $n = n$".
The reading of quantifiers in mathematical English is on the page [[quantifiers in mathematical writing|EGTZPA6QH3]].

## Remarks

### Checking a vacuous statement

Take "every prime number $n$ with $24 < n < 28$ is even", the example [[every prime number between 24 and 28 is even|1SWS4DH1KK]].
The integers in the range are $25 = 5 \cdot 5$, $26 = 2 \cdot 13$ and $27 = 3 \cdot 9$, and none of them is prime.
So for each $n$ in the range the implication "if $n$ is prime, then $n$ is even" has a false antecedent and is true.
The statement is true, and nobody had to check whether any number is even.
For the same reason "every prime number between 24 and 28 is odd" is also true.

### The empty set and other edge cases

[[The empty set is a subset of every set|AF3SAHVDR4]], because $\varnothing \subseteq B$ means $\forall x \, (x \in \varnothing \to x \in B)$, and every instance has a false antecedent.
The empty function $f \colon \varnothing \to B$ is [[injective|09NWETVTNY]], since the condition "for all $a, b \in \varnothing$, if $f(a) = f(b)$, then $a = b$" ranges over nothing.
Every real number $b$ is an upper bound of $\varnothing$, because "$x \le b$ for all $x \in \varnothing$" holds vacuously.
That is why the empty set has no [[supremum|0R3H5PANRQ]] in $\mathbb{R}$: there is no least upper bound among all real numbers.

### What is not vacuous

[[An existential statement over the empty set is false|CHKD0587G6]]: "some element of $\varnothing$ is even" needs a witness, and there is none.
The restricted existential form uses $\land$, not $\to$, and a conjunction with a false part is false.
"If $2$ is even, then $4$ is even" is true, but not vacuously, because its antecedent is true and the consequent had to be checked.
"Every element of $\{0\}$ is even" is also true but not vacuous, since $0 = 2 \cdot 0$ was checked.

### Both P and not P

For every predicate $P$, both $\forall x \in \varnothing \; P(x)$ and $\forall x \in \varnothing \; \neg P(x)$ are true.
This is not a contradiction.
The negation of $\forall x \in \varnothing \; P(x)$ is $\exists x \in \varnothing \; \neg P(x)$, by the [[negation of a universal statement|0P3A06QNDP]], and that statement is false.
It also follows that the step from $\forall x \in A \; P(x)$ to $\exists x \in A \; P(x)$ is valid for all $P$ exactly when $A$ is nonempty.

The formula $\neg p \to (p \to q)$, the propositional core of vacuous truth, is a [[tautology|05006AJ7DZ]].
It is valid in [[intuitionistic logic|Q11N8X99FK]] too, because it follows from [[explosion|TTKZGJEEK7]], and in Lean a proof of it uses `absurd`.

### Watch out

A vacuous implication gives no information about its consequent.
"If $0 = 1$, then the Riemann hypothesis holds" is true and says nothing about the Riemann hypothesis.
The opposite error is to call "every element of $\varnothing$ is even" false or meaningless; it is true, because no counterexample exists.
A third trap is to conclude "$S$ has a positive element" from "every element of $S$ is positive" without first checking that $S$ is nonempty.

### History

Philo of Megara proposed the truth condition of the material conditional, under which a conditional with a false antecedent is true.
In the traditional logic that follows Aristotle, "every $A$ is $B$" was often read as implying that some $A$ exists.
Modern logic, from Frege's Begriffsschrift of 1879 on, reads "every $A$ is $B$" as $\forall x \, (A(x) \to B(x))$, which is true when nothing is an $A$.

### Try it

Is "every perfect square $n$ with $50 < n < 60$ is divisible by $7$" true?
Yes, vacuously: $7^2 = 49$ and $8^2 = 64$, so no perfect square lies in the range.

Is "some real $x$ with $x^2 < 0$ is positive" true?
No: no real $x$ has $x^2 < 0$, so there is no witness, and an existential statement over an empty set is false.

## Explanations

### L1 human

"All the unicorns in this room are blue" is true when the room has no unicorns.
To break the claim, someone would have to show a unicorn in the room that is not blue.
No such unicorn exists, so the claim cannot be broken, and it counts as true.
A promise "if it snows here in July, I will pay you 100 dollars" is not broken in a year without snow in July.

### L2 human

Decide whether "every real solution of $x^2 + 1 = 0$ is greater than $100$" is true.
Write the statement as $\forall x \in S \; (x > 100)$, where $S = \{x \in \mathbb{R} \mid x^2 + 1 = 0\}$.
For each real $x$ we have $x^2 \ge 0$, so
$$x^2 + 1 \ge 1 > 0,$$
and $S = \varnothing$.
The statement means $\forall x \in \mathbb{R} \; (x \in S \to x > 100)$, and every antecedent $x \in S$ is false, so every instance is true.
The statement is vacuously true, and by the same steps "every real solution of $x^2 + 1 = 0$ is less than $0$" is true.
Vacuous truth turns up at the edges of a general argument: an empty set, a base case with no elements, or a case that the hypotheses exclude.
Watch out: combining the two true statements into "some real number is greater than $100$ and less than $0$" would need an element of $S$, and $S$ is empty.

### L3 human

In a [[Boolean algebra|0XADJKM699]] the least element $0$ satisfies $0 \le b$ for each $b$, and the implication $0 \to b = \neg 0 \lor b$ is the greatest element $1$.
A universal quantifier is a meet over the domain, and the meet of the empty family is $1$; an existential quantifier is a join, and the join of the empty family is $0$.
The same convention gives the empty sum $0$, the empty product $1$, and the empty intersection of subsets of $X$ equal to $X$.
In set theory and category theory the empty set is an initial object: there is exactly one function from $\varnothing$ to each set, the empty function.

Classical first-order logic assumes that the domain is nonempty, so $\forall x \, P(x) \to \exists x \, P(x)$ is valid there, while the restricted form over a set $A$ keeps vacuous truth for $A = \varnothing$.
Free and inclusive logics allow empty domains and drop this validity.
Relevance logics reject vacuous implications such as $\neg p \to (p \to q)$, which are among the [[paradoxes of material implication|3T7ZJFC9QF]].
