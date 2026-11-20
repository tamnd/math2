---
tag: W28EY7C3FA
kind: definition
name: Logic of paradox
msc: ["03B53", "03B50"]
topics: [NJB94B39QK]
audience: ug2
defines: BXJZG67PX3
uses: [09K9MWD2QQ, 029JBBF693, 1HK0VYWTV7, SZHA10A9X7]
sources:
  - url: https://plato.stanford.edu/entries/logic-paraconsistent/
    locator: Paraconsistent Logic (SEP entry), section 3.6
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
  - book: isbn:9780521670265
---

## Definition

The formulas are those of [[propositional logic|09K9MWD2QQ]] built from atoms with $\neg$, $\land$ and $\lor$.
The material conditional is the abbreviation $\varphi \supset \psi := \neg\varphi \lor \psi$.

The truth values are $\mathsf{T} = 1$, $\mathsf{B} = \tfrac12$ and $\mathsf{F} = 0$.
An *LP valuation* is a map $v$ from atoms to $\set{1, \tfrac12, 0}$, extended to all formulas by the [[strong Kleene|SZHA10A9X7]] tables:
$$v(\neg\varphi) = 1 - v(\varphi), \quad v(\varphi \land \psi) = \min(v(\varphi), v(\psi)), \quad v(\varphi \lor \psi) = \max(v(\varphi), v(\psi)).$$
The *designated* values are $1$ and $\tfrac12$.

For a set $\Gamma$ of formulas and a formula $\varphi$, $\Gamma \vDash_{\mathrm{LP}} \varphi$ means: every LP valuation that gives each member of $\Gamma$ a designated value gives $\varphi$ a designated value.
The *logic of paradox* LP is this [[consequence relation|1HK0VYWTV7]].
A formula $\varphi$ is an *LP tautology* when $\emptyset \vDash_{\mathrm{LP}} \varphi$.

## Notation

The same tables with the single designated value $1$ give *strong Kleene logic* K3, written $\Gamma \vDash_{\mathrm{K3}} \varphi$.
Many authors write $t$, $b$, $f$ for $\mathsf{T}$, $\mathsf{B}$, $\mathsf{F}$.
In the coding by numbers, $\varphi$ is designated in LP exactly when $v(\varphi) \neq 0$, and in K3 exactly when $v(\varphi) = 1$.

## Remarks

The tables restricted to $\set{0, 1}$ are the classical tables.
So every classical valuation is an LP valuation, and every LP-valid inference is classically valid.
The [[negation|029JBBF693]] table fixes $\tfrac12$; this is the source of paraconsistency.
Some authors present LP with a relational semantics: a valuation relates each atom to $1$, to $0$, or to both, but never to neither.
The two presentations give the same consequence relation, with "related to both" coded as $\tfrac12$.

## Explanations

### L1 human

LP is classical logic with one extra truth value, "both".
"Not both" is again "both".
"And" takes the lower of two values, and "or" takes the higher.
A formula counts as accepted when its value is true or both.

### L2 human

We compute $v(p \land \neg p)$ for each value of $p$.

- $v(p) = 1$: $\min(1, 0) = 0$.
- $v(p) = \tfrac12$: $\min(\tfrac12, \tfrac12) = \tfrac12$.
- $v(p) = 0$: $\min(0, 1) = 0$.

So the contradiction $p \land \neg p$ is designated exactly when $v(p) = \tfrac12$.
A trap is to think that $\supset$ is a primitive with its own table; here it is defined from $\neg$ and $\lor$.

### L3 human

LP is the logic of the three-element Kleene lattice $0 < \tfrac12 < 1$ with the involution $a \mapsto 1 - a$ and the filter $\set{\tfrac12, 1}$.
K3 uses the same algebra with the filter $\set{1}$.
The choice of filter, not the algebra, separates the paraconsistent logic from the paracomplete one.
