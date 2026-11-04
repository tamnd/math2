---
tag: RKQWD3FMKV
kind: proof
name: Proof that a continuous real function on a compact set attains its bounds
msc: [54C30]
proves: 0V4DET59NW
uses: [0K9AAJ8G51, 07PFYV65MB, 0E1MMCAY5B, 0P953MG05E, 0AXWET80YW, 0EDH403M21, 0BTMQ04556, 04KFTA34C5, 0G5AV9Q4RR, 0A6YRNZB2R]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_value_theorem
    locator: Generalization to metric and topological spaces
---

## Proof

We show that the image $f(K)$ contains its supremum and its infimum.

1. Let $S = f(K) \subseteq \R$. Since $K$ is nonempty, $S$ is nonempty.
2. The [[continuous image of a compact set is compact|0K9AAJ8G51]]. So $S$ is compact in $\R$.
3. Give $\R$ the [[Euclidean metric|0E1MMCAY5B]] $d(s, t) = \abs{s - t}$. By the [[Heine–Borel theorem|07PFYV65MB]] with $n = 1$, the set $S$ is [[closed|0G5AV9Q4RR]] and [[bounded|0P953MG05E]].
4. By step 3 there is a real $M$ with $\abs{s - t} \le M$ for all $s, t \in S$. Fix $t_0 \in S$. Then $t_0 - M \le s \le t_0 + M$ for each $s \in S$.
5. So $S$ is bounded above and below. By the [[completeness axiom|0AXWET80YW]], $S$ has a [[supremum|0BTMQ04556]] $\beta$. By the [[existence of the infimum|0EDH403M21]], $S$ has an [[infimum|04KFTA34C5]] $\alpha$.
6. Suppose $\beta \notin S$. Then $\beta$ lies in $\R \setminus S$, which is open because $S$ is closed.
7. By the definition of the [[metric topology|0A6YRNZB2R]], there is $\varepsilon > 0$ with $(\beta - \varepsilon, \beta + \varepsilon) \cap S = \varnothing$.
8. Let $s \in S$. Then $s \le \beta$, and $s \notin (\beta - \varepsilon, \beta]$ by step 7. So $s \le \beta - \varepsilon$.
9. Thus $\beta - \varepsilon$ is an upper bound of $S$ that is smaller than $\beta$. This contradicts the definition of the supremum. Hence $\beta \in S$.
10. In the same way, suppose $\alpha \notin S$. Then some $\varepsilon > 0$ gives $(\alpha - \varepsilon, \alpha + \varepsilon) \cap S = \varnothing$.
11. Each $s \in S$ has $s \ge \alpha$ and $s \notin [\alpha, \alpha + \varepsilon)$, so $s \ge \alpha + \varepsilon$. Then $\alpha + \varepsilon$ is a lower bound larger than $\alpha$, a contradiction. Hence $\alpha \in S$.
12. By steps 9 and 11, there are $a, b \in K$ with $f(a) = \alpha$ and $f(b) = \beta$.
13. For each $x \in K$, $f(x) \in S$, so $\alpha \le f(x) \le \beta$. That is, $f(a) \le f(x) \le f(b)$ for all $x \in K$.

## Idea

Compactness passes from $K$ to the image $f(K)$, and a compact subset of $\R$ is closed and bounded. A bounded set has a supremum and an infimum. Because the set is closed, these two numbers cannot sit outside it, so they are values of $f$.
