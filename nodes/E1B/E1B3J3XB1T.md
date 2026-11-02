---
tag: E1B3J3XB1T
kind: definition
name: Recurrent point
msc: [37B20]
defines: 4SQHHRPKMV
uses: [0VKD1TP7F3, 0VGFHTM75Y, YF4XH2BEG5, 0AA97XA70K, CRGZZKQ7Z9]
sources:
  - url: https://en.wikipedia.org/wiki/Recurrent_point
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $f \colon X \to X$ be a [[continuous map|0VGFHTM75Y]].
A point $x \in X$ is *recurrent* for $f$ if there is a strictly increasing sequence of positive integers $n_1 < n_2 < \cdots$ such that $f^{n_k}(x) \to x$ as $k \to \infty$.

## Remarks

Equivalent form: $x$ is recurrent if and only if $x \in \omega(x)$, where $\omega(x)$ is the $\omega$-[[limit set|YF4XH2BEG5]] of $x$, the set of limits of sequences $f^{n_k}(x)$ with $n_k \to \infty$.
The same condition $x \in \omega(x)$ defines recurrence on a general topological space.
Every point on a [[periodic orbit|0AA97XA70K]] is recurrent: if $f^p(x) = x$, take $n_k = kp$.
Every point of a [[minimal set|CRGZZKQ7Z9]] is recurrent.
Example: for $f(x) = x + \alpha \bmod 1$ on the circle with $\alpha$ irrational, Dirichlet's approximation theorem gives infinitely many $n$ with $n\alpha$ within $1/n$ of an integer, so $f^{n}(x) \to x$ along these $n$.
Non-example: for $f(x) = x/2$ on $\R$, the point $x = 1$ has $f^n(1) = 2^{-n} \to 0$, so no subsequence tends to $1$.

## Explanations

### L1 human

A recurrent point is a point that its own orbit approaches again and again.
