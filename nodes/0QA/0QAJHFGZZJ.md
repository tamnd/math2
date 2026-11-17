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

Let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0QHEWQD30B]] on $D$.
The uniqueness quantifier forms the proposition $\exists! x \, P(x)$, read "there is exactly one $x$ such that $P(x)$".
This proposition is true when exactly one element $a$ of $D$ makes $P(a)$ true, and it is false otherwise.
In first-order logic it is not a new symbol but an abbreviation, built from the [[existential quantifier|0MSRQHCNN9]], the [[universal quantifier|0GHS47PDAQ]] and [[equality|E918704SKV]]:
$$\exists! x \, P(x) \quad \text{abbreviates} \quad \exists x \, \bigl( P(x) \land \forall y \, ( P(y) \to y = x ) \bigr).$$
The precise definition is on the page [[uniqueness quantifier (definition)|0N3ADS4CHH]].
The quantifier matters because it is the logical form of the word "the": "the identity element", "the limit", "the solution" all rest on a statement $\exists! x \, P(x)$.

## Motivation

The two basic quantifiers count in a rough way.
The formula $\exists x \, P(x)$ says "at least one", and $\forall x \, P(x)$ says "all".
Mathematics often needs "exactly one", for example in "each real number has exactly one cube root" or in the definition of a [[function|0EPAT51DXQ]].
"Exactly one" is "at least one" together with "at most one".
"At least one" is $\exists x \, P(x)$.
"At most one" says that any two elements with the property are equal, so it needs the equality sign.
Putting the two parts together gives the uniqueness quantifier, and this shows that "exactly one" is expressible in the language of $\forall$, $\exists$ and $=$.

## Notation

The standard symbol is $\exists! x \, P(x)$, and some books write $\exists_1 x \, P(x)$ or $\exists^{=1} x \, P(x)$.
The restricted form $\exists! x \in A \; P(x)$ means $\exists! x \, (x \in A \land P(x))$, with a conjunction and not with an implication.
There are two equivalent expansions:
$$\text{(A)} \quad \exists x \, \bigl( P(x) \land \forall y \, ( P(y) \to y = x ) \bigr),$$
$$\text{(B)} \quad \exists x \, P(x) \;\land\; \forall x \, \forall y \, \bigl( P(x) \land P(y) \to x = y \bigr).$$
Form (B) separates the existence part from the uniqueness part, and form (A) names the unique element.
In the Lean library Mathlib, `ExistsUnique` is defined by form (A), and `∃! x, P x` is notation for it.

## Remarks

### Examples

1. [[The equation x^2 = x + 2 has exactly one natural solution|QMYHS34Z1G]]: over $\mathbb{N}$ only $x = 2$ works, but over $\mathbb{Z}$ also $x = -1$ works. The truth of $\exists!$ depends on the domain.
2. [[The definition of a function uses the uniqueness quantifier|P4NCHC44NJ]]: a relation $f \subseteq X \times Y$ is a function when $\forall x \in X \; \exists! y \in Y \; (x, y) \in f$.
3. $\exists! p \, (p \text{ is prime} \land p \text{ is even})$ is true over the integers. The prime $2$ is even, and each even number $n > 2$ has the divisor $2$ with $1 < 2 < n$, so it is not prime.
4. $\exists! x \in \mathbb{R} \; x^3 = 8$ is true. The number $2$ works, and $x \mapsto x^3$ is strictly increasing, so no other real number has cube $8$.
5. $\forall x \in \mathbb{R} \; \exists! y \in \mathbb{R} \; x + y = 0$ is true. The number $y = -x$ works, and $x + y = 0 = x + y'$ gives $y = y'$.

### Non-examples

1. [[The formula "exists x for all y, P(y) implies y = x" says "at most one"|KGGR81G9DV]]: it is true for a predicate that no element satisfies, so it is not $\exists! x \, P(x)$.
2. [[The equation x^2 = 4 has a solution but not exactly one|A82V4N0G1P]]: over $\mathbb{R}$ the predicate $x^2 = 4$ has the two solutions $2$ and $-2$, so the uniqueness part fails.
3. The formula $\exists x \, \bigl( P(x) \land \forall y \, ( y = x ) \bigr)$ is not the uniqueness quantifier. It says that the whole domain has exactly one element and that this element has property $P$. Over $\mathbb{N}$ with $P(x)$ meaning $x = 0$, it is false, although $\exists! x \, P(x)$ is true.

### Basic properties

1. Forms (A) and (B) are equivalent. The proof uses only the rules of the quantifiers and of equality.
    1. Assume (A), and let $a$ satisfy $P(a)$ and $\forall y \, (P(y) \to y = a)$. Reason: elimination of $\exists$.
    2. Then $\exists x \, P(x)$, with witness $a$. Reason: $P(a)$ from step 1.
    3. Let $x$ and $y$ satisfy $P(x)$ and $P(y)$. Then $x = a$ and $y = a$. Reason: the second part of step 1, applied to $x$ and to $y$.
    4. So $x = y$. Reason: symmetry and transitivity of equality. Steps 2 to 4 give (B).
    5. Conversely, assume (B), and let $a$ satisfy $P(a)$. Reason: the first conjunct of (B).
    6. Let $y$ satisfy $P(y)$. The second conjunct of (B), applied to $y$ and $a$, gives $y = a$. So $\forall y \, (P(y) \to y = a)$.
    7. Steps 5 and 6 show that $a$ is a witness for (A). No step uses the [[law of excluded middle|0RYYK8PG4S]], so the equivalence also holds in [[intuitionistic logic|Q11N8X99FK]].
