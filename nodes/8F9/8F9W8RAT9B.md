---
tag: 8F9W8RAT9B
kind: proof
name: Proof of the derivative as a little-o approximation
msc: [26B05]
proves: 0MN882VJ4P
uses: [08EVNYZF42, 00A0RPAQ8A]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.3.5
---

## Proof

We unfold the definition of the limit in both directions.

1. Let $V$, $W$, $U$, $f$, $x$ and $A$ be as in the statement, with $V$ and $W$ [[normed vector spaces|00A0RPAQ8A]]. For $h \in V$ with $x + h \in U$, put $r(h) = f(x + h) - f(x) - A h$.
2. Then $f(x + h) = f(x) + A h + r(h)$ for each such $h$, and $r(0) = f(x) - f(x) - A 0 = 0$.
3. By the definition of the [[Fréchet derivative|08EVNYZF42]], $A$ is the derivative of $f$ at $x$ exactly when $\|r(h)\| / \|h\| \to 0$ as $h \to 0$. The limit is over $h \ne 0$ with $x + h \in U$.
4. Suppose first that $A$ is the derivative. Let $\varepsilon > 0$. By step 3 there is $\delta > 0$ with $\|r(h)\| / \|h\| < \varepsilon$ for $0 < \|h\| < \delta$ and $x + h \in U$.
5. For these $h$, multiplying by $\|h\| > 0$ gives $\|r(h)\| \le \varepsilon \|h\|$.
6. For $h = 0$, step 2 gives $\|r(0)\| = 0 = \varepsilon \|0\|$. So $\|r(h)\| \le \varepsilon \|h\|$ for each $h$ with $\|h\| < \delta$ and $x + h \in U$. Thus $r(h) = o(\|h\|)$.
7. Conversely, suppose that $r(h) = o(\|h\|)$. Let $\varepsilon > 0$. Apply the little-o condition to $\varepsilon / 2$. This gives $\delta > 0$ with $\|r(h)\| \le (\varepsilon / 2) \|h\|$ for $\|h\| < \delta$ and $x + h \in U$.
8. For $0 < \|h\| < \delta$ with $x + h \in U$, divide by $\|h\|$. This gives $\|r(h)\| / \|h\| \le \varepsilon / 2 < \varepsilon$.
9. So $\|r(h)\| / \|h\| \to 0$ as $h \to 0$. By step 3, $A$ is the Fréchet derivative of $f$ at $x$.

## Idea

The two conditions say the same thing about the error $r(h)$. The limit form divides by $\|h\|$, and the little-o form multiplies back. The only extra point is $h = 0$, where the error is $0$, so the inequality holds there too.
