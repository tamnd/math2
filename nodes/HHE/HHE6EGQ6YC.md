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

Let $AP = \{\mathit{req}, \mathit{grant}\}$, and take the response formula of [[linear temporal logic|RMJ56ZPA63]]:
$$\rho = G(\mathit{req} \to F\,\mathit{grant}).$$
Take the lasso-shaped word $w = u\,v^\omega$ with prefix $u = \{\mathit{req}\}\,\{\mathit{req}\}$ and loop $v = \{\mathit{grant}\}\,\emptyset\,\{\mathit{req}\}$.
We check that $w \models \rho$.

1. The positions of $w$ are these: $\mathit{req}$ at $0$ and $1$, and then, for each $k \ge 0$, $\mathit{grant}$ at $2 + 3k$, nothing at $3 + 3k$, and $\mathit{req}$ at $4 + 3k$.
2. By [[the definition|8S64VZ6A1S]], $w \models \rho$ means that $w^i \models \mathit{req} \to F\,\mathit{grant}$ for every $i \ge 0$.
3. At $i = 0$ and $i = 1$ there is a request, and position $2$ has a grant, so $F\,\mathit{grant}$ holds there.
4. At $i = 4 + 3k$ there is a request, and position $5 + 3k = 2 + 3(k + 1)$ has a grant.
5. At every other position there is no request, so the implication holds.
   Hence $w \models \rho$.

A stronger variant fails on the same word.
The formula $G(\mathit{req} \to X\,\mathit{grant})$ fails at $0$, because position $1$ has a request and no grant.

## Remarks

Why do only finitely many positions matter?
For $i \ge 2$ the suffix $w^i$ depends only on $i \bmod 3$, so $w$ has at most five distinct suffixes.
In fact it has four, since both $w^1$ and $w^4$ equal $\{\mathit{req}\}\,v^\omega$.
So checking $G\psi$ on this word needs only the positions $0$ to $4$.
This is why model checkers report counterexamples as lasso words: every nonempty [[Büchi automaton|92DM43HQZT]] accepts one.

Change the loop and the answer changes.
The word $\{\mathit{req}\}\,\emptyset^\omega$ violates $\rho$ at position $0$, but no finite prefix of it shows the violation, since a grant could still come later.

## Explanations

### L1 human

The word is the log of a server that runs forever.
It gets two requests, then repeats "grant, idle, request" forever.
"Every request is eventually granted" is true: after every request, a grant comes within three steps.
"Every request is granted at the very next step" is false, because the second request comes right after the first.

### L2 human

To check $G\psi$ on $u v^\omega$, list the positions of $u$ and one pass through $v$.
Here positions $0$ and $1$ are the prefix, and positions $2$, $3$ and $4$ are the first pass through the loop.
Position $5$ has the same suffix as position $2$, so nothing new appears after $4$.
For $F\,\mathit{grant}$ at position $4$, look ahead into the next pass of the loop, and find the grant at position $5$.
Watch out: for an eventuality at the end of the loop, the witness is in the next pass, not in the same one.
