---
tag: QDJ2XA38WH
kind: proof
name: Proof of the sequence characterisation of uniform continuity
msc: ["54E40"]
proves: 0FHSDCQACY
uses: [063W5JMY85, 06JYPJ4WHH, 0A3GWZ86AY]
sources:
  - url: https://sam.nitk.ac.in/courses/Monthly%20Seminar/2020/uniform%20continuity.pdf
    locator: Theorem 11
---

## Proof

We prove each implication. The second one is proved by contraposition.

1. Let $(X, d_X)$ and $(Y, d_Y)$ be [[metric spaces|063W5JMY85]] and let $f \colon X \to Y$ be a function.
2. Assume condition 1. Let $(x_n)$ and $(y_n)$ be sequences in $X$ with $d_X(x_n, y_n) \to 0$. Let $\varepsilon > 0$ be real.
3. By condition 1, there is $\delta > 0$ with $d_Y(f(x), f(y)) < \varepsilon$ whenever $d_X(x, y) < \delta$.
4. Since $d_X(x_n, y_n) \to 0$ in $\R$, there is an integer $N$ with $d_X(x_n, y_n) < \delta$ for all $n \ge N$.
5. By steps 3 and 4, $d_Y(f(x_n), f(y_n)) < \varepsilon$ for all $n \ge N$.
6. Since $\varepsilon$ was arbitrary, $d_Y(f(x_n), f(y_n)) \to 0$ in the sense of [[convergence|06JYPJ4WHH]] in $\R$. So condition 2 holds.
7. Now assume that condition 1 fails. Then there is a real $\varepsilon > 0$ with the following property.
8. For each real $\delta > 0$ there are $x, y \in X$ with $d_X(x, y) < \delta$ and $d_Y(f(x), f(y)) \ge \varepsilon$.
9. For each integer $n \ge 1$, apply step 8 with $\delta = 1/n$. This gives points $x_n, y_n \in X$ with $d_X(x_n, y_n) < 1/n$ and $d_Y(f(x_n), f(y_n)) \ge \varepsilon$.
10. Let $\eta > 0$. Since [[the reals are Archimedean|0A3GWZ86AY]], there is an integer $N > 1/\eta$. For $n \ge N$ we get $d_X(x_n, y_n) < 1/n \le 1/N < \eta$. So $d_X(x_n, y_n) \to 0$.
11. But $d_Y(f(x_n), f(y_n)) \ge \varepsilon$ for every $n$, so this sequence does not tend to $0$.
12. By steps 10 and 11, condition 2 fails. So condition 2 implies condition 1.
13. By steps 2 to 6 and step 12, the two conditions are equivalent.

## Idea

If one $\delta$ works everywhere, then pairs of points that get close are eventually within $\delta$, and their images get close.
If no $\delta$ works, take $\delta = 1/n$ for each $n$ and collect the bad pairs: they form two sequences that come together while their images stay apart.
