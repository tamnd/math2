---
tag: PJA9JVQ5XN
kind: definition
name: Weak Kleene logics B3 and PWK
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
defines: BCK5QXQXA6
uses: [66NMTCQNQV, AJEJS6TFWP, K6CVH3D7R8]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: "2.2 From two to three truth values: gaps and gluts"
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
    locator: Bochvar's internal three-valued logic
---

## Definition

The *weak Kleene algebra* $\mathbf{WK}_3$ has universe $\set{0, \tfrac12, 1}$ and the operations
$$\neg x = 1 - x, \qquad x \land y = \begin{cases} \tfrac12 & \text{if } x = \tfrac12 \text{ or } y = \tfrac12, \\ \min(x, y) & \text{otherwise}, \end{cases} \qquad x \lor y = \begin{cases} \tfrac12 & \text{if } x = \tfrac12 \text{ or } y = \tfrac12, \\ \max(x, y) & \text{otherwise}. \end{cases}$$
Implication is the abbreviation $\varphi \to \psi = \neg \varphi \lor \psi$.

1. *Bochvar's logic* $\mathrm{B}_3$ is the logic of the [[logical matrix|AJEJS6TFWP]] $\langle \mathbf{WK}_3, \set{1} \rangle$.
2. *Paraconsistent weak Kleene logic* $\mathsf{PWK}$ is the logic of the matrix $\langle \mathbf{WK}_3, \set{\tfrac12, 1} \rangle$.

So $\Gamma \models_{\mathrm{B}_3} \varphi$ iff every valuation with value $1$ on $\Gamma$ gives $\varphi$ the value $1$, and $\mathsf{PWK}$ uses "value $\ne 0$" in place of "value $1$".

The binary tables, with the row for $x$ and the column for $y$:

| $x$ | $x \land 0$ | $x \land \tfrac12$ | $x \land 1$ | $x \lor 0$ | $x \lor \tfrac12$ | $x \lor 1$ |
|---|---|---|---|---|---|---|
| $0$ | $0$ | $\tfrac12$ | $0$ | $0$ | $\tfrac12$ | $1$ |
| $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |
| $1$ | $0$ | $\tfrac12$ | $1$ | $1$ | $\tfrac12$ | $1$ |

## Notation

SEP writes $*$ for the middle value and $\mathbf{WK}_3$ for the algebra.
Other names for $\mathrm{B}_3$ are "Bochvar's internal logic" and "Kleene's weak three-valued logic"; Halldén called $\mathsf{PWK}$ "the logic of nonsense".

## Remarks

1. Example: $p \land q \models_{\mathrm{B}_3} p$. If $p \land q = 1$, then neither value is $\tfrac12$ and $\min(p, q) = 1$, so $p = 1$.
2. Non-example: $p \models_{\mathrm{B}_3} p \lor q$ fails at $p = 1$, $q = \tfrac12$, where $p \lor q = \tfrac12$.
3. The [[designated value|K6CVH3D7R8]] set is the only difference between $\mathrm{B}_3$ and $\mathsf{PWK}$, as with [[strong Kleene logic|SZHA10A9X7]] and $\mathsf{LP}$.
4. In $\mathsf{PWK}$, $p \models p \lor q$ holds: if $p = 1$, then $p \lor q \in \set{\tfrac12, 1}$; if $p = \tfrac12$, then $p \lor q = \tfrac12$.

## Explanations

### L1 human

The weak Kleene tables are the classical tables plus one rule.
If any input is $\tfrac12$, the output is $\tfrac12$.
Bochvar counts only $1$ as true; Halldén counts $1$ and $\tfrac12$ as acceptable.

### L2 human

To check an inference in $\mathrm{B}_3$, test the valuations that give every premise the value $1$.
Then every variable of the premises is classical, but the conclusion may contain new variables with value $\tfrac12$.
The typical failure comes from a new variable in the conclusion, as in remark 2.
A trap: $\mathrm{B}_3$ and $\mathsf{PWK}$ fail different inferences; addition fails only in $\mathrm{B}_3$ and explosion fails only in $\mathsf{PWK}$.
