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

The [[Sheffer stroke|1NNYWRN6B8]] $p \uparrow q$ is false when $p$ and $q$ are both true, and true otherwise.
We check three [[logical equivalences|06GYGS41JK]]:
$$\neg p \equiv p \uparrow p, \qquad p \land q \equiv (p \uparrow q) \uparrow (p \uparrow q), \qquad p \lor q \equiv (p \uparrow p) \uparrow (q \uparrow q).$$

1. [[Negation|029JBBF693]]. At $p = \mathsf{T}$, $p \uparrow p = \mathsf{T} \uparrow \mathsf{T} = \mathsf{F}$. At $p = \mathsf{F}$, $p \uparrow p = \mathsf{F} \uparrow \mathsf{F} = \mathsf{T}$. These are the values of $\neg p$.
2. [[Conjunction|025YZN3VJW]]. By step 1 applied to the formula $p \uparrow q$, the formula $(p \uparrow q) \uparrow (p \uparrow q)$ has the value of $\neg(p \uparrow q)$. Since $p \uparrow q$ has the value of $\neg(p \land q)$, this is $\neg\neg(p \land q)$, which has the value of $p \land q$.
3. [[Disjunction|0F72FK8EKB]]. By step 1, $(p \uparrow p) \uparrow (q \uparrow q)$ has the value of $\neg p \uparrow \neg q$, which is $\neg(\neg p \land \neg q)$. By [[De Morgan's laws|09PKJKA6J0]], this has the value of $p \lor q$.

The table confirms steps 2 and 3 in all four rows.

| $p$ | $q$ | $p \uparrow q$ | $(p \uparrow q) \uparrow (p \uparrow q)$ | $p \land q$ | $p \uparrow p$ | $q \uparrow q$ | $(p \uparrow p) \uparrow (q \uparrow q)$ | $p \lor q$ |
|---|---|---|---|---|---|---|---|---|
| T | T | F | T | T | F | F | T | T |
| T | F | T | F | F | F | T | T | T |
| F | T | T | F | F | T | F | T | T |
| F | F | T | F | F | T | T | F | F |

## Remarks

The example shows that the stroke alone expresses $\neg$, $\land$ and $\lor$.
Since $\set{\neg, \land}$ is [[functionally complete|TDZVCWYJ9F]], the stroke alone is functionally complete.
The same method gives $p \to q \equiv p \uparrow (q \uparrow q)$, because $q \uparrow q$ is $\neg q$ and $p \uparrow \neg q$ is $\neg(p \land \neg q)$.

The formulas grow fast.
The formula for $p \land q$ uses the stroke three times, and a formula with $k$ conjunctions in $\neg$, $\land$ can need many more strokes after translation.
In circuits, each stroke is one NAND gate, so the length of the formula is the cost of the circuit.

## Explanations

### L1 human

The stroke means "not both".
"Not both $p$ and $p$" is the same as "not $p$", because $p$ and $p$ are the same statement.
To get "and", we say "not both" twice: "it is not true that (not both $p$ and $q$)".
Two "nots" cancel, and what is left is "$p$ and $q$".

### L2 human

We write $\neg(p \lor q)$ with the stroke alone, and we check one row.

1. By the example, $p \lor q \equiv (p \uparrow p) \uparrow (q \uparrow q)$. Call this formula $D$.
2. By step 1 of the example, $\neg D \equiv D \uparrow D$.
3. So $\neg(p \lor q) \equiv \big((p \uparrow p) \uparrow (q \uparrow q)\big) \uparrow \big((p \uparrow p) \uparrow (q \uparrow q)\big)$.
4. Check at $p = \mathsf{F}$, $q = \mathsf{F}$: $p \uparrow p = \mathsf{T}$, $q \uparrow q = \mathsf{T}$, so $D = \mathsf{T} \uparrow \mathsf{T} = \mathsf{F}$, and $D \uparrow D = \mathsf{F} \uparrow \mathsf{F} = \mathsf{T}$. This is the value of $\neg(\mathsf{F} \lor \mathsf{F})$.

The typical use of these translations is to rewrite a circuit with one type of gate.
A trap: the formula $p \uparrow q$ is not $\neg p \uparrow \neg q$; at $p = q = \mathsf{T}$ the first is $\mathsf{F}$ and the second is $\mathsf{F} \uparrow \mathsf{F} = \mathsf{T}$.
