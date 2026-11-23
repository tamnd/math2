---
tag: 6EAWB0HSJZ
kind: example
name: The proposition "n is negative" is not the negation of "n is positive"
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 029JBBF693
    note: for n = 0 both propositions are false, while a proposition and its negation have opposite truth values
uses: [029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Negation
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
---

## Example

For an integer $n$, let $p$ be "$n$ is positive", that is, $n > 0$, and let $r$ be "$n$ is negative", that is, $n < 0$.
The proposition $r$ is the opposite of $p$, but it is not the [[negation|029JBBF693]] of $p$.
We check the condition that fails.

1. The negation of $p$ must be true whenever $p$ is false, for every value of $n$.
2. Take $n = 0$.
   Then $0 > 0$ is false, so $p$ is F.
3. For $n = 0$ the inequality $0 < 0$ is also false, so $r$ is F.
4. So $p$ and $r$ are both F at $n = 0$, and $r$ breaks the row "$p$ F, $\neg p$ T" of the truth table of negation.
5. The correct negation is "$n \le 0$", which is T at $n = 0$.

## Remarks

A negation and an opposite are different things.
Two opposite statements cannot both be true, but they can both be false.
A statement and its negation can be neither both true nor both false.

The gap between the opposites is the set of values where both fail, here the single value $n = 0$.
If we restrict $n$ to the nonzero integers, the gap disappears, and "$n < 0$" is equivalent to the negation of "$n > 0$" on that domain.
The same gap separates "every student passed" from "no student passed": both are false when some students passed and some failed.

## Explanations

### L1 human

"The number is positive" and "the number is negative" sound like a claim and its denial.
They are not, because of the number $0$.
Zero is neither positive nor negative, so for $0$ both claims are false.
The real denial of "the number is positive" is "the number is zero or negative".

### L2 human

Is "$f$ is decreasing" the negation of "$f$ is increasing", for functions $f \colon \mathbb{R} \to \mathbb{R}$?
Here "increasing" means $f(a) \le f(b)$ whenever $a < b$, and "decreasing" means $f(a) \ge f(b)$ whenever $a < b$.
Take $f(x) = x^2$.
It is not increasing, because $f(-1) = 1 > 0 = f(0)$, and it is not decreasing, because $f(0) = 0 < 1 = f(1)$.
Both statements are false for $f$, so "decreasing" is not the negation of "increasing".
Test a proposed negation on such a boundary case before you use it in a proof.
Watch out: the true negation of "$f$ is increasing" is "there are $a < b$ with $f(a) > f(b)$", which is much weaker than "$f$ is decreasing".
