---
tag: DJ1RWAEHYD
kind: example
name: A student referee report on a proof about irrational numbers
msc: ["00A35", "11J72"]
topics: [STSM6PR7TX]
audience: ug2
instance_of: [4M98ZZNK0E]
uses: [4M98ZZNK0E, 0DZXAXEJQ9, 0NCJ5WXN6Z, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Irrational_number
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Peer_review
    locator: lead section
---

## Example

The statement is that if $r$ is a rational number and $x$ is an [[irrational number|0DZXAXEJQ9]], then $r + x$ is irrational.
A real number is irrational when it is not of the form $a/b$ with integers $a$ and $b \ne 0$.
A student hands in the following proof.

> (1) Suppose that $r$ is rational, $x$ is irrational, and $r + x$ is rational.
> (2) Then $r + x = q$ for a rational number $q$.
> (3) So $x = q - r$.
> (4) So $x$ is rational, which contradicts the hypothesis that $x$ is irrational.
> (5) Hence $r + x$ is irrational.

We check it by the method of [[checking a proof|4M98ZZNK0E]].
The frame is a [[proof by contradiction|0J0XBKG64S]], and line (1) assumes the correct negation, since a real number that is not irrational is rational.
Lines (2) and (3) are correct: one names $r + x$, and the other subtracts $r$ from both sides.
Line (4) claims that $q - r$ is rational without a reason.
The claim is true, so this is a gap, not an error.
It is filled by writing $q = a/b$ and $r = c/d$ with integers $a, b, c, d$ and $b, d \ne 0$, so that $q - r = (ad - bc)/(bd)$, a quotient of integers with a nonzero denominator.

Both hypotheses are used in line (4): "$x$ is irrational" for the contradiction, and "$r$ is rational" inside the claim about $q - r$.
To confirm this, drop "$r$ is rational" and take $r = -\sqrt{2}$ and $x = \sqrt{2}$, so that $r + x = 0$ is rational and the conclusion fails.
Lines (1) to (3) still hold with $q = 0$, and line (4) fails, since $q - r = \sqrt{2}$ is irrational.
So the dropped hypothesis enters exactly where the gap was found.

The report reads as follows.

> Summary: the proof assumes that $r + x$ is rational and derives that $x$ is rational, a contradiction.
> Verdict: correct with a minor gap.
> Line (4): the claim that a difference of rational numbers is rational needs a reason, and a two-line computation with fractions supplies it.
> Presentation: the proof should say that $r$ and $x$ are real numbers.

## Remarks

The gap in line (4) is minor for a reader who knows the arithmetic of fractions.
In a first course on proofs, where the closure of the [[rational numbers|0NCJ5WXN6Z]] under subtraction is new, a grader may ask for the computation.

The test with $r = -\sqrt{2}$ shows that the gap is the only place where the hypothesis on $r$ enters, so the gap is a real part of the proof and not a decoration.

For products the statement needs a new hypothesis.
With $r = 0$ the product $rx = 0$ is rational, so the correct statement assumes $r \ne 0$, and line (4) then uses $x = q/r$.

## Explanations

### L1 human

The claim is that a fraction plus a number that is not a fraction is never a fraction.
The student's proof says: if the sum were a fraction, then the non-fraction would be a fraction minus a fraction.
A careful checker asks why a fraction minus a fraction is a fraction.
The answer is a short computation, for example $\frac{3}{4} - \frac{1}{6} = \frac{18 - 4}{24} = \frac{14}{24}$.
So the proof is correct, but one reason is missing, and the report says so.

### L2 human

Each part of the report has a purpose.
The summary shows that the checker understood the method of the proof.
The verdict is one of four: correct, correct with minor gaps, incomplete, or wrong.
Each problem is tied to a line and has a kind, such as gap, error or unclear notation, and a repair when one is known.
Comments on presentation stay separate from problems of logic.

In peer assessment, each student checks another student's proof and writes such a report.
Watch out: the gap in line (4) is not an error, because an error is a false step and the step of line (4) is true.
