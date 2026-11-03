---
tag: ZYDZME1BH3
kind: definition
name: Divide-and-conquer algorithm
msc: [68W40, 68W01]
defines: G9NFJ55KCX
uses: [9DMSG5HAQX, 0FYX44GP92]
sources:
  - url: https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm
---

## Definition

Let $I$ be a set of problem instances with a size function $\abs{\cdot} \colon I \to \N$.
A *divide-and-conquer algorithm* on $I$ is a recursive [[algorithm|9DMSG5HAQX]] given by:

1. a direct method that solves every instance of size at most a constant $n_0$;
2. a *divide* step that maps each instance $x$ with $\abs{x} > n_0$ to finitely many instances $x_1, \dots, x_a$ of $I$ with $\abs{x_i} < \abs{x}$;
3. a *combine* step that computes the solution of $x$ from the solutions of $x_1, \dots, x_a$.

On an instance of size greater than $n_0$, the algorithm divides, solves each $x_i$ recursively, and combines.

## Remarks

Clause 2 makes the recursion terminate, since the sizes strictly decrease in $\N$.
If dividing and combining cost $f(n)$ and each subproblem has size about $n/b$, the running time satisfies the [[recurrence|0FYX44GP92]] $T(n) = a\,T(n/b) + f(n)$.

Example: Karatsuba multiplication of two $n$-digit numbers writes $x = x_1 B + x_0$ and $y = y_1 B + y_0$ with $B$ a power of the base of about half the length, and uses $x y = x_1 y_1 B^2 + \big((x_1 + x_0)(y_1 + y_0) - x_1 y_1 - x_0 y_0\big) B + x_0 y_0$.
This needs three recursive products of about half size instead of four, so $T(n) = 3T(n/2) + O(n)$ and $T(n) = O(n^{\log_2 3})$.

Non-example: a recursion that reduces an instance of size $n$ to an instance of the same size $n$ fails clause 2, and it need not terminate.
