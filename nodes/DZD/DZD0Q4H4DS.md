---
tag: DZD0Q4H4DS
kind: definition
name: Newton series
msc: [39A70, 41A58]
defines: Y2HXSEA2EE
uses: [E38801KVJ1, 0JH4MN4K1C]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Definition

Let $f \colon \C \to \C$ be a function and let $a \in \C$.
For $k \in \N$ let $\Delta^k f(a)$ be the [[$k$-th forward difference|E38801KVJ1]] of $f$ at $a$ with step $1$.
For $s \in \C$ let $\binom{s}{k} = \frac{s(s-1)\cdots(s-k+1)}{k!}$, with $\binom{s}{0} = 1$.
The *Newton series* of $f$ at $a$ is the [[series|0JH4MN4K1C]]
$$\sum_{k=0}^{\infty} \binom{x - a}{k} \Delta^k f(a),$$
viewed as a series of functions of $x \in \C$.

## Remarks

Example: for $f(x) = 2^x$ and $a = 0$, $\Delta^k f(0) = 1$ for all $k$, so the Newton series is $\sum_k \binom{x}{k}$.
This is the binomial series of $(1 + z)^x$ at $z = 1$, which converges to $2^x$ for real $x > -1$.
Non-example: $\sum_k \frac{x^k}{k!}$ is the Taylor series of $e^x$ at $0$, not its Newton series.
The Newton series of $e^x$ at $0$ has coefficients $\Delta^k e^x |_{x=0} = (e - 1)^k$, and since $e - 1 > 1$ it diverges at every real $x$ that is not a natural number.
At $x = a + n$ with $n \in \N$, only the terms with $k \le n$ are nonzero, and the sum is $f(a + n)$ by [[Newton's forward difference formula|DDHCMKHD2T]].
