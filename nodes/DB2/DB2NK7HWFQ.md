---
tag: DB2NK7HWFQ
kind: example
name: "The parity of three inputs: p ⊕ q ⊕ r"
msc: ["03B05", "06E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [PTMR3P9J6C]
uses: [PTMR3P9J6C, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Parity_function
    locator: lead section
---

## Example

A hall lamp is wired to three switches, and each flip of any switch changes the lamp.
Let $p$, $q$, $r$ say that the first, second and third switch has been flipped.
We compute the [[truth table|05RSK4Q657]] of $(p \oplus q) \oplus r$, where $\oplus$ is the [[exclusive or|PTMR3P9J6C]], and compare it with the number of true inputs.

1. In each row, compute $p \oplus q$ first.
   It is T exactly when $p$ and $q$ differ.
2. Then compute $(p \oplus q) \oplus r$.
   It is T exactly when $p \oplus q$ and $r$ differ.
3. The last column counts the inputs that are T.

| $p$ | $q$ | $r$ | $p \oplus q$ | $(p \oplus q) \oplus r$ | number of T |
|---|---|---|---|---|---|
| T | T | T | F | T | $3$ |
| T | T | F | F | F | $2$ |
| T | F | T | T | F | $2$ |
| T | F | F | T | T | $1$ |
| F | T | T | T | F | $2$ |
| F | T | F | T | T | $1$ |
| F | F | T | F | T | $1$ |
| F | F | F | F | F | $0$ |

4. The formula is T in the rows with $1$ or $3$ true inputs, and F in the rows with $0$ or $2$ true inputs.
5. So $(p \oplus q) \oplus r$ is T exactly when an odd number of $p$, $q$, $r$ is T.
6. The same computation for $p \oplus (q \oplus r)$ gives the same column, because the value depends only on the number of true inputs.
   So $\oplus$ is associative, and we may write $p \oplus q \oplus r$.

## Remarks

### Parity for any number of inputs

With $1$ for T and $0$ for F, the value is $p + q + r$ modulo $2$.
The row TTT gives T, since $1 + 1 + 1 = 3$ is odd.
This row separates the exclusive or of three inputs from [["exactly one of three"|ZV2QXSKFRG]].
The same rule holds for any number of inputs: $p_1 \oplus \cdots \oplus p_n$ is T exactly when an odd number of the $p_i$ is T.
Each new input that is T changes the value, and each new input that is F leaves it unchanged, so the rule follows by induction on $n$.

### The parity bit

An application is the [[parity bit|D0E6Y0P30Q]].
For the data bits $1, 0, 1, 1$, the exclusive or is $1 \oplus 0 \oplus 1 \oplus 1 = 1$.
A sender appends this bit, so the five bits $1, 0, 1, 1, 1$ hold an even number of $1$s.
If one bit flips during transmission, the number of $1$s becomes odd, and the receiver detects the error.
If two bits flip, the count is even again, and the check does not detect the error.

## Explanations

### L1 human

Three people each may flip a light switch, and the lamp starts off.
Every flip changes the lamp from off to on or from on to off.
If one person flips, the lamp is on.
If two people flip, the second flip undoes the first, and the lamp is off.
If all three flip, the lamp is on again.
So the lamp is on when an odd number of people flip, and that is the exclusive or of the three flips.

### L2 human

Compute $1 \oplus 1 \oplus 0 \oplus 1 \oplus 1 \oplus 0$ in two ways.

1. From left to right: $1 \oplus 1 = 0$, then $0 \oplus 0 = 0$, then $0 \oplus 1 = 1$, then $1 \oplus 1 = 0$, then $0 \oplus 0 = 0$.
2. By counting: there are four $1$s, an even number, so the result is $0$.
3. The two ways agree, as associativity and the parity rule say.

The parity rule replaces a long chain of exclusive ors by a count.
Watch out: the result depends on whether the count is odd, not on whether it is $1$.
Four true inputs give F, and three true inputs give T.
