---
tag: VS6SNA8Z23
kind: example
name: Simultaneous and successive substitution differ
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [NCDZ969V7X]
uses: [XN8TQE6SRK, 6D3WA7N2W4]
sources:
  - url: https://en.wikipedia.org/wiki/Substitution_(logic)
    locator: lead section
---

## Example

Let $+$ be a binary function symbol and let $t = x + y$, with distinct variables $x$ and $y$.
We compare the simultaneous swap $\theta = \{ x \mapsto y, \ y \mapsto x \}$ with two successive single substitutions, using the clauses of the [[definition|XN8TQE6SRK]].

1. Simultaneous: $t\theta = x\theta + y\theta = y + x$, by clauses 3 and 1.
2. Successive, $x$ first: $t[y/x] = y + y$, and then $(y + y)[x/y] = x + x$.
3. Successive, $y$ first: $t[x/y] = x + x$, and then $(x + x)[y/x] = y + y$.
4. The three results $y + x$, $x + x$ and $y + y$ are pairwise different terms.
5. A fresh variable $z$ repairs the successive method: $t[z/x] = z + y$, then $(z + y)[x/y] = z + x$, then $(z + x)[y/z] = y + x$, which is $t\theta$.

## Remarks

A simultaneous substitution is not, in general, a sequence of single substitutions.
The first single substitution creates new occurrences of $y$, and the second one then replaces them too.

The two methods agree when no term put in contains a variable that is replaced later.
Check: $\{ x \mapsto 0, \ y \mapsto 1 \}$ gives $0 + 1$ in either way.

The same happens in formulas.
The swap turns $x < y$ into $y < x$, while the successive substitutions give $x < x$ or $y < y$.

## Explanations

### L1 human

Two people trade seats at the same moment: each sits where the other sat.
If one moves first, that person sits on the other, and the other then has no free seat.
Simultaneous substitution is the trade at the same moment.
Successive substitution moves one at a time and gets in the way.
A spare chair, the fresh variable $z$, lets the trade work one step at a time.

### L2 human

We check the swap in $(\mathbb{N}, <)$, with $x \mapsto 1$ and $y \mapsto 2$.

1. The formula $x < y$ is true, since $1 < 2$.
2. The swapped formula $y < x$ is false, since $2 < 1$ fails.
3. The successive results $x < x$ and $y < y$ are false for every value, since $<$ is irreflexive.

The typical use of simultaneous substitution is to rename all free variables of a formula at once, for example in unification.
Watch out for a program that applies the pairs of $\theta$ one by one: it computes a successive result, not $t\theta$.
