---
tag: AHM8HYZDMM
kind: example
name: Strong Kleene disjunction is not weak Kleene
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
instance_of: [SZHA10A9X7]
not_instance_of:
  - target: BCK5QXQXA6
    note: the value 1/2 is not infectious, since max(1, 1/2) = 1
uses: [PJA9JVQ5XN, 74R8A41V6M]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
---

## Example

Take the entry $1 \lor \tfrac12$ in two three-valued disjunctions on $\{0, \tfrac12, 1\}$.
The [[strong Kleene disjunction|74R8A41V6M]] is $x \lor_s y = \max(x, y)$.
The [[weak Kleene disjunction|PJA9JVQ5XN]] $\lor_w$ agrees with $\max$ on $\{0, 1\}$ and gives $\tfrac12$ whenever an input is $\tfrac12$.

1. The strong table gives $1 \lor_s \tfrac12 = \max(1, \tfrac12) = 1$.
2. The weak table gives $1 \lor_w \tfrac12 = \tfrac12$, since one input is $\tfrac12$.
3. Since $1 \ne \tfrac12$, the two tables differ at $(1, \tfrac12)$.
4. So $p \models p \lor q$ is valid with $\lor_s$ and the designated set $\{1\}$, while it fails with $\lor_w$ at $p = 1$, $q = \tfrac12$.

## Remarks

The tables also differ at $(\tfrac12, 1)$ for $\lor$, and at $(0, \tfrac12)$ and $(\tfrac12, 0)$ for $\land$, where the strong table gives $0$.
They agree at every other entry and on $\neg$.
So the property "the value $\tfrac12$ is infectious" separates the weak tables from the strong ones.
The strong scheme lets a classical input decide the result whenever it decides it classically, and the weak scheme never does.

## Explanations

### L1 human

In strong Kleene logic, "true or undefined" is true.
In weak Kleene logic, "true or meaningless" is meaningless.
The two logics differ exactly in such cases.

### L2 human

To separate the two schemes, find an entry where one input decides the classical result, and put $\tfrac12$ in the other input.
The strong table keeps the classical result, and the weak table gives $\tfrac12$.
The typical use is to tell which of the two schemes a given evaluation follows.
Watch out: both tables give $0 \lor \tfrac12 = \tfrac12$, so that entry does not separate them.
