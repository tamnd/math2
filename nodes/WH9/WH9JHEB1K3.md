---
tag: WH9JHEB1K3
kind: example
name: Negation, disjunction and conjunction from the Peirce arrow
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: ug1
instance_of: [1NNYWRN6B8]
uses: [1NNYWRN6B8, 029JBBF693, 025YZN3VJW, 0F72FK8EKB, 06GYGS41JK]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_NOR
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
---

## Example

Now the factory makes only NOR gates, and the engineer must again build NOT, OR and AND.
The Peirce arrow $p \downarrow q$, "neither $p$ nor $q$", is T when $p$ and $q$ are both F, and F otherwise.
It is the dual of the [[Sheffer stroke|1NNYWRN6B8]], which treats both connectives.
We check three [[logical equivalences|06GYGS41JK]]:
$$\neg p \equiv p \downarrow p, \qquad p \lor q \equiv (p \downarrow q) \downarrow (p \downarrow q), \qquad p \land q \equiv (p \downarrow p) \downarrow (q \downarrow q).$$

1. [[Negation|029JBBF693]]: at $p$ = T, $p \downarrow p = \mathrm{T} \downarrow \mathrm{T} = \mathrm{F}$, and at $p$ = F, $p \downarrow p = \mathrm{F} \downarrow \mathrm{F} = \mathrm{T}$.
   These are the values of $\neg p$.
2. [[Disjunction|0F72FK8EKB]]: by step 1 applied to $p \downarrow q$, the formula $(p \downarrow q) \downarrow (p \downarrow q)$ has the value of $\neg(p \downarrow q) = \neg\neg(p \lor q)$.
   That is the value of $p \lor q$.
3. [[Conjunction|025YZN3VJW]]: by step 1, $(p \downarrow p) \downarrow (q \downarrow q)$ has the value of $\neg p \downarrow \neg q = \neg(\neg p \lor \neg q)$.
   By [[De Morgan's laws|09PKJKA6J0]], this is the value of $p \land q$.

The table confirms steps 2 and 3 in all four rows.

| $p$ | $q$ | $p \downarrow q$ | $(p \downarrow q) \downarrow (p \downarrow q)$ | $p \lor q$ | $p \downarrow p$ | $q \downarrow q$ | $(p \downarrow p) \downarrow (q \downarrow q)$ | $p \land q$ |
|---|---|---|---|---|---|---|---|---|
| T | T | F | T | T | F | F | T | T |
| T | F | F | T | T | F | T | F | F |
| F | T | F | T | T | T | F | F | F |
| F | F | T | F | F | T | T | F | F |

## Remarks

### The mirror image

The example is the mirror image of [[the example for the stroke|S3KJ52G2SF]].
Each formula there becomes a formula here when $\uparrow$ is replaced by $\downarrow$ and $\land$ by $\lor$.
This is the duality of $\land$ and $\lor$: exchanging T and F in all tables turns NAND into NOR and $\land$ into $\lor$.

### Completeness of the arrow

Since $\{\neg, \lor\}$ is [[functionally complete|TDZVCWYJ9F]], steps 1 and 2 already show that the Peirce arrow alone is functionally complete.
Implication follows as well: $p \to q \equiv \neg p \lor q$, and both $\neg$ and $\lor$ are expressed above.

## Explanations

### L1 human

The Peirce arrow means "neither ... nor".
"Neither $p$ nor $p$" says the same as "not $p$".
"Neither (neither $p$ nor $q$) nor (neither $p$ nor $q$)" says "not (neither $p$ nor $q$)", which means "$p$ or $q$".
So "neither ... nor" alone can say "not" and "or", and with those it can say everything else.

### L2 human

Write $p \to q$ with the Peirce arrow alone, and check the row where it is false.

1. $p \to q \equiv \neg p \lor q$.
2. By step 1 of the example, $\neg p \equiv p \downarrow p$.
3. By step 2 of the example, $A \lor B \equiv (A \downarrow B) \downarrow (A \downarrow B)$, with $A = p \downarrow p$ and $B = q$.
4. So $p \to q \equiv \big((p \downarrow p) \downarrow q\big) \downarrow \big((p \downarrow p) \downarrow q\big)$.
5. Check the row TF: $p \downarrow p = \mathrm{F}$, then $(p \downarrow p) \downarrow q = \mathrm{F} \downarrow \mathrm{F} = \mathrm{T}$, and $\mathrm{T} \downarrow \mathrm{T} = \mathrm{F}$.
   This is the value of $\mathrm{T} \to \mathrm{F}$.

This is how circuits are designed from NOR gates only.
Watch out: $p \downarrow q$ is not $\neg p \lor \neg q$, since that formula is $p \uparrow q$, the stroke.
