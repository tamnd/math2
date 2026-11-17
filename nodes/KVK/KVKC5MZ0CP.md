---
tag: KVKC5MZ0CP
kind: example
name: The one-way equals sign in n² + 3n = O(n²)
msc: ["00A35", "41A60"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [BCGR3NPPXC]
uses: [BCGR3NPPXC, 0TGV80E6A4]
sources:
  - url: https://en.wikipedia.org/wiki/Big_O_notation
    locator: lead section
---

## Example

By the definition of [[big O notation|0TGV80E6A4]], $f(n) = O(g(n))$ means: there are constants $C > 0$ and $N$ such that $|f(n)| \le C \, |g(n)|$ for all $n \ge N$.
We prove $n^2 + 3n = O(n^2)$ and then show why the sign $=$ here is one-way.

1. For $n \ge 1$ we have $3n \le 3n^2$, so $n^2 + 3n \le n^2 + 3n^2 = 4n^2$.
2. So $C = 4$ and $N = 1$ work, and $n^2 + 3n = O(n^2)$.
3. In the same way, $n \le n^2$ for $n \ge 1$, so $C = 1$ and $N = 1$ give $n = O(n^2)$.
4. If the two signs $=$ were equalities of functions, symmetry and transitivity would give $n = n^2 + 3n$ for every $n$.
5. At $n = 1$ this would say $1 = 4$, which is false.
6. So $O(n^2)$ is a class of functions, and "$f = O(g)$" means $f \in O(g)$. The sign does not allow the sides to be exchanged or chained like an equality.

## Remarks

The example shows the main difference between the $=$ of big O notation and the $=$ of [[equality, definition and equivalence signs|BCGR3NPPXC]].
Donald Knuth calls such statements "one-way equalities".
Chains that read from left to right stay valid: $n^2 + 3n = O(n^2) = O(n^3)$ means $n^2 + 3n \in O(n^2) \subseteq O(n^3)$.
A chain that reads from right to left, such as $O(n^2) = n$, is not valid.

## Explanations

### L1 human

The statement $n^2 + 3n = O(n^2)$ says "for large $n$, $n^2 + 3n$ is at most a fixed multiple of $n^2$".
Here the multiple $4$ works, because $n^2 + 3n \le 4n^2$ once $n \ge 1$.
The same is true of $n$ alone, since $n \le n^2$.
So two different expressions are both "$O(n^2)$", and the sign $=$ here does not mean "the same".

### L2 human

We show that $n^2 = O(n)$ is false, so the sign is not symmetric.

1. Suppose there are $C > 0$ and $N$ with $n^2 \le C n$ for all $n \ge N$.
2. For $n \ge 1$ this gives $n \le C$.
3. Take an integer $n > \max(C, N, 1)$. Then $n \le C$ fails, which is a contradiction.
4. So $n^2 \ne O(n)$, although $n = O(n^2)$.

The typical use of big O is to state the running time of an algorithm, as in "insertion sort uses $O(n^2)$ comparisons".
A trap: $O(n^2)$ gives an upper bound only, so the statement $n = O(n^2)$ is true even though $n^2$ is a poor bound for $n$.
