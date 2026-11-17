---
tag: AJR1GG3GF3
kind: example
name: Fermat's Last Theorem was a conjecture before 1994
msc: ["00A35", "11D41"]
topics: [N4P3E53HM0]
audience: school
not_instance_of:
  - target: KK5F0F03ZW
    note: for more than three centuries the statement had the name of a theorem but no accepted proof, so in that time it was a conjecture, not a theorem
uses: [KK5F0F03ZW, 0Y5X3SDBCZ, 0E741HSMJ1]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Wiles%27s_proof_of_Fermat%27s_Last_Theorem
    locator: lead section
---

## Example

The statement is [[Fermat's Last Theorem|0Y5X3SDBCZ]]: for each integer $n > 2$, there are no positive integers $a$, $b$ and $c$ with $a^n + b^n = c^n$.
We check its status at different times against the meaning of the word [[theorem|KK5F0F03ZW]].

1. A theorem is a statement with an accepted proof. The name of a statement does not give it a proof.
2. Around 1637, Pierre de Fermat wrote the statement in the margin of a book and wrote that he had a proof. No such proof was ever found.
3. Fermat's method of infinite descent proves the [[case $n = 4$|0E741HSMJ1]], and Leonhard Euler published a proof for $n = 3$ in 1770. These are proofs of special cases, not of the statement.
4. So, from 1637 until 1994, the full statement had no accepted proof. In that time it was a conjecture, although its name called it a theorem.
5. Andrew Wiles gave a proof in 1994, with one step completed jointly with Richard Taylor, and the proof was published in 1995.
6. From 1994 on, the statement is a theorem. Its name now matches its status.

## Remarks

The example shows that the label "theorem" in a name is a historical fact, not a certificate.
The name became usual because the statement was the last of Fermat's claims that remained without proof.
A statement with the name of a conjecture can also be a theorem now: the Poincaré conjecture was proved by Grigori Perelman.
For this reason, a careful text checks the status of a named result before it uses the result in a proof.

The special cases in step 3 had real proofs.
For a fixed exponent such as $n = 4$, the statement was a theorem long before 1994.
Only the statement for all $n > 2$ waited for Wiles.

## Explanations

### L1 human

Fermat's Last Theorem says that $a^n + b^n = c^n$ has no solution in positive whole numbers when $n$ is $3$ or more.
Fermat wrote it down around 1637 and said that he had a proof, but nobody found one.
For more than three hundred years, nobody could prove it, so it was really a guess with a famous name.
Andrew Wiles proved it in 1994.
Only from then on was it truly a theorem.

### L2 human

We sort four statements by their status in the year 1990.

1. "$a^4 + b^4 = c^4$ has no solution in positive integers": a theorem in 1990, proved by Fermat's method of descent.
2. "$a^3 + b^3 = c^3$ has no solution in positive integers": a theorem in 1990, with a proof published by Euler in 1770 and later proofs.
3. "$a^n + b^n = c^n$ has no solution for each $n > 2$": a conjecture in 1990, despite its name.
4. "There are infinitely many prime numbers": a theorem since Euclid.

The typical use of this check is to read the status of a result in a reliable source before using it.
A trap is to cite a famous name in a proof without knowing whether the result is proved.
