---
tag: CHCZB472JH
kind: proof
name: Proof of the limit of a product of sequences
msc: [40A05]
proves: 0734RSVF2V
uses: [09G6KHS6GY, 0S4JF619V7, 03HF5PMY5T, 0GMV7GP8W0]
sources:
  - url: https://www.jirka.org/ra/html/sec_factslimsseqs.html
    locator: Proposition 2.2.5
---

## Proof

1. Since $(a_n)$ converges, it is bounded, because [[convergent sequences are bounded|0S4JF619V7]]. So there is $K \ge 0$ with $|a_n| \le K$ for all $n$.
2. For each $n$ we have the identity $a_n b_n - a b = a_n (b_n - b) + b (a_n - a)$. To check it, expand the right side: $a_n b_n - a_n b + b a_n - a b$.
3. By the [[triangle inequality|03HF5PMY5T]] and since the [[absolute value is multiplicative|0GMV7GP8W0]],
$$|a_n b_n - a b| \le |a_n|\,|b_n - b| + |b|\,|a_n - a| \le K |b_n - b| + |b|\,|a_n - a|.$$
4. Let $\varepsilon > 0$. The numbers $K + 1$ and $|b| + 1$ are positive.
5. By the [[epsilon-N definition|09G6KHS6GY]], there is $N_1$ with $|b_n - b| < \varepsilon / (2(K + 1))$ for all $n \ge N_1$.
6. In the same way, there is $N_2$ with $|a_n - a| < \varepsilon / (2(|b| + 1))$ for all $n \ge N_2$.
7. Let $N = \max(N_1, N_2)$ and $n \ge N$. By steps 3, 5 and 6,
$$|a_n b_n - a b| \le \frac{K \varepsilon}{2(K + 1)} + \frac{|b| \varepsilon}{2(|b| + 1)} < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
The last step holds because $K/(K + 1) < 1$ and $|b|/(|b| + 1) < 1$.
8. So $a_n b_n \to a b$ by the epsilon-N definition.

## Idea

We split the error $a_n b_n - ab$ into two pieces, and each piece contains one small factor. The other factor stays bounded, because a convergent sequence is bounded. The constants $K + 1$ and $|b| + 1$ avoid a division by zero.
