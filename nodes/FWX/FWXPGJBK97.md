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
The variable $x$ is not given a value, so the sentence alone is an open sentence.
A reader understands it as the [[conditional statement|FA6YZGR2SS]] with a hidden [[universal quantifier|0GHS47PDAQ]]:
$$\text{for every real number } x, \text{ if } x > 2, \text{ then } x^2 > 4.$$
We check that this statement is true, and we see why the quantifier matters.

1. Let $x$ be a real number with $x > 2$. This is the hypothesis.
2. Since $x > 2 > 0$, we may multiply the inequality $x > 2$ by the positive number $x$. This gives $x^2 > 2x$.
3. Since $x > 2$, we have $2x > 4$.
4. Steps 2 and 3 give $x^2 > 2x > 4$, so $x^2 > 4$. This is the conclusion.
5. The real number $x$ in step 1 was arbitrary, so the conditional holds for every real $x$.

## Remarks

The example shows that the quantifier, not the conditional, carries the word "every".
Without the quantifier, the open sentence "if $x > 2$, then $x^2 > 4$" has a truth value only after we choose $x$.
For $x = 3$ both parts are true, for $x = -3$ the hypothesis is false and the conclusion is true, and for $x = 1$ both parts are false.
In all three cases the conditional is true, and the proof shows that it is true for every $x$.

The converse "for every real $x$, if $x^2 > 4$, then $x > 2$" is false.
The number $x = -3$ has $x^2 = 9 > 4$, but $x = -3 \leq 2$.
The correct biconditional is "for every real $x$, $x^2 > 4$ if and only if $x > 2$ or $x < -2$".

If we change the domain to the positive real numbers, the converse becomes true.
For $x > 0$, the inequality $x^2 > 4$ gives $(x - 2)(x + 2) > 0$, and $x + 2 > 0$, so $x - 2 > 0$.
So the hidden quantifier also hides a domain, and the domain can change the truth value.
The page [[quantifiers in mathematical writing|EGTZPA6QH3]] treats such implicit quantifiers.

## Explanations

### L1 human

"If a number is bigger than $2$, then its square is bigger than $4$."
The sentence does not name a number.
It means: for every number, if it is bigger than $2$, then its square is bigger than $4$.
For $3$, the square is $9$, which is bigger than $4$.
For $2.5$, the square is $6.25$, which is bigger than $4$.
The proof shows that no number bigger than $2$ fails.

### L2 human

We find the hidden quantifiers in "if $a$ divides $b$ and $b$ divides $c$, then $a$ divides $c$".

1. The letters $a$, $b$ and $c$ have no values, so each one is bound by a hidden "for every".
2. The domain is the integers, as the word "divides" suggests.
3. The full statement is "for all integers $a$, $b$, $c$, if $a \mid b$ and $b \mid c$, then $a \mid c$".
4. Proof: write $b = ak$ and $c = bl$ with integers $k$ and $l$. Then $c = a(kl)$, so $a \mid c$.

The typical use is in a proof of a conditional with variables: we fix arbitrary values of the variables, assume the hypothesis, and reach the conclusion.

A trap: a student checks the conditional for a few values, for example $x = 3$ and $x = 10$, and stops.
This checks some instances, but the hidden "for every" needs an argument for each $x$.
