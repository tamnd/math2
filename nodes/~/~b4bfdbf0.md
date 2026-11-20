---
tag: ~b4bfdbf0
kind: concept
name: Fuzzy logic
aliases: [fuzzy-logic, mathematical-fuzzy-logic]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
uses: [DWYCKAKXZD, GV9NVFFFXF]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: lead section; 1. Fuzzy connectives based on t-norms; 10. Fuzzy logic and vagueness
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: lead section; Fuzzy systems; Logical analysis
  - book: isbn:9780792352389
---

## Summary

*Fuzzy logic* has two uses.
In the narrow sense, *mathematical fuzzy logic*, it is a family of [[many-valued logics|DWYCKAKXZD]] with truth values in $[0, 1]$, read as degrees of truth.
These logics have truth-functional connectives, a consequence relation, proof systems and completeness theorems.
In the broad sense, used in engineering, "fuzzy logic" names methods for computing with degrees, such as fuzzy control and fuzzy classification.
These methods do not define a consequence relation.

## Motivation

Many predicates are vague: "tall", "young", "huge".
For a vague predicate there is no sharp line between the cases where it applies and the cases where it does not.
Fuzzy logic gives such statements intermediate degrees of truth, and computes the degree of a compound statement from the degrees of its parts.
SEP describes the sorites paradox as the main test case: see [[the sorites example|~671c3327]].

## Notation

The truth values are $[0, 1]$, with $0$ for "totally false" and $1$ for "totally true".
The weak connectives are $x \land y = \min(x, y)$ and $x \lor y = \max(x, y)$.
In mathematical fuzzy logic, the strong conjunction is a [[t-norm|~a4e21349]] $*$, written $\&$ in SEP and $\otimes$ or $\odot$ elsewhere.
Implication is the residuum $\Rightarrow_*$ of the t-norm, and $\neg x = x \Rightarrow_* 0$.
The consequence relation preserves the value $1$.

## Remarks

### Examples

1. [[Łukasiewicz logic|~ca73eab3]]: the t-norm $\max(0, x + y - 1)$ and the implication $\min(1, 1 - x + y)$.
2. Gödel logic: the t-norm $\min$; its implication is $1$ if $x \le y$, else $y$.
3. [[Product logic|~fc3c462d]]: the t-norm $x \cdot y$; its implication is $1$ if $x \le y$, else $y / x$.
4. [[Hájek's basic logic BL|~c93e8aa5]], the logic of all continuous t-norms.
5. [[MTL|~bb574db9]], the logic of all left-continuous t-norms, which SEP calls the weakest logic of this kind.
6. Logics with truth constants, such as [[Pavelka logic|~4b515603]].

### Non-examples

1. A fuzzy controller, such as the Mamdani method: it maps numbers to numbers through rules, and it has no consequence relation; see [[the fuzzy control non-example|~a3f0a267]].
2. [[Probability logic|~d75535ab]]: the probability of $\varphi \land \psi$ is not a function of the probabilities of $\varphi$ and $\psi$, so it is not truth-functional.
3. [[Fuzzy set theory|GV9NVFFFXF]] alone: a fuzzy set is a membership function, and it is a set-theoretic object, not a logic.

### Basic properties

1. On the values $0$ and $1$ the connectives behave classically, as SEP states.
2. Excluded middle $\varphi \lor \neg \varphi$ is not a tautology under any t-norm interpretation, according to SEP.
3. Strong conjunction implies weak conjunction, but not conversely: $\varphi \mathbin{\&} \psi \to \varphi \land \psi$ is valid in MTL, and its converse is not.
4. Each left-continuous t-norm has a unique residuum, and SEP gives the residua of the three basic t-norms.
5. In Łukasiewicz and Gödel logic, deciding validity is coNP-complete, as in classical logic.

### History

SEP and Wikipedia state that the term comes from Zadeh's fuzzy sets of 1965.
Wikipedia notes that infinite-valued logic had been studied since the 1920s by Łukasiewicz and Tarski.
SEP attributes the semantics with $\min$, $\max$ and $1 - x$ to Goguen (1975).
The narrow sense became a discipline of mathematical logic after Hájek's monograph of 1998, according to SEP.

### Common errors

1. Reading engineering fuzzy logic as a logic.
   A fuzzy controller computes an output; it does not say which conclusions follow from which premises.
2. Taking $\min$, $\max$ and $1 - x$ as the whole logic.
   With designated value $1$ these connectives give no tautologies, since every formula has value $\tfrac12$ when all variables have value $\tfrac12$.
3. Confusing degrees of truth with probabilities.
   A degree is truth-functional, and a probability is not.
4. Assuming a single fuzzy logic.
   Each choice of t-norm gives a different logic, with different tautologies.

## Explanations

### L1 human

In ordinary logic a statement is true or false.
In fuzzy logic a statement can be true to a degree, like $0.7$.
"Ann is tall" can be more true for a tall person than for a person of middle height.
Engineers also use the words "fuzzy logic" for controllers in machines, such as washing machines; that is a different thing.

### L2 human

To work in a fuzzy logic, first fix the t-norm.
Then compute the value of each formula from the values of its variables.
A formula is a tautology if its value is $1$ for all values of the variables.

Example: in Łukasiewicz logic, at $p = 0.7$ and $q = 0.4$, $p \mathbin{\&} q = 0.1$ and $p \to q = 0.7$.
A trap: the tautologies change with the t-norm; $\neg \neg p \to p$ is a Łukasiewicz tautology but not a Gödel tautology.

### L3 human

Mathematical fuzzy logic studies these logics as objects of mathematical logic.
SEP reports that Běhounek and Cintula proposed to define fuzzy logics as logics complete with respect to linearly ordered algebras.
Under this view, MTL is the base, and BL, Łukasiewicz, Gödel and product logic are its axiomatic extensions.
The first-order versions behave differently: Gödel logic keeps strong completeness, while the first-order Łukasiewicz tautologies are not recursively axiomatizable; see [[the complexity statement|~c6c9b1d6]].
