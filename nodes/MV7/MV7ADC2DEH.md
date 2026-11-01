---
tag: MV7ADC2DEH
kind: statement
role: theorem
name: McShane–Whitney extension
msc: [26B35, 54C20, "54E40"]
uses: [0AW1E6YTJY, 0VKD1TP7F3, 0QF1MZ9FRG, 0R3H5PANRQ]
about: [0AW1E6YTJY]
sources:
  - url: https://en.wikipedia.org/wiki/Lipschitz_continuity
---

## Statement

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]], let $A \subseteq X$ be nonempty, and let $L \ge 0$.
Let $f \colon A \to \R$ satisfy $\abs{f(a) - f(b)} \le L \, d(a, b)$ for all $a, b \in A$.
For $x \in X$ set
$$F(x) = \inf_{a \in A} \bigl( f(a) + L \, d(x, a) \bigr), \qquad G(x) = \sup_{a \in A} \bigl( f(a) - L \, d(x, a) \bigr).$$
Then:

1. $F$ and $G$ are real-valued, equal $f$ on $A$, and satisfy the [[Lipschitz condition|0AW1E6YTJY]] with constant $L$ on $X$.
2. Every function $h \colon X \to \R$ that equals $f$ on $A$ and is Lipschitz with constant $L$ satisfies $G \le h \le F$ on $X$.

## Remarks

Proof idea: fix $a_0 \in A$; for $a \in A$, $f(a) + L d(x, a) \ge f(a_0) - L d(a, a_0) + L d(x, a) \ge f(a_0) - L d(x, a_0)$, so the [[infimum|0QF1MZ9FRG]] is finite.
For $x \in A$ the same inequality with $a_0 = x$ shows $F(x) \ge f(x)$, and the choice $a = x$ gives $F(x) \le f(x)$.
Each function $x \mapsto f(a) + L d(x, a)$ is $L$-Lipschitz, and an infimum of $L$-Lipschitz functions that is finite is $L$-Lipschitz.
Example: on $X = \R$ with $A = \set{0, 1}$, $f(0) = 0$, $f(1) = 1$ and $L = 1$, both $F$ and $G$ equal $x$ on $[0, 1]$, while $F(x) = \abs{x}$ and $G(x) = x$ for $x \le 0$, and $F(x) = x$ and $G(x) = 1 - \abs{x - 1}$ for $x \ge 1$.
For maps into $\R^m$ with $m \ge 2$, the same constant needs the [[Kirszbraun theorem|2ZM39HSFTQ]].

## Explanations

### L1 human

A real function that is Lipschitz on part of a metric space extends to the whole space with the same Lipschitz constant.
The formula is explicit: take the lowest of the cones $f(a) + L d(x, a)$ that sit on the graph of $f$.
The highest of the downward cones $f(a) - L d(x, a)$ gives a second extension.
These two extensions are the largest and the smallest possible ones.

### L2 human

The result needs no structure on $X$ beyond the metric, unlike the vector-valued [[Kirszbraun theorem|2ZM39HSFTQ]].
It shows, for example, that every Lipschitz function on a closed set of $\R^n$ extends to $\R^n$, which is useful before applying [[Rademacher's theorem|QEY26RT19R]].