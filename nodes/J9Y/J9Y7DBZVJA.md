---
tag: J9Y7DBZVJA
kind: definition
name: Dilogarithm
msc: ["33B30", "11G55"]
defines: G0X0NWSDB7
uses: [96CHDZKGQ0, 02QGGD5G87]
sources:
  - url: https://en.wikipedia.org/wiki/Dilogarithm
---

## Definition

The *dilogarithm* is the function $\operatorname{Li}_2 \colon \C \setminus (1, \infty) \to \C$ given by
$$\operatorname{Li}_2(z) = -\int_0^z \frac{\log(1 - u)}{u}\, du.$$
Here $\log$ is the principal branch of the [[complex logarithm|02QGGD5G87]].
The path of integration lies in $\C \setminus [1, \infty)$, except possibly for its endpoint $z = 1$.
The function is holomorphic on $\C \setminus [1, \infty)$ and continuous at $z = 1$.

## Remarks

For $\abs{z} \le 1$ it agrees with the series $\sum_{k \ge 1} \frac{z^k}{k^2}$, so it is the [[polylogarithm|96CHDZKGQ0]] $\operatorname{Li}_2$.
The integral does not depend on the path, because $\C \setminus [1, \infty)$ is simply connected and the integrand is holomorphic there (the singularity at $u = 0$ is removable).

Example: $\operatorname{Li}_2(1) = \sum_{k \ge 1} k^{-2} = \frac{\pi^2}{6}$, and $\operatorname{Li}_2(-1) = \sum_{k \ge 1} \frac{(-1)^k}{k^2} = -\frac{\pi^2}{12}$.
Euler's reflection formula $\operatorname{Li}_2(z) + \operatorname{Li}_2(1 - z) = \frac{\pi^2}{6} - \log z \log(1 - z)$ at $z = \frac12$ gives $\operatorname{Li}_2(\frac12) = \frac{\pi^2}{12} - \frac{(\ln 2)^2}{2}$.

Non-example of a valid argument: for real $x > 1$ the point $x$ lies on the cut $[1, \infty)$.
The limits of $\operatorname{Li}_2$ from above and below the cut differ by $2\pi i \ln x$, so $\operatorname{Li}_2$ has no continuous extension there.
