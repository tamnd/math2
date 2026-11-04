---
tag: 7EDZQY5MV9
kind: proof
name: Proof that the continued fraction of a real number is finite exactly when the number is rational
msc: [11A55]
proves: 0PMY0YQYXX
uses: [0SJ7Z6VKWK, 0YVRNEDSVG, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_continued_fraction
    locator: Finite continued fractions
---

## Proof

We use the notation $x_n$, $a_n$ of the [[continued fraction expansion|0SJ7Z6VKWK]] of $x$: $x_0 = x$, $a_n = \floor{x_n}$, and $x_{n+1} = 1/(x_n - a_n)$ when $x_n \ne a_n$.

1. Suppose the expansion is finite. Then the process stops at some $n$, so $x_n = a_n$ is an integer.
2. For $k < n$, the process did not stop at $k$, so $x_{k+1} = 1/(x_k - a_k)$. Solving gives $x_k = a_k + 1/x_{k+1}$.
3. If $x_{k+1}$ is rational, then so is $x_k = a_k + 1/x_{k+1}$, since $a_k$ is an integer.
4. By step 1 and step 3, applied for $k = n-1, n-2, \dots, 0$ in turn, each $x_k$ is rational. In particular $x = x_0$ is rational.
5. Conversely, let $x = r/s$ with integers $r$ and $s$, $s > 0$. We show that the process stops.
6. Claim: if the process has not stopped before step $k$, then $x_k = r_k / s_k$ with integers $r_k$ and $s_k$, and $1 \le s_k \le s - k$.
7. For $k = 0$, take $r_0 = r$ and $s_0 = s$.
8. Suppose the claim holds for $k$, and the process does not stop at $k$, so $x_k \ne a_k$. Since $a_k$ is the [[floor|0YVRNEDSVG]] of $x_k$, we have $0 < x_k - a_k < 1$.
9. Put $t_k = r_k - a_k s_k$, an integer. Then $x_k - a_k = t_k / s_k$, so $0 < t_k < s_k$ by step 8.
10. Then $x_{k+1} = 1/(x_k - a_k) = s_k / t_k$. Put $r_{k+1} = s_k$ and $s_{k+1} = t_k$. We get $1 \le s_{k+1} \le s_k - 1 \le s - (k+1)$. This proves the claim by [[induction|0ASJVEFA9J]] on $k$.
11. If the process had not stopped before step $s$, the claim would give $1 \le s_s \le 0$, which is impossible. So the process stops at some $k < s$, and the expansion of $x$ is finite.
12. So the expansion of $x$ is finite if and only if $x$ is rational.

## Idea

For a fraction $r/s$, each step of the algorithm replaces the denominator by a smaller positive integer, exactly as in the Euclidean algorithm.
A decreasing sequence of positive integers must stop.
Conversely, a finite expansion can be folded back from its last term, and each step keeps the number rational.
