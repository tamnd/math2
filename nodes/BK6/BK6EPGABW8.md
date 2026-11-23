---
tag: BK6EPGABW8
kind: example
name: The four-valued Łukasiewicz logic refutes Wajsberg's axiom
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
not_instance_of:
  - target: 1CE2TGM6MQ
    note: the four-valued Łukasiewicz matrix gives Wajsberg's fourth axiom the value 2/3, so it is not a model of Ł3
uses: [F9NDCFY3GS, JQ713VVD0G]
sources:
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.3 More than Three Values; 5.4 Axioms and Definitions
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Real-valued semantics
---

## Example

Let $\mathrm{Ł}_4$ be the matrix with values $\{0, \tfrac13, \tfrac23, 1\}$, designated set $\{1\}$, $\neg x = 1 - x$ and $x \to y = \min(1, 1 - x + y)$.
We evaluate Wajsberg's axiom $\mathrm{W4} = ((p \to \neg p) \to p) \to p$ at $p = \tfrac23$.

1. The operations are well defined on $\mathrm{Ł}_4$, because $1 - x$ and $\min(1, 1 - x + y)$ are again multiples of $\tfrac13$ in $[0, 1]$.
2. Negate: $\neg p = 1 - \tfrac23 = \tfrac13$.
3. The first implication is $p \to \neg p = \min(1, 1 - \tfrac23 + \tfrac13) = \tfrac23$.
4. The second is $(p \to \neg p) \to p = \tfrac23 \to \tfrac23 = 1$.
5. The last is $1 \to \tfrac23 = \tfrac23$, which is not designated.

So $\mathrm{W4}$ is not a tautology of $\mathrm{Ł}_4$, while it is a tautology of [[Łukasiewicz's three-valued logic|F9NDCFY3GS]].
Hence $\mathrm{Ł}_4$ is not a model of $\mathrm{Ł}_3$.

## Remarks

The other three Wajsberg axioms are tautologies of every Łukasiewicz matrix, including $[0, 1]$, as [[the axioms of Łukasiewicz logic|JQ713VVD0G]] show.
So $\mathrm{W4}$ is the axiom that cuts $\mathrm{Ł}_3$ out of the larger Łukasiewicz logics.
The same valuation $p = \tfrac23$ refutes $\mathrm{W4}$ in $[0, 1]$, so $\mathrm{W4}$ is not a theorem of infinite-valued Łukasiewicz logic either.

The other values of $\mathrm{Ł}_4$ do not refute it.
At $p = \tfrac13$ we get $\tfrac13 \to \tfrac23 = 1$, then $1 \to \tfrac13 = \tfrac13$, then $\tfrac13 \to \tfrac13 = 1$.
At $p = 0$ and $p = 1$ the classical table gives $1$.
In general a tautology of $\mathrm{Ł}_n$ need not survive in a larger $\mathrm{Ł}_m$: the values of $\mathrm{Ł}_3$ lie among those of $\mathrm{Ł}_5$, but not among those of $\mathrm{Ł}_4$, since $\tfrac12$ is not a multiple of $\tfrac13$.

## Explanations

### L1 human

Łukasiewicz's logics come with three, four or more values.
Wajsberg found an axiom that holds when there are three values.
With four values, the value two thirds makes the axiom only two thirds true.
So the axiom tells the three-valued logic apart from the others.

### L2 human

List the values of $\mathrm{Ł}_4$, which are $0, \tfrac13, \tfrac23, 1$, and compute $\mathrm{W4}$ at each.
The results are $1$, $1$, $\tfrac23$ and $1$.
One value below $1$ is enough to refute a tautology, so the axiom fails.
The typical use is to separate two finite-valued logics by one formula.
Watch out: a law of a smaller Łukasiewicz matrix can fail in a larger one, because $\mathrm{Ł}_4$ does not contain $\mathrm{Ł}_3$ as a submatrix.
