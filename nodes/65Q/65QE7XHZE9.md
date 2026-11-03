---
tag: 65QE7XHZE9
kind: proof
name: Proof that convergent sequences are Cauchy
msc: [40A05]
proves: 0QY87R9CY3
uses: [0AZ3R52593, 0QZMTN5AXX, 09G6KHS6GY, 03HF5PMY5T]
sources:
  - url: https://www.jirka.org/ra/html/sec_cauchy.html
    locator: Theorem 2.4.5
---

## Proof

1. Since $(a_n)$ is a [[convergent sequence|0AZ3R52593]], it converges to some real number $L$.
2. Let $\varepsilon > 0$. By the [[epsilon-N definition|09G6KHS6GY]], there is $N$ with $|a_n - L| < \varepsilon/2$ for all $n \ge N$.
3. Let $m, n \ge N$. By the [[triangle inequality|03HF5PMY5T]],
$$|a_m - a_n| \le |a_m - L| + |L - a_n| < \frac{\varepsilon}{2} + \frac{\varepsilon}{2} = \varepsilon.$$
4. So $(a_n)$ is a [[Cauchy sequence|0QZMTN5AXX]].

## Idea

If all late terms are close to $L$, then any two late terms are close to each other. The triangle inequality makes this exact, with half of $\varepsilon$ for each distance to $L$.
