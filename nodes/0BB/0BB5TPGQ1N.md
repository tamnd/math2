---
tag: 0BB5TPGQ1N
kind: concept
name: Proof by contrapositive
aliases: [proof-by-contraposition]
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: school
specializes: [0B94TKFQJX]
uses: [04T1CT7212, 0NTF6DMVAP, K930V33BSC]
sources:
  - url: https://en.wikipedia.org/wiki/Contraposition
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.2
same_as:
  wikidata: Q1077442
  wikipedia: Contraposition
---

## Summary

A proof by contrapositive proves an [[implication|0ZNX6DQ3EJ]] "if $P$, then $Q$" by giving a [[direct proof|0NTF6DMVAP]] of the implication "if not $Q$, then not $P$".
The second implication is the [[contrapositive|04T1CT7212]] of the first, and the two are logically equivalent: each is false exactly when $P$ is true and $Q$ is false.
So a proof of one is a proof of the other.
The method helps when the negation of the conclusion is a concrete fact that is easy to use, and the hypothesis is not.

## Motivation

Some hypotheses give little to work with.
Consider "if $n^2$ is even, then $n$ is even".
The hypothesis gives $n^2 = 2k$, and there is no direct way to get a formula for $n$ from it.
The negated conclusion "$n$ is odd" gives $n = 2k + 1$, and squaring this formula is easy.
In general, the method trades a hypothesis that is hard to use for a negated conclusion that is easy to use.
This often happens when $Q$ is itself a negative statement, such as "$x$ is irrational" or "$f$ is not constant", because then "not $Q$" is a positive statement with a formula.

## Notation

For the implication $P \Rightarrow Q$, the contrapositive is $\neg Q \Rightarrow \neg P$.
It must not be confused with the [[converse|09A3N7ZN5G]] $Q \Rightarrow P$ or with the inverse $\neg P \Rightarrow \neg Q$, which are not equivalent to $P \Rightarrow Q$.
For a universal implication "for all $x$, if $P(x)$ then $Q(x)$", the contrapositive is "for all $x$, if not $Q(x)$ then not $P(x)$"; the quantifier stays in front.
A proof usually opens with "We prove the contrapositive." and then "Assume not $Q$."
In Lean, the Mathlib tactic `contrapose` changes a goal $P \to Q$ with hypothesis $P$ into the goal $\neg Q \to \neg P$, and the lemma `not_imp_not` states the equivalence.

## Remarks

### Examples

1. [[If n^2 is even, then n is even|MKNWSR8WRN]]: the contrapositive "if $n$ is odd, then $n^2$ is odd" has a two-line direct proof.
2. [[If a + b >= 100, then a >= 50 or b >= 50|3ENDPQZA6V]]: the contrapositive "if $a < 50$ and $b < 50$, then $a + b < 100$" follows by adding the two inequalities.
3. For real $x$, if $x^3 + x \neq 0$, then $x \neq 0$. The contrapositive "if $x = 0$, then $x^3 + x = 0$" is a substitution.
4. For integers $a$ and $b$, if $ab$ is even, then $a$ is even or $b$ is even. The contrapositive says that a product of two odd integers is odd.
5. For a function $f$, if $f$ is not continuous at $a$, then $f$ is not [[differentiable|0K57YG3BB8]] at $a$. This is the contrapositive of "differentiable implies continuous", and it is the way this fact is usually applied.

### Non-examples

1. [[Proving the inverse instead of the contrapositive|D0531MQ745]]: from "if $P$, then $Q$" a student proves "if not $P$, then not $Q$", which is equivalent to the converse.
2. A [[proof by contradiction|0J0XBKG64S]] of "if $P$, then $Q$" assumes $P$ and not $Q$ together and derives any contradiction. It is a different method, although a proof by contrapositive can be rewritten as one.
3. Proving the converse "if $Q$, then $P$". For "if $n$ is a multiple of $4$, then $n$ is even", the converse is false ($n = 2$), so a proof of the converse cannot be a proof of the original claim.

### Basic properties

