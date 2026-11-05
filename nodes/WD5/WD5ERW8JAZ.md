---
tag: WD5ERW8JAZ
kind: statement
role: theorem
name: Roth's theorem with popular differences
sources:
  - wikipedia: en:62455443@r1365048018
    locator: Roth's theorem on arithmetic progressions, section Extensions and generalizations > Roth's theorem with popular differences
    note: adopted
    mention: wikipedia://en/62455443#9Z64
    sections: [Statement]
inventory: [BBMK5P21GX]
---

## Statement

Another generalization of Roth's theorem shows that for positive density subsets, there not only exists a 3-term arithmetic progression, but that there exist many 3-APs all with the same common difference.

> **Roth's theorem with popular differences:** For all $\epsilon > 0$, there exists some $n_0 = n_0(\epsilon)$ such that for every $n > n_0$ and $A \subset \mathbb{F}_3^n$ with $|A| = \alpha3^n,$ there exists some $y \neq 0$ such that $|\{x : x, x + y, x + 2y \in A\}| \ge (\alpha^3 - \epsilon)3^n.$

If $A$ is chosen randomly from $\mathbb{F}_3^n,$ then we would expect there to be $\alpha^33^n$ progressions for each value of $y$. The popular differences theorem thus states that for each $|A|$ with positive density, there is some $y$ such that the number of 3-APs with common difference $y$ is close to what we would expect.

This theorem was first proven by Green in 2005, who gave a bound of $n_0 = \text{tow}((1/\epsilon)^{O(1)}),$ where $\text{tow}$ is the tower function. In 2019, Fox and Pham recently improved the bound to $n_0 = \text{tow}(O(\log\frac{1}{\epsilon})).$

A corresponding statement is also true in $\mathbb{Z}$ for both 3-APs and 4-APs. However, the claim has been shown to be false for 5-APs.
