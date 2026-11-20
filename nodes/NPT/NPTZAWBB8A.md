---
tag: NPTZAWBB8A
kind: example
name: Excluded middle has truth degree one half
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
instance_of: [YG62F8YC0P]
uses: [JQ713VVD0G]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 5. Other notable fuzzy logics
  - book: isbn:9780792352389
---

## Example

In [[Łukasiewicz semantics|JQ713VVD0G]], $p \lor \neg p$ has value $\max(x, 1 - x)$ at $e(p) = x$.
We compute its truth degree in two theories of [[rational Pavelka logic|YG62F8YC0P]].

Empty theory:

1. $\max(x, 1 - x) \ge \tfrac12$ for every $x \in [0, 1]$, since one of $x$ and $1 - x$ is at least $\tfrac12$.
2. At $x = \tfrac12$ the value is $\tfrac12$.
3. So $\lVert p \lor \neg p \rVert_\emptyset = \tfrac12$.
4. For each rational $r \le \tfrac12$, $\overline{r} \to (p \lor \neg p)$ has value $\min(1, 1 - r + \max(x, 1 - x)) = 1$, so it is a tautology.
5. For $r > \tfrac12$, it has value $1 - r + \tfrac12 < 1$ at $x = \tfrac12$, so it is not a tautology.

Theory $T = \set{\overline{0.6} \to p}$:

6. The models of $T$ are the evaluations with $x \ge 0.6$.
7. For $x \ge 0.6$, $\max(x, 1 - x) = x$, with infimum $0.6$ at $x = 0.6$.
8. So $\lVert p \lor \neg p \rVert_T = 0.6$.

## Remarks

1. By Pavelka-style completeness, the provability degree of $p \lor \neg p$ is also $\tfrac12$ in the empty theory and $0.6$ in $T$.
2. In classical logic $p \lor \neg p$ has degree $1$; SEP notes that excluded middle is not a tautology under any t-norm interpretation.
3. Step 5 shows that no bound above $\tfrac12$ is provable, by soundness.

## Explanations

### L1 human

"$p$ or not $p$" is at least half true for every degree of $p$.
It is exactly half true when $p$ is half true.
If we know $p$ to degree $0.6$, then "$p$ or not $p$" is known to degree $0.6$.

### L2 human

1. Write the value of the formula as a function of $x = e(p)$.
2. Minimize it over the models of the theory.

A trap: the degree is a minimum over models, not a value at one model.
