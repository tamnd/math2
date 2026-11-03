---
tag: BTQKXCRPX5
kind: definition
name: Karmarkar's algorithm
msc: [90C05, 90C51, 68Q25]
defines: 8DGAXR9WZR
uses: [VNMXB0J2KA, 0B8KZRT28M, 0VD9ZSWWJG, YX1DJK2QAG, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Karmarkar's_algorithm
---

## Definition

Let $n \ge 2$, let $A$ be a real $m \times n$ [[matrix|0VD9ZSWWJG]] and $c \in \R^n$, and let $e = (1, \dots, 1) \in \R^n$.
Consider the [[linear program|VNMXB0J2KA]] in *Karmarkar's canonical form*: minimize $c^T x$ subject to $A x = 0$, $e^T x = 1$, $x \ge 0$.
Assume that $A e = 0$, so that the centre $e/n$ of the [[simplex|YX1DJK2QAG]] $\set{x \ge 0 : e^T x = 1}$ is feasible, and that the optimal value is $0$.
Let $r = 1/\sqrt{n(n-1)}$ and fix a step parameter $\alpha \in (0, 1)$; Karmarkar used $\alpha = 1/4$.
*Karmarkar's algorithm* starts at $x^0 = e/n$ and repeats these steps until $c^T x^k$ is below a prescribed tolerance.

1. Let $D = \mathrm{diag}(x^k)$, and let $B$ be the $(m + 1) \times n$ matrix with rows those of $A D$ and then $e^T$.
2. Let $p$ be the [[orthogonal projection|0B8KZRT28M]] of $D c$ onto the null space of $B$.
3. Let $z = e/n - \alpha r \, p / \norm{p}$.
4. Let $x^{k+1} = D z / (e^T D z)$.

## Remarks

The map $x \mapsto D^{-1} x / (e^T D^{-1} x)$ is a projective transformation that maps the simplex to itself and $x^k$ to its centre $e/n$.
Because the optimal value is $0$, the transformed objective can be taken as the linear function $z \mapsto (D c)^T z$.
Step 3 is a step of length $\alpha r$ against the projected gradient, inside the largest ball around $e/n$ in the simplex, whose radius is $r$.
Step 4 maps the result back.

For $\alpha = 1/4$, the potential $f(x) = \sum_{j=1}^n \ln \bigl(c^T x / x_j\bigr)$ decreases by at least a fixed positive constant at every step.
Hence the algorithm reaches a point with $c^T x \le 2^{-O(L)}$ after $O(n L)$ steps, where $L$ is the bit length of the data.
A final rounding step then gives an exact optimal vertex, and the total work is $O(n^{3.5} L)$ arithmetic operations.
Every linear program can be brought into the canonical form with these assumptions.

Example: for $n = 2$, $A$ the zero matrix and $c = (1, 0)$, the optimum is $x = (0, 1)$ with value $0$, and $A e = 0$ holds.
At $x^0 = (1/2, 1/2)$, one has $D c = (1/2, 0)$ and $p = (1/4, -1/4)$, so the step moves towards $(0, 1)$ along the segment.

Non-example: the [[algorithm|9DMSG5HAQX]] that moves from vertex to adjacent vertex is the simplex algorithm, not Karmarkar's algorithm; Karmarkar's iterates stay in the interior, with $x^k > 0$.
