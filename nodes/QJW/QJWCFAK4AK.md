---
tag: QJWCFAK4AK
kind: statement
role: theorem
name: First main theorem of Nevanlinna theory
msc: ["30D35"]
uses: [0NSD1TPHR0, YT6Z0GWS0W, 1EHH63VNAD, 497K99BQ4Y]
about: [1EHH63VNAD, YT6Z0GWS0W]
sources:
  - url: https://en.wikipedia.org/wiki/Nevanlinna_theory
---

## Statement

Let $f$ be a [[meromorphic function|0NSD1TPHR0]] on $\C$ that is not constant, and let $a \in \C$.
For $r > 0$, let $m(r, a)$ and $N(r, a)$ be the proximity function and the counting function of $f$ at the value $a$, as in [[Nevanlinna theory|1EHH63VNAD]].
Let $T(r, f)$ be the [[Nevanlinna characteristic|YT6Z0GWS0W]] of $f$.
Then
$$m(r, a) + N(r, a) = T(r, f) + O(1) \qquad (r \to \infty),$$
where the bounded term depends on $f$ and $a$ but not on $r$.
More precisely, if $f(0) \ne a$ and $0$ is not a pole of $f$, then
$$\abs{\, m(r, a) + N(r, a) - T(r, f) + \log \abs{f(0) - a} \,} \le \log^+ \abs{a} + \log 2 \quad \text{for all } r > 0.$$

## Remarks

Apply [[Jensen's formula|497K99BQ4Y]] to $g = f - a$.
In Nevanlinna's notation it reads $T(r, g) - T(r, 1/g) = \log \abs{g(0)}$, and $T(r, 1/g) = m(r, a) + N(r, a)$.
The inequalities $\log^+ \abs{u - a} \le \log^+ \abs{u} + \log^+ \abs{a} + \log 2$ and its symmetric form show that $T(r, f - a)$ and $T(r, f)$ differ by at most $\log^+ \abs{a} + \log 2$.
For example, for $f(z) = e^z$ and $a = 0$ there are no solutions of $f(z) = 0$, so $N(r, 0) = 0$, and $m(r, 0) = r/\pi = T(r, f)$.

## Explanations

### L1 human

For each value $a$, the quantity $m(r, a) + N(r, a)$ measures how much $f$ is attracted to $a$ on the disc of radius $r$.
The counting part $N$ comes from the points where $f$ takes the value $a$.
The proximity part $m$ comes from the places on the circle where $f$ is very close to $a$.
The theorem says that the total is essentially the same for every value $a$, namely $T(r, f)$.

### L2 human

The first main theorem is a reformulation of Jensen's formula, and it is easy compared with the [[second main theorem|GWYE6745JK]].
It gives the upper bound $N(r, a) \le T(r, f) + O(1)$, which says that no value is taken too often.
It also justifies the definition of the defect $\delta(a) = 1 - \limsup_{r \to \infty} N(r, a)/T(r, f)$, which lies between $0$ and $1$.
The second main theorem gives the much deeper lower bound for most values.
