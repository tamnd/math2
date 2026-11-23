---
tag: ZP7N9AK9ZX
kind: example
name: "Exportation: (p and q) implies r is equivalent to p implies (q implies r)"
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0JMR2HM2N2]
uses: [0JMR2HM2N2, 05RSK4Q657, 0NMG7W7Q11, 025YZN3VJW]
sources:
  - url: https://en.wikipedia.org/wiki/Exportation_(logic)
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Example

"If it is Saturday and it is sunny, we go to the beach" says the same as "if it is Saturday, then, if it is sunny, we go to the beach".
With $p$ for "it is Saturday", $q$ for "it is sunny" and $r$ for "we go to the beach", the two sentences are
$$(p \land q) \to r \qquad \text{and} \qquad p \to (q \to r).$$
We show that they are [[logically equivalent|0JMR2HM2N2]] by finding the rows where each is false.

1. An [[implication|0NMG7W7Q11]] $a \to b$ is false only when $a$ is true and $b$ is false.
2. So $(p \land q) \to r$ is false only when $p \land q$ is true and $r$ is false.
   By the definition of [[conjunction|025YZN3VJW]], this is the single row $p$ T, $q$ T, $r$ F.
3. The formula $p \to (q \to r)$ is false only when $p$ is true and $q \to r$ is false.
4. The formula $q \to r$ is false only when $q$ is true and $r$ is false.
   So $p \to (q \to r)$ is false only in the row $p$ T, $q$ T, $r$ F.
5. Both formulas are false in the same single row and true in the other seven rows.

The full [[truth table|05RSK4Q657]], with the $2^3 = 8$ rows in the standard order, confirms this.

| $p$ | $q$ | $r$ | $p \land q$ | $(p \land q) \to r$ | $q \to r$ | $p \to (q \to r)$ |
|---|---|---|---|---|---|---|
| T | T | T | T | T | T | T |
| T | T | F | T | F | F | F |
| T | F | T | F | T | T | T |
| T | F | F | F | T | T | T |
| F | T | T | F | T | T | T |
| F | T | F | F | T | F | T |
| F | F | T | F | T | T | T |
| F | F | F | F | T | T | T |

The fifth and the seventh columns agree in every row, so $(p \land q) \to r \equiv p \to (q \to r)$.

## Remarks

The equivalence is called exportation, because the hypothesis $p$ moves out of the conjunction.
It explains a habit of mathematical writing.
A theorem "if $p$ and $q$, then $r$" is often proved in the form "assume $p$; now, if $q$, then $r$".
In type theory and in Lean the same equivalence is currying: a function of a pair corresponds to a function that returns a function.

The equivalence fails when the conjunction becomes a disjunction.
In the row $p$ T, $q$ F, $r$ F, the formula $(p \lor q) \to r$ is $\mathrm{T} \to \mathrm{F}$, which is false, while $p \to (q \to r)$ is $\mathrm{T} \to \mathrm{T}$, which is true.

Implication is not associative either.
In the row $p$ F, $q$ F, $r$ F, the formula $(p \to q) \to r$ is $\mathrm{T} \to \mathrm{F}$, which is false, while $p \to (q \to r)$ is true because $p$ is false.

## Explanations

### L1 human

"If it is Saturday and it is sunny, we go to the beach" and "if it is Saturday, then, if it is sunny, we go to the beach" are two ways to say one rule.
Both are broken in exactly one situation: a sunny Saturday without a trip to the beach.
In every other situation both are kept, so the two sentences are logically equivalent.

### L2 human

We use exportation to organize a proof that if $n$ is even and $3$ divides $n$, then $6$ divides $n$, for an integer $n$.

1. By exportation, it is enough to prove: if $n$ is even, then, if $3$ divides $n$, then $6$ divides $n$.
2. Assume that $n$ is even, so $n = 2k$ for an integer $k$.
3. Now assume that $3$ divides $n = 2k$.
   Since $3$ is prime and $3$ does not divide $2$, the number $3$ divides $k$, so $k = 3m$ for an integer $m$.
4. Then $n = 6m$, so $6$ divides $n$.

Proofs of theorems with several hypotheses take the hypotheses in one at a time like this, and exportation is the reason it is allowed.
Watch out for the wrong bracketing: $(p \to q) \to r$ is a different formula, as the remarks show.
