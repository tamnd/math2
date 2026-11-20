---
tag: ~5cda3dd2
kind: example
name: Contraction fails in abelian logic
msc: ["03B47"]
topics: [98QF5J4W16]
audience: research
not_instance_of:
  - target: ~54d8cf2f
    note: the contraction formula has the value v(p) in abelian logic, so it fails at v(p) = -1
uses: [~48af5789, ~54d8cf2f]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_logic
    locator: section A, Abelian logic
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.4 A continuum of truth values
    note: Marcos, Přenosil and Egré, Many-Valued Logic, Stanford Encyclopedia of Philosophy, revision of 2026-09-29
---

## Example

The contraction formula $(p \to (p \to q)) \to (p \to q)$ is not valid in [[abelian logic|~48af5789]].
So abelian logic does not have [[contraction|~54d8cf2f]] in this form.

1. $v(p \to q) = v(q) - v(p)$.
2. $v(p \to (p \to q)) = v(q) - v(p) - v(p) = v(q) - 2v(p)$.
3. $v((p \to (p \to q)) \to (p \to q)) = (v(q) - v(p)) - (v(q) - 2v(p)) = v(p)$.
4. Take $v(p) = -1$ and $v(q) = 0$; the value is $-1 < 0$.
5. So the formula is not valid.

## Remarks

The value of the general form $(A \to (A \to B)) \to (A \to B)$ is $v(A)$.
So an instance is valid when $A$ is valid, for example when $A$ is $q \to q$.
The Wikipedia glossary states that abelian logic rejects contraction, and this example shows it.

## Explanations

### L1 human

Using $p$ twice counts its value twice.
Contraction claims that twice is as good as once, and this fails when the value of $p$ is negative.

### L2 human

We check step 4 with the numbers.

1. $v(p \to q) = 0 - (-1) = 1$.
2. $v(p \to (p \to q)) = 1 - (-1) = 2$.
3. The value of the whole formula is $1 - 2 = -1$.

The typical use of such a valuation is to refute a formula by one choice of numbers.
A trap: with $v(p) \geq 0$, the value is not negative, so a refutation needs a negative value for $p$.
