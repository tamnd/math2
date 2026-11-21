---
tag: PPTAJEWFBD
kind: example
name: A subalgebra of the five-valued Moisil chain that is not closed under Łukasiewicz implication
msc: ["03G20", "03B50"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [51A2GMPDYK]
uses: [15PMWZPYQ6, 8T4M7RN9AC]
sources:
  - book: isbn:9780792360094
---

## Example

Take $L_5 = \set{0, \tfrac14, \tfrac12, \tfrac34, 1}$ as an algebra in $\mathbf{LM}_5$, with $\sim x = 1 - x$ and $\varphi_i(\tfrac{j}{4}) = 1$ iff $i + j \ge 5$.
Let $S = \set{0, \tfrac14, \tfrac34, 1}$.

1. Lattice. $S$ is a chain, so it is closed under $\max$ and $\min$.
2. Negation. $\sim 0 = 1$ and $\sim \tfrac14 = \tfrac34$, so $S$ is closed under $\sim$.
3. Operators. Each $\varphi_i$ takes values in $\set{0, 1} \subseteq S$.
4. So $S$ is a subalgebra of $L_5$, and it satisfies [[the definition|15PMWZPYQ6]], since the clauses are universal.
5. The Łukasiewicz implication $x \to y = \min(1, 1 - x + y)$ gives $\tfrac34 \to \tfrac14 = \tfrac12 \notin S$.

So $S$ is a [[Łukasiewicz-Moisil algebra|51A2GMPDYK]], and $\to$ is not a term operation of $\mathbf{LM}_5$: term operations preserve subalgebras.

## Remarks

1. The same works for every $n \ge 5$ with $S = \set{0, \tfrac{1}{n - 1}, \tfrac{n - 2}{n - 1}, 1}$. Then $\tfrac{n - 2}{n - 1} \to \tfrac{1}{n - 1} = \tfrac{2}{n - 1}$, which is not in $S$ for $n \ge 5$.
2. So for $n \ge 5$, $L_n$ as an $\mathbf{LM}_n$ algebra and $L_n$ as an [[MV-algebra|8T4M7RN9AC]] have different term operations.
3. For $n = 4$, the set $S$ is all of $L_4$, and the argument does not apply.

## Explanations

### L1 human

Remove the middle value $\tfrac12$ from the five values.
The Moisil operations never produce $\tfrac12$ from the other values.
Łukasiewicz implication does produce it.
So the Moisil operations cannot build Łukasiewicz implication.

### L2 human

1. Compute $\varphi_i(\tfrac34)$: $j = 3$, so $\varphi_i = 1$ iff $i \ge 2$, and the pattern is $(0, 1, 1, 1)$.
2. Compute $\varphi_i(\tfrac14)$: $j = 1$, so the pattern is $(0, 0, 0, 1)$.
3. All values are $0$ or $1$, inside $S$.
4. But $1 - \tfrac34 + \tfrac14 = \tfrac12$.

The typical use: this is the standard argument that $\mathbf{LM}_n$ is weaker than $n$-valued Łukasiewicz logic for $n \ge 5$.
The trap: a term operation must preserve every subalgebra; finding one subalgebra that it leaves is enough to show that it is not a term.
