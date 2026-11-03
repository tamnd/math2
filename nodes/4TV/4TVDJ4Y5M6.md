---
tag: 4TVDJ4Y5M6
kind: definition
name: Universal code
msc: [94A45, 94A29, 68P30]
defines: NZMKB1EXDG
uses: [GNB3T6TD0M, 0D6J4B671D, Y86E072V0V, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_code_(data_compression)
---

## Definition

Let $C \colon \N_{\ge 1} \to \set{0,1}^*$ be a binary [[prefix code|GNB3T6TD0M]] for the positive integers, and write $\ell(n) = \abs{C(n)}$.
For a [[probability mass function|0D6J4B671D]] $p$ on $\N_{\ge 1}$, let $\mathrm{H}(p) = -\sum_n p(n) \log_2 p(n)$ be its [[entropy|Y86E072V0V]] and $L_p = \sum_n p(n) \ell(n)$ the [[expected|0WQNRCNY3M]] length.
Call $p$ *monotone* if $p(n) \ge p(n+1)$ for all $n \ge 1$.
The code $C$ is *universal* if there is a constant $K$ such that
$$L_p \le K \max(1, \mathrm{H}(p))$$
for every monotone $p$ with $\mathrm{H}(p) < \infty$.

## Remarks

A universal code is *asymptotically optimal* if moreover $L_p / \mathrm{H}(p) \le R(\mathrm{H}(p))$ for a function $R$ with $R(t) \to 1$ as $t \to \infty$.
Example: the Elias gamma code writes $\floor{\log_2 n}$ zeros followed by the binary form of $n$, so $\ell(n) = 2\floor{\log_2 n} + 1$.
For monotone $p$ one has $n\,p(n) \le \sum_{i \le n} p(i) \le 1$, so $\log_2 n \le -\log_2 p(n)$.
Hence $L_p \le 2\mathrm{H}(p) + 1 \le 3 \max(1, \mathrm{H}(p))$, and the gamma code is universal.
Non-example: the unary code with $\ell(n) = n$ is not universal.
For $p(n) = c/n^2$, with $c$ the normalizing constant, the entropy is finite but $L_p = \sum_n c/n$ is infinite.
In a wider sense, "universal coding" also means compression that adapts to an unknown source, as Lempel–Ziv coding does.
