---
tag: VXV7M0QDH6
kind: concept
name: Epsilon over three argument
aliases: [epsilon-over-three-argument, epsilon-third-argument, three-epsilon-argument]
msc: ["00A35", "40A30"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: ug2
specializes: [0B94TKFQJX]
uses: [RXG5JTZ2PZ, 03HF5PMY5T, 08VZ57PT26, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_limit_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Uniform_convergence
    locator: lead section
---

## Summary

The epsilon over three argument controls a hard function through an easy function close to it, using three small steps instead of one large one.

Here is the pattern on a real goal: if [[continuous functions|0X3WGX95FE]] $f_n$ converge [[uniformly|08VZ57PT26]] to $f$ on $\mathbb{R}$, then $f$ is continuous.
Fix a point $c$ and $\varepsilon > 0$.
By uniform convergence, choose one index $N$ with $\lvert f_N(y) - f(y) \rvert < \varepsilon/3$ for every $y$.
Since $f_N$ is continuous at $c$, choose $\delta > 0$ with $\lvert f_N(x) - f_N(c) \rvert < \varepsilon/3$ whenever $\lvert x - c \rvert < \delta$.
For such $x$ the [[triangle inequality|03HF5PMY5T]] gives
$$\lvert f(x) - f(c) \rvert \le \lvert f(x) - f_N(x) \rvert + \lvert f_N(x) - f_N(c) \rvert + \lvert f_N(c) - f(c) \rvert < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon.$$

In general, the method bounds $\lvert f(x) - f(y) \rvert$ by walking from $f(x)$ to $g(x)$, then to $g(y)$, then to $f(y)$, where $g$ is the approximation.
The approximation is fixed first, and it must be good at every point the middle step uses.

## Motivation

A common question asks whether a limit of good functions is again good.
To show that $f$ is continuous at $c$, you must compare $f(x)$ with $f(c)$, but you know nothing about $f$ directly.
You know two other things: $f_N$ is close to $f$, and $f_N$ is continuous.
The triangle inequality uses both facts at once, with $f_N$ as a bridge from $f(x)$ to $f(c)$.

The bridge needs uniform convergence.
For [[x^n on [0, 1]|0YSRR1JTKZ]] each function is continuous and the pointwise limit jumps from $0$ to $1$ at $x = 1$.
There no single $N$ makes $\lvert x^N - 0 \rvert$ small for all $x$ near $1$, so the outer steps cannot both be small.
The same three steps transfer continuity, uniform continuity and integrability from approximations to their limits, which is why the pattern recurs throughout analysis.

## Notation

The clean form makes each term less than $\varepsilon/3$ and ends with "$< \varepsilon$".
Many books make each term less than $\varepsilon$ and end with "$< 3\varepsilon$".
This is also correct, because $3\varepsilon$ is an arbitrary positive number when $\varepsilon$ is.
With two terms the same method is an epsilon over two argument, with the split $\varepsilon/2 + \varepsilon/2$.
The step "choose $N$ with $\lvert f_N(y) - f(y) \rvert < \varepsilon/3$ for all $y$" is often written $\lVert f_N - f \rVert_\infty < \varepsilon/3$, with the supremum norm.

## Remarks

### Why the order of the choices matters

The proof makes two choices, and their order decides whether it is valid.
First $N$, which depends only on $\varepsilon$; then $\delta$, which depends on $\varepsilon$, on $c$ and on the function $f_N$.
If $N$ depended on $x$, the middle term would compare different functions for different $x$, and no single $\delta$ would exist.
Uniform convergence is exactly what lets $N$ come first.

The three terms must form a chain $f(x) \to f_N(x) \to f_N(c) \to f(c)$ in which each step changes one thing.
A two-term split $\lvert f(x) - f_N(x) \rvert + \lvert f_N(x) - f(c) \rvert$ fails, because its second term compares $f_N$ with $f$ at different points, and no hypothesis controls that.

### Where the pattern appears

The [[uniform limit theorem|0X9XT05JVC]] is the model case, with the [[proof by an epsilon over three argument|1ND5X51YWH]] above.
[[A uniform limit of uniformly continuous functions is uniformly continuous|7MA5SPJ7M7]] uses the same three terms with a $\delta$ that does not depend on the point.
[[A uniform limit of Riemann integrable functions is Riemann integrable|52DMP8VXW4]] uses differences of upper and lower sums as the three terms.

A [[Cauchy sequence|0PWX18FM4G]] with a convergent subsequence converges, by an epsilon over two argument: $\lvert a_n - L \rvert \le \lvert a_n - a_{n_k} \rvert + \lvert a_{n_k} - L \rvert$.
In the proof of the [[Arzelà-Ascoli theorem|0381S8Z5P0]], an [[equicontinuous|0MW2WXTHMC]] sequence on a compact metric space that converges on a dense set converges uniformly, by comparing $f_n(x)$ with $f_m(x)$ through a nearby point of the dense set.

### What the method needs

The triangle inequality is the engine, so the method needs a metric or a norm, and it works in every [[metric space|0VKD1TP7F3]].
The outer terms must be small at every point the middle term uses.
In the continuity proof these are $x$ and $c$, and $x$ ranges over a neighborhood of $c$, so the approximation must be uniform on that neighborhood.
Uniform convergence on each compact set is enough for continuity on $\mathbb{R}$, since continuity is a local property.

The argument shows that the continuous functions form a closed set among the bounded functions with the supremum norm.
Since the bounded functions form a complete space, the bounded continuous functions form a [[Banach space|06GZ956657]].

### Watch out

The main slip chooses $N$ after $x$, so that $N$ depends on $x$; that is pointwise convergence in disguise, and [[the argument fails for x^n on [0, 1]|JKPVHGFN1R]].
A second slip makes the outer term small at $c$ only and forgets the point $x$.
A third slip writes a term such as $\lvert f(x) - f_N(c) \rvert$, which changes two things at once.

### History

Augustin-Louis Cauchy claimed in 1821 that a convergent series of continuous functions has a continuous sum.
Niels Henrik Abel pointed to counterexamples among Fourier series in 1826.
Cauchy's argument works under uniform convergence, and the corrected theorem is proved today by an epsilon over three argument.

### Try it

Show that a uniform limit of bounded functions is bounded.
Choose $N$ with $\lvert f_N(y) - f(y) \rvert < 1$ for all $y$; if $\lvert f_N \rvert \le M$, then $\lvert f(y) \rvert < M + 1$.

Let $f_n \to f$ uniformly, with each $f_n$ continuous, and let $x_n \to x$.
Show that $f_n(x_n) \to f(x)$.
Split $\lvert f_n(x_n) - f(x) \rvert \le \lvert f_n(x_n) - f(x_n) \rvert + \lvert f(x_n) - f(x) \rvert$; the first term is small by uniform convergence, and the second because $f$ is continuous.

## Explanations

### L1 human

Suppose you want to know that two friends live close to each other, but you cannot measure the distance between them.
You know that each lives next to a bus stop, and the two bus stops are close.
Then the friends live close too: the distance is at most the walk to the first stop, plus the ride, plus the walk from the second stop.
If each part is less than $1$ kilometer, the total is less than $3$ kilometers.
The epsilon over three argument does this with numbers, and the bus stops are the values of a simple function close to the hard one.

### L2 human

We run the uniform limit theorem on $f_n(x) = x + \frac{\sin(nx)}{n}$, with limit $f(x) = x$, to see the order of the choices.

1. The convergence is uniform: $\lvert f_n(x) - f(x) \rvert = \frac{\lvert \sin(nx) \rvert}{n} \le \frac1n$ for all $x$.
2. Let $c \in \mathbb{R}$ and $\varepsilon > 0$, and choose an integer $N > 3/\varepsilon$.
   Then $\lvert f_N(y) - f(y) \rvert \le \frac1N < \frac{\varepsilon}{3}$ for all $y$.
3. The function $f_N$ is continuous at $c$, so there is $\delta > 0$ with $\lvert f_N(x) - f_N(c) \rvert < \varepsilon/3$ when $\lvert x - c \rvert < \delta$.
4. For such $x$, the triangle inequality gives $\lvert f(x) - f(c) \rvert < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon$.

Here $f(x) = x$ is already known to be continuous, so the example only shows the mechanics.
The real use is a function known only as a limit, such as the sum of a power series or of a uniformly convergent Fourier series.
Watch out: $N$ in step 2 must not depend on $x$, or step 3 has no fixed function to work with.

### L3 human

The argument proves that a continuity property is closed under uniform limits: $C(X)$ is closed in the space $B(X)$ of bounded functions with the supremum norm, and so $C(X)$ is complete.
The same structure shows that the uniform closure of an algebra of continuous functions is an algebra, a step in the [[Stone-Weierstrass theorem|1P8D3MK79H]].
The [[density argument|J2J35J3055]] uses the three terms in another way: it approximates an arbitrary element by one from a dense class, applies a property there, and returns.
The Moore-Osgood theorem on interchanging two limits is a general form, with the uniform limit theorem as a special case.
In functional analysis the pattern shows that a norm limit of compact operators is compact.
