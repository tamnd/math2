---
tag: 8WH2SKSAZD
kind: example
name: A rate of metastability for monotone bounded sequences
msc: ["03F10", "03F60", "40A05"]
topics: [8XY7JYZKFW]
audience: research
instance_of: [XR1JXQG1CD]
uses: [XR1JXQG1CD, 4BCD1EM542, 0FM6N4R0VB, YWZQC5E54B]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_mining
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Monotone_convergence_theorem
    locator: lead section
---

## Example

Let $(a_n)$ be a nonincreasing sequence of real numbers in $[0, 1]$.
The [[monotone convergence theorem|0FM6N4R0VB]] says that $(a_n)$ converges, and we extract from its proof a rate of metastability, as in [[proof mining|XR1JXQG1CD]].
For $g : \mathbb{N} \to \mathbb{N}$ let $\tilde g(n) = n + g(n)$, and for $\varepsilon > 0$ let $K = \lceil 1 / \varepsilon \rceil$.

**Claim.** For every $\varepsilon > 0$ and every $g$, some $n \le \tilde g^{(K)}(0)$ has $\lvert a_i - a_j \rvert \le \varepsilon$ for all $i, j \in [n, n + g(n)]$.

We check the claim in six steps.

1. Let $n_0 = 0$ and $n_{k+1} = \tilde g(n_k)$.
   Then $n_0 \le n_1 \le \cdots$, since $g(n) \ge 0$, and $n_k = \tilde g^{(k)}(0)$.
2. The window of $n_k$ is $[n_k, n_k + g(n_k)] = [n_k, n_{k+1}]$.
   The sequence is nonincreasing there, so $\lvert a_i - a_j \rvert \le a_{n_k} - a_{n_{k+1}}$ for $i, j$ in the window.
3. Suppose that the claim fails for each of $n_0, \dots, n_{K-1}$.
   Then each of these windows has a pair more than $\varepsilon$ apart, so $a_{n_k} - a_{n_{k+1}} > \varepsilon$ for each $k < K$, by step 2.
4. Add these $K$ inequalities.
   The sum telescopes:
   $$a_{n_0} - a_{n_K} = \sum_{k < K} (a_{n_k} - a_{n_{k+1}}) > K \varepsilon \ge 1.$$
5. But $a_{n_0} \le 1$ and $a_{n_K} \ge 0$, so $a_{n_0} - a_{n_K} \le 1$.
   This contradicts step 4.
6. So some $n_k$ with $k < K$ satisfies the claim, and $n_k \le n_K = \tilde g^{(K)}(0)$.

So $\Phi(\varepsilon, g) = \tilde g^{(K)}(0)$ is a rate of metastability for every nonincreasing sequence in $[0, 1]$.

## Remarks

The main feature is uniformity: $\Phi$ depends only on $\varepsilon$ and $g$, not on the sequence.
The argument is a finite form of the classical proof, with the [[no-counterexample interpretation|4BCD1EM542]] of the Cauchy property in place of the Cauchy property itself.
A [[rate of convergence|YWZQC5E54B]] cannot be uniform in this way: the sequence that is $1$ up to index $N$ and $0$ after it needs a rate at least $N$ for $\varepsilon = \tfrac{1}{2}$.
For a single computable sequence a computable rate of convergence need not exist at all, by the [[Specker sequence|P9W51PW5HK]].

The parameters change the rate in a simple way.
For sequences in $[0, b]$ the total fall is at most $b$, so $K = \lceil b / \varepsilon \rceil$ windows are needed.
For nondecreasing sequences the same argument works with $a_{n_{k+1}} - a_{n_k}$ in place of $a_{n_k} - a_{n_{k+1}}$.
For $g(n) = 0$ every window has one point and the claim says nothing, so the content grows with $g$.

## Explanations

### L1 human

A decreasing sequence in $[0, 1]$ converges, but no formula says when it gets close to its limit.
Metastability asks a weaker question.
Given a rule $g$ for the size of a window, find a starting point $n$ where the sequence stays within $\varepsilon$ from $n$ to $n + g(n)$.
Jump from window to window, and note that each window where the sequence moves more than $\varepsilon$ uses up $\varepsilon$ of a total drop of at most $1$.
So after at most $1 / \varepsilon$ windows a quiet window must appear.

### L2 human

We compute the rate for $\varepsilon = \tfrac{1}{2}$ and $g(n) = n + 1$.
Then $K = 2$ and $\tilde g(n) = 2n + 1$, so the window starts are
$$n_0 = 0, \qquad n_1 = 1, \qquad n_2 = 3.$$
The claim gives some $n \in \{0, 1\}$ with $\lvert a_i - a_j \rvert \le \tfrac{1}{2}$ on $[n, 2n + 1]$, and $\Phi = 3$.

Try the sequence $1, 0.4, 0.3, 0.3, \dots$.
On $[0, 1]$ the drop is $0.6$, so $n = 0$ fails, and on $[1, 3]$ the drop is $0.4 - 0.3 = 0.1$, so $n = 1$ works.
Check: the two drops add to $0.7 \le 1$, as step 5 requires.
The typical use is as the model case for metastability results in fixed point and ergodic theory.
Watch out: the window rule $g$ is part of the input, so the claim is not a rate of convergence.
