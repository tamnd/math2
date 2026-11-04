---
tag: PAQC17KXRG
kind: proof
name: Proof that differentiable functions are continuous
msc: [26A24]
proves: 07ZMX4ANJS
uses: [0A61B60B5R, 0F1WR9C83K, 0GBZDAFPX8, 0W8YHHGCJG, 0EEE2CZB2A, 03HF5PMY5T]
sources:
  - url: https://proofwiki.org/wiki/Differentiable_Function_is_Continuous
---

## Proof

1. Since $f$ is [[differentiable|0A61B60B5R]] at $a$, it has a [[derivative|0F1WR9C83K]] $L = f'(a)$. For $h \ne 0$ with $a + h \in I$, write $q(h) = \frac{f(a + h) - f(a)}{h}$. Then $q(h) \to L$ as $h \to 0$.
2. By the [[epsilon-delta form of limits|0GBZDAFPX8]] with $\varepsilon = 1$, there is $\delta_1 > 0$ with $\abs{q(h) - L} < 1$ whenever $0 < \abs{h} < \delta_1$ and $a + h \in I$.
3. For such $h$, the [[triangle inequality|03HF5PMY5T]] gives $\abs{q(h)} \le \abs{q(h) - L} + \abs{L} < \abs{L} + 1$.
4. So $\abs{f(a + h) - f(a)} = \abs{q(h)} \, \abs{h} \le (\abs{L} + 1) \abs{h}$ for these $h$. This also holds for $h = 0$, where both sides are $0$.
5. Let $\varepsilon > 0$. Put $\delta = \min\left(\delta_1, \frac{\varepsilon}{\abs{L} + 1}\right) > 0$.
6. Let $x \in I$ with $\abs{x - a} < \delta$, and put $h = x - a$. By step 4, $\abs{f(x) - f(a)} \le (\abs{L} + 1) \abs{h} < (\abs{L} + 1) \cdot \frac{\varepsilon}{\abs{L} + 1} = \varepsilon$.
7. By the [[epsilon-delta form of continuity|0W8YHHGCJG]], $f$ is [[continuous at|0EEE2CZB2A]] $a$.

## Idea

Near $a$, the difference quotient stays close to $f'(a)$, so it is bounded. Then $f(x) - f(a)$ is a bounded number times $x - a$. This product is small when $x$ is close to $a$.
