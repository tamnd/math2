---
tag: PW316WQX7E
kind: example
name: The three-valued Łukasiewicz-Moisil chain
msc: ["03G20", "03B50"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [51A2GMPDYK]
uses: [15PMWZPYQ6, 1CE2TGM6MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
  - book: isbn:9780863802621
---

## Example

Take $L_3 = \set{0, \tfrac12, 1}$ with $\max$, $\min$ and $\sim x = 1 - x$.
Put $\varphi_1 x = 1$ if $x = 1$ and $0$ otherwise, and $\varphi_2 x = 1$ if $x \ge \tfrac12$ and $0$ otherwise.
We check [[the definition|15PMWZPYQ6]].

1. De Morgan algebra. $\sim$ reverses the order of the chain and $\sim \sim x = x$.
2. Clause 1. Each $\varphi_i$ is monotone on a chain, so it preserves $\max$ and $\min$, and it fixes $0$ and $1$.
3. Clauses 2 and 3. Each value of $\varphi_i$ is $0$ or $1$, and $\varphi_i$ fixes $0$ and $1$.
4. Clause 4. $\varphi_1 \sim x = 1$ iff $x = 0$ iff $\varphi_2 x = 0$. And $\varphi_2 \sim x = 1$ iff $x \le \tfrac12$ iff $\varphi_1 x = 0$.
5. Clause 5. $\varphi_1 x \le \varphi_2 x$, since $x = 1$ implies $x \ge \tfrac12$.
6. Clause 6. The pairs $(\varphi_1 x, \varphi_2 x)$ are $(0, 0)$, $(0, 1)$, $(1, 1)$, and they are distinct.

So $L_3$ is a [[Łukasiewicz-Moisil algebra|51A2GMPDYK]] with $n = 3$.

## Remarks

1. $\varphi_1$ is the "necessarily" operator and $\varphi_2$ is the "possibly" operator of Łukasiewicz's modal reading of [[three-valued logic|1CE2TGM6MQ]].
2. The Łukasiewicz implication $x \to y = \min(1, 1 - x + y)$ is a term: $x \to y = \sim x \lor y \lor (\sim \varphi_1 x \land \varphi_2 y)$. A check of the nine pairs confirms the formula.
3. The center of $L_3$ is $\set{0, 1}$.
4. $L_3$ has exactly two subalgebras: $\set{0, 1}$ and $L_3$.

## Explanations

### L1 human

The three values are false, half and true.
"Necessarily $x$" is true only when $x$ is true.
"Possibly $x$" is true when $x$ is at least half.
These two tests tell the three values apart.

### L2 human

1. Check the formula of remark 2 at $x = y = \tfrac12$.
2. $\sim x \lor y = \tfrac12$.
3. $\sim \varphi_1 x = \sim 0 = 1$, and $\varphi_2 y = 1$, so the last term is $1$.
4. So $x \to y = 1 = \min(1, 1 - \tfrac12 + \tfrac12)$.

The typical use: $L_3$ generates $\mathbf{LM}_3$, and it is term-equivalent to the three-element MV-algebra.
The trap: $\sim x \lor y$ alone gives $\tfrac12$ at $x = y = \tfrac12$, which is the Kleene value, not the Łukasiewicz value.
