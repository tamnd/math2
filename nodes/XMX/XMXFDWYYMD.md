---
tag: XMXFDWYYMD
kind: statement
role: theorem
name: Bounded gaps between primes
msc: [11N05, 11N36]
uses: [01826KMG2H, 033RZ32T4Q, 5252P3NHT7, B3JMY54GJF]
about: [01826KMG2H, 0FER36N8SB]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_gap
---

## Statement

Let $p_n$ denote the $n$-th [[prime number|01826KMG2H]].
There is a constant $H$ such that $p_{n+1} - p_n \le H$ for infinitely many $n$.
Equivalently,
$$\liminf_{n \to \infty} \, (p_{n+1} - p_n) < \infty,$$
where $\liminf$ is the [[limit inferior|033RZ32T4Q]].

## Remarks

Yitang Zhang proved the statement in 2013 with $H = 7 \cdot 10^7$.
James Maynard, and independently Terence Tao, gave a simpler proof with $H = 600$, and the Polymath project lowered the bound to $H = 246$.
Maynard's method also shows that for every $m \ge 1$, $\liminf_{n \to \infty} (p_{n+m} - p_n) < \infty$.
The proof builds on the method of Goldston, Pintz and Yıldırım: a [[Selberg sieve|5252P3NHT7]] with multidimensional weights detects a tuple $n + h_1, \ldots, n + h_k$ that contains at least two primes.
The input on primes in arithmetic progressions is the [[Bombieri–Vinogradov theorem|B3JMY54GJF]] in Maynard's version and a strengthening of it for smooth moduli in Zhang's version.
The [[twin prime conjecture|0FER36N8SB]] is the claim that $H = 2$ works; it remains open.

## Explanations

### L1 human

The primes become rarer as numbers grow: on average the gap after $p$ is about $\log p$.
Still, this theorem says that the primes keep coming in close pairs forever: some fixed distance $H$ is reached again and again.
The twin prime conjecture predicts the smallest possible distance $H = 2$, as in $11, 13$ or $41, 43$; the best proven value is $246$.

### L2 human

The statement is the first unconditional step towards the twin prime conjecture.
Goldston, Pintz and Yıldırım had shown that bounded gaps would follow from a level of distribution of the primes greater than $1/2$, which is beyond the [[Bombieri–Vinogradov theorem|B3JMY54GJF]].
Zhang proved such a level for a restricted class of moduli; Maynard changed the sieve weights so that the level $1/2$ is already enough.
Under the Elliott–Halberstam conjecture and its generalisations, the method gives smaller values of $H$, down to $6$.
