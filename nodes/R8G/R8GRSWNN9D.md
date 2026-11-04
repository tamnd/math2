---
tag: R8GRSWNN9D
kind: proof
name: Proof of Grönwall's inequality
msc: [26D10, 34A40]
proves: 07EJHQYR9A
uses: [063H5KJC69, 0EX9GFJ0B3, 0RXX2PT1MQ, 0V9A43H7WV, 0P9BNBW2W3, 026BJBQNGJ]
sources:
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: Differential form; Integral form for continuous functions
---

## Proof

We multiply by an integrating factor and show that the product is non-increasing.

1. Let $B(t) = \int_a^t \beta(s)\, ds$ for $t \in I$. Since $\beta$ is continuous, $B$ is continuous on $I$ and $B'(t) = \beta(t)$ for $t \in I^\circ$, by the [[first fundamental theorem of calculus|063H5KJC69]].
2. By the [[chain rule|0RXX2PT1MQ]] and [[the derivative of the exponential|0EX9GFJ0B3]], $t \mapsto e^{-B(t)}$ is differentiable on $I^\circ$ with derivative $-\beta(t) e^{-B(t)}$. Also $e^{-B(t)} > 0$, because [[the exponential function is positive|0P9BNBW2W3]].

Differential form.

3. Let $v(t) = u(t)\, e^{-B(t)}$ for $t \in I$. Then $v$ is continuous on $I$.
4. By the [[product rule|0V9A43H7WV]] and step 2, for $t \in I^\circ$ we have $v'(t) = \left( u'(t) - \beta(t) u(t) \right) e^{-B(t)}$.
5. The hypothesis gives $u'(t) - \beta(t) u(t) \le 0$, and $e^{-B(t)} > 0$. So $v'(t) \le 0$ on $I^\circ$.
6. Then $-v$ has a non-negative derivative on $I^\circ$, so $-v$ is [[increasing|026BJBQNGJ]] on $I$. Hence $v(t) \le v(a) = u(a)$ for each $t \in I$, since $B(a) = 0$.
7. Multiplying by $e^{B(t)} > 0$ gives $u(t) \le u(a)\, e^{B(t)}$, which is the differential form.

Integral form.

8. Fix $t \in I$. If $t = a$, the hypothesis gives $u(a) \le \alpha(a) = \alpha(a) e^{B(a)}$. So let $t > a$, and put $c = \alpha(t)$.
9. For $s \in [a, t]$ we have $\alpha(s) \le c$, because $\alpha$ is non-decreasing. So $u(s) \le c + S(s)$, where $S(s) = \int_a^s \beta(r) u(r)\, dr$.
10. The function $S$ is continuous on $[a, t]$, and $S'(s) = \beta(s) u(s)$ for $s \in (a, t)$, by the first fundamental theorem of calculus.
11. Since $\beta(s) \ge 0$, step 9 gives $\beta(s) u(s) \le c\, \beta(s) + \beta(s) S(s)$ for $s \in [a, t]$.
12. Let $q(s) = e^{-B(s)} \left( S(s) + c \right)$ for $s \in [a, t]$. By the product rule and step 2, $q'(s) = e^{-B(s)} \left( \beta(s) u(s) - \beta(s) S(s) - c\, \beta(s) \right)$ on $(a, t)$.
13. By step 11 the bracket in step 12 is at most $0$, so $q'(s) \le 0$ on $(a, t)$. As in step 6, $q(t) \le q(a) = c$, since $S(a) = 0$ and $B(a) = 0$.
14. Multiplying $q(t) \le c$ by $e^{B(t)} > 0$ gives $S(t) + c \le c\, e^{B(t)}$.
15. By step 9 with $s = t$, $u(t) \le c + S(t) \le c\, e^{B(t)} = \alpha(t) \exp\left( \int_a^t \beta(s)\, ds \right)$. This is the integral form.

## Idea

The function $e^{B}$ with $B' = \beta$ solves $v' = \beta v$. Dividing $u$ by it turns the growth condition into the statement that a function has a non-positive derivative, so it can only decrease. In the integral form the same trick is applied to the integral term $S$, after the monotone $\alpha$ is frozen at its value at $t$.
