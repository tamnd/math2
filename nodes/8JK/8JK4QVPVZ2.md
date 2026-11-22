---
tag: 8JK4QVPVZ2
kind: example
name: A function that eventually exceeds every power of n
msc: ["03D20", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [V2H30SA654]
uses: [V2H30SA654, 0EPAT51DXQ, 0G9EKM0E15, N470JF7ZJX]
sources:
  - url: https://en.wikipedia.org/wiki/Ackermann_function
    locator: lead section
---

## Example

For $k \ge 1$, let $f_k \colon \mathbb{N} \to \mathbb{N}$ be the [[function|0EPAT51DXQ]] $f_k(n) = n^k$.
We build by [[diagonalization|V2H30SA654]] a function $g$ such that, for each $k$, $g(n) > f_k(n)$ for all $n \ge k$.

1. Define $g(0) = 1$, and for $n \ge 1$
   $$g(n) = \max\{f_1(n), \ldots, f_n(n)\} + 1.$$
2. For $n \ge 1$, the largest of $n^1, \ldots, n^n$ is $n^n$, because for $n \ge 1$ the powers do not decrease as the exponent grows.
   So $g(n) = n^n + 1$.
3. Fix $k \ge 1$, and let $n \ge k$.
   Then $f_k$ is one of $f_1, \ldots, f_n$ in the maximum.
4. So $g(n) \ge f_k(n) + 1 > f_k(n)$ for all $n \ge k$.
5. Therefore no single power $n^k$ bounds $g$ for large $n$, and in particular $g$ is not a polynomial.

We check small values for $k = 3$.

1. $g(3) = 3^3 + 1 = 28 > 27 = f_3(3)$.
2. $g(4) = 4^4 + 1 = 257 > 64 = f_3(4)$.
3. For $n = 2 < k$ the bound can fail, and it does: $g(2) = 5 < 8 = f_3(2)$.

## Remarks

The function $g$ beats $f_n$ at the place $n$, and the maximum carries the win to all later places.
The same construction works for any sequence $f_1, f_2, \ldots$ of functions on $\mathbb{N}$: the function $g$ eventually exceeds each $f_k$.
So no countable family of functions eventually dominates every function on $\mathbb{N}$.

A plain diagonal $g(n) = f_n(n) + 1$ beats $f_n$ only at the place $n$.
For the powers, it happens to be the same function $n^n + 1$, because the powers increase with $k$.
For a general sequence the maximum is needed, because the single value $f_n(n)$ does not control $f_k(n)$ for $k < n$.
The [[Ackermann function|N470JF7ZJX]] $n \mapsto A(n, n)$ is a diagonal of the family of functions $A(m, \cdot)$, and it eventually exceeds every primitive recursive function.

## Explanations

### L1 human

Think of a list of growth rules: $n$, then $n^2$, then $n^3$, and so on.
You want a rule that, in the end, grows faster than each of them.
At step $n$, look at the first $n$ rules, take the biggest value, and add one.
At step $4$, this gives $4^4 + 1 = 257$, more than $4$, $16$, $64$ and $256$.
So the new rule catches every rule in the list from some step on.

### L2 human

We diagonalize against the linear functions $f_k(n) = kn$ for $k \ge 1$.
For $n \ge 1$ the construction gives
$$g(n) = \max\{1 \cdot n, 2 \cdot n, \ldots, n \cdot n\} + 1 = n^2 + 1.$$
For fixed $k$ and $n \ge k$ we have $g(n) = n^2 + 1 \ge kn + 1 > f_k(n)$.
So $g$ is eventually larger than every linear function.
Check with $k = 5$ and $n = 5$: $g(5) = 26 > 25 = f_5(5)$.

The typical use is a proof that a countable class of functions misses a fast enough function.
Watch out: do not expect $g(n) > f_k(n)$ for every $n$, since the bound holds only from $n = k$ on.
