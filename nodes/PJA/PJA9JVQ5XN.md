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

The weak Kleene logics use the classical tables on $\{0, 1\}$ and give the value $\tfrac12$ to every compound with a part of value $\tfrac12$; they differ only in the designated set.

The *weak Kleene algebra* $\mathbf{WK}_3$ has the universe $\{0, \tfrac12, 1\}$ and the operations below.
$$\neg x = 1 - x, \qquad x \land y = \begin{cases} \tfrac12 & \text{if } x = \tfrac12 \text{ or } y = \tfrac12, \\ \min(x, y) & \text{otherwise}, \end{cases} \qquad x \lor y = \begin{cases} \tfrac12 & \text{if } x = \tfrac12 \text{ or } y = \tfrac12, \\ \max(x, y) & \text{otherwise} \end{cases}$$
Implication is the abbreviation $\varphi \to \psi = \neg \varphi \lor \psi$.
*Bochvar's logic* $\mathrm{B}_3$ is the logic of the [[logical matrix|AJEJS6TFWP]] $\langle \mathbf{WK}_3, \{1\} \rangle$.
*Paraconsistent weak Kleene logic* $\mathsf{PWK}$ is the logic of the matrix $\langle \mathbf{WK}_3, \{\tfrac12, 1\} \rangle$.
So $\Gamma \models_{\mathrm{B}_3} \varphi$ iff every valuation with the value $1$ on $\Gamma$ gives $\varphi$ the value $1$, and $\mathsf{PWK}$ uses "value $\ne 0$" in place of "value $1$".

The binary tables, with the row for $x$:

| $x$ | $x \land 0$ | $x \land \tfrac12$ | $x \land 1$ | $x \lor 0$ | $x \lor \tfrac12$ | $x \lor 1$ |
|---|---|---|---|---|---|---|
| $0$ | $0$ | $\tfrac12$ | $0$ | $0$ | $\tfrac12$ | $1$ |
| $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $\tfrac12$ |
| $1$ | $0$ | $\tfrac12$ | $1$ | $1$ | $\tfrac12$ | $1$ |

## Notation

Some texts write $*$ for the middle value and $\mathbf{WK}_3$ for the algebra.
Other names for $\mathrm{B}_3$ are "Bochvar's internal logic" and "Kleene's weak three-valued logic", and Halldén called $\mathsf{PWK}$ "the logic of nonsense".

## Remarks

Each part of the definition has a reason.
The classical tables on $\{0, 1\}$ make every valid inference of either logic classically valid.
The infectious $\tfrac12$ models a meaningless part, which no classical value of another part can repair.
The [[designated value|K6CVH3D7R8]] set is the only difference between $\mathrm{B}_3$ and $\mathsf{PWK}$, just as it is between [[strong Kleene logic|SZHA10A9X7]] and $\mathsf{LP}$.

Conjunction elimination $p \land q \models_{\mathrm{B}_3} p$ holds.
If $p \land q = 1$, then neither value is $\tfrac12$ and $\min(p, q) = 1$, so $p = 1$.
Addition $p \models_{\mathrm{B}_3} p \lor q$ fails at $p = 1$, $q = \tfrac12$, where $p \lor q = \tfrac12$.
In $\mathsf{PWK}$ addition holds.
If $p = 1$, then $p \lor q \in \{\tfrac12, 1\}$, and if $p = \tfrac12$, then $p \lor q = \tfrac12$, so the conclusion is designated in both cases.

## Explanations

### L1 human

The weak Kleene tables are the classical tables plus one rule.
If any input is $\tfrac12$, the output is $\tfrac12$.
Bochvar counts only $1$ as true, and Halldén counts $1$ and $\tfrac12$ as acceptable.

### L2 human

To check an inference in $\mathrm{B}_3$, test the valuations that give every premise the value $1$.
Then every variable of the premises is classical, but the conclusion may contain new variables with the value $\tfrac12$.
The typical failure comes from such a new variable, as with addition.
Watch out: $\mathrm{B}_3$ and $\mathsf{PWK}$ fail different inferences, since addition fails only in $\mathrm{B}_3$ and explosion fails only in $\mathsf{PWK}$.
