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

A student is asked to prove that $n^2 - n$ is even for every integer $n$.
She computes $0, 2, 6, 12, 20$ for $n = 1, 2, 3, 4, 5$, sees that all five are even, and writes "so it is true for all $n$".
Asked whether she is sure, she says yes, and asked how she would convince a friend, she says she would show more examples.
Her arithmetic is right and her conclusion is true, but what convinces her is a list of cases.

A person's proof scheme is what convinces that person that a mathematical claim is true, and what the person offers to convince others.
Guershon Harel and Larry Sowder introduced the idea in 1998, in *Research in Collegiate Mathematics Education III*.
They called the first act ascertaining, which removes one's own doubts, and the second persuading, which removes the doubts of others.
They sorted proof schemes into three classes: external conviction, empirical, and analytic, a class that they later called deductive.
The student above holds an empirical scheme, and much of the teaching of [[proof|0B94TKFQJX]] aims to change such a scheme.

## Motivation

A teacher shows a correct proof, and one student still wants to check one more example.
Another student is satisfied by ten examples and sees no need for a proof.
A third accepts any argument with plenty of algebra, whether or not the algebra is right.
The three students have different standards of conviction, and a lesson that ignores the difference will reach only some of them.
The notion of a proof scheme names these standards, so that a teacher or a researcher can describe them and plan for them.

## Notation

Harel and Sowder divide each class further.
External conviction has three subclasses: authoritarian (an authority says so), ritual (the argument has the look of a proof), and non-referential symbolic (symbols are moved without reference to what they mean).
The empirical class has two: inductive (examples or measurements) and perceptual (pictures, without attention to the general case).
The analytic class, named deductive in their 2007 survey chapter, has two as well: transformational (general operations on objects, aimed at a goal) and axiomatic (the understanding that results rest on accepted axioms and definitions).
Some authors write "proof scheme" for the whole of a person's standards, and others for one class of argument.

## Remarks

### Three students, three schemes

The opening student checked cases, and Harel and Sowder would call her scheme inductive empirical; [[the odd-sum version|6G5GATCE78]] works through the same pattern for another claim.
A student with a perceptual scheme believes that the three medians of a triangle meet in one point because they do in a drawing, and does not ask whether the drawing is special.
An authoritarian student accepts that $0.999\ldots = 1$ because the teacher says so, and cannot say why.
A ritual student accepts a two-column argument because it has two columns, even when one of the reasons is wrong.
A transformational student writes odd numbers as $2a + 1$ and $2b + 1$ and shows that the sum is $2(a + b + 1)$, as [[the transformational example|GA27MSTQQD]] describes.

### A scheme belongs to a person

A scheme is not a text and not a method.
[[A written argument on its own|6FQKMC0PB2]] has no scheme, because the same argument can convince one reader by its logic and another only after a numerical check.
A [[proof method|G9JFJGY4TQ]] such as proof by contradiction is a form of argument, while a scheme is a standard that accepts or rejects arguments of any form.
A person can hold several schemes and use different ones in different topics, for example deductive in algebra and empirical in geometry.
So a researcher needs a pattern of many answers, and often an interview, before classifying a student.

### Examples still matter

A deductive scheme does not make examples useless.
A person with a deductive scheme uses examples to understand a claim, to find the idea of a proof and to test a conjecture, as [[examples in mathematical practice|F3NNR77WKP]] describes.
What changes is the role of the examples: they suggest and test, but they do not establish a general claim.

### What the research found

Harel and Sowder built the framework from exploratory teaching experiments with university students in the United States, so it is a classification grounded in observation, not a measured distribution of schemes.
Earlier work had found the same standards.
Gary Martin and Harel (1989) found that many preservice elementary teachers accepted inductive arguments as proofs, while they also rated deductive arguments highly.
Daniel Chazan (1993) interviewed high school geometry students and found that some treated measured examples as proof, while others doubted that a deductive proof covers all cases.
Lulu Healy and Celia Hoyles (2000) surveyed about 2,500 high-attaining students aged 14 to 15 in England.
Many of them chose empirical arguments as the ones closest to their own approach, but expected algebraic arguments to receive the best mark from a teacher.

### History

Harel and Sowder published the framework in 1998.
In their chapter in the *Second Handbook of Research on Mathematics Teaching and Learning* (2007), they renamed the analytic class as the deductive class.
Nicolas Balacheff (1988) had earlier described a related ladder of student arguments: naive empiricism, the crucial experiment, the generic example and the thought experiment.

### Watch out

A teacher may treat an empirical argument as laziness.
The student in the opening may sincerely hold an empirical scheme, and until that changes she will not see why a proof is needed.
A task where examples mislead, such as [[a polynomial with forty prime values|H75AB4EJT5]], is a better response than a lower mark.
A teacher may also reward the form of a proof more than its content, which strengthens the ritual scheme.

### Try it

First, a student says "I checked it on my calculator for a thousand values of $n$".
Which scheme does that suggest?
It suggests an inductive empirical scheme, since the conviction comes from cases, however many.

Second, a student copies a textbook proof exactly and says "that's how proofs look".
That remark points to a ritual scheme, although an interview should check it.

## Explanations

### L1 human

Different people are convinced by different things.
Some believe a claim because a teacher or a book says it.
Some believe it after a few examples, for example after checking that $2 + 4 = 6$, $6 + 8 = 14$ and $10 + 12 = 22$ are even.
Others believe it only when they see a reason that works for all numbers.
A proof scheme is the name for what convinces a person, and teachers of proof try to move students from the first two kinds to the third.

### L2 human

Return to the claim that $n^2 - n$ is even, and compare three answers.
Student A is the student of the opening, with five even values and the words "so it is true".
Student B writes "$n^2 - n = n(n - 1)$, so it is even" and, when asked why, says that it looks like the proofs in the book.
Student C writes the same factorization and adds that one of the consecutive integers $n - 1$ and $n$ is even.

Check student C's reason by cases.
If $n$ is even, the factor $n$ is even; if $n$ is odd, the factor $n - 1$ is even.
In both cases the product is even, for every integer $n$.

So A shows an inductive empirical scheme, B suggests a ritual scheme in spite of correct algebra, and C shows a transformational scheme.
Watch out: B's text is almost a proof, and only the interview revealed the scheme, so a text alone can mislead in both directions.

### L3 human

Proof schemes belong to the cognitive research on proof, in which conviction is a state of a person, not a logical property of a text.
The framework is close to Balacheff's ladder and to the van Hiele levels of [[geometry education|1D7PZ2TF5Y]], which also place deduction at a late stage.
It contrasts with the logical view of [[mathematical proof|0B94TKFQJX]] and with the [[Toulmin model|RVZCSFDB2Y]], which studies the structure of public arguments.
The empirical scheme lies behind many errors in [[student difficulties with proof|5K2969GSWE]], and a [[generic proof|SG9XA69J64]] is a common bridge from the empirical scheme to the deductive one.
