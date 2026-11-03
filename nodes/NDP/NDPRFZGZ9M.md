---
tag: NDPRFZGZ9M
kind: definition
name: Boolean circuit
msc: [68Q06, 94C11]
defines: SQXNFGVADX
uses: [0R5HTV7REV, 0A58THH5XV]
sources:
  - url: https://en.wikipedia.org/wiki/Boolean_circuit
---

## Definition

Let $n, m \ge 1$.
A *Boolean circuit* with $n$ inputs and $m$ outputs is a finite [[directed graph|0R5HTV7REV]] $C$ without directed cycles, with the following labels.

1. Each vertex of in-degree $0$ is an input vertex labelled by a variable $x_1, \dots, x_n$ or by a constant $0$ or $1$.
2. Each other vertex is a gate labelled $\wedge$ or $\vee$ with in-degree $2$, or $\neg$ with in-degree $1$.
3. A list of $m$ vertices is marked as the outputs.

For $a \in \set{0,1}^n$, each vertex $v$ gets a value $v(a) \in \set{0, 1}$, defined along the edges since there are no cycles.
An input vertex labelled $x_i$ gets $a_i$, and a constant gets its own value.
A gate gets the conjunction, disjunction or negation of the values of its in-neighbours.
The circuit computes the [[Boolean function|0A58THH5XV]] $f_C \colon \set{0,1}^n \to \set{0,1}^m$ whose value at $a$ is the list of values of the outputs.
The *size* of $C$ is the number of gates, and the *depth* is the largest number of edges on a directed path.

## Remarks

Example: for $n = 2$, take gates $g_1 = \neg x_1$, $g_2 = \neg x_2$, $g_3 = x_1 \wedge g_2$, $g_4 = g_1 \wedge x_2$ and the output $g_5 = g_3 \vee g_4$.
The graph has no cycles, every gate has the right in-degree, and $f_C(a_1, a_2) = 1$ exactly when $a_1 \ne a_2$.
So $C$ computes exclusive or with size $5$ and depth $3$.
Non-example: a graph in which the output of an $\vee$ gate feeds back into its own input has a directed cycle, so it is not a circuit.
Its values cannot be defined step by step from the inputs.
Every Boolean function has a circuit, for example one built from its disjunctive normal form.
A language $L \subseteq \set{0,1}^*$ is decided by a family $(C_n)_{n \ge 1}$ of circuits if $C_n$ computes the indicator function of $L \cap \set{0,1}^n$ for every $n$.
