---
tag: TQTDKMBJ0F
kind: definition
name: Reverse mathematics
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: grad
defines: 7SQS69T17R
uses: [DC60FYCSPM, Y92NXGEQBD, ~58b63877]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: General principles
---

## Definition

Let $\mathsf{RCA}_0$ be the [[base system|~58b63877]] of [[second-order arithmetic|DC60FYCSPM]]: the basic axioms, induction for $\Sigma^0_1$ formulas, and comprehension for $\Delta^0_1$ formulas.
Let $S$ be a theory in $L_2$ that contains $\mathsf{RCA}_0$, and let $\tau$ be a sentence of $L_2$.
Then $\tau$ is *equivalent to $S$ over $\mathsf{RCA}_0$* if both of these hold:

1. $S \vdash \tau$;
2. $\mathsf{RCA}_0 + \tau$ proves every axiom of $S$.

*Reverse mathematics* is the study of which subsystems of second-order arithmetic prove which theorems of ordinary mathematics, coded as sentences of $L_2$ with the codes of the [[definition|Y92NXGEQBD]].
Its typical results are proofs of a theorem in a subsystem $S$, and equivalences of a theorem to $S$ over $\mathsf{RCA}_0$.

## Notation

Part 2 is called the *reversal*.
For sentences, $\mathsf{RCA}_0 \vdash \tau \leftrightarrow \sigma$ is written $\tau \equiv \sigma$ over $\mathsf{RCA}_0$, or $\tau \leftrightarrow \sigma$ when the base is clear.

## Remarks

The base theory is part of the definition.
Over a stronger base, more theorems become provable, and then all of them are equivalent to each other.
The choice of $\mathsf{RCA}_0$ makes the base match computable mathematics: its least $\omega$-model consists of the computable sets.

Example: the Heine-Borel theorem for $[0, 1]$ is equivalent to $\mathsf{WKL}_0$ over $\mathsf{RCA}_0$, and the Bolzano-Weierstrass theorem is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.

Non-example: weak König's lemma is provable in $\mathsf{ACA}_0$, but it is not equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.
Part 2 fails: the $\omega$-model of the low sets satisfies $\mathsf{WKL}_0$ and not $\mathsf{ACA}_0$.

## Explanations

### L1 human

A theorem is matched to an axiom system when two things hold.
The axioms prove the theorem.
The theorem, together with a weak base, proves the axioms back.

### L2 human

To show that $\tau$ is equivalent to $\mathsf{ACA}_0$, one proves $\tau$ from arithmetical comprehension, and then one proves arithmetical comprehension from $\tau$ in $\mathsf{RCA}_0$.
Since $\mathsf{ACA}_0$ is equivalent over $\mathsf{RCA}_0$ to the statement that the range of every one-to-one function exists, the second part usually proves this one statement.
A trap is to use, inside the reversal, a set that $\mathsf{RCA}_0$ cannot build.
