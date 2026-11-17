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

Consider the argument:

- Premise 1: if $12$ is divisible by $4$, then $12$ is even.
- Premise 2: $12$ is divisible by $4$.
- Conclusion: $12$ is even.

The argument is valid: it is an instance of [[modus ponens|0Y0MQYST0M]], "from $p \to q$ and $p$, infer $q$".
We show that it has no syllogistic mood.

1. A [[mood|1TD6HRM5NG]] is a list of three letters A, E, I, O, one for each proposition of a categorical syllogism. So each proposition must be one of "all $S$ are $P$", "no $S$ is $P$", "some $S$ is $P$", "some $S$ is not $P$".
2. Premise 1 is a [[conditional statement|FA6YZGR2SS]] that joins two whole sentences. It is not of any of the four kinds, because it joins sentences and not classes.
3. Premise 2 says something about one object, the number $12$. It has no word "all", "no" or "some", so it is not of any of the four kinds either.
4. The argument has no letter for premise 1 and no letter for premise 2, so it has no mood.
5. Its validity comes from the meaning of "if ... then" alone: if $p$ is true and $p \to q$ is true, then $q$ is true by the truth table of the conditional. This is a law of [[propositional logic|09K9MWD2QQ]], not of syllogistic.

## Remarks

The example shows that syllogistic covers only one kind of valid argument: arguments about classes with "all", "no" and "some".
Arguments whose force comes from the connectives "if", "and", "or" and "not" belong to propositional logic, which the Stoics studied separately from Aristotle's syllogistic.
Traditional logic sometimes rewrote a sentence about one object as a universal sentence, "all things identical with $12$ are divisible by $4$".
If we also replace premise 1 by the stronger general premise "all multiples of $4$ are even", we get a related argument.
It reads "all multiples of $4$ are even, all things identical with $12$ are multiples of $4$, so all things identical with $12$ are even", which is [[Barbara|AC6XQ4KRNT]].
That related argument has a mood, but the given argument, with a conditional premise about one number, has none.
The [[hypothetical syllogism|7MT8CPCEM4]] "from $p \to q$ and $q \to r$, infer $p \to r$" is also called a syllogism, but it is a rule of propositional logic and has no mood for the same reason.

## Explanations

### L1 human

The argument "if it rains, the street is wet; it rains; so the street is wet" is correct.
But it is not about groups of things, such as "all cats" or "some dogs".
It is about whole sentences, "it rains" and "the street is wet", joined by "if ... then".
The moods of syllogisms only describe arguments about groups, with the words "all", "no" and "some".
So this argument has no mood, although it is correct.

### L2 human

We compare the propositional and the syllogistic form of a similar argument.

1. Propositional form: from "if $n$ is divisible by $4$ then $n$ is even" and "$n$ is divisible by $4$" infer "$n$ is even". Here $n$ is one fixed number.
2. Syllogistic form: from "all multiples of $4$ are even" and "all multiples of $12$ are multiples of $4$" infer "all multiples of $12$ are even". This is Barbara.
3. Predicate logic covers both: $\forall x\,(F(x) \to E(x))$ with $F(12)$ gives $E(12)$, and with $\forall x\,(T(x) \to F(x))$ it gives $\forall x\,(T(x) \to E(x))$.

The typical use of the comparison is to choose the right logic for an argument: connectives call for propositional logic, and "all" and "some" with classes call for syllogistic or predicate logic.
The trap is to call every two-premise argument a syllogism and to look for a mood where there is none.
