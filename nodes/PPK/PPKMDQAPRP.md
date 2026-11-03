---
tag: PPKMDQAPRP
kind: definition
name: Berlekamp–Massey algorithm
msc: [94A55, 94B35, 68W30]
defines: TXR1WX1NTT
uses: [WHX90SGEJ5, V2C6HQQAHK]
sources:
  - url: https://en.wikipedia.org/wiki/Berlekamp%E2%80%93Massey_algorithm
---

## Definition

Let $F$ be a field and let $s = (s_0, \dots, s_{N-1})$ be a sequence over $F$.
The *Berlekamp–Massey algorithm* computes an integer $L$ and a polynomial $C(x) = 1 + c_1 x + \cdots + c_L x^L \in F[x]$ as follows.
It keeps polynomials $C(x)$ and $B(x)$, integers $L$ and $m$, and a nonzero $b \in F$.

1. Set $C(x) = 1$, $B(x) = 1$, $L = 0$, $m = 1$ and $b = 1$.
2. For $n = 0, 1, \dots, N - 1$, compute the discrepancy $d = s_n + \sum_{i=1}^{L} c_i s_{n-i}$, where $c_i$ is the coefficient of $x^i$ in $C(x)$. Then:
   - if $d = 0$, replace $m$ by $m + 1$;
   - if $d \ne 0$ and $2L \le n$, let $T(x) = C(x)$, replace $C(x)$ by $C(x) - d b^{-1} x^m B(x)$, then set $L = n + 1 - L$, $B(x) = T(x)$, $b = d$ and $m = 1$;
   - if $d \ne 0$ and $2L > n$, replace $C(x)$ by $C(x) - d b^{-1} x^m B(x)$ and $m$ by $m + 1$.
3. Output $L$ and $C(x)$.

## Remarks

The output is a [[linear-feedback shift register|WHX90SGEJ5]] of length $L$ with connection polynomial $C(x)$ that generates $s$, and $L$ is the [[linear complexity|V2C6HQQAHK]] of $s$.
The algorithm uses $O(N^2)$ operations in $F$.

Example: over $\F_2$ let $s = (1, 1, 0, 1, 1, 0)$.
At $n = 0$, $d = 1$ and $2L = 0 \le 0$, so $C = 1 + x$, $L = 1$, $B = 1$, $m = 1$.
At $n = 1$, $d = s_1 + s_0 = 0$, so $m = 2$.
At $n = 2$, $d = s_2 + s_1 = 1$ and $2L = 2 \le 2$, so $C = 1 + x + x^2$, $L = 2$, $B = 1 + x$, $m = 1$.
At $n = 3, 4, 5$ the discrepancies $s_n + s_{n-1} + s_{n-2}$ are $0$.
The output is $L = 2$ and $C(x) = 1 + x + x^2$, the rule $s_n = s_{n-1} + s_{n-2}$.

Non-example: the ring $\Z/4\Z$ is not a field.
There the step $C(x) - d b^{-1} x^m B(x)$ breaks down as soon as $b = 2$, because $2$ has no inverse.
So the procedure above is not defined over $\Z/4\Z$.

Massey's analysis also shows that if $2L \le N$ for the output $L$, then the shortest generating register is unique.
