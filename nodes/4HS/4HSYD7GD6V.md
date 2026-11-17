---
tag: 4HSYD7GD6V
kind: example
name: A bare computation is not a written proof
msc: ["00A35", "97E50"]
topics: [STSM6PR7TX]
audience: ug1
not_instance_of:
  - target: 8JQHJK94RZ
    note: the text does not state what is proved, gives no reason for its main step, and has no sentences that guide the reader
uses: [8JQHJK94RZ, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
---

## Example

A student must prove the following claim.

> For every real number $x$, if $x^2 - 5x + 6 < 0$, then $2 < x < 3$.

The student hands in this text.

> $(x - 2)(x - 3) < 0$.
> $x \in (2, 3)$.
> $\blacksquare$

We check the text against the rules of [[writing proofs|8JQHJK94RZ]].

1. The text does not state what is proved. It does not say that $x$ is real or that $x^2 - 5x + 6 < 0$ is assumed.
2. The first line does not say where it comes from. The reader must find the factorization $x^2 - 5x + 6 = (x - 2)(x - 3)$ alone.
3. The step from the first line to the second line has no reason. It is the main step of the proof, and it needs an argument about signs.
4. The text has no words, so the reader cannot tell which line is assumed and which line is derived.

The rest of the page writes the proof.

> Let $x$ be a real number with $x^2 - 5x + 6 < 0$.
> We expand $(x - 2)(x - 3) = x^2 - 3x - 2x + 6 = x^2 - 5x + 6$, so $(x - 2)(x - 3) < 0$.
> A product of two real numbers is negative only when one factor is positive and the other factor is negative.
> So we have two cases.
> Case 1: $x - 2 < 0$ and $x - 3 > 0$.
> Then $x < 2$ and $x > 3$, and no real number satisfies both.
> So this case does not occur.
> Case 2: $x - 2 > 0$ and $x - 3 < 0$.
> Then $x > 2$ and $x < 3$.
> Only Case 2 occurs, so $2 < x < 3$.
> $\square$

## Remarks

1. The student's two lines are true, and they are the right outline. The text fails as a proof because the reader cannot check it, not because a line is false.
2. The written proof is a [[proof by cases|0WCP0PVET6]]. The case split is the content that the bare text hides.
3. A check with a number supports the claim: for $x = 2.5$ we get $6.25 - 12.5 + 6 = -0.25 < 0$, and $2 < 2.5 < 3$. A check of one number is not a proof.
4. A shorter proof is acceptable for a reader who has seen many quadratic inequalities. It reads "The roots of $x^2 - 5x + 6$ are $2$ and $3$, and the leading coefficient is positive, so the polynomial is negative exactly between the roots". This text still states the reason for its step.

## Explanations

### L1 human

Writing only the answer is like handing in "$15$" for a word problem.
The answer may be right, but nobody can see how it was found or check it.
Here the student writes two short lines with symbols and no words.
A proof must say what it assumes, what each line follows from, and what it shows at the end.
The corrected version is longer, but each sentence can be checked on its own.

### L2 human

We repair a second bare text: "$n = 2k$, $n^2 = 4k^2 = 2(2k^2)$." for the claim "if $n$ is an even integer, then $n^2$ is even".

1. State the claim and the assumption: "Let $n$ be an even integer."
2. Give the reason for the form: "By the definition of an even integer, $n = 2k$ for an integer $k$."
3. Keep the calculation as a sentence: "Then $n^2 = 4k^2 = 2(2k^2)$."
4. Give the reason for the type: "The number $2k^2$ is an integer."
5. State the conclusion: "So $n^2$ is even."

The typical use of this repair is to turn scratch work into a proof that a grader or a reader can check.
A trap is to add words that do not carry reasons, such as a claim that the main step is easy.
The step still needs its argument.
