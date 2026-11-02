---
tag: VJNTCDZS2H
kind: statement
role: theorem
name: Littlewood's L1 norm conjecture
msc: [42A05, 26D05]
uses: [J3NJQ5FZJ5, SASP14MA1Z]
about: [J3NJQ5FZJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Littlewood_conjecture
---

## Statement

There is an absolute constant $c > 0$ with the following property.
Let $N \ge 1$ and let $n_1 < n_2 < \cdots < n_N$ be distinct integers.
Then the [[trigonometric polynomial|J3NJQ5FZJ5]] $f(x) = \sum_{k=1}^{N} e^{i n_k x}$ satisfies
$$\frac{1}{2\pi} \int_{-\pi}^{\pi} \abs{f(x)} \, dx \ge c \log N.$$

## Remarks

Littlewood conjectured this bound, and it was proved in 1981, independently by McGehee, Pigno and Smith and by Konyagin.
McGehee, Pigno and Smith proved more: for all complex $a_1, \ldots, a_N$,
$$\frac{1}{2\pi} \int_{-\pi}^{\pi} \Big\lvert \sum_{k=1}^{N} a_k e^{i n_k x} \Big\rvert \, dx \ge c \sum_{k=1}^{N} \frac{\abs{a_k}}{k}.$$
Taking all $a_k = 1$ gives the conjecture, because $\sum_{k=1}^{N} 1/k \ge \log N$.
Their proof constructs, by duality, a bounded function whose pairing with $f$ is large.

The order $\log N$ is sharp.
For $n_k = k$ one has $\abs{f(x)} = \abs{\sin(Nx/2) / \sin(x/2)}$, the absolute value of a Dirichlet-type kernel, and its $L^1$ norm grows like $\frac{4}{\pi^2} \log N$, as for the [[Lebesgue constants|RWKQ5EP4YF]].

## Explanations

### L1 human

Add $N$ pure waves of size one with different whole-number frequencies.
At $x = 0$ they all line up and the sum has size $N$, but at most points they partly cancel.
The theorem says that the cancellation can never be too strong on average: the average size of the sum is at least a constant times $\log N$.

### L2 human

In the $L^2$ norm the answer is exact: the norm is $\sqrt N$ by Parseval's identity, whatever the frequencies.
The $L^1$ norm is much harder because no orthogonality is available.
The McGehee–Pigno–Smith inequality is a version of Hardy's inequality for functions whose Fourier coefficients are supported on an arbitrary set of integers.
Before the full solution, P. J. Cohen proved a lower bound tending to infinity with $N$, as part of his work on idempotent measures.
