---
tag: NY1PHJHKN9
kind: proof
name: Proof that the derivative gives the directional derivatives
msc: [26B05]
proves: 0A6PMR20N4
uses: [0135XZZQ8M, 05EGFBZTGC, 01ZQQDCERP, 0DC3MPR7C9]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.3.9
---

## Proof

We put $h = t v$ in the definition of the derivative.

1. Let $U$, $f$ and $a$ be as in the statement, let $L = Df(a)$, and let $v \in \mathbb{R}^n$.
2. If $v = 0$, then $(f(a + t v) - f(a)) / t = 0 = L v$ for each $t \ne 0$. So the limit is $L v$. From now on, suppose that $v \ne 0$.
3. Since $U$ is [[open|01ZQQDCERP]], there is $\rho > 0$ such that the [[open ball|0DC3MPR7C9]] $B(a, \rho)$ lies in $U$. So $a + t v \in U$ when $|t| < \rho / \|v\|$.
4. Let $\varepsilon > 0$. Since $f$ is [[differentiable|0135XZZQ8M]] at $a$, there is $\delta > 0$ with $\|f(a + h) - f(a) - L h\| < \varepsilon \|h\|$. This holds for $0 < \|h\| < \delta$ with $a + h \in U$.
5. Let $0 < |t| < \min(\delta, \rho) / \|v\|$ and put $h = t v$. Then $a + h \in U$ by step 3, and $0 < \|h\| = |t| \|v\| < \delta$.
6. Since $L$ is linear, $L h = t L v$. So by step 4,
$$\left\| \frac{f(a + t v) - f(a)}{t} - L v \right\| = \frac{\|f(a + h) - f(a) - L h\|}{|t|} < \frac{\varepsilon |t| \|v\|}{|t|} = \varepsilon \|v\|.$$
7. As $\varepsilon > 0$ was arbitrary, the difference quotient tends to $L v$ as $t \to 0$.
8. So $f$ [[has the directional derivative|05EGFBZTGC]] $Df(a)(v)$ at $a$ in the direction $v$.

## Idea

Moving along the line $a + t v$ is a special way of letting $h$ tend to $0$. The derivative controls the error for all small $h$, so in particular for $h = t v$. Dividing by $t$ turns the linear term $L(t v)$ into the constant $L v$.
