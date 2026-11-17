---
tag: YVNRVXJR68
kind: concept
name: Proof schemes
aliases: [proof-scheme, harel-sowder-proof-schemes, empirical-proof-scheme, deductive-proof-scheme]
msc: ["97E50", "97C30"]
topics: [VHGA6J4NZK]
audience: research
uses: [0B94TKFQJX, 5V35SGEN1T, ENY0GKRJS8]
sources:
  - url: https://doi.org/10.1090/cbmath/007/07
    locator: pages 234-283
  - url: https://doi.org/10.2307/749651
    locator: pages 396-428
  - url: https://doi.org/10.2307/749097
    locator: pages 41-51
  - url: https://doi.org/10.1007/BF01273371
    locator: pages 359-387
---

## Summary

A person's proof scheme is what convinces that person that a mathematical claim is true, and what the person offers to convince others.
Guershon Harel and Larry Sowder (1998) called the first act ascertaining, which removes one's own doubts, and the second act persuading, which removes the doubts of others.
They sorted proof schemes into three classes: external conviction (by an authority, by the form of an argument, or by symbols without meaning), empirical (by examples or by pictures), and analytic (by general reasoning about the objects), later called deductive.
The idea matters because a student's proof scheme decides which arguments the student accepts and writes, and teaching can aim at a change of scheme.

## Motivation

A teacher shows a correct [[proof|0B94TKFQJX]], and the student still wants to check one more example.
Another student is satisfied by ten examples, and sees no need for a proof.
A third student accepts any argument with much algebra, whether or not the algebra is correct.
The three students have different standards of conviction.
The notion of a proof scheme names these standards, so that a teacher or a researcher can describe them and plan for them.

## Notation

Harel and Sowder named the subclasses as follows.

- External conviction: authoritarian (an authority says so), ritual (the argument has the look of a proof), non-referential symbolic (symbols are manipulated without reference to their meaning).
- Empirical: inductive (examples or measurements), perceptual (pictures, without attention to the general case).
- Analytic (1998), later deductive (2007): transformational (general operations on objects, with goals and anticipation), axiomatic (the understanding that results rest on accepted axioms and definitions).

Some authors write "proof scheme" for the whole of a person's standards, and others for one class of argument.

## Remarks

### Examples

1. [[An empirical proof scheme|6G5GATCE78]]: a student checks that $1 + 3$, $5 + 7$ and $11 + 13$ are even and concludes that the sum of two odd numbers is always even.
2. [[A transformational proof scheme|GA27MSTQQD]]: a student writes the odd numbers as $2a + 1$ and $2b + 1$ and shows that the sum is $2(a + b + 1)$.
3. Authoritarian scheme: a student accepts that $0.999\ldots = 1$ only because the teacher says so, and cannot explain why.
4. Ritual scheme: a student accepts a two-column argument as a proof because it has two columns, even when one reason is wrong.
5. Perceptual scheme: a student believes that the three medians of a triangle meet in one point because they do in a drawing. The student does not ask whether the drawing is special.

### Non-examples

1. [[A written argument alone|6FQKMC0PB2]] is not a proof scheme. A scheme belongs to a person, and the same argument can convince one reader and fail to convince another.
2. A [[proof method|G9JFJGY4TQ]], such as proof by contradiction, is not a proof scheme. A method is a form of argument, and a scheme is a standard of conviction that can accept or reject arguments of any form.

### Basic properties

1. A person can hold several schemes at once, and use different schemes for different topics. A student may be deductive in algebra and empirical in geometry.
2. The classes are not ordered in time for each person, but teaching usually aims to move students from external and empirical schemes to deductive schemes.
3. A deductive scheme does not make examples useless. A person with a deductive scheme uses examples to understand and to test, as the page on [[examples in mathematical practice|F3NNR77WKP]] shows, but not to prove a general claim.

### History

Harel and Sowder published the framework in 1998, from teaching experiments with university students in the United States.
Earlier work had described related standards.
Gary Martin and Harel (1989) found that many preservice elementary teachers accepted inductive arguments as proofs, while they also accepted deductive arguments.
Daniel Chazan (1993) found that some high school geometry students treated measured examples as proof, and that some doubted that a deductive proof covers all cases.
In a chapter of 2007, Harel and Sowder renamed the analytic class as the deductive class.

### Common errors

1. A teacher treats a student's empirical argument as laziness. The student may sincerely hold an empirical scheme, and the scheme must change before the student sees the need for a proof.
2. A researcher classifies a student by one answer. A scheme is shown by the pattern of many answers, and one answer can mislead.
3. A teacher rewards the form of a proof more than its content. This strengthens the ritual scheme.

## Explanations

### L1 human

Different people are convinced by different things.
Some believe a claim because a teacher or a book says it.
Some believe it after a few examples, for example after they check that $2 + 4 = 6$, $6 + 8 = 14$ and $10 + 12 = 22$ are all even.
Others believe it only when they see a reason that works for all numbers.
A proof scheme is the name for what convinces a person.
Teachers of proof try to move students from the first two kinds to the third.

### L2 human

We classify the answers of three students to the claim "for all integers $n$, the number $n^2 - n$ is even".

1. Student A writes: "$2^2 - 2 = 2$, $3^2 - 3 = 6$, $4^2 - 4 = 12$, $5^2 - 5 = 20$. All are even, so it is true." The argument uses examples only. This is an inductive empirical scheme.
2. Student B writes: "$n^2 - n = n(n - 1)$. So it is even." The student gives no reason for the last step. When asked, the student says: "It looks like the proofs in the book." This suggests a ritual scheme, although the algebra is right.
3. Student C writes: "$n^2 - n = n(n - 1)$. One of two consecutive integers $n - 1$ and $n$ is even, so the product is even." The argument works for all $n$ by general reasoning about the objects. This is a transformational scheme.
4. We check student C's step: if $n$ is even, then $n$ is a factor that is even; if $n$ is odd, then $n - 1$ is even. In both cases the product $n(n - 1)$ is even.
5. Student B's written text is almost a proof. The classification depends on the interview, not only on the text.

The typical use is in teaching: a teacher who knows that student A holds an empirical scheme gives a task where examples mislead, such as the [[values of n^2 + n + 41|H75AB4EJT5]].
A trap is step 2: a text that looks deductive can hide a ritual scheme, and a short text can hide a deductive scheme.

### L3 human

Proof schemes belong to the cognitive research on proof, in which conviction is a psychological state, not a logical property of a text.
The framework is close to the levels of Nicolas Balacheff (naive empiricism, the test of one critical case, the generic example, the thought experiment), and to the van Hiele levels of [[geometry education|1D7PZ2TF5Y]], which also place deduction at a late stage.
It contrasts with the logical view of [[mathematical proof|0B94TKFQJX]] and with the social view of the [[Toulmin model|RVZCSFDB2Y]], which looks at the structure of public arguments.
The empirical scheme is the basis of many errors on the page [[student difficulties with proof|5K2969GSWE]], and a [[generic proof|SG9XA69J64]] is a common bridge from the empirical to the deductive scheme.
