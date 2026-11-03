---
tag: HVK6T8FEPZ
kind: proof
name: Proof of the epsilon-N definition of the limit of a sequence
msc: [40A05]
proves: 09G6KHS6GY
uses: [0XKWSSY8P2, 00S7C68D51]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Real numbers
---

## Proof

We prove the two implications separately.

1. For real numbers $x$, $L$ and $\varepsilon > 0$, we have $|x - L| < \varepsilon$ if and only if $L - \varepsilon < x < L + \varepsilon$. This follows from the definition of the [[absolute value|00S7C68D51]].
2. Assume first that $(a_n)$ converges to $L$ in the sense of the [[limit of a sequence|0XKWSSY8P2]]. Let $\varepsilon > 0$.
3. The set $U = (L - \varepsilon, L + \varepsilon)$ is an open interval, and it contains $L$.
4. By the definition of the limit, there is a natural number $N$ with $a_n \in U$ for all $n \ge N$.
5. By step 1, this means $|a_n - L| < \varepsilon$ for all $n \ge N$. So the condition of the statement holds.
6. Conversely, assume the condition of the statement. Let $U$ be an open interval that contains $L$.
7. If $U$ has a left endpoint $c$, then $c < L$, so $L - c > 0$. If $U$ has a right endpoint $d$, then $L < d$, so $d - L > 0$.
8. Let $\varepsilon$ be the minimum of $1$ and of those numbers $L - c$ and $d - L$ that exist. Then $\varepsilon > 0$.
9. Let $x$ satisfy $L - \varepsilon < x < L + \varepsilon$. Then $c \le L - \varepsilon < x$ when $c$ exists, and $x < L + \varepsilon \le d$ when $d$ exists. So $x \in U$.
10. By the condition, there is a natural number $N$ with $|a_n - L| < \varepsilon$ for all $n \ge N$.
11. By steps 1 and 9, $a_n \in U$ for all $n \ge N$.
12. The open interval $U$ that contains $L$ was arbitrary. So $(a_n)$ converges to $L$, and the equivalence is proved.

## Idea

The intervals $(L - \varepsilon, L + \varepsilon)$ are special open intervals around $L$. Conversely, each open interval around $L$ contains one of them. So "eventually inside every open interval around $L$" and "eventually within $\varepsilon$ of $L$ for every $\varepsilon$" say the same thing.
