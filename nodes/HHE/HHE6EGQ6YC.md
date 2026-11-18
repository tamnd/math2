---
tag: HHE6EGQ6YC
kind: example
name: The response property on a lasso-shaped word
msc: ["03B44", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [RMJ56ZPA63]
uses: [8S64VZ6A1S, RMJ56ZPA63]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_temporal_logic
    locator: section Semantics
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 5
---

## Example

Let $AP = \set{\mathit{req}, \mathit{grant}}$ and consider the response formula of [[linear temporal logic|RMJ56ZPA63]]
$$\rho = G(\mathit{req} \to F\,\mathit{grant}).$$
Take the lasso-shaped word $w = u\,v^\omega$ with prefix $u = \set{\mathit{req}}\,\set{\mathit{req}}$ and loop $v = \set{\mathit{grant}}\,\emptyset\,\set{\mathit{req}}$.

1. The positions of $w$ are: $\mathit{req}$ at $0$ and $1$, and then for each $k \ge 0$, $\mathit{grant}$ at $2 + 3k$, nothing at $3 + 3k$, $\mathit{req}$ at $4 + 3k$.
2. By [[the definition|8S64VZ6A1S]], $w \models \rho$ means that $w^i \models \mathit{req} \to F\,\mathit{grant}$ for every $i \ge 0$.
3. At $i = 0$ and $i = 1$ there is a request, and position $2$ has a grant. So $F\,\mathit{grant}$ holds there.
4. At $i = 4 + 3k$ there is a request, and position $5 + 3k = 2 + 3(k + 1)$ has a grant.
5. At every other position there is no request, so the implication holds.
6. Hence $w \models \rho$.

Two variants fail on the same word.

7. $G(\mathit{req} \to X\,\mathit{grant})$ fails at $0$: position $1$ has no grant.
8. $GF\,\mathit{req} \wedge FG \neg\mathit{grant}$ fails, since grants occur at all positions $2 + 3k$.

## Remarks

For $i \ge 2$ the suffix $w^i$ depends only on $i \bmod 3$, so $w$ has at most five distinct suffixes.
In fact it has four, since $w^1 = w^4 = \set{\mathit{req}}\,v^\omega$.
So checking $G\psi$ on a lasso word needs only finitely many positions, here $0$ to $4$.
This is why model checkers report counterexamples as lasso words: every nonempty [[Büchi automaton|92DM43HQZT]] accepts one.
The word $\set{\mathit{req}}\,\emptyset^\omega$ violates $\rho$, but no finite prefix of it shows the violation, since a grant could still come.

## Explanations

### L1 human

The word is a log of a server that runs forever.
It gets two requests, then repeats "grant, idle, request" forever.
"Every request is eventually granted" is true: after every request, a grant comes within three steps.
"Every request is granted at the very next step" is false, because the second request comes right after the first.

### L2 human

To check $G\psi$ on $u v^\omega$, list the positions of $u$ and one pass through $v$.

1. Positions $0, 1$ are the prefix, and positions $2, 3, 4$ are the first pass through the loop.
2. Position $5$ has the same suffix as position $2$, so nothing new appears after $4$.
3. For $F\,\mathit{grant}$ at position $4$, look ahead into the next pass of the loop: position $5$.

A trap: for an eventuality at the end of the loop, the witness is in the next pass, not in the same one.
