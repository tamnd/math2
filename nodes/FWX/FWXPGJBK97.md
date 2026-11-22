---
tag: FWXPGJBK97
kind: example
name: 'A conditional with a hidden quantifier: "if x > 2, then x^2 > 4"'
msc: ["97E40"]
topics: [WMY13MXY3W]
audience: school
instance_of: [FA6YZGR2SS]
uses: [FA6YZGR2SS, EGTZPA6QH3, 0GHS47PDAQ]
sources:
  - url: https://en.wikipedia.org/wiki/Material_conditional
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Quantifier_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.1
---

## Example

A textbook writes: "if $x > 2$, then $x^2 > 4$".
The variable $x$ has no value, so the sentence alone is an open sentence.
Every reader understands it as a [[conditional statement|FA6YZGR2SS]] with a hidden [[universal quantifier|0GHS47PDAQ]]:
$$\text{for every real number } x, \text{ if } x > 2, \text{ then } x^2 > 4.$$
We prove this statement and then see what the quantifier does.

1. Let $x$ be a real number with $x > 2$.
   This is the hypothesis.
2. Since $x > 2 > 0$, we may multiply the inequality $x > 2$ by the positive number $x$, and we get $x^2 > 2x$.
3. Since $x > 2$, we also have $2x > 4$.
4. Steps 2 and 3 give $x^2 > 2x > 4$, so $x^2 > 4$.
   This is the conclusion.
5. The real number $x$ in step 1 was arbitrary, so the conditional holds for every real $x$.

## Remarks

The quantifier, not the conditional, carries the word "every".
Without it, "if $x > 2$, then $x^2 > 4$" has a truth value only after we choose $x$.
For $x = 3$ both parts are true, for $x = -3$ the hypothesis is false and the conclusion true, and for $x = 1$ both parts are false.
The conditional is true in all three cases, and the proof shows that it is true for every $x$.

The converse, "for every real $x$, if $x^2 > 4$, then $x > 2$", is false.
The number $x = -3$ has $x^2 = 9 > 4$ but $x \le 2$.
The correct biconditional is "for every real $x$, $x^2 > 4$ if and only if $x > 2$ or $x < -2$".

The hidden quantifier also hides a domain, and the domain can change the truth value.
Over the positive real numbers the converse is true: from $x^2 > 4$ we get
$$(x - 2)(x + 2) > 0,$$
and $x + 2 > 0$, so $x - 2 > 0$.
[[Quantifiers in mathematical writing|EGTZPA6QH3]] treats such implicit quantifiers in general.

## Explanations

### L1 human

"If a number is bigger than $2$, then its square is bigger than $4$."
The sentence does not name a number.
It means that for every number, if it is bigger than $2$, then its square is bigger than $4$.
For $3$ the square is $9$, which is bigger than $4$.
For $2.5$ the square is $6.25$, which is bigger than $4$.
The proof shows that no number bigger than $2$ fails.

### L2 human

Find the hidden quantifiers in "if $a$ divides $b$ and $b$ divides $c$, then $a$ divides $c$".
The letters $a$, $b$ and $c$ have no values, so each carries a hidden "for every", and the word "divides" tells us that the domain is the integers.
The full statement is: for all integers $a$, $b$ and $c$, if $a \mid b$ and $b \mid c$, then $a \mid c$.
To prove it, write $b = ak$ and $c = bl$ with integers $k$ and $l$.
Then
$$c = bl = (ak)l = a(kl),$$
so $a \mid c$.

This is the standard shape of a proof of a conditional with variables: fix arbitrary values, assume the hypothesis, reach the conclusion.
Watch out: checking the conditional for a few values, such as $x = 3$ and $x = 10$, checks only those instances.
The hidden "for every" needs an argument that works for each $x$.
