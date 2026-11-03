---
tag: TM7E68ZG4G
kind: proof
name: Proof of the monotone convergence theorem for sequences
msc: [40A05]
proves: 0FM6N4R0VB
uses: [0KN22AAW5R, 05FQ3VGAR9, 0AXWET80YW, 0BTMQ04556, 0M8TGGP9JP, 09G6KHS6GY, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Monotone_convergence_theorem
    locator: Convergence of a monotone sequence of real numbers
---

## Proof

1. Let $S = \{a_n : n \in \mathbb{N}\}$. The set $S$ is nonempty, since it contains $a_0$.
2. The sequence is [[bounded above|05FQ3VGAR9]], so $S$ is bounded above. By the [[completeness axiom|0AXWET80YW]], $S$ has a [[supremum|0BTMQ04556]] $s$.
3. Since $s$ is an upper bound of $S$, we have $a_n \le s$ for all $n$.
4. The sequence is increasing in the sense of a [[monotone sequence|0KN22AAW5R]]: $a_n \le a_{n+1}$ for all $n$. By [[induction|0ASJVEFA9J]] on $n$, this gives $a_m \le a_n$ for all $m \le n$.
5. Let $\varepsilon > 0$. Then $s - \varepsilon < s$.
6. By the [[approximation property of the supremum|0M8TGGP9JP]], there is an element of $S$ greater than $s - \varepsilon$. So there is $N$ with $a_N > s - \varepsilon$.
7. For $n \ge N$, steps 3, 4 and 6 give $s - \varepsilon < a_N \le a_n \le s$.
8. So $|a_n - s| < \varepsilon$ for all $n \ge N$.
9. By the [[epsilon-N definition|09G6KHS6GY]], $(a_n)$ converges, and its limit is $s = \sup \{a_n : n \in \mathbb{N}\}$.

## Idea

The completeness of $\mathbb{R}$ gives a candidate for the limit, the supremum $s$. Just below $s$ there is some term, since $s$ is the least upper bound. Every later term is at least as large and still at most $s$, so it is trapped close to $s$.