2. $\exists! x \, P(x)$ implies $\exists x \, P(x)$, by the first part of form (B). The converse is false, as non-example 2 shows.
3. $\exists! x \, P(x)$ is true exactly when the truth set $\{x \in D : P(x)\}$ has exactly one element.
4. On a two-element domain $\{a, b\}$, $\exists! x \, P(x)$ is equivalent to $P(a) \oplus P(b)$, the [[exclusive or|PTMR3P9J6C]]. On a three-element domain this fails: $P(a) \oplus P(b) \oplus P(c)$ is also true when all three are true.
5. The negation of $\exists! x \, P(x)$ is $\forall x \, \neg P(x) \lor \exists x \, \exists y \, (P(x) \land P(y) \land x \neq y)$. It follows from form (B), [[De Morgan's laws|09PKJKA6J0]] and the [[negation of a universal statement|0P3A06QNDP]].
6. The proof methods for statements of this form, existence first and uniqueness second, are on the pages [[existence and uniqueness statements|ACSC75R7R5]] and [[proof of uniqueness|GQHHNV79PA]].

### History

Gottlob Frege introduced quantifiers with bound variables in his Begriffsschrift of 1879, and with equality they can express "exactly one".
Bertrand Russell analysed the word "the" in 1905 as a claim of existence and uniqueness, the theory of [[definite descriptions|PD2R4XT79Q]].

### Common errors

1. A student writes $\exists x \, \forall y \, (P(y) \to y = x)$ for "exactly one". This formula omits $P(x)$, and it says only "at most one", as non-example 1 shows.
2. A student writes the restricted form $\exists! x \in A \; P(x)$ as $\exists! x \, (x \in A \to P(x))$. Over $\mathbb{Z}$ with $A = \{1\}$ and $P(x)$ meaning $x > 0$, the first is true, but every integer satisfies $x \in A \to P(x)$, so the second is false.
3. A student reads $\exists! x \, \exists! y \, P(x, y)$ as "exactly one pair". The page [[existence and uniqueness statements|ACSC75R7R5]] gives a domain where this reading fails.
4. A student uses the exclusive or of $P(a)$, $P(b)$ and $P(c)$ for "exactly one of three". Property 4 shows that this is wrong when all three are true.

## Explanations

### L1 human

"Exactly one" says two things: "at least one" and "not two different ones".
Take the numbers from $1$ to $10$, and ask which of them are even and a multiple of $5$.
The number $10$ is even and a multiple of $5$, so there is at least one.
The only other multiple of $5$ in the list is $5$, and $5$ is odd.
So no second number has both properties.
The sentence "exactly one number from $1$ to $10$ is even and a multiple of $5$" is true.

### L2 human

We decide whether $\exists! x \in D \; P(x)$ is true, where $D = \{1, 2, 3, 4, 5, 6\}$ and $P(x)$ means "$x$ divides $6$ and $x > 3$".

1. Compute the truth set. The divisors of $6$ in $D$ are $1$, $2$, $3$ and $6$, and of these only $6$ is greater than $3$. So the truth set is $\{6\}$.
2. Check form (A) with the witness $x = 6$. $P(6)$ is true, and $P(y)$ is false for every $y \neq 6$ in $D$, so $\forall y \, (P(y) \to y = 6)$ holds.
3. Check form (B). Existence holds by step 2. If $P(x)$ and $P(y)$, then $x = 6$ and $y = 6$ by step 1, so $x = y$.
4. So $\exists! x \in D \; P(x)$ is true.
5. Change $P(x)$ to "$x$ divides $6$ and $x > 1$". The truth set becomes $\{2, 3, 6\}$, and form (B) fails with $x = 2$, $y = 3$.

The typical use of the quantifier is in definitions: "the" is allowed exactly when the matching $\exists!$ statement is true.
A trap is to check only the uniqueness part, for example in the formula of common error 1, which is also true when the truth set is empty.

### L3 human

The same pattern defines the counting quantifiers $\exists^{\geq n}$, $\exists^{\leq n}$ and $\exists^{=n}$ for each fixed $n$, with $n$ variables and the pairwise inequalities between them.
The compactness theorem shows that no single first-order formula expresses "there are infinitely many $x$ with $P(x)$", so counting by formulas stops at finite numbers.
Form (A) is already in [[prenex normal form|CS82V969DE]] with prefix $\exists x \, \forall y$, so a statement $\forall x \, \exists! y \, R(x, y)$ has the more complex prefix $\forall x \, \exists y \, \forall z$.
In type theory and in proof assistants, a proof of $\exists! x \, P(x)$ gives a term with the property, and the axiom of unique choice turns $\forall x \, \exists! y \, R(x, y)$ into a function.
This is the logical reason why the definition of a function by its graph and the definition of a function as a rule agree.
