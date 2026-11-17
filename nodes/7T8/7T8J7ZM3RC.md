---
tag: 7T8J7ZM3RC
kind: example
name: The superexponential function is not provably total in elementary function arithmetic
msc: ["03F30"]
topics: [QHCRN4JVG0]
audience: research
not_instance_of:
  - target: 2JD80TE553
    note: "The superexponential function is not a provably total function of EFA, because it grows faster than every elementary function."
uses: [2JD80TE553, RJ3MCAAZSV, NT65WHM5VV, 5NVA2JRHPV]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_function_arithmetic
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Tetration
    locator: lead section
---

## Example

Let $s(0) = 1$ and $s(x + 1) = 2^{s(x)}$, so $s(x)$ is a tower of $x$ twos, a case of [[tetration|NT65WHM5VV]].
We show that $s$ is not provably total in [[elementary function arithmetic|2JD80TE553]].
We cite two facts.
Fact A: every provably total function of $\mathsf{EFA}$ is [[elementary recursive|RJ3MCAAZSV]].
Fact B: for every elementary $f$ there is $k$ with $f(x) \le t_k(x)$ for all large $x$, where $t_0(x) = x$ and $t_{k+1}(x) = 2^{t_k(x)}$.

1. $s(m) \ge 2^m$ for all $m$, by induction: $s(0) = 1 = 2^0$, and $s(m + 1) = 2^{s(m)} \ge 2^{2^m} \ge 2^{m + 1}$.
2. $s(n) = t_k(s(n - k))$ for $n \ge k$, by $k$ uses of the recursion.
3. Let $n \ge 2k + 1$ and $m = n - k$, so $m \ge k + 1 \ge 1$. Then $s(m) \ge 2^m \ge 2m > m + k = n$, by step 1.
4. Each $t_k$ is strictly increasing. So $s(n) = t_k(s(m)) > t_k(n)$, by steps 2 and 3.
5. Step 4 holds for all $n \ge 2k + 1$, so no $k$ satisfies Fact B for $s$. So $s$ is not elementary.
6. By Fact A, $s$ is not provably total in $\mathsf{EFA}$.

So for every $\Sigma_1$ formula $\sigma(x, y)$ that defines the graph of $s$ in $\mathfrak{N}$, $\mathsf{EFA} \nvdash \forall x \, \exists y \, \sigma(x, y)$.

## Remarks

The function $s$ is [[primitive recursive|5NVA2JRHPV]], so $\mathsf{PRA}$ has a term for it and $\mathsf{I}\Sigma_1$ proves it total.
So $s$ separates $\mathsf{EFA}$ from $\mathsf{I}\Sigma_1$.
Each fixed tower $t_k$ is provably total in $\mathsf{EFA}$, by $k$ uses of the axiom $\mathsf{exp}$.
The failure is in the passage from "each $k$" to "all $x$": proving $\forall x \, \exists y \, (y = s(x))$ needs induction on a formula with an unbounded $\exists y$.
Each true instance $s(\overline{n}) = \overline{v}$ is still provable, even in $\mathsf{Q}$; only the uniform statement fails.

## Explanations

### L1 human

The superexponential function stacks powers of $2$: $s(1) = 2$, $s(2) = 2^2 = 4$, $s(3) = 2^4 = 16$, $s(4) = 2^{16} = 65536$.
Elementary function arithmetic can show that each fixed stack of powers, such as $2^{2^{2^x}}$, exists.
It cannot show that a stack of every height exists.
The reason is that $s$ grows faster than every function the theory can prove total.

### L2 human

We check step 3 for $k = 2$ and $n = 5$.

1. $m = n - k = 3$, and $s(3) = 16 \ge 2^3 = 8$.
2. $16 > 5 = n$.
3. $s(5) = 2^{2^{16}} = t_2(16)$, while $t_2(5) = 2^{32}$.
4. Since $16 > 5$, $t_2(16) > t_2(5)$, so $s(5) > t_2(5)$.

The typical use is as the standard witness that $\mathsf{EFA}$ is strictly weaker than $\mathsf{I}\Sigma_1$ and $\mathsf{PRA}$.
A trap is to confuse "the graph of $s$ is definable" with "$s$ is provably total": the graph has a $\Sigma_1$ definition, but totality is not provable.
