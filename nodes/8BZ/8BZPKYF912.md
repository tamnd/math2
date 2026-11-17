---
tag: 8BZPKYF912
kind: concept
name: Ambiguity in mathematical language
msc: ["97E40", "00A35"]
topics: [WMY13MXY3W]
audience: ug1
uses: [S9MHMRAX88, 12QQ51VK01, EGTZPA6QH3, ACSC75R7R5]
sources:
  - url: https://en.wikipedia.org/wiki/Ambiguity
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Order_of_operations
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
---

## Summary

A phrase is ambiguous when it has two or more meanings, and mathematical English inherits several ambiguities from ordinary English.
The article "a" can mean "every" or "some", and the article "the" assumes that exactly one object fits.
The word "or" is often exclusive in speech, but in mathematics it is inclusive unless "but not both" is added.
The word "any" can mean "every" or "some", depending on the sentence.
Spoken formulas have no parentheses, so "$x$ plus $y$ squared" can mean $(x + y)^2$ or $x + y^2$.
The word "not" has a scope, and "all primes are not even" can mean "no prime is even" or "not every prime is even".
The words "let" and "suppose" both introduce something, but "let" fixes a name or an arbitrary object, and "suppose" adds an assumption.
Mathematical writing removes these ambiguities by fixed conventions, by careful word choice and by symbols.

## Motivation

A proof is only as good as the reading of its statement.
If two readers resolve an ambiguity in different ways, they disagree about what was proved, and neither sees why.
Many errors of students come from a reading that ordinary English allows but mathematics does not intend.
A list of the common ambiguities and of the conventions that settle them helps both in reading and in writing.

## Notation

Symbols settle most ambiguities of spoken formulas.
Parentheses fix the grouping: $(x + y)^2$ and $x + y^2$ are different expressions.
The order of operations fixes what parentheses leave out: powers come before products, and products before sums, so $2 + 3 \cdot 4^2 = 2 + 48 = 50$.
The exclusive "or" has its own symbol $\oplus$, and the inclusive "or" is $\lor$.
The scope of a quantifier or of a negation is shown by its place in a formula: $\neg \forall p \, E(p)$ and $\forall p \, \neg E(p)$ are different statements.

## Remarks

### Examples

1. [[The word "any" as "every" and as "some"|K0N4D582KJ]]: "if $x^2 = 4$ for any $x$" and "$x^2 \geq 0$ for any $x$" use "any" in two senses.
2. [[Two readings of "$x$ plus $y$ squared"|DGFD0V9SH2]]: for $x = 1$ and $y = 2$, the readings give $9$ and $5$.
3. "A square is a rectangle" uses "a" for every square. "$x$ is a root of $p$" uses "a" for some root, one of possibly several.
4. "All primes are not even" can mean "no prime is even", which is false, or "not all primes are even", which is true. The second reading is the usual intent, and "not all primes are even" says it without ambiguity.
5. "Let $x$ be a real number" introduces an arbitrary real number, and the argument proves a claim for all of them. "Suppose $\sqrt{2}$ is rational" adds an assumption, and in a proof by contradiction the assumption is later shown to be false.

### Non-examples

1. [[The phrase "the identity element of a group" is not ambiguous|VSKA5NHDRZ]]: a group has exactly one identity element, so "the" picks out one object.
2. "Every integer is even or odd" is not ambiguous. No integer is both even and odd, so the inclusive and the exclusive "or" give the same statement.
3. The formula $x \leq y$ is not ambiguous. It means "$x < y$ or $x = y$", with the inclusive "or", and every reader of mathematics reads it this way.

### Basic properties

1. In mathematics, "or" is inclusive. "$P$ or $Q$" is true when both $P$ and $Q$ are true.
2. The article "a" in a definition or in a general claim means "every". After "there is", it means "some".
3. The phrase "the $x$ such that $P(x)$" is correct only when exactly one $x$ has $P(x)$. See [[existence and uniqueness statements|ACSC75R7R5]].
4. Spoken formulas follow the written order of operations unless the speaker marks the grouping, for example with "the quantity $x$ plus $y$, squared".
5. An ambiguous sentence is not a [[statement|S9MHMRAX88]] until one reading is chosen, since the readings can have different truth values.

### History

Paul Halmos, in How to Write Mathematics (1970), advised writers to avoid the word "any" and to use "every" or "some" in its place.
Mohan Ganesalingam, in The Language of Mathematics (2013), gave a linguistic analysis of mathematical texts, and he showed how the types of mathematical objects resolve many of their ambiguities.

### Common errors

1. A student reads "or" as exclusive and rejects a case where both parts hold. For example, the student thinks that "$6$ is even or a multiple of $3$" is false.
2. A student reads "for any $\varepsilon > 0$ there is $\delta > 0$" as "for some $\varepsilon$". The phrase means "for every $\varepsilon$" here, and the wrong reading is a much weaker statement.
3. A student writes "the root of $x^2 - 2$", although there are two roots. The phrase does not say which root is meant.
4. A student types `-3^2` into a calculator, expects $9$, and gets $-9$. By the order of operations, the power is taken first, so $-3^2 = -(3^2)$.
5. A student starts a proof by contradiction with "let $\sqrt{2}$ be rational". The line is an assumption to be refuted, not a choice of an object, and "suppose" says this.

## Explanations

### L1 human

"Would you like tea or coffee?" usually means one of them, not both.
In mathematics, "or" allows both.
The sentence "$6$ is even or $6$ is a multiple of $3$" is true, and it stays true because both parts hold.
In speech, "$3$ plus $4$ times $2$" could be $14$ or $11$.
Written as $3 + 4 \times 2$, it is $11$, because we multiply before we add.

### L2 human

We remove the ambiguity from the sentence "the square of any number is not negative".

1. Find the article: "the square of" a number is one number, its square. This use of "the" is safe, because each number has exactly one square.
2. Find "any": the claim is about every number, so "any" means "every".
3. Find the scope of "not": the sentence says that each square fails to be negative. It does not say "not every square is negative".
4. Find the domain: "number" means real number here. For complex numbers the claim is false, since $i^2 = -1$.
5. Rewrite: "for every real number $x$, $x^2 \geq 0$". This version has one reading.

The typical use of this rewriting is before a proof starts: each ambiguity resolved is one less way to prove the wrong statement.

A trap: in step 4, the domain was not written, and a reader in a course on complex numbers reads the sentence differently.

### L3 human

Linguists distinguish lexical ambiguity, as in the two senses of "any", from structural ambiguity, as in "$x$ plus $y$ squared", and from scope ambiguity, as in "all primes are not even".
Formal languages remove all three: a formal grammar for logic or for arithmetic is designed to be unambiguous, unlike an [[ambiguous grammar|HFD162F9PH]], where one string has two parse trees.
Polish notation of Jan Łukasiewicz needs no parentheses, because the position of each operator fixes the grouping.
Proof assistants such as Lean fix a precedence for each operator, and elaboration with types resolves overloaded symbols, as Ganesalingam proposed for mathematical English.
Some ambiguity is useful: authors write $f(x)$ for both a function and its value, and they identify isomorphic objects, because the reader can reconstruct the precise meaning.
