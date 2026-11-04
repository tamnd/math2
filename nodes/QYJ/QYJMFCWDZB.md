---
tag: QYJMFCWDZB
kind: proof
name: Proof of Taylor's theorem with the Peano remainder
msc: [41A58]
proves: 03AJHX431A
uses: [03QHBVW4TT, 0HFSFVMWQB, 04TSHB9H8D, 0TXTSEMHR5]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor%27s_theorem
    locator: Statement of the theorem
---

## Proof

We rewrite the conclusion of Taylor's theorem in little o notation.

1. Let $P_k(x) = \sum_{j=0}^{k} \frac{f^{(j)}(a)}{j!} (x - a)^j$, the [[Taylor polynomial|0HFSFVMWQB]] of degree $k$ of $f$ at $a$.
2. As in [[little o notation|04TSHB9H8D]], with $x \to a$ in place of $x \to \infty$, the claim means the following. For each $\varepsilon > 0$ there is $\delta > 0$ with $|f(x) - P_k(x)| \le \varepsilon |x - a|^k$ for all $x \in I$ with $|x - a| < \delta$.
3. By [[Taylor's theorem|03QHBVW4TT]], there is $h_k \colon I \to \R$ with $h_k(x) \to 0$ as $x \to a$ and $f(x) - P_k(x) = h_k(x)(x - a)^k$ for all $x \in I$.
4. Let $\varepsilon > 0$. By the definition of the [[limit|0TXTSEMHR5]] applied to $(-\varepsilon, \varepsilon)$, there is $\delta > 0$ with $|h_k(x)| < \varepsilon$ for $x \in I$ and $0 < |x - a| < \delta$.
5. For such $x$, $|f(x) - P_k(x)| = |h_k(x)| \, |x - a|^k \le \varepsilon |x - a|^k$.
6. For $x = a$, step 3 gives $f(a) - P_k(a) = 0$. So the inequality of step 2 holds at $a$ as well.
7. Hence $f(x) = P_k(x) + o\big((x - a)^k\big)$ as $x \to a$.

## Idea

Taylor's theorem already writes the error as $h_k(x)(x - a)^k$ with $h_k \to 0$. Saying that the error is $o((x - a)^k)$ is just another way to say that this factor $h_k$ tends to $0$.
