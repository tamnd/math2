---
tag: MNSSV4QHD1
kind: statement
role: theorem
name: Fundamental theorem of the calculus of finite differences
msc: [39A12, 39A70]
uses: [TXTR68V4R1, 5VK9NZM0R7]
about: [SMAQN2N739, FT9JQA58KJ]
sources:
  - url: https://en.wikipedia.org/wiki/Indefinite_sum
---

## Statement

Let $G$ be an additive abelian group, let $F \colon \Z \to G$ be a function, and let $\Delta F(k) = F(k + 1) - F(k)$ be its [[forward difference|TXTR68V4R1]].
Then for all integers $a \le b$,
$$\sum_{k=a}^{b-1} \Delta F(k) = F(b) - F(a).$$
Equivalently, if $F$ is an [[indefinite sum|5VK9NZM0R7]] of $f \colon \Z \to G$, then $\sum_{k=a}^{b-1} f(k) = F(b) - F(a)$.

## Remarks

The proof is a telescoping sum: $\sum_{k=a}^{b-1} (F(k+1) - F(k))$ cancels to $F(b) - F(a)$, as in a [[telescoping series|0GXKM1R7E4]].
For $a = b$ both sides are $0$.
Example: $\Delta (k)_3 = 3 (k)_2$ for the falling factorial $(k)_3 = k(k-1)(k-2)$, so $\sum_{k=0}^{n-1} k(k-1) = \frac{n(n-1)(n-2)}{3}$.
A related identity, with $\Delta$ of step $h$ on any additive commutative monoid, is $\sum_{k=0}^{n-1} f(x + kh) = \sum_{j=0}^{n-1} \binom{n}{j+1} \Delta_h^j f(x)$, obtained by summing [[Newton's forward difference formula|DDHCMKHD2T]].

## Explanations

### L1 human

Adding up all the steps of a function gives its total change.
This is the discrete version of $\int_a^b F'(x)\,dx = F(b) - F(a)$.
To sum $f(a) + \dots + f(b-1)$, it is enough to find one function $F$ whose steps are the values of $f$.

### L2 human

The theorem reduces the evaluation of finite sums to finding indefinite sums, just as the [[fundamental theorem of calculus|0NHGY0N0JB]] reduces integrals to antiderivatives.
A table of differences, such as $\Delta (k)_m = m (k)_{m-1}$ for [[falling factorials|0SJNCJCCQG]] and $\Delta c^k = (c - 1) c^k$, becomes a table of sums.
To sum $k^2$, write $k^2 = (k)_2 + (k)_1$, which gives $\sum_{k=0}^{n-1} k^2 = \frac{(n)_3}{3} + \frac{(n)_2}{2}$.
[[Summation by parts|9G82Z17DKA]] is the discrete analogue of integration by parts and is proved from the same telescoping.
