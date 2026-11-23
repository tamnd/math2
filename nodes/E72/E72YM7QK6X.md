---
tag: E72YM7QK6X
kind: example
name: Modus ponens is not a categorical syllogism
msc: ["03B05", "03B10"]
topics: [H8QZY0RZXZ]
audience: school
not_instance_of:
  - target: 1TD6HRM5NG
    note: the premises are a conditional sentence and a sentence about one object, not categorical propositions of the kinds A, E, I, O, so the argument has no mood
uses: [1TD6HRM5NG, MZBNX2T6Q6, 0Y0MQYST0M, FA6YZGR2SS, 7MT8CPCEM4]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
---

## Example

Consider the argument: if $12$ is divisible by $4$, then $12$ is even; $12$ is divisible by $4$; so $12$ is even.
It is valid, because it is an instance of [[modus ponens|0Y0MQYST0M]], "from $p \to q$ and $p$, infer $q$".
We show that it has no syllogistic mood.

1. A [[mood|1TD6HRM5NG]] is a list of three letters from A, E, I, O, one for each proposition of a categorical syllogism.
   So each proposition must have one of the forms "all $S$ are $P$", "no $S$ is $P$", "some $S$ is $P$" or "some $S$ is not $P$".
2. The first premise is a [[conditional statement|FA6YZGR2SS]] that joins two whole sentences, not two classes, so it has none of the four forms.
3. The second premise says something about one object, the number $12$, with no "all", "no" or "some", so it has none of the four forms either.
4. So neither premise has a letter, and the argument has no mood.
5. Its validity comes from the truth table of the conditional alone: if $p$ and $p \to q$ are both true, then $q$ is true.
   This is a law of [[propositional logic|09K9MWD2QQ]], not of syllogistic.

## Remarks

Syllogistic covers one kind of valid argument: arguments about classes with "all", "no" and "some".
Arguments whose force comes from "if", "and", "or" and "not" belong to propositional logic, which the Stoics studied apart from Aristotle's syllogistic.

Traditional logic sometimes rewrote a sentence about one object as a universal one: "all things identical with $12$ are multiples of $4$".
Replace the conditional by the general premise "all multiples of $4$ are even" as well.
The result is "all multiples of $4$ are even, all things identical with $12$ are multiples of $4$, so all things identical with $12$ are even".
That is [[Barbara|AC6XQ4KRNT]], and it has a mood, but it is a different argument from the one with a conditional premise about one number.
The [[hypothetical syllogism|7MT8CPCEM4]], "from $p \to q$ and $q \to r$, infer $p \to r$", is also called a syllogism, and it has no mood for the same reason.

## Explanations

### L1 human

The argument "if it rains, the street is wet; it rains; so the street is wet" is correct.
But it is not about groups of things, such as "all cats" or "some dogs".
It is about whole sentences, "it rains" and "the street is wet", joined by "if, then".
Moods only describe arguments about groups, with "all", "no" and "some", so this argument has no mood although it is correct.

### L2 human

We compare three forms of a similar argument.

1. Propositional form: from "if $n$ is divisible by $4$ then $n$ is even" and "$n$ is divisible by $4$", infer "$n$ is even", for one fixed number $n$.
2. Syllogistic form: from "all multiples of $4$ are even" and "all multiples of $12$ are multiples of $4$", infer "all multiples of $12$ are even", which is Barbara.
3. Predicate logic covers both: $\forall x\,(F(x) \to E(x))$ with $F(12)$ gives $E(12)$, and with $\forall x\,(T(x) \to F(x))$ it gives $\forall x\,(T(x) \to E(x))$.

Connectives call for propositional logic, and "all" and "some" with classes call for syllogistic or predicate logic.
The trap is to call every two-premise argument a syllogism and to look for a mood where there is none.
