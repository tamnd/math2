---
tag: 0QAJHFGZZJ
kind: concept
name: Uniqueness quantifier
aliases: [unique-existential-quantifier, uniqueness-quantification]
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
uses: [0QHEWQD30B, 0GHS47PDAQ, 0MSRQHCNN9, E918704SKV]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
same_as:
  wikidata: Q2502253
  wikipedia: Uniqueness quantification
---

## Summary

The uniqueness quantifier says "exactly one": "there is exactly one $x$ such that $P(x)$" claims that some element has the property and that no second element has it.
"Exactly one number from $1$ to $10$ is even and a multiple of $5$" is true, because $10$ has both properties and the only other multiple of $5$ in the range, $5$, is odd.
"Exactly one number from $1$ to $10$ is a multiple of $5$" is false, because $5$ and $10$ both are.
In general, let $D$ be a domain of discourse and $P(x)$ a [[predicate|0QHEWQD30B]] on $D$.
The proposition $\exists! x \, P(x)$ is true when exactly one $a \in D$ makes $P(a)$ true, and false otherwise.
In first-order logic it is an abbreviation built from the [[existential quantifier|0MSRQHCNN9]], the [[universal quantifier|0GHS47PDAQ]] and [[equality|E918704SKV]]:
$$\exists! x \, P(x) \quad \text{means} \quad \exists x \, \bigl( P(x) \land \forall y \, ( P(y) \to y = x ) \bigr).$$
The [[formal definition|0N3ADS4CHH]] states this with every condition.

## Motivation

The formula $\exists x \, P(x)$ says "at least one", and $\forall x \, P(x)$ says "all".
Mathematics often needs "exactly one", as in "each real number has exactly one cube root" or in the definition of a [[function|0EPAT51DXQ]].
"Exactly one" is "at least one" together with "at most one", and "at most one" says that any two elements with the property are equal, so it needs the equality sign.
The uniqueness quantifier is also the logical form of the word "the".
"The identity element", "the limit" and "the solution" are allowed only after the matching statement $\exists! x \, P(x)$ has been proved.

## Notation

The standard symbol is $\exists! x \, P(x)$, and some books write $\exists_1 x \, P(x)$ or $\exists^{=1} x \, P(x)$.
The restricted form $\exists! x \in A \; P(x)$ means $\exists! x \, (x \in A \land P(x))$, with a conjunction and not an implication.
There are two equivalent expansions:
$$\text{(A)} \quad \exists x \, \bigl( P(x) \land \forall y \, ( P(y) \to y = x ) \bigr),$$
$$\text{(B)} \quad \exists x \, P(x) \;\land\; \forall x \, \forall y \, \bigl( P(x) \land P(y) \to x = y \bigr).$$
Form (A) names the unique element, and form (B) separates existence from uniqueness.
In Mathlib, `ExistsUnique` is defined by form (A), and `∃! x, P x` is notation for it.

## Remarks

### A first check on a small domain

Let $D = \{1, 2, 3, 4, 5, 6\}$ and let $P(x)$ be "$x$ divides $6$ and $x > 3$".
The divisors of $6$ in $D$ are $1, 2, 3, 6$, and of these only $6$ is greater than $3$, so the truth set is $\{6\}$.
Form (A) holds with $x = 6$: $P(6)$ is true, and $P(y)$ is false for every $y \neq 6$ in $D$.
So $\exists! x \in D \; P(x)$ is true.
Change $P(x)$ to "$x$ divides $6$ and $x > 1$", and the truth set becomes $\{2, 3, 6\}$.
Existence still holds, but uniqueness fails with $x = 2$ and $y = 3$, so the $\exists!$ statement is false.
In general, $\exists! x \, P(x)$ is true exactly when the truth set $\{x \in D : P(x)\}$ has exactly one element.

### Examples

[[The equation $x^2 = x + 2$ has exactly one natural solution|QMYHS34Z1G]], namely $2$, while over $\mathbb{Z}$ the second solution $-1$ makes $\exists!$ false.
[[The definition of a function uses the uniqueness quantifier|P4NCHC44NJ]]: a relation $f \subseteq X \times Y$ is a function when $\forall x \in X \; \exists! y \in Y \; (x, y) \in f$.
Over $\mathbb{Z}$, $\exists! p \, (p \text{ is prime} \land p \text{ is even})$ is true, because each even $n > 2$ has the divisor $2$.
$\exists! x \in \mathbb{R} \; (x^3 = 8)$ is true, because $x \mapsto x^3$ is strictly increasing and $2^3 = 8$.

### What is not "exactly one"

[[The formula $\exists x \, \forall y \, (P(y) \to y = x)$ says "at most one"|KGGR81G9DV]], and it is true for a predicate with no witness, so it is not $\exists! x \, P(x)$.
[[The equation $x^2 = 4$ has a solution but not exactly one|A82V4N0G1P]]: over $\mathbb{R}$ the solutions are $2$ and $-2$, so uniqueness fails.
The formula $\exists x \, \bigl( P(x) \land \forall y \, ( y = x ) \bigr)$ says that the whole domain has one element and that this element has property $P$.
Over $\mathbb{N}$ with $P(x)$ meaning $x = 0$, it is false, although $\exists! x \, P(x)$ is true.

