---
tag: YP4WMTVCPP
kind: proof
name: Proof that continuity is equivalent to sequential continuity in metric spaces
msc: ["54E35"]
proves: 0VGPKZ8MRK
uses: [063W5JMY85, 0SY9ECQ19Q, 0YF82GBTND, 06JYPJ4WHH, 0A3GWZ86AY]
sources:
  - url: https://proofwiki.org/wiki/Sequential_Continuity_is_Equivalent_to_Continuity_in_Metric_Space
---

## Proof

We prove the forward direction directly and the converse by contraposition.

1. Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$.
2. By definition, $f$ is [[continuous|0SY9ECQ19Q]] when $f^{-1}(V)$ is open in $X$ for each open $V$ of $Y$.
3. By [[continuity via open sets|0YF82GBTND]], $f$ is continuous if and only if condition (C) holds. (C): for each $a \in X$ and $\varepsilon > 0$ there is $\delta > 0$ such that $d_X(x, a) < \delta$ implies $d_Y(f(x), f(a)) < \varepsilon$.
4. Suppose $f$ is continuous. Let $(x_n)$ be a sequence that [[converges|06JYPJ4WHH]] to $x \in X$, and let $\varepsilon > 0$.
5. By (C) at $a = x$, there is $\delta > 0$ such that $d_X(z, x) < \delta$ implies $d_Y(f(z), f(x)) < \varepsilon$.
6. Since $x_n \to x$, there is an integer $N$ with $d_X(x_n, x) < \delta$ for all $n \ge N$.
7. By step 5, $d_Y(f(x_n), f(x)) < \varepsilon$ for all $n \ge N$. Hence $f(x_n) \to f(x)$.
8. Conversely, suppose $f$ is not continuous. By step 3, (C) fails at some $a \in X$.
9. So there is $\varepsilon > 0$ such that each $\delta > 0$ has some $x \in X$ with $d_X(x, a) < \delta$ and $d_Y(f(x), f(a)) \ge \varepsilon$.
10. For each integer $n \ge 1$, apply step 9 with $\delta = 1/n$. This gives $x_n \in X$ with $d_X(x_n, a) < 1/n$ and $d_Y(f(x_n), f(a)) \ge \varepsilon$.
11. We show $x_n \to a$. Let $\eta > 0$. The [[reals are Archimedean|0A3GWZ86AY]], so some natural number $N$ has $N \eta > 1$. Then $N \ge 1$.
12. For $n \ge N$, we get $d_X(x_n, a) < 1/n \le 1/N < \eta$. So $x_n \to a$.
13. But $d_Y(f(x_n), f(a)) \ge \varepsilon$ for every $n$. So no $N$ makes $d_Y(f(x_n), f(a)) < \varepsilon$ for all $n \ge N$, and $f(x_n) \not\to f(a)$.
14. So if $f(x_n) \to f(x)$ for every convergent sequence $x_n \to x$, then $f$ is continuous.

## Idea

Continuity in a metric space is the epsilon-delta condition. A convergent sequence eventually enters the $\delta$-ball, so its image eventually enters the $\varepsilon$-ball. If continuity fails at a point, the radii $1/n$ pick out bad points that converge to it while their images stay away.
