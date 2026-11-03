---
tag: SYKKE9WBGB
kind: proof
name: Proof that a decreasing sequence bounded below converges
msc: [40A05]
proves: 02V2GYAC8P
uses: [0FM6N4R0VB, 0KN22AAW5R, 05FQ3VGAR9, 04KFTA34C5, 0BTMQ04556, 09G6KHS6GY]
sources:
  - url: https://en.wikipedia.org/wiki/Monotone_convergence_theorem
    locator: Convergence of a monotone sequence of real numbers
---

## Proof

We apply the monotone convergence theorem to the sequence $(-a_n)$.

1. For each $n$, let $b_n = -a_n$. Since $a_n \ge a_{n+1}$, we get $b_n \le b_{n+1}$. So $(b_n)$ is increasing, in the sense of a [[monotone sequence|0KN22AAW5R]].
2. Since $(a_n)$ is [[bounded below|05FQ3VGAR9]], there is $m$ with $a_n \ge m$ for all $n$. Then $b_n \le -m$ for all $n$, so $(b_n)$ is bounded above.
3. By the [[monotone convergence theorem|0FM6N4R0VB]], $(b_n)$ converges to $t = \sup \{b_n : n \in \mathbb{N}\}$.
4. We show that $-t$ is the [[infimum|04KFTA34C5]] of $A = \{a_n : n \in \mathbb{N}\}$. Since $t$ is an upper bound of the $b_n$, we get $-t \le a_n$ for all $n$. So $-t$ is a lower bound of $A$.
5. Let $\ell$ be a lower bound of $A$. Then $-\ell \ge b_n$ for all $n$, so $-\ell$ is an upper bound of the $b_n$. Since $t$ is their [[supremum|0BTMQ04556]], $t \le -\ell$, that is $\ell \le -t$.
6. By steps 4 and 5, $-t = \inf A$.
7. Let $\varepsilon > 0$. By step 3 and the [[epsilon-N definition|09G6KHS6GY]], there is $N$ with $|b_n - t| < \varepsilon$ for all $n \ge N$.
8. For these $n$, $|a_n - (-t)| = |-(b_n - t)| = |b_n - t| < \varepsilon$.
9. So $(a_n)$ converges, and its limit is $-t = \inf \{a_n : n \in \mathbb{N}\}$.

## Idea

Changing the sign turns a decreasing sequence into an increasing one, and a lower bound into an upper bound. It also turns the infimum into the supremum. So the increasing case gives the decreasing case at once.