1. $P \Rightarrow Q$ and $\neg Q \Rightarrow \neg P$ are logically equivalent. The truth tables agree in all four rows; see the [[proof by a truth table|SWH5EJP8PS]].
2. The contrapositive of the contrapositive is the original implication, after removing double negations.
3. The direction from $P \Rightarrow Q$ to $\neg Q \Rightarrow \neg P$ is valid in intuitionistic logic. The other direction uses the [[double negation law|0NFAGWH84K]], so it is valid in classical logic only.
4. A proof by contrapositive needs the negation of $Q$ in a usable form. The rules for [[negating mathematical statements|K930V33BSC]] turn "not ($A$ or $B$)" into "not $A$ and not $B$", and "not for all" into "there exists ... not".

### History

The equivalence of an implication with its contrapositive is one of the laws of classical logic, and it is valid in the propositional logic that Frege and Russell made formal.
Arend Heyting's formal system of intuitionistic logic of 1930 keeps only one direction of this law.
In mathematics education, many transition-to-proof books treat the contrapositive as a separate method in the chapter after direct proof, for example Velleman's How to Prove It in Section 3.2.

### Common errors

1. Negating the conclusion wrongly. The negation of "$a \geq 50$ or $b \geq 50$" is "$a < 50$ and $b < 50$", not "$a < 50$ or $b < 50$".
2. Proving the inverse $\neg P \Rightarrow \neg Q$ instead of the contrapositive. This is the error of non-example 1.
3. Calling the proof a contradiction. If the argument assumes not $Q$ and ends with not $P$, it is a proof by contrapositive. Writing "contradiction" at the end adds an unnecessary step.

## Explanations

### L1 human

"If it rains, then the street is wet" says the same thing as "if the street is dry, then it did not rain".
Both sentences rule out the same situation: rain on a dry street.
So to prove the first sentence, one can prove the second one instead.
In mathematics this helps when the second sentence is easier.
For example, "if $n \times n$ is even, then $n$ is even" is hard to start.
"If $n$ is odd, then $n \times n$ is odd" is easy: $3 \times 3 = 9$, $5 \times 5 = 25$, and the algebra shows it for every odd $n$.

### L2 human

We prove: for every integer $n$, if $n^2 - 6n + 5$ is even, then $n$ is odd.

1. We prove the contrapositive: if $n$ is even, then $n^2 - 6n + 5$ is odd.
2. Assume $n$ is even. Then $n = 2k$ for an integer $k$.
3. Compute: $n^2 - 6n + 5 = 4k^2 - 12k + 5 = 2(2k^2 - 6k + 2) + 1$.
4. The number $2k^2 - 6k + 2$ is an integer, so $n^2 - 6n + 5$ is odd.
5. This proves the contrapositive, and so the original statement.

The typical use: when the conclusion is "$n$ is odd", "$x$ is irrational" or "$x \neq 0$", its negation gives a formula, and the contrapositive starts from that formula.

A trap: in step 1 the negation of "$n$ is odd" must be "$n$ is even".
This uses the fact that each integer is even or odd and not both, which is a theorem about the integers, not a rule of logic.

### L3 human

In classical propositional logic, $P \to Q$ and $\neg Q \to \neg P$ have the same truth table, and a proof by contrapositive is a direct proof of the second formula followed by this equivalence.
In intuitionistic logic, $\neg Q$ is defined as $Q \to \bot$, and composition gives $(P \to Q) \to (\neg Q \to \neg P)$ for free; the reverse implication fails in general, which is one reason why constructive mathematics prefers direct proofs of positive statements.
In category theory, the step from $P \to Q$ to $\neg Q \to \neg P$ is the contravariant functor $\operatorname{Hom}(-, \bot)$ applied to the arrow $P \to Q$.
The method appears in analysis as the contrapositive form of many limit statements: "if $a_n$ does not tend to $0$, then $\sum a_n$ diverges" is the usual form of the divergence test.
The related method of [[proof by contradiction|0J0XBKG64S]] is more general, and the topic [[fallacies and errors in proofs|T6QQ749DM5]] treats the confusion of an implication with its converse and inverse.
