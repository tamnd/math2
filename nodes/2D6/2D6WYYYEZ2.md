---
tag: 2D6WYYYEZ2
kind: example
name: A paramodulation refutation
msc: ["03B10", "03B35"]
topics: [TTCRX3NFNY]
audience: grad
instance_of: [Y90Z13AXY8]
uses: [Y90Z13AXY8, DEB3CF4Z2D, RJJ9D0WF53, T3SXVH3ZZC]
sources:
  - url: https://en.wikipedia.org/wiki/Resolution_(logic)
    locator: Paramodulation
---

## Example

We refute four [[clauses|T3SXVH3ZZC]] by one step of paramodulation, which replaces $f(g(y))$ by $g(y)$, and two steps of [[first-order resolution|DEB3CF4Z2D]].
The clauses, with variables already renamed apart, are
$$C_1 = \{ f(x) = x, R(x) \}, \quad C_2 = \{ P(f(g(y)), y) \}, \quad C_3 = \{ \neg P(g(b), b) \}, \quad C_4 = \{ \neg R(g(b)) \}.$$
Here $=$ is the logical equality symbol, $f$ and $g$ are unary function symbols, $b$ is a constant, $P$ is binary and $R$ is unary.

The paramodulation rule takes $C \cup \{ s = t \}$ and $D \cup \{ L \}$, where $L$ contains a subterm $u$ and $\sigma$ is an mgu of $s$ and $u$.
It derives $(C \cup D \cup \{ L' \})\sigma$, where $L'$ comes from $L$ by replacing that occurrence of $u$ by $t$.

1. Choose the equation.
   In $C_1$ take $s = f(x)$ and $t = x$, so $C = \{ R(x) \}$.
2. Choose the subterm.
   In $C_2$ take $L = P(f(g(y)), y)$ and $u = f(g(y))$, its first argument, so $D = \varnothing$.
3. Unify $s$ with $u$.
   The [[unification|RJJ9D0WF53]] of $f(x)$ and $f(g(y))$ reduces to the equation $x = g(y)$, and $x$ does not occur in $g(y)$.
   The mgu is $\sigma_1 = \{ x \mapsto g(y) \}$.
4. Check: $f(x)\sigma_1 = f(g(y)) = u\sigma_1$.
5. Replace.
   $L'$ is $P(x, y)$, with $t = x$ in place of $u$.
6. The paramodulant is $\{ R(x), P(x, y) \}\sigma_1 = \{ R(g(y)), P(g(y), y) \}$, and we call it $C_5$.
7. Resolve $C_5$ with $C_3$ on $P(g(y), y)$ and $\neg P(g(b), b)$.
   The equations are $g(y) = g(b)$ and $y = b$.
   The first reduces to $y = b$, which gives $y \mapsto b$, and the second then becomes $b = b$ and is deleted.
8. The mgu is $\sigma_2 = \{ y \mapsto b \}$, and the resolvent is $\{ R(g(y)) \}\sigma_2 = \{ R(g(b)) \}$, which we call $C_6$.
9. Resolve $C_6$ with $C_4$ on $R(g(b))$ and $\neg R(g(b))$.
   The atoms are equal, the mgu is the empty substitution $\varepsilon$, and the resolvent is the empty clause $\square$.

Check by meaning that the set is unsatisfiable.
In a model, $C_4$ makes $R(g(b))$ false, so $C_1$ at $x = g(b)$ gives $f(g(b)) = g(b)$.
Then $C_2$ at $y = b$ gives $P(f(g(b)), b)$, that is $P(g(b), b)$, which contradicts $C_3$.

## Remarks

### Why paramodulation was needed

If $=$ is read as an ordinary binary predicate $E$, the four clauses are satisfiable.
Take the ground terms over $b$, $f$ and $g$ as the domain, $E$ true everywhere, $R$ false everywhere, and $P(s, t)$ true unless $s$ is the term $g(b)$ and $t$ is the term $b$.
Then $C_2$ holds because $f(g(t))$ is never the term $g(b)$, and $C_1$, $C_3$ and $C_4$ hold by the choice of $E$, $P$ and $R$.
In this structure $E$ is not a congruence, since $E(f(g(b)), g(b))$ holds while $P(f(g(b)), b)$ is true and $P(g(b), b)$ is false.

### Equality axioms as clauses

Without paramodulation, a prover could add equality axioms as clauses, for example $\{ \neg\, x_1 = y_1, \neg P(x_1, z), P(y_1, z) \}$ for the first argument of $P$.
Resolution with such clauses also finds a refutation.
But these clauses match almost every literal, and the search grows much faster.

### The same step in superposition

Take a superposition prover with an ordering in which $f(x) \succ x$ and the equation $f(x) = x$ is the maximal literal of $C_1$.
Then the step above is allowed, because it rewrites with the larger side $f(x)$ of the equation.
The reverse step, which would rewrite an occurrence of $x$ into $f(x)$, is forbidden.

## Explanations

### L1 human

One fact says: for every $x$, either $f(x)$ equals $x$, or $x$ has the property $R$.
For the object $g(b)$ we know that it does not have property $R$, so $f(g(b))$ equals $g(b)$.
A second fact says something about $f(g(b))$, and we may replace it by $g(b)$.
The result contradicts a third fact.
Paramodulation is the computer's way of doing this "replace equals by equals" step, with letters instead of fixed objects.

### L2 human

A paramodulation step has four parts.
First we pick an equation $s = t$ in one clause and a subterm $u$ of a literal in another clause.
Then we compute the mgu $\sigma$ of $s$ and $u$, and if there is none, the step is not possible.
Next we replace the chosen occurrence of $u$ by $t$.
Last we collect the remaining literals of both clauses and apply $\sigma$ to everything.
The typical use is reasoning in algebra, for example with the group axioms as unit equations.
Watch out: keep the other literals of the equation clause.
Here $R(g(y))$ must stay in $C_5$, since the clause $C_1$ gives $f(x) = x$ only when $R(x)$ fails.
