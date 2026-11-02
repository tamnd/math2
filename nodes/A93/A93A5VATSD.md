---
tag: A93A5VATSD
kind: statement
role: theorem
name: Heine's transformation
msc: [33D15]
uses: [EB4N9RQR51, Y1X8ZZQ7VM, VVT27RB46B]
about: [EB4N9RQR51]
sources:
  - url: https://en.wikipedia.org/wiki/Basic_hypergeometric_series
---

## Statement

Let $a, b, c, q, z \in \C$ with $0 < \abs{q} < 1$, $\abs{z} < 1$, $0 < \abs{b} < 1$, and with $c$ and $az$ not of the form $q^{-m}$ for an integer $m \ge 0$.
Then
$${}_2\phi_1 \left( \begin{matrix} a, b \\ c \end{matrix} ; q, z \right) = \frac{(b; q)_\infty\, (az; q)_\infty}{(c; q)_\infty\, (z; q)_\infty}\; {}_2\phi_1 \left( \begin{matrix} c/b, z \\ az \end{matrix} ; q, b \right),$$
where ${}_2\phi_1$ is the [[basic hypergeometric series|EB4N9RQR51]] and $(\cdot\,; q)_\infty$ is the [[q-Pochhammer symbol|Y1X8ZZQ7VM]].

## Remarks

Proof idea: write $\frac{(b; q)_n}{(c; q)_n} = \frac{(b; q)_\infty}{(c; q)_\infty} \cdot \frac{(c q^n; q)_\infty}{(b q^n; q)_\infty}$.
Expand $\frac{(c q^n; q)_\infty}{(b q^n; q)_\infty}$ by the [[q-binomial theorem|VVT27RB46B]] as a series in $b q^n$, exchange the two sums, and sum over $n$ with the $q$-binomial theorem again.
Example: for $c = b$ the left side is ${}_1\phi_0(a; -; q, z) = \frac{(az; q)_\infty}{(z; q)_\infty}$, and on the right ${}_2\phi_1(1, z; az; q, b) = 1$ since $(1; q)_n = 0$ for $n \ge 1$; both sides agree.
Iterating the transformation gives two more forms, and the three are often called Heine's first, second and third transformations.
The third form is ${}_2\phi_1(a, b; c; q, z) = \frac{(abz/c; q)_\infty}{(z; q)_\infty}\, {}_2\phi_1(c/a, c/b; c; q, abz/c)$, valid when both series converge.

## Explanations

### L1 human

Heine's transformation rewrites one basic hypergeometric series as an infinite product times another basic hypergeometric series with permuted parameters.
The roles of the variable $z$ and the parameter $b$ are exchanged.
Such a change can turn a slowly converging series into a fast one, or a hard sum into an easy one.

### L2 human

It is the first and most used transformation of the ${}_2\phi_1$ series, and its third form is the $q$-analogue of Euler's transformation of the [[hypergeometric series|428M453CR2]] ${}_2F_1$.
Setting $z = c/(ab)$ and summing the right side with the $q$-binomial theorem gives the $q$-Gauss sum ${}_2\phi_1(a, b; c; q, c/(ab)) = \frac{(c/a, c/b; q)_\infty}{(c, c/(ab); q)_\infty}$ for $\abs{c/(ab)} < 1$.
Its terminating case leads to the [[q-Vandermonde identity|MBRSCQRGGH]].
