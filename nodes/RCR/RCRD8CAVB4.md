---
tag: RCRD8CAVB4
kind: problem
name: Tarski's high school algebra problem
msc: [08B05, 03C05]
uses: [PKD440G2XW, 9Q008GMZSW, 72S3YSQFZ7]
about: [9Q008GMZSW]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski%27s_high_school_algebra_problem
    locator: Statement of the problem
same_as:
  wikidata: Q7686759
  wikipedia: Tarski's high school algebra problem
history:
  posed_by: "Alfred Tarski"
---

## Problem

Consider the signature with a constant $1$ and binary operations $+$, $\cdot$ and exponentiation $x^y$, interpreted in the positive integers.
Let $\mathrm{HSI}$ be the following eleven [[identities|PKD440G2XW]]:

1. $x + y \approx y + x$ and $(x + y) + z \approx x + (y + z)$;
2. $x \cdot 1 \approx x$, $x \cdot y \approx y \cdot x$ and $(x \cdot y) \cdot z \approx x \cdot (y \cdot z)$;
3. $x \cdot (y + z) \approx x \cdot y + x \cdot z$;
4. $1^x \approx 1$, $x^1 \approx x$, $x^{y + z} \approx x^y \cdot x^z$, $(x \cdot y)^z \approx x^z \cdot y^z$ and $(x^y)^z \approx x^{y \cdot z}$.

The problem asks whether every identity in this signature that holds in the positive integers can be derived from $\mathrm{HSI}$ in [[equational logic|72S3YSQFZ7]].

## Remarks

The answer is no.
Alex Wilkie found, around 1980, an identity true in the positive integers that cannot be derived from $\mathrm{HSI}$.
Later, R. Gurevič showed that the identities true in the positive integers with $1$, $+$, $\cdot$ and exponentiation have no finite [[equational basis|9Q008GMZSW]] at all.
Every identity without exponentiation that holds in the positive integers is derivable from the identities in items 1 to 3.
Indeed, both sides expand to the same polynomial; this is why the question was natural.

## Explanations

### L1 human

School algebra teaches a short list of rules for adding, multiplying and taking powers.
Tarski asked whether these rules are enough to prove every true equation built from $1$, $+$, $\times$ and powers.
Surprisingly, they are not: there are true equations that the school rules cannot prove.
Even worse, no finite list of rules can do the job.
