---
tag: ~a72cd9fe
kind: example
name: Strong Kleene disjunction is not weak Kleene
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
instance_of: [SZHA10A9X7]
not_instance_of:
  - target: BCK5QXQXA6
    note: the value 1/2 is not infectious, since max(1, 1/2) = 1
uses: [~aa4cad6e, ~e50e75c5]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
---

## Example

The [[strong Kleene disjunction|~e50e75c5]] is $x \lor_s y = \max(x, y)$ on $\set{0, \tfrac12, 1}$.
The [[weak Kleene disjunction|~aa4cad6e]] $\lor_w$ gives $\tfrac12$ whenever an input is $\tfrac12$.

1. $1 \lor_s \tfrac12 = \max(1, \tfrac12) = 1$.
2. $1 \lor_w \tfrac12 = \tfrac12$, since one input is $\tfrac12$.
3. $1 \ne \tfrac12$, so the two tables differ at $(1, \tfrac12)$.
4. Then $p \models p \lor q$ is valid with $\lor_s$ and designated set $\set{1}$, but fails with $\lor_w$ at $p = 1$, $q = \tfrac12$.

## Remarks

1. The tables also differ at $(\tfrac12, 1)$ for $\lor$, and at $(0, \tfrac12)$ and $(\tfrac12, 0)$ for $\land$.
2. They agree at the other entries and on $\neg$.
3. So the property "the value $\tfrac12$ is infectious" separates the weak tables from the strong ones.

## Explanations

### L1 human

In strong Kleene logic, "true or undefined" is true.
In weak Kleene logic, "true or meaningless" is meaningless.
The two logics differ exactly in such cases.

### L2 human

1. Find an entry where one input decides the classical result.
2. Put $\tfrac12$ in the other input.
3. The strong table keeps the classical result; the weak table gives $\tfrac12$.

The typical use is to tell which of the two schemes a given evaluation follows.
A trap: both tables give $0 \lor \tfrac12 = \tfrac12$, so that entry does not separate them.
