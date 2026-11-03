---
tag: 95CYGNRQQ6
kind: concept
name: q-ary entropy function
msc: [94A17, 94B65]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_(information_theory)
---

## Summary

The $q$-ary entropy function $H_q(x) = x \log_q (q - 1) - x \log_q x - (1 - x) \log_q (1 - x)$ generalizes the [[binary entropy function|GW25TGD33J]] to alphabets with $q$ symbols.
It is the [[Shannon entropy|Y86E072V0V]] in base $q$ of a random letter of a special kind.
This letter equals a fixed letter with probability $1 - x$, and otherwise it is uniform on the other $q - 1$ letters.
In coding theory it measures the volume of Hamming balls: a ball of radius $xn$ in $\set{0, \dots, q-1}^n$ has about $q^{n H_q(x)}$ points when $0 \le x \le 1 - 1/q$.
For this reason it appears in the [[Gilbert–Varshamov bound|1NYCGYDNTX]] and the [[Hamming bound|RZEGDKR7C7]].

## Explanations

### L1 human

Send one letter from an alphabet of $q$ letters through a noisy line.
With probability $1 - x$ it arrives intact, and otherwise it turns into one of the other $q - 1$ letters at random.
The $q$-ary entropy function measures, in units of one letter, how uncertain the received letter is.
For $q = 2$ it is the binary entropy function, and at $x = 1 - 1/q$ it reaches its maximum value $1$, which means the received letter is completely random.
