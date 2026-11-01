---
tag: Y00AZRQE13
kind: definition
name: Hardy space
msc: [30H10]
defines: PNNNFJVF6W
uses: [0NAHXR1FRH, 8G5ABXRK85, 0D6KXBHKC0]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy_space
---

## Definition

Let $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$ be the [[unit disc|8G5ABXRK85]] and let $0 < p < \infty$.
The *Hardy space* $H^p$ is the set of [[holomorphic functions|0NAHXR1FRH]] $f \colon \mathbb{D} \to \C$ such that
$$\norm{f}_{H^p} = \sup_{0 < r < 1} \left( \frac{1}{2\pi}\int_0^{2\pi} \abs{f(r e^{i\theta})}^p \, d\theta \right)^{1/p} < \infty.$$
The space $H^\infty$ is the set of bounded holomorphic functions on $\mathbb{D}$, with $\norm{f}_{H^\infty} = \sup_{z \in \mathbb{D}} \abs{f(z)}$.

## Remarks

The integral means increase with $r$, because $\abs{f}^p$ is [[subharmonic|Z1MHMGFNFW]], so the supremum is a limit as $r \to 1$.
For $f(z) = \sum_{n \ge 0} a_n z^n$, a [[power series|0D6KXBHKC0]] on $\mathbb{D}$, Parseval's identity gives $\frac{1}{2\pi}\int_0^{2\pi} \abs{f(re^{i\theta})}^2 d\theta = \sum \abs{a_n}^2 r^{2n}$, so $\norm{f}_{H^2}^2 = \sum_{n \ge 0} \abs{a_n}^2$.
Example: $f(z) = \log(1 - z) = -\sum_{n \ge 1} z^n/n$ has $\sum 1/n^2 < \infty$, so $f \in H^2$.
Non-example: $g(z) = 1/(1 - z) = \sum_{n \ge 0} z^n$ has all coefficients $1$, so $g \notin H^2$; in fact $g \in H^p$ exactly for $p < 1$.
For $1 \le p \le \infty$, $H^p$ is a [[Banach space|06GZ956657]]; for $0 < p < 1$ it is a complete metric space but not a normed space.
There are also Hardy spaces of the upper half-plane and of domains in $\C^n$ and $\R^n$.
