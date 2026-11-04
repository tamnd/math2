---
tag: 4NTFQV870Y
kind: proof
name: Proof of Riesz's lemma
msc: [46B20]
proves: 097C7KCAT5
uses: [0G5AV9Q4RR, 0D2W7FS52T, 068P0P32DW, 0EPTJA5QV4]
sources:
  - url: https://en.wikipedia.org/wiki/Riesz%27s_lemma
    locator: Proof
---

## Proof

We take a point outside $Y$, move it by a nearly closest point of $Y$, and normalise.

1. Since $Y \neq X$, choose $x_0 \in X$ with $x_0 \notin Y$. Let $r = \inf_{y \in Y} \|x_0 - y\|$. This is a real number $r \ge 0$, since $Y$ contains $0$ and the norms are nonnegative.
2. $r > 0$. If $r = 0$, then for each $\varepsilon > 0$ there is $y \in Y$ with $\|x_0 - y\| < \varepsilon$. So $x_0$ is in the closure of $Y$, by [[closure in a metric space|068P0P32DW]].
3. As $Y$ is [[closed|0G5AV9Q4RR]], it equals its closure, by [[this result|0D2W7FS52T]]. So $x_0 \in Y$, a contradiction.
4. Since $0 < \alpha < 1$ and $r > 0$, we have $r / \alpha > r$. So $r / \alpha$ is not a lower bound of the distances, and there is $y_0 \in Y$ with $\|x_0 - y_0\| < r / \alpha$.
5. Let $d = \|x_0 - y_0\|$. Then $d \ge r > 0$. Let $x = (x_0 - y_0) / d$. Then $\|x\| = 1$.
6. Let $y \in Y$. Then $x - y = (x_0 - y_1) / d$, where $y_1 = y_0 + d \, y$.
7. As $Y$ is a [[linear subspace|0EPTJA5QV4]], $y_1 \in Y$. So $\|x_0 - y_1\| \ge r$, by the definition of $r$.
8. Hence $\|x - y\| = \|x_0 - y_1\| / d \ge r / d > r / (r / \alpha) = \alpha$.
9. So $\|x\| = 1$ and $\|x - y\| \ge \alpha$ for all $y \in Y$.

## Idea

A point outside a closed subspace has a positive distance $r$ from it. We pick a point of $Y$ almost as close as possible, within the factor $1/\alpha$, and normalise the difference. The new vector has distance $r/d$ from $Y$, and this ratio is above $\alpha$ because $d$ is almost $r$.
