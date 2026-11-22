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

Mathematical English borrows its words from ordinary English, and with the words come their double meanings.
Compare "any natural number is a sum of four squares" with "if any root of $p$ is negative, then $p$ has a real root".
In the first sentence "any" means "every", and in the second it means "some".
A reader who mixes them up reads a different theorem.

A phrase is *ambiguous* when it has two or more meanings.
The common sources in mathematics are few.
The article "a" can mean "every" or "some", and "the" assumes that exactly one object fits.
The word "or" is often exclusive in speech, but in mathematics it is inclusive.
The word "any" can mean "every" or "some".
A spoken formula has no parentheses, so "$x$ plus $y$ squared" can mean $(x + y)^2$ or $x + y^2$.
The word "not" has a scope, so "all primes are not even" has two readings.
Mathematical writing removes these ambiguities with fixed conventions, careful word choice and symbols.

## Motivation

A proof is only as good as the reading of its statement.
If two readers resolve an ambiguity in different ways, they disagree about what was proved, and neither sees why.
Many errors of students come from a reading that ordinary English allows but the author did not intend.
So a reader needs to know where ambiguity hides, and a writer needs to know the conventions that settle it.

## Notation

Symbols settle most ambiguities of spoken formulas.
Parentheses fix the grouping: $(x + y)^2$ and $x + y^2$ are different expressions.
The order of operations fixes what the parentheses leave out.
Powers come before products, and products before sums, so $2 + 3 \cdot 4^2 = 2 + 48 = 50$.
The exclusive "or" has its own symbol $\oplus$, and the inclusive "or" is $\lor$.
The scope of a quantifier or of a negation is shown by its place in a formula: $\neg \forall p \, E(p)$ and $\forall p \, \neg E(p)$ are different statements.

## Remarks

### Small words with two meanings

The word "any" is the worst offender.
[[The word "any" as "every" and as "some"|K0N4D582KJ]] shows that "$x^2 \ge 0$ for any $x$" uses it for every $x$, and "if $x^2 = 4$ for any $x$" uses it for some $x$.
The safe choice is to write "every" or "some" instead.

The article "a" has the same problem.
"A square is a rectangle" means every square.
"$x$ is a root of $p$" means one root, perhaps one of several.
As a rule, "a" in a definition or in a general claim means "every", and "a" after "there is" means "some".

The article "the" makes a different claim: that exactly one object fits.
"The root of $x^2 - 2$" names nothing definite, because $x^2 - 2$ has the two roots $\sqrt{2}$ and $-\sqrt{2}$.
The phrase "the $x$ such that $P(x)$" is correct only after a proof of [[existence and uniqueness|ACSC75R7R5]].

### Or, not, and their scope

In mathematics, "or" is inclusive: "$P$ or $Q$" is true when both $P$ and $Q$ are true.
So "$6$ is even or a multiple of $3$" is true, although both parts hold.
To exclude the case of both, an author writes "but not both" or "exactly one of".

The word "not" applies to a part of the sentence, its scope, and English does not always show which part.
"All primes are not even" can mean "no prime is even", which is false, because of $2$.
It can also mean "not all primes are even", which is true, because of $3$.
The second reading is the usual intent, and the words "not all primes are even" say it with one meaning.

### Spoken formulas

A spoken formula loses its parentheses.
[[Two readings of "$x$ plus $y$ squared"|DGFD0V9SH2]] gives $9$ and $5$ for $x = 1$ and $y = 2$.
A speaker marks the grouping with words, as in "the quantity $x$ plus $y$, all squared".
Written formulas follow the order of operations, and that order also has a trap: $-3^2 = -(3^2) = -9$, not $9$.

### Let and suppose

The words "let" and "suppose" both start a line of a proof, but they do different jobs.
"Let $x$ be a real number" introduces an arbitrary real number, and the argument proves a claim for all of them.
"Suppose $\sqrt{2}$ is rational" adds an assumption, and in a proof by contradiction the assumption is later shown to be false.
A line such as "let $\sqrt{2}$ be rational" treats an assumption as a choice of object, and "suppose" is the right word.

### What is not ambiguous

[[The phrase "the identity element of a group" is not ambiguous|VSKA5NHDRZ]]: a group has exactly one identity element, so "the" picks out one object.
"Every integer is even or odd" is not ambiguous either.
No integer is both even and odd, so the inclusive and the exclusive "or" give the same statement.
The formula $x \leq y$ means "$x < y$ or $x = y$", with the inclusive "or", and every reader of mathematics reads it so.
An ambiguous sentence is not yet a [[statement|S9MHMRAX88]], since its readings can have different truth values.

### Watch out

The first error is to read "or" as exclusive and to reject a case where both parts hold.
The second error is to read "for any $\varepsilon > 0$ there is $\delta > 0$" as "for some $\varepsilon$".
Here "any" means "every", and the wrong reading is a much weaker statement.
The third error is to write "the root" or "the solution" when there are several.
The fourth error is to type `-3^2` into a calculator and expect $9$.

### History

Paul Halmos, in How to Write Mathematics (1970), advised writers to avoid the word "any" and to use "every" or "some" in its place.
Mohan Ganesalingam, in The Language of Mathematics (2013), gave a linguistic analysis of mathematical texts, and he showed how the types of mathematical objects resolve many of their ambiguities.

### Try it

First, give the two readings of "every student did not pass", and say which words fix each one.
One reading is "no student passed", and the other is "not every student passed".

Second, compute "$2$ times $3$ plus $4$" in both groupings.
The results are $2 \cdot (3 + 4) = 14$ and $2 \cdot 3 + 4 = 10$.

## Explanations

### L1 human

"Would you like tea or coffee?" usually means one of them, not both.
In mathematics, "or" allows both.
The sentence "$6$ is even or $6$ is a multiple of $3$" is true, and it stays true because both parts hold.
In speech, "$3$ plus $4$ times $2$" could be $14$ or $11$.
Written as $3 + 4 \times 2$, it is $11$, because we multiply before we add.

### L2 human

Remove the ambiguity from the sentence "the square of any number is not negative".

1. Find the article.
   "The square of" a number is safe, because each number has exactly one square.
2. Find "any".
   The claim is about every number, so "any" means "every".
3. Find the scope of "not".
   The sentence says that each square fails to be negative, not that some square fails to be negative.
4. Find the domain.
   "Number" means real number here, since for complex numbers the claim is false: $i^2 = -1$.
5. Rewrite: "for every real number $x$, $x^2 \geq 0$".
   This version has one reading.

Do this rewriting before a proof starts, because each ambiguity left in is one more way to prove the wrong statement.
Watch out: in step 4 the domain was not written, and a reader in a course on complex numbers reads the sentence differently.

### L3 human

Linguists distinguish lexical ambiguity, as in the two senses of "any", from structural ambiguity, as in "$x$ plus $y$ squared", and from scope ambiguity, as in "all primes are not even".
Formal languages remove all three.
A formal grammar for logic or for arithmetic is designed to be unambiguous, unlike an [[ambiguous grammar|HFD162F9PH]], where one string has two parse trees.
The Polish notation of Jan Łukasiewicz needs no parentheses, because the position of each operator fixes the grouping.
Proof assistants such as Lean fix a precedence for each operator, and elaboration with types resolves overloaded symbols, as Ganesalingam proposed for mathematical English.
Some ambiguity is useful.
Authors write $f(x)$ for both a function and its value, and they identify isomorphic objects, because the reader can reconstruct the precise meaning.
