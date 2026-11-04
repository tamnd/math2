---
tag: 1ND5X51YWH
kind: proof
name: Proof of the uniform limit theorem by an epsilon over three argument
msc: [40A30, 26A15]
proves: 0X9XT05JVC
uses: [08HJRTG5N7, 0EEE2CZB2A, 0W8YHHGCJG, 03HF5PMY5T]
sources:
  - url: https://www.jirka.org/ra/html/sec_liminter.html
    locator: Theorem 6.2.2
---

## Proof

We use an $\varepsilon/3$ argument with the epsilon-delta form of continuity.

1. Let $S \subseteq \R$, let each $f_n \colon S \to \R$ be continuous, and let $f_n \to f$ [[uniformly on $S$|08HJRTG5N7]].
2. Fix $c \in S$ and $\varepsilon > 0$. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], it suffices to find $\delta > 0$ with $|f(x) - f(c)| < \varepsilon$ for all $x \in S$ with $|x - c| < \delta$.
3. By uniform convergence, there is $N$ with $|f_n(y) - f(y)| < \frac{\varepsilon}{3}$ for all $n \ge N$ and all $y \in S$. In particular, this holds for $n = N$.
4. The function $f_N$ is [[continuous at|0EEE2CZB2A]] $c$. By the epsilon-delta form, there is $\delta > 0$ with $|f_N(x) - f_N(c)| < \frac{\varepsilon}{3}$ for all $x \in S$ with $|x - c| < \delta$.
5. Let $x \in S$ with $|x - c| < \delta$. By the [[triangle inequality|03HF5PMY5T]],
$$|f(x) - f(c)| \le |f(x) - f_N(x)| + |f_N(x) - f_N(c)| + |f_N(c) - f(c)|.$$
6. The first and third terms are less than $\frac{\varepsilon}{3}$ by step 3, with $y = x$ and $y = c$. The middle term is less than $\frac{\varepsilon}{3}$ by step 4.
7. So $|f(x) - f(c)| < \varepsilon$. By step 2, $f$ is continuous at $c$.
8. Since $c \in S$ was arbitrary, $f$ is continuous on $S$.

## Idea

Near $c$, the limit $f$ is within $\varepsilon/3$ of a single continuous function $f_N$, at every point at once. The function $f_N$ moves by less than $\varepsilon/3$ near $c$. Three small errors add up to less than $\varepsilon$. Uniformity is what lets one $N$ work at both $x$ and $c$.
