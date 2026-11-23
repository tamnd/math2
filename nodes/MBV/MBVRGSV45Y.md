---
tag: MBVRGSV45Y
kind: example
name: The classical tautology p → p is not a tautology of strong Kleene logic
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
instance_of: [SZHA10A9X7]
illustrates: [ND17WYDNA5]
uses: [74R8A41V6M, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Kleene and Priest logics
---

## Example

The formula $p \to p$ is a classical [[tautology|05006AJ7DZ]].
In the [[strong Kleene matrix|74R8A41V6M]], $p \to p$ abbreviates $\neg p \lor p$, with the value $\max(1 - x, x)$ at $p = x$.

1. At $p = 0$ the value is $\max(1, 0) = 1$.
2. At $p = 1$ the value is $\max(0, 1) = 1$.
3. At $p = \tfrac12$ the value is $\max(\tfrac12, \tfrac12) = \tfrac12$.
4. The value $\tfrac12$ is not designated, so step 3 refutes $p \to p$.

So $p \to p$ is not a tautology of $\mathsf{K}_3$, although the inference $p \models_{\mathsf{K}_3} p$ is valid.

## Remarks

The same valuation refutes $p \lor \neg p$ and $\neg(p \land \neg p)$, since each has the value $\tfrac12$.
In [[Łukasiewicz's three-valued logic|1CE2TGM6MQ]], $\tfrac12 \to \tfrac12 = 1$, so $p \to p$ is a tautology there.
The example shows the failure of the deduction theorem in $\mathsf{K}_3$: $p \models p$ holds, but $p \to p$ is not a tautology.

## Explanations

### L1 human

"If $p$ then $p$" sounds always true.
In strong Kleene logic it means "not $p$, or $p$".
When $p$ is undefined, both parts are undefined, so the whole is undefined.

### L2 human

Rewrite $\to$ with $\neg$ and $\lor$, give every variable the value $\tfrac12$, and read off the value.
If it is not $1$, the formula is not a tautology.
The typical use is a fast test, and in $\mathsf{K}_3$ every formula fails it.
Watch out: the $\mathsf{K}_3$ implication is not the Łukasiewicz implication, even though both logics use the same three values.
