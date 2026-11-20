---
tag: ~fffdddf4
kind: example
name: Partial recursive predicates obey the strong Kleene tables
msc: ["03B50", "03D10"]
topics: [WZP584JQ06]
audience: grad
instance_of: [SZHA10A9X7]
uses: [~e50e75c5]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
---

## Example

Let $P(n)$ and $Q(n)$ be predicates computed by algorithms that may run forever.
Give $P(n)$ the value $1$ if its algorithm stops with "yes", $0$ if it stops with "no", and $\tfrac12$ if it never stops.
Compute "$P(n)$ or $Q(n)$" by running both algorithms in parallel, one step each in turn.
Answer "yes" as soon as one says "yes", and "no" when both have said "no".

1. If $P(n) = 1$ and $Q(n) = \tfrac12$, the parallel run stops with "yes", so the disjunction has value $1 = \max(1, \tfrac12)$.
2. If $P(n) = 0$ and $Q(n) = \tfrac12$, the run never says "yes" and never sees two "no" answers, so the value is $\tfrac12 = \max(0, \tfrac12)$.
3. If $P(n) = Q(n) = 0$, the run stops with "no", so the value is $0 = \max(0, 0)$.
4. The other cases follow in the same way, and the result is always $\max(P(n), Q(n))$.
5. Conjunction runs in parallel with "no" as the early answer, which gives $\min(P(n), Q(n))$.
6. Negation swaps "yes" and "no" and keeps "never stops", which gives $1 - P(n)$.

So the parallel evaluation is exactly the strong Kleene table.

## Remarks

1. Sequential evaluation, which first finishes $P(n)$ and then runs $Q(n)$, gives a different table: $\tfrac12 \lor 1 = \tfrac12$, since the run never reaches $Q$. That table is not commutative.
2. The value $\tfrac12$ is not a third answer; it records the absence of an answer.
3. This was Kleene's motivation for the tables, according to the SEP entry on many-valued logic.

## Explanations

### L1 human

Some computer programs never stop.
Ask two programs a question at the same time.
If one says "yes", you can say "yes" to "one or the other", even if the other program is still running.

### L2 human

Each step of the check compares what the parallel run can see with the strong Kleene value.
The typical use is to explain why $\tfrac12 \lor 1 = 1$ but $\tfrac12 \lor 0 = \tfrac12$.
A trap: a program cannot detect that another program runs forever, so it cannot answer "undefined" as an output.
