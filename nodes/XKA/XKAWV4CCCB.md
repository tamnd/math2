---
tag: XKAWV4CCCB
kind: definition
name: Szász–Mirakyan operator
msc: [41A36, 41A35, 41A25]
defines: GRQJ49XQNR
uses: [0XB9GQTN9G, AQDXWH4812]
sources:
  - url: https://en.wikipedia.org/wiki/Sz%C3%A1sz%E2%80%93Mirakyan_operator
---

## Definition

Let $f \colon [0, \infty) \to \R$ satisfy $\abs{f(t)} \le C e^{A t}$ for some constants $C, A \ge 0$ and all $t \ge 0$.
For an integer $n \ge 1$, the *Szász–Mirakyan operator* $S_n$ maps $f$ to the function
$$S_n(f)(x) = e^{-nx} \sum_{k=0}^{\infty} \frac{(nx)^k}{k!} \, f\left(\frac{k}{n}\right), \qquad x \ge 0.$$

## Remarks

The growth bound makes the series converge for all $x \ge 0$.
Each $S_n$ is a [[positive linear operator|AQDXWH4812]].
The weights $e^{-nx} (nx)^k / k!$ are the probabilities of the [[Poisson distribution|0XB9GQTN9G]] with mean $nx$.

Example: if $N$ is Poisson with mean $nx$, then $E[N] = nx$ and $E[N^2] = nx + n^2 x^2$.
So $S_n(1) = 1$, $S_n(t)(x) = x$ and $S_n(t^2)(x) = x^2 + x/n$.

Non-example: $f(t) = e^{t^2}$ is not in the domain, since $e^{k^2/n^2} (nx)^k / k!$ does not tend to $0$ as $k \to \infty$ when $x > 0$.

From the three moments and Korovkin's theorem, $S_n f \to f$ uniformly on each interval $[0, b]$ for every bounded continuous $f$.
