---
tag: RXWW8J8RGJ
kind: example
name: A diamond on the two-element algebra that fails normality
msc: ["03G05", "03B45"]
topics: [QYA4H5Y7VR]
audience: research
not_instance_of:
  - target: 3H85NSFWHK
    note: the diamond sends 0 to 1, so the box fails the law that box 1 = 1
uses: [JCP47TNBSD, 0WG43AC0EV]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
---

## Example

On the [[two-element Boolean algebra|0WG43AC0EV]] $\set{0, 1}$, put $\Diamond x = 1$ for both $x$.
The dual box is $\Box x = \neg \Diamond \neg x = 0$ for both $x$.

1. $\Diamond(x \lor y) = 1 = \Diamond x \lor \Diamond y$, so $\Diamond$ preserves binary joins.
2. $\Diamond 0 = 1 \ne 0$, so $\Diamond$ fails the normality law.
3. Dually, $\Box 1 = 0 \ne 1$.

So $(\set{0, 1}, \Box)$ is not a [[modal algebra|JCP47TNBSD]].

## Remarks

1. The example shows that normality is independent of additivity.
2. The algebra models a logic in which $\Diamond \bot$ is valid; such a logic is not normal.
3. Rule necessitation fails for it: $\top$ is valid, while $\Box \top$ takes the value $0$.

## Explanations

### L1 human

Here "possibly" is always true, even for a false statement.
A normal modal logic does not allow this: a contradiction is never possible.

### L2 human

1. Compute $\Box(1 \land 1) = 0$ and $\Box 1 \land \Box 1 = 0$: meets are preserved.
2. Compute $\Box 1 = 0$: the top is not preserved.
3. So only the clause $\Box 1 = 1$ of the definition fails.

The typical use: it separates the two clauses in the definition of a modal algebra.
The trap: preserving binary meets does not give $\Box 1 = 1$, because the empty meet is a separate case.
