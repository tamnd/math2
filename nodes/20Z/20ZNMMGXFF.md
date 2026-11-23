---
tag: 20ZNMMGXFF
kind: example
name: The biconditional "x^2 = 1 if and only if x = 1" for x = 1, −1, 2
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0S6GMNJ62Y]
uses: [0S6GMNJ62Y, 0V6GAWTBYW, 0ZNX6DQ3EJ]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_biconditional
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Example

A student claims "a real number squares to $1$ if and only if it is $1$", and we test the claim at three numbers.
For a real number $x$, let $p$ be "$x^2 = 1$" and $q$ be "$x = 1$".
At each value we compute the [[biconditional|0S6GMNJ62Y]] $p \leftrightarrow q$ and also $(p \to q) \land (q \to p)$.

| $x$ | $p$ | $q$ | $p \to q$ | $q \to p$ | $p \leftrightarrow q$ |
|---|---|---|---|---|---|
| $1$ | T | T | T | T | T |
| $-1$ | T | F | F | T | F |
| $2$ | F | F | T | T | T |

1. At $x = 1$, $x^2 = 1$, so both sides are T, and the row TT of the [[truth table|0V6GAWTBYW]] gives T.
2. At $x = -1$, $x^2 = (-1)(-1) = 1$, so $p$ is T and $q$ is F.
   The row TF gives F, and indeed $p \to q$ is F there.
3. At $x = 2$, $x^2 = 4 \neq 1$, so both sides are F, and the row FF gives T.
4. The row FT occurs for no real $x$.
   If $q$ is T, then $x = 1$, so $x^2 = 1$ and $p$ is T.

So the claim is true at $x = 1$ and $x = 2$, and false at $x = -1$.

## Remarks

### Which direction fails

The universal claim "for every real $x$, $x^2 = 1$ if and only if $x = 1$" is false, and $x = -1$ is the counterexample.
Step 4 shows that the direction $(\Leftarrow)$, "if $x = 1$, then $x^2 = 1$", holds for every $x$.
So only the direction $(\Rightarrow)$ fails.

### Two repairs

Change $q$ to "$x = 1$ or $x = -1$", and the biconditional becomes true for every real $x$.
Indeed $x^2 = 1$ gives $(x - 1)(x + 1) = 0$, so $x = 1$ or $x = -1$, and both values give $x^2 = 1$.
Alternatively, restrict $x$ to the positive real numbers, and the original biconditional becomes true, because $x = -1$ is no longer allowed.

## Explanations

### L1 human

The sentence "a number squares to $1$ exactly when the number is $1$" sounds right at first.
For the number $1$ both parts are true.
For the number $2$ both parts are false, since $2 \cdot 2 = 4$.
For the number $-1$ the first part is true, since $(-1) \cdot (-1) = 1$, but the second part is false.
So the two parts do not always agree, and the sentence is false.

### L2 human

Test the claim "for every real $x$, $x^3 = 8$ if and only if $x = 2$".

1. $(\Leftarrow)$ If $x = 2$, then $x^3 = 8$.
2. $(\Rightarrow)$ If $x^3 = 8$, then $x^3 - 8 = (x - 2)(x^2 + 2x + 4) = 0$.
3. The factor $x^2 + 2x + 4 = (x + 1)^2 + 3$ is at least $3$, so it is not $0$.
4. So $x - 2 = 0$, and $x = 2$.
5. Both directions hold, so the biconditional is true for every real $x$.

Splitting into two directions shows which one can fail, so we look for a counterexample only there.
Watch out: the analogy with $x^2 = 1$ suggests a second solution $x = -2$, but $(-2)^3 = -8 \neq 8$.
