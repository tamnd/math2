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

Give $p$ the value $0.3$ in [[Łukasiewicz semantics|JQ713VVD0G]].
Then $\neg p$ has the value $0.7$, and $p \lor \neg p$ has the value $\max(0.3, 0.7) = 0.7$.
In general $p \lor \neg p$ has the value $\max(x, 1 - x)$ at $e(p) = x$.
We compute its truth degree in two theories of [[rational Pavelka logic|YG62F8YC0P]].

First take the empty theory.

1. For every $x \in [0, 1]$ we have $\max(x, 1 - x) \ge \tfrac12$, since one of $x$ and $1 - x$ is at least $\tfrac12$.
2. At $x = \tfrac12$ the value is $\tfrac12$.
3. So $\lVert p \lor \neg p \rVert_\emptyset = \tfrac12$.
4. For each rational $r \le \tfrac12$, the formula $\overline{r} \to (p \lor \neg p)$ has the value $\min(1, 1 - r + \max(x, 1 - x)) = 1$, so it is a tautology.
5. For $r > \tfrac12$ it has the value $1 - r + \tfrac12 < 1$ at $x = \tfrac12$, so it is not a tautology.

Now take $T = \{\overline{0.6} \to p\}$.
The value of $\overline{0.6} \to p$ is $\min(1, 0.4 + x)$, which is $1$ exactly when $x \ge 0.6$.
So the models of $T$ are the evaluations with $x \ge 0.6$.
For such $x$ we have $\max(x, 1 - x) = x$, with the smallest value $0.6$ at $x = 0.6$.
So $\lVert p \lor \neg p \rVert_T = 0.6$.

## Remarks

By Pavelka-style completeness, the provability degree of $p \lor \neg p$ is also $\tfrac12$ in the empty theory and $0.6$ in $T$.
In the empty theory the supremum is attained, by step 4 with $r = \tfrac12$, and step 5 shows by soundness that no bound above $\tfrac12$ is provable.

In classical logic $p \lor \neg p$ has degree $1$.
In any t-norm logic with residuated negation it falls short of $1$: for $0 < x < 1$ the negation $\neg x$ is below $1$, so $\max(x, \neg x) < 1$.
The degree $\tfrac12$ is special to the Łukasiewicz negation $1 - x$; in Gödel logic $\neg x = 0$ for $x > 0$, and the infimum of $\max(x, \neg x)$ is $0$.

## Explanations

### L1 human

"$p$ or not $p$" is at least half true, whatever the degree of $p$.
It is exactly half true when $p$ is half true.
If we know $p$ to degree $0.6$, then "$p$ or not $p$" is known to degree $0.6$.

### L2 human

To compute a truth degree, write the value of the formula as a function of $x = e(p)$.
Then find the smallest value over the models of the theory.
Watch out: the degree is an infimum over all models, not the value at one chosen model.
