---
tag: F9NDCFY3GS
kind: definition
name: Łukasiewicz three-valued logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
defines: 1CE2TGM6MQ
uses: [66NMTCQNQV, AJEJS6TFWP, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Three-valued logic
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.4 Axioms and Definitions
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Łukasiewicz logic
---

## Definition

Łukasiewicz's three-valued logic is the logic of one three-valued matrix with a negation and an implication, in which only the top value counts as true.

*Łukasiewicz's three-valued logic* $\mathrm{Ł}_3$ is the logic of the [[logical matrix|AJEJS6TFWP]] $\langle \{0, \tfrac12, 1\}, \neg, \to, \{1\} \rangle$ with the operations below.
$$\neg x = 1 - x, \qquad x \to y = \min(1, 1 - x + y)$$
The other connectives are abbreviations: $\varphi \lor \psi$ is $(\varphi \to \psi) \to \psi$, and $\varphi \land \psi$ is $\neg(\neg \varphi \lor \neg \psi)$.
So $\Gamma \models_{\mathrm{Ł}_3} \varphi$ iff every valuation that gives all members of $\Gamma$ the value $1$ gives $\varphi$ the value $1$.

The tables of $\neg$ and $\to$, with the row for $x$:

| $x$ | $\neg x$ | $x \to 0$ | $x \to \tfrac12$ | $x \to 1$ |
|---|---|---|---|---|
| $0$ | $1$ | $1$ | $1$ | $1$ |
| $\tfrac12$ | $\tfrac12$ | $\tfrac12$ | $1$ | $1$ |
| $1$ | $0$ | $0$ | $\tfrac12$ | $1$ |

## Notation

The derived connectives have the values $x \lor y = \max(x, y)$ and $x \land y = \min(x, y)$.
We also use $x \oplus y = \neg x \to y = \min(1, x + y)$ and $x \odot y = \neg(x \to \neg y) = \max(0, x + y - 1)$.
In Polish notation Wajsberg's axioms read $CpCqp$, $CCpqCCqrCpr$, $CCNpNqCqp$ and $CCCpNppp$.

## Remarks

Each part of the definition has a reason.
The values $0$ and $1$ with the classical tables on them make $\mathrm{Ł}_3$ a conservative change of classical logic: no new law appears that is not classical.
The designated set $\{1\}$ makes the middle value "not yet true", so a formula that can take the value $\tfrac12$ is not a law.
The implication is chosen so that $x \to y = 1$ exactly when $x \le y$, which makes $p \to p$ a law and keeps modus ponens valid.

The derived connectives have the values $\max$ and $\min$.
If $x \le y$, then $x \to y = 1$ and $1 \to y = y = \max(x, y)$.
If $x > y$, then $x \to y = 1 - x + y$, and the second step gives the value below.
$$(1 - x + y) \to y = \min(1, x) = x = \max(x, y)$$
De Morgan then turns $\max$ into $\min$.

With modus ponens as the only rule, the tautologies of $\mathrm{Ł}_3$ are the theorems of four schemas due to Wajsberg.
They are W1 $\varphi \to (\psi \to \varphi)$, W2 $(\varphi \to \psi) \to ((\psi \to \chi) \to (\varphi \to \chi))$, W3 $(\neg \varphi \to \neg \psi) \to (\psi \to \varphi)$ and W4 $((\varphi \to \neg \varphi) \to \varphi) \to \varphi$.
We check W4 row by row.
At $x = 0$ we get $0 \to 1 = 1$, then $1 \to 0 = 0$, then $0 \to 0 = 1$.
At $x = \tfrac12$ we get $\tfrac12 \to \tfrac12 = 1$, then $1 \to \tfrac12 = \tfrac12$, then $\tfrac12 \to \tfrac12 = 1$.
At $x = 1$ we get $1 \to 0 = 0$, then $0 \to 1 = 1$, then $1 \to 1 = 1$.
W1 to W3 hold in every Łukasiewicz matrix, but W4 fails in the four-valued one, as [[the four-valued counter-model|BK6EPGABW8]] shows.

For a quick contrast, $p \to p$ is a tautology and $p \lor \neg p$ is not, by [[the evaluation at one half|6S872VHF67]].
[[Strong Kleene logic|SZHA10A9X7]] has the same $\neg$, $\land$ and $\lor$, and its implication $\max(1 - x, y)$ differs from the table above only at $x = y = \tfrac12$.
The [[concept page|1CE2TGM6MQ]] gives the motivation and the uses.

## Explanations

### L1 human

The three values are false ($0$), possible ($\tfrac12$) and true ($1$).
"Not" swaps false and true and keeps possible.
"If $x$ then $y$" is fully true when $x$ is at most $y$; otherwise it loses as much truth as $x$ exceeds $y$.
Only the value $1$ counts as true.

### L2 human

We evaluate $\neg p \to (p \to q)$ at $p = \tfrac12$ and $q = 0$.
First $\neg p = \tfrac12$ and $p \to q = \tfrac12 \to 0 = \tfrac12$, so the whole formula is $\tfrac12 \to \tfrac12 = 1$.
In general the formula has the value below, so it is a tautology.
$$\neg x \to (x \to y) = \min\bigl(1, x + \min(1, 1 - x + y)\bigr) = \min(1, 1 + x, 1 + y) = 1$$
The typical use of the tables is such a row-by-row check.
Watch out: $\lor$ is not $\neg \varphi \to \psi$, which is the strong disjunction $\oplus$.
