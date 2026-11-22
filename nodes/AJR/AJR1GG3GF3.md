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

The statement is [[Fermat's Last Theorem|0Y5X3SDBCZ]]: for every integer $n > 2$, no positive integers $a$, $b$ and $c$ satisfy $a^n + b^n = c^n$.
We check its status at different times against the meaning of the word [[theorem|KK5F0F03ZW]].

1. A theorem is a statement with an accepted proof.
   The name of a statement does not give it a proof.
2. Around 1637 Pierre de Fermat wrote the statement in the margin of a book and wrote that he had a proof.
   No such proof was ever found.
3. Fermat's method of infinite descent proves the [[case n = 4|0E741HSMJ1]], and Leonhard Euler published a proof for $n = 3$ in 1770.
   These prove special cases, not the statement.
4. So from 1637 until 1994 the full statement had no accepted proof.
   In that time it was a conjecture, although its name called it a theorem.
5. Andrew Wiles gave a proof in 1994, with one step completed jointly with Richard Taylor, and the proof was published in 1995.
6. From then on the statement is a theorem, and its name matches its status.

## Remarks

A name that contains "theorem" is a fact about history, not a certificate of proof.
The name became usual because the statement was the last of Fermat's claims that remained without proof.
The reverse also happens: the Poincaré conjecture is now a theorem, proved by Grigori Perelman, and it keeps its old name.
So a careful author checks the status of a named result before using it as a step in a proof.

The special cases had real proofs.
For a fixed exponent such as $n = 4$ the statement was a theorem long before 1994, and the cases $n = 3$ and $n = 4$ together settle every exponent divisible by $3$ or $4$.
For example, a solution with $n = 6$ would give $(a^2)^3 + (b^2)^3 = (c^2)^3$, a solution with exponent $3$, which Euler's case excludes.
Only the statement for all $n > 2$ waited for Wiles.

## Explanations

### L1 human

Fermat's Last Theorem says that $a^n + b^n = c^n$ has no solution in positive whole numbers when $n$ is $3$ or more.
For $n = 2$ there are many solutions, such as $3^2 + 4^2 = 5^2$.
Fermat wrote the claim down around 1637 and said that he had a proof, but nobody found one.
For more than three hundred years nobody could prove it, so it was really a guess with a famous name.
Andrew Wiles proved it in 1994, and only from then on was it truly a theorem.

### L2 human

Sort four statements by their status in the year 1990.
"$a^4 + b^4 = c^4$ has no solution in positive integers" was a theorem, proved by Fermat's method of descent.
"$a^3 + b^3 = c^3$ has no solution in positive integers" was a theorem, with a proof published by Euler in 1770 and later proofs.
"$a^n + b^n = c^n$ has no solution for every $n > 2$" was a conjecture, despite its name.
"There are infinitely many primes" had been a theorem since Euclid.
The test in each case is the same: is there an accepted proof, not what is the statement called.
