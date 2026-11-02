---
tag: EFYGR426DF
kind: statement
role: proposition
name: Differences of polynomials vanish beyond the degree
msc: [39A70, 39A12]
uses: [E38801KVJ1, 0Q9EZS90GY, 0DPF6WRZW6]
about: [3039GWNHWS]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Statement

Let $R$ be a commutative ring, let $h \in R$, and let $p \in R[x]$ be a [[polynomial|0Q9EZS90GY]].
Let $n \in \N$ with $\deg p < n$, where the [[degree|0DPF6WRZW6]] of the zero polynomial is $-\infty$.
Then the [[$n$-th forward difference|E38801KVJ1]] of the polynomial function $x \mapsto p(x)$ on $R$ with step $h$ is zero:
$$\Delta_h^n p(x) = 0 \quad \text{for all } x \in R.$$

## Remarks

The key step is that $\Delta_h$ lowers the degree: for $m \ge 1$, $(x + h)^m - x^m = \sum_{j<m} \binom{m}{j} h^{m-j} x^j$ has degree less than $m$, and $\Delta_h$ sends constants to $0$.
Induction on $n$ then gives the claim.
The same computation shows more: if $p$ has degree $d$ and leading coefficient $a$, then $\Delta_h^d p$ is the constant $d!\, a\, h^d$.
Example: for $p(x) = x^3$ and $h = 1$, the third differences of $0, 1, 8, 27, 64$ are all $6 = 3!$, and the fourth differences are $0$.
Over $\R$ there is a converse: a function $f \colon \Z \to \R$ with $\Delta^n f = 0$ agrees on $\Z$ with a polynomial of degree less than $n$.

## Explanations

### L1 human

Write the values of a polynomial at equally spaced points and take differences again and again.
For a polynomial of degree $d$, the $d$-th row is constant and every later row is zero.
This is the discrete form of the fact that the $(d+1)$-th derivative of a polynomial of degree $d$ is zero.

### L2 human

The fact gives a practical test: if a table of values has constant $d$-th differences, the data fit a polynomial of degree $d$.
With the [[expansion of iterated differences in shifts|24D1EGHP4G]] it yields identities such as $\sum_{k=0}^{n} (-1)^k \binom{n}{k} k^m = 0$ for $0 \le m < n$.
Combined with [[Newton's forward difference formula|DDHCMKHD2T]], it shows that a polynomial of degree $d$ is determined by its values at $d + 1$ equally spaced points.
It is then given by a finite [[Newton series|Y2HXSEA2EE]].