### The rules you can use

Forms (A) and (B) are equivalent.
From (A), take $a$ with $P(a)$ and $\forall y \, (P(y) \to y = a)$; then $a$ is a witness for $\exists x \, P(x)$, and any $x, y$ with $P(x)$ and $P(y)$ satisfy $x = a = y$.
From (B), take $a$ with $P(a)$; for any $y$ with $P(y)$, the second conjunct applied to $y$ and $a$ gives $y = a$, so $a$ is a witness for (A).
Neither direction uses the [[law of excluded middle|0RYYK8PG4S]], so the equivalence also holds in [[intuitionistic logic|Q11N8X99FK]].
$\exists! x \, P(x)$ implies $\exists x \, P(x)$, and the converse fails, as $x^2 = 4$ shows.
By form (B), [[De Morgan's laws|09PKJKA6J0]] and the [[negation of a universal statement|0P3A06QNDP]], the negation of $\exists! x \, P(x)$ is $\forall x \, \neg P(x) \lor \exists x \, \exists y \, (P(x) \land P(y) \land x \neq y)$.
Proofs of such statements prove existence first and uniqueness second; see [[existence and uniqueness statements|ACSC75R7R5]] and [[proof of uniqueness|GQHHNV79PA]].

### Watch out

Writing $\exists x \, \forall y \, (P(y) \to y = x)$ for "exactly one" omits $P(x)$ and says only "at most one".
Writing $\exists! x \in A \; P(x)$ as $\exists! x \, (x \in A \to P(x))$ is also wrong.
Over $\mathbb{Z}$ with $A = \{1\}$ and $P(x)$ meaning $x > 0$, the first is true, but every integer satisfies the implication, $1$ because $1 > 0$ and the others vacuously, so the second is false.
On a two-element domain $\{a, b\}$, $\exists! x \, P(x)$ is equivalent to the [[exclusive or|PTMR3P9J6C]] $P(a) \oplus P(b)$, but on three elements $P(a) \oplus P(b) \oplus P(c)$ is also true when all three instances are true.
Finally, $\exists! x \, \exists! y \, P(x, y)$ does not say "exactly one pair".

### History

Gottlob Frege introduced quantifiers with bound variables in his Begriffsschrift of 1879, and together with equality they can express "exactly one".
Bertrand Russell analyzed the word "the" in 1905 as a claim of existence and uniqueness, in his theory of [[definite descriptions|PD2R4XT79Q]].

### Try it

Is $\exists! x \in \mathbb{Z} \; (x^2 = 2x)$ true?
No: $x^2 - 2x = x(x - 2)$, so both $0$ and $2$ are solutions.

Is $\exists! x \in \mathbb{R} \; (2x + 1 = 7)$ true?
Yes: $x = 3$ works, and $2x + 1 = 7 = 2y + 1$ gives $x = y$.

## Explanations

### L1 human

"Exactly one" says two things: "at least one" and "not two different ones".
Among the numbers from $1$ to $10$, ask which are even and a multiple of $5$.
The number $10$ is, so there is at least one.
The only other multiple of $5$ in the list is $5$, and $5$ is odd, so there is no second one.
So "exactly one number from $1$ to $10$ is even and a multiple of $5$" is true.

### L2 human

Prove $\exists! x \in \mathbb{R} \; (x^3 = -27)$ with form (A).
The candidate is $a = -3$, and $(-3)^3 = -27$, which gives existence.
For uniqueness, let $y$ be a real number with $y^3 = -27$.
Then $y^3 + 27 = (y + 3)(y^2 - 3y + 9) = 0$.
The second factor equals $(y - \tfrac{3}{2})^2 + \tfrac{27}{4} > 0$, so $y + 3 = 0$ and $y = -3$.
The words "the cube root of $-27$" are justified by this statement.
Watch out: stopping after existence proves only $\exists x \, P(x)$.

### L3 human

The same pattern defines the counting quantifiers $\exists^{\geq n}$, $\exists^{\leq n}$ and $\exists^{=n}$ for each fixed $n$, with $n$ variables and the pairwise inequalities between them.
The compactness theorem shows that no single first-order formula expresses "there are infinitely many $x$ with $P(x)$", so counting by formulas stops at finite numbers.
Form (A) has the prefix $\exists x \, \forall y$, so a statement $\forall x \, \exists! y \, R(x, y)$ has the prenex prefix $\forall x \, \exists y \, \forall z$; see [[prenex normal form|CS82V969DE]].
In proof assistants, the axiom of unique choice turns a proof of $\forall x \, \exists! y \, R(x, y)$ into a function.
This is the logical reason why the definition of a function by its graph agrees with the definition of a function as a rule.
