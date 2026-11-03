---
tag: W0V3GVZ4VQ
kind: statement
role: theorem
name: Guruswami–Sudan algorithm
msc: [94B35, 94B05]
uses: [5VBWJ7EFTX, G4C8XDKQVY, 0ZXZ82FTX2]
about: [5VBWJ7EFTX, T88M6XTTRP]
sources:
  - url: https://en.wikipedia.org/wiki/List_decoding
---

## Statement

Let $\F_q$ be a [[finite field|0ZXZ82FTX2]], let $1 \le k \le n$, and let $a_1, \dots, a_n \in \F_q$ be distinct.
There is an algorithm, running in time polynomial in $n$ and $\log q$, with the following property.
Given $y \in \F_q^n$, it outputs a list containing every polynomial $f \in \F_q[x]$ with $\deg f < k$ such that
$$\abs{\set{i : f(a_i) = y_i}} > \sqrt{(k - 1)\, n}.$$
In other words, the [[Reed–Solomon code|5VBWJ7EFTX]] of dimension $k$ at these points can be [[list decoded|T88M6XTTRP]] from fewer than $n - \sqrt{(k-1) n}$ errors in polynomial time.

## Remarks

The algorithm has two steps.
First, it finds by linear algebra a nonzero bivariate polynomial $Q(x, z)$ of small $(1, k - 1)$-weighted degree that vanishes with a chosen multiplicity $r$ at each of the points $(a_i, y_i)$.
Second, it factors $Q$ and keeps the factors of the form $z - f(x)$ with $\deg f < k$.
A counting argument shows that $Q(x, f(x))$ has more roots, counted with multiplicity, than its degree whenever $f$ agrees with $y$ often enough, so $Q(x, f(x)) = 0$ and $z - f(x)$ divides $Q$.
Sudan's earlier version used multiplicity $r = 1$ and needed roughly $\sqrt{2kn}$ agreements.

For rate $R = k/n$, the fraction of errors handled is about $1 - \sqrt{R}$.
This is larger than the unique decoding radius $(1 - R)/2$ for every $0 < R < 1$, since $1 - \sqrt{R} = (1 - R)/(1 + \sqrt{R})$.
For example, at $R = 1/4$ unique decoding handles a fraction $3/8$ of errors, while the algorithm handles almost $1/2$.

## Explanations

### L1 human

A Reed–Solomon codeword is the list of values of a low-degree polynomial.
Even when nearly half of the values are corrupted, this algorithm finds every low-degree polynomial that fits enough of the received values.
There may be several, so it returns a short list instead of one answer.

### L2 human

The classical decoders, such as the [[Berlekamp–Welch algorithm|D2WZ0M5RWX]], stop at half the minimum distance $n - k + 1$.
The Guruswami–Sudan algorithm reaches the radius $n - \sqrt{(k-1)n}$, which is the Johnson radius for Reed–Solomon codes.
Its two ingredients, interpolation with multiplicities and root finding of bivariate polynomials, reappear in list decoding of [[algebraic geometry codes|DY3CHS08CT]] and in later capacity-achieving list decodable codes.
