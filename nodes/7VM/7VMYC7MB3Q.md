---
tag: 7VMYC7MB3Q
kind: statement
role: theorem
name: Bisection method
msc: [65H05]
uses: [TR4CNS5PMJ, 0X3WGX95FE, 00KAFBR32E, MF56GK7QY2]
about: [TR4CNS5PMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bisection_method
same_as:
  wikidata: Q866300
  wikipedia: Bisection method
---

## Statement

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a [[continuous function|0X3WGX95FE]] with $f(a) f(b) < 0$.
The *bisection method* sets $a_0 = a$ and $b_0 = b$.
For $k \ge 0$ it lets $m_k = (a_k + b_k)/2$ and proceeds as follows.
If $f(m_k) = 0$ it stops with the zero $m_k$; if $f(a_k) f(m_k) < 0$ it sets $(a_{k+1}, b_{k+1}) = (a_k, m_k)$; otherwise it sets $(a_{k+1}, b_{k+1}) = (m_k, b_k)$.
If the method does not stop, then for every $k \ge 0$:

1. $f(a_k) f(b_k) < 0$, so $[a_k, b_k]$ contains a zero of $f$;
2. $b_k - a_k = (b - a)/2^k$;
3. the sequences $(a_k)$, $(b_k)$ and $(m_k)$ converge to the same zero $r$ of $f$, and $\abs{m_k - r} \le (b - a)/2^{k+1}$.

## Remarks

Clause 1 holds by induction, since the new interval keeps an endpoint where $f$ is negative and one where it is positive.
The [[intermediate value theorem|00KAFBR32E]] then gives a zero in it.
Clause 2 is immediate, and the [[nested intervals theorem|MF56GK7QY2]] gives a common limit $r$ of $a_k$ and $b_k$; by continuity $f(r)^2 = \lim f(a_k) f(b_k) \le 0$, so $f(r) = 0$.
Example: for $f(x) = x^2 - 2$ on $[1, 2]$, the midpoints are $1.5, 1.25, 1.375, 1.4375, \ldots$, and $20$ steps locate $\sqrt{2}$ within $2^{-21} < 5 \times 10^{-7}$.
Continuity is needed: $f(x) = 1/x$ for $x \ne 0$ and $f(0) = 1$ changes sign on $[-1, 1]$, and bisection gives $[-1, 0], [-1/2, 0], \ldots$ and converges to $0$, which is not a zero.
The error bound halves at each step, so the method converges linearly with ratio $1/2$ in the sense of the error bound, whatever $f$ is.

## Explanations

### L1 human

If a continuous function is negative at one end of an interval and positive at the other, it must cross zero somewhere in between.
Check the middle: the sign there tells which half still has a crossing.
Keep halving.
After $k$ steps the zero is trapped in an interval $2^k$ times shorter than at the start.

### L2 human

Bisection is the simplest [[root-finding algorithm|TR4CNS5PMJ]] and the most robust: it needs only continuity and a sign change, and its error bound is known in advance.
It gains one binary digit per step, so it is slow compared with [[Newton's method|07EXVNF9VP]] or the [[secant method|9ZC177PVPC]].
Practical methods such as [[Brent's method|5F76XA1ABC]] combine a fast open method with bisection steps to keep the guarantee.
It is also the constructive content of the intermediate value theorem.
