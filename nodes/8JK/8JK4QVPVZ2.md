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

For $k \ge 1$, let $f_k \colon \N \to \N$ be the [[function|0EPAT51DXQ]] $f_k(n) = n^k$.
We build by [[diagonalization|V2H30SA654]] a function $g$ such that, for each $k$, $g(n) > f_k(n)$ for all $n \ge k$.

1. Define $g(n) = \max\set{f_1(n), \ldots, f_n(n)} + 1$ for $n \ge 1$, and $g(0) = 1$.
2. For $n \ge 1$, the largest of $n^1, \ldots, n^n$ is $n^n$, because $n \ge 1$. So $g(n) = n^n + 1$.
3. Fix $k$, and let $n \ge k$. Then $f_k$ is one of $f_1, \ldots, f_n$ in the maximum.
4. So $g(n) \ge f_k(n) + 1 > f_k(n)$ for all $n \ge k$.
5. So $g$ is not bounded by any single power $n^k$ for large $n$, and in particular $g$ is not a polynomial.

We check small values for $k = 3$.

1. $g(3) = 3^3 + 1 = 28 > 27 = f_3(3)$.
2. $g(4) = 4^4 + 1 = 257 > 64 = f_3(4)$.
3. For $n = 2 < k$, the bound fails: $g(2) = 5 < 8 = f_3(2)$.

## Remarks

The example shows the diagonal method for growth rates: $g$ beats $f_n$ at the place $n$, and the maximum carries the win to all later places.
The general form uses any sequence $f_1, f_2, \ldots$ of functions on $\N$: the same $g$ eventually exceeds each $f_k$.
So no countable family of functions eventually dominates every function on $\N$.

A strict diagonal $g(n) = f_n(n) + 1$ beats $f_n$ only at the place $n$.
For the powers, $f_n(n) + 1 = n^n + 1$ is the same function, because the powers increase with $k$.
For a general sequence the maximum is needed, because the single value $f_n(n)$ does not control $f_k(n)$ for $k < n$.
The [[Ackermann function|N470JF7ZJX]] $n \mapsto A(n, n)$ is a diagonal of the family of functions $A(m, \cdot)$, and it eventually exceeds every primitive recursive function.

## Explanations

### L1 human

Think of a list of growth rules: $n$, then $n^2$, then $n^3$, and so on.
We want a rule that grows faster than each of them in the end.
At step $n$, we look at the first $n$ rules, take the biggest value, and add one.
At step $4$, this gives $4^4 + 1 = 257$, more than $4$, $16$, $64$ and $256$.
So our rule catches every rule in the list from some step on.

### L2 human

We diagonalize against the list $f_1(n) = n$, $f_2(n) = 2n$, $f_3(n) = 3n$, and so on, with $f_k(n) = kn$.

1. Define $g(n) = \max\set{1 \cdot n, 2 \cdot n, \ldots, n \cdot n} + 1 = n^2 + 1$ for $n \ge 1$.
2. For fixed $k$ and $n \ge k$, we have $g(n) = n^2 + 1 \ge kn + 1 > f_k(n)$.
3. So $g$ is eventually larger than every linear function $kn$.

The typical use is a proof that a countable class of functions does not contain a fast enough function.
A trap is to expect $g(n) > f_k(n)$ for every $n$: the bound holds only from $n = k$ on.
