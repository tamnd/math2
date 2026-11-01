---
tag: 8VRTPECBPZ
kind: statement
role: theorem
name: Liouville's theorem (differential algebra)
msc: [12H05, 33F10]
uses: [GA5PTQGC6G, 3J89REV9WQ, 0EQWVHF3W5, 0BYWRWFT4F]
about: [GA5PTQGC6G, 0BYWRWFT4F]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville's_theorem_(differential_algebra)
same_as:
  wikidata: Q2404702
  wikipedia: Liouville's theorem (differential algebra)
---

## Statement

Let $(F, \partial)$ be a [[differential field|GA5PTQGC6G]] of characteristic $0$, with [[derivation|3J89REV9WQ]] $\partial$, and write $u' = \partial u$.
A differential [[field extension|0EQWVHF3W5]] $E = F(t_1, \dots, t_m)$ of $F$ is *elementary* if, for each $i$, with $F_{i-1} = F(t_1, \dots, t_{i-1})$, one of the following holds:

1. $t_i$ is algebraic over $F_{i-1}$;
2. $t_i' = u'/u$ for some nonzero $u \in F_{i-1}$ (a logarithm);
3. $t_i' = u' t_i$ for some $u \in F_{i-1}$ (an exponential).

Let $\alpha \in F$.
Suppose that some elementary extension $E$ of $F$ with the same field of constants as $F$ contains an element $y$ with $y' = \alpha$.
Then there are constants $c_1, \dots, c_n$ of $F$, nonzero elements $u_1, \dots, u_n \in F$, and an element $v \in F$ such that
$$\alpha = v' + \sum_{i=1}^{n} c_i \frac{u_i'}{u_i}.$$

## Remarks

The proof goes by induction on the length of the tower $F \subseteq F_1 \subseteq \cdots \subseteq E$.
At each step one writes the antiderivative in terms of the last generator $t_i$ and compares coefficients.
This works because derivatives of rational functions in a logarithm or an exponential have a controlled form.
An algebraic step is removed by taking traces, which is where the characteristic $0$ is used.

Example: over $F = \C(x)$ with $\partial = d/dx$, the element $\alpha = 1/x$ has the antiderivative $\log x$, and indeed $\alpha = c_1 u_1'/u_1$ with $c_1 = 1$, $u_1 = x$, $v = 0$.
The theorem is the tool that proves that $e^{-x^2}$, $e^x/x$ and $1/\log x$ have no [[antiderivative|0BYWRWFT4F]] built from elementary functions.

The hypothesis on the constants cannot be dropped.
Over $F = \R(x)$, the element $\alpha = 1/(1 + x^2)$ has the antiderivative $\arctan x = \frac{1}{2i} \log \frac{x - i}{x + i}$, which lies in an elementary extension that contains the new constant $i$.
But $\alpha$ has no expression of the form above with real constants and $u_i, v \in \R(x)$.

## Explanations

### L1 human

Some functions, such as $e^{-x^2}$, have no antiderivative that can be written with the usual functions: powers, roots, exponentials, logarithms and their combinations.
Liouville's theorem explains why.
If an elementary antiderivative exists, it must have a very special shape: a function from the same field plus a sum of constant multiples of logarithms of such functions.
One can then check that no function of this shape works.

### L2 human

The theorem turns the question "is this integral elementary?" into an algebraic question about the field $F$.
For $F = \C(x, e^{g})$ with $g$ a nonconstant polynomial, it reduces to a first-order linear differential equation over $\C(x)$.
This gives a classical criterion for rational $f$: the integral $\int f e^{g} \, dx$ is elementary exactly when $R' + g' R = f$ has a solution $R \in \C(x)$.
The [[Risch algorithm|VJ51B7J125]] makes this reduction systematic and decides elementary integrability in towers of logarithms, exponentials and algebraic functions.
The theorem is a basic result of differential algebra, alongside the theory of [[Picard–Vessiot extensions|TB53Y5NMJD]].
