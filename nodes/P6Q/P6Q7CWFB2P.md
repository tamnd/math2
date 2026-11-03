---
tag: P6Q7CWFB2P
kind: proof
name: Proof that exponentials dominate powers in sequences, by the ratio of consecutive terms
msc: [26A12]
proves: 0MVTCFW42K
uses: [09G6KHS6GY, 08QAX4H1PF, 0RAM4E07NR, 0734RSVF2V, 0TZK91NQE3, 09AZCV6GMC, 0ASJVEFA9J]
sources:
  - url: https://www.jirka.org/ra/html/sec_factslimsseqs.html
    locator: Lemma 2.2.12
---

## Proof

We compare consecutive terms and then use [[induction|0ASJVEFA9J]].

1. For each integer $n \ge 1$, let $x_n = n^k / r^n$. Since $r > 1$, we have $r^n > 0$, so $x_n > 0$.
2. By the example [[1/n tends to zero|08QAX4H1PF]], $1/n \to 0$. The constant sequence $1$ tends to $1$. By the [[limit of a sum|0RAM4E07NR]], $1 + 1/n \to 1$.
3. We show $(1 + 1/n)^j \to 1$ for each natural number $j$, by induction on $j$. For $j = 0$ the sequence is the constant $1$.
4. If $(1 + 1/n)^j \to 1$, then $(1 + 1/n)^{j+1} = (1 + 1/n)^j (1 + 1/n) \to 1 \cdot 1 = 1$, by the [[limit of a product|0734RSVF2V]] and step 2. In particular $(1 + 1/n)^k \to 1$.
5. Let $q = (1 + r)/2$. Then $1 < q < r$.
6. Apply the [[epsilon-N definition|09G6KHS6GY]] to step 4 with $\varepsilon = q - 1 > 0$. There is an integer $N \ge 1$ with $(1 + 1/n)^k < q$ for all $n \ge N$.
7. For $n \ge 1$,
$$\frac{x_{n+1}}{x_n} = \frac{(n+1)^k}{n^k} \cdot \frac{r^n}{r^{n+1}} = \frac{(1 + 1/n)^k}{r}.$$
8. Let $c = q/r$. Then $0 < c < 1$. By steps 6 and 7, $x_{n+1} < c\, x_n$ for all $n \ge N$.
9. By induction on $n$, step 8 gives $x_n \le x_N c^{n - N}$ for all $n \ge N$. Write $C = x_N c^{-N}$, so $x_n \le C c^n$ for $n \ge N$, and $C > 0$.
10. Since $1/c > 1$, [[the sequence (1/c)^n tends to infinity|0TZK91NQE3]], in the sense of a [[sequence tending to infinity|09AZCV6GMC]].
11. Let $\varepsilon > 0$. By step 10 with the bound $C/\varepsilon$, there is $N'$ with $(1/c)^n > C/\varepsilon$ for all $n \ge N'$. For these $n$, $C c^n < \varepsilon$.
12. For $n \ge \max(N, N')$, steps 1, 9 and 11 give $0 < x_n \le C c^n < \varepsilon$. So $|x_n - 0| < \varepsilon$.
13. By the epsilon-N definition, $n^k / r^n \to 0$.

## Idea

Going from $n$ to $n + 1$ multiplies $n^k$ by $(1 + 1/n)^k$, which tends to $1$. It multiplies $r^n$ by the fixed number $r > 1$. So from some point on, each step shrinks the quotient by a fixed factor $c < 1$, and it decays like the geometric sequence $c^n$.
