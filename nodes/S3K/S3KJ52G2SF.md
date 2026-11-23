---
tag: S3KJ52G2SF
kind: example
name: Negation, conjunction and disjunction from the Sheffer stroke
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
instance_of: [1NNYWRN6B8]
uses: [1NNYWRN6B8, 029JBBF693, 025YZN3VJW, 0F72FK8EKB, 06GYGS41JK]
sources:
  - url: https://en.wikipedia.org/wiki/Sheffer_stroke
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

A factory makes only NAND gates, and an engineer must build NOT, AND and OR from them.
The [[Sheffer stroke|1NNYWRN6B8]] $p \uparrow q$ is F when $p$ and $q$ are both T, and T otherwise.
We check three [[logical equivalences|06GYGS41JK]]:
$$\neg p \equiv p \uparrow p, \qquad p \land q \equiv (p \uparrow q) \uparrow (p \uparrow q), \qquad p \lor q \equiv (p \uparrow p) \uparrow (q \uparrow q).$$

1. [[Negation|029JBBF693]]: at $p$ = T, $p \uparrow p = \mathrm{T} \uparrow \mathrm{T} = \mathrm{F}$, and at $p$ = F, $p \uparrow p = \mathrm{F} \uparrow \mathrm{F} = \mathrm{T}$.
   These are the values of $\neg p$.
2. [[Conjunction|025YZN3VJW]]: by step 1 applied to the formula $p \uparrow q$, the formula $(p \uparrow q) \uparrow (p \uparrow q)$ has the value of $\neg(p \uparrow q)$.
   Since $p \uparrow q$ has the value of $\neg(p \land q)$, this is $\neg\neg(p \land q)$, which has the value of $p \land q$.
3. [[Disjunction|0F72FK8EKB]]: by step 1, $(p \uparrow p) \uparrow (q \uparrow q)$ has the value of $\neg p \uparrow \neg q$, which is $\neg(\neg p \land \neg q)$.
   By [[De Morgan's laws|09PKJKA6J0]], this has the value of $p \lor q$.

The table confirms steps 2 and 3 in all four rows.

| $p$ | $q$ | $p \uparrow q$ | $(p \uparrow q) \uparrow (p \uparrow q)$ | $p \land q$ | $p \uparrow p$ | $q \uparrow q$ | $(p \uparrow p) \uparrow (q \uparrow q)$ | $p \lor q$ |
|---|---|---|---|---|---|---|---|---|
| T | T | F | T | T | F | F | T | T |
| T | F | T | F | F | F | T | T | T |
| F | T | T | F | F | T | F | T | T |
| F | F | T | F | F | T | T | F | F |

## Remarks

### Completeness of the stroke

The stroke alone expresses $\neg$, $\land$ and $\lor$.
Since $\{\neg, \land\}$ is [[functionally complete|TDZVCWYJ9F]], the stroke alone is functionally complete.
The same method gives $p \to q \equiv p \uparrow (q \uparrow q)$, because $q \uparrow q$ is $\neg q$ and $p \uparrow \neg q$ is $\neg(p \land \neg q)$.

### The cost of one connective

The formulas grow fast.
The formula for $p \land q$ uses the stroke three times, and the formula for $p \lor q$ also uses it three times.
In circuits each stroke is one NAND gate, so the number of strokes is the number of gates.

## Explanations

### L1 human

The stroke means "not both".
"Not both $p$ and $p$" is the same as "not $p$", because $p$ and $p$ are the same statement.
To get "and", we say "not both" twice: "it is not true that (not both $p$ and $q$)".
Two "nots" cancel, and what is left is "$p$ and $q$".

### L2 human

Write $\neg(p \lor q)$ with the stroke alone, and check one row.

1. By the example, $p \lor q \equiv (p \uparrow p) \uparrow (q \uparrow q)$.
   Call this formula $D$.
2. By step 1 of the example, $\neg D \equiv D \uparrow D$.
3. So $\neg(p \lor q) \equiv \big((p \uparrow p) \uparrow (q \uparrow q)\big) \uparrow \big((p \uparrow p) \uparrow (q \uparrow q)\big)$.
4. Check the row FF: $p \uparrow p = \mathrm{T}$ and $q \uparrow q = \mathrm{T}$, so $D = \mathrm{T} \uparrow \mathrm{T} = \mathrm{F}$, and $D \uparrow D = \mathrm{F} \uparrow \mathrm{F} = \mathrm{T}$.
   This is the value of $\neg(\mathrm{F} \lor \mathrm{F})$.

Such translations rewrite a circuit with one type of gate.
Watch out: $p \uparrow q$ is not $\neg p \uparrow \neg q$.
At $p$ = $q$ = T the first is F, and the second is $\mathrm{F} \uparrow \mathrm{F} = \mathrm{T}$.
