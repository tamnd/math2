---
tag: M4RE41HFMG
kind: proof
name: Proof that limits preserve non-strict inequalities
msc: [40A05]
proves: 0N32V0E3XJ
uses: [09G6KHS6GY, 00S7C68D51, 0J0XBKG64S]
sources:
  - url: https://www.jirka.org/ra/html/sec_factslimsseqs.html
    locator: Lemma 2.2.3
---

## Proof

We argue [[by contradiction|0J0XBKG64S]].

1. Assume that $a > b$. Let $\varepsilon = (a - b)/2$. Then $\varepsilon > 0$.
2. By the [[epsilon-N definition|09G6KHS6GY]], there is $N_1$ with $|a_n - a| < \varepsilon$ for all $n \ge N_1$.
3. In the same way, there is $N_2$ with $|b_n - b| < \varepsilon$ for all $n \ge N_2$.
4. Let $n = \max(N, N_1, N_2)$. By the definition of the [[absolute value|00S7C68D51]], step 2 gives $a_n > a - \varepsilon$, and step 3 gives $b_n < b + \varepsilon$.
5. We have $a - \varepsilon = (a + b)/2 = b + \varepsilon$. So $b_n < (a + b)/2 < a_n$.
6. This contradicts the hypothesis $a_n \le b_n$, which holds because $n \ge N$.
7. Hence $a \le b$.

## Idea

If $a > b$, the midpoint $(a + b)/2$ separates them. For large $n$ the term $a_n$ lies above the midpoint and $b_n$ lies below it. This breaks the inequality $a_n \le b_n$.
