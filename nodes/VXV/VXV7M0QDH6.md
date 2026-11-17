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

The epsilon over three argument bounds $\lvert f(x) - f(y) \rvert$ for a limit object $f$ through an approximation $g$ that is easier to control.
The [[triangle inequality|03HF5PMY5T]] splits the quantity into three terms:
$$\lvert f(x) - f(y) \rvert \le \lvert f(x) - g(x) \rvert + \lvert g(x) - g(y) \rvert + \lvert g(y) - f(y) \rvert.$$
We first choose $g$ so that the two outer terms are less than $\varepsilon/3$ at all points.
Then a property of $g$ makes the middle term less than $\varepsilon/3$.
The sum is then less than $\varepsilon$.
The order of the choices is the heart of the method.
The approximation is fixed first, and it must be good uniformly in $x$ and $y$.
The argument matters because it transfers properties such as continuity, uniform continuity and integrability from approximations to their limits.

## Motivation

A typical question asks whether a limit of good functions is again good.
For example, let $f_n$ be [[continuous functions|0X3WGX95FE]] with $f_n(x) \to f(x)$ at each point $x$.
To show that $f$ is continuous at $c$, we must compare $f(x)$ with $f(c)$, but we know nothing about $f$ directly.
We know two things: each $f_n$ is close to $f$, and each $f_n$ is continuous.
The triangle inequality lets us use both facts at once, with $f_N$ as a bridge from $f(x)$ to $f(c)$.
The example [[x^n on [0, 1]|0YSRR1JTKZ]] shows that the bridge collapses if $f_N$ is close to $f$ only point by point, so [[uniform convergence|08VZ57PT26]] is the right hypothesis.

## Notation

1. The clean form makes each of the three terms less than $\varepsilon/3$ and ends with "$< \varepsilon$".
2. Another common form makes each term less than $\varepsilon$ and ends with "$< 3\varepsilon$". This is also correct, because $\varepsilon > 0$ is arbitrary, so $3\varepsilon$ is an arbitrary positive number too.
3. When only two terms appear, the same method is called an epsilon over two argument, with the split $\varepsilon/2 + \varepsilon/2$.
4. In analysis texts the step "choose $N$ with $\sup_x \lvert f_N(x) - f(x) \rvert < \varepsilon/3$" is often written $\lVert f_N - f \rVert_\infty < \varepsilon/3$, with the supremum norm.

## Remarks

### Examples

1. The [[uniform limit theorem|0X9XT05JVC]]: a uniform limit of continuous functions is continuous. Its [[proof by an epsilon over three argument|1ND5X51YWH]] is the model of the method.
2. [[A uniform limit of uniformly continuous functions is uniformly continuous|7MA5SPJ7M7]]: the same three terms, with a $\delta$ that does not depend on the point.
3. [[A uniform limit of Riemann integrable functions is Riemann integrable|52DMP8VXW4]]: the three terms are differences of upper and lower sums, and the middle term is small for a good partition.
4. A [[Cauchy sequence|0PWX18FM4G]] with a convergent subsequence converges. This is an epsilon over two argument: $\lvert a_n - L \rvert \le \lvert a_n - a_{n_k} \rvert + \lvert a_{n_k} - L \rvert$.
5. A step in the proof of the [[Arzelà-Ascoli theorem|0381S8Z5P0]]: an [[equicontinuous|0MW2WXTHMC]] sequence of functions on a compact metric space that converges at each point of a dense set converges uniformly. The proof compares $f_n(x)$ and $f_m(x)$ through a nearby point of the dense set.

### Non-examples

1. [[The epsilon over three argument fails for x^n on [0, 1]|JKPVHGFN1R]]: the functions converge only pointwise. The index $N$ that makes the outer terms small depends on the point, and the argument cannot be completed at $x = 1$.
2. A two-term estimate $\lvert f(x) - f(c) \rvert \le \lvert f(x) - f_N(x) \rvert + \lvert f_N(x) - f(c) \rvert$ does not work. The second term compares $f_N$ with $f$ at different points, and no hypothesis controls it.
3. An argument that chooses $\delta$ first and the index $N$ afterwards, with $N$ depending on $x$, has the wrong order. The middle term then involves a function that is not fixed when $\delta$ is chosen.

### Basic properties

1. The method needs a metric or a norm, because it uses the triangle inequality. It works in every [[metric space|0VKD1TP7F3]].
2. The outer terms must be small at all the points that the middle term involves. In the continuity proof these are $x$ and $c$, and $x$ ranges over a neighbourhood, so the approximation must be uniform on that neighbourhood.
3. The method proves that the set of continuous functions is closed in the space of bounded functions with the supremum norm. With the completeness of the bounded functions, this gives that the bounded continuous functions form a [[Banach space|06GZ956657]].
4. The same three terms prove the interchange of limits $\lim_{x \to c} \lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} \lim_{x \to c} f_n(x)$ under uniform convergence.

### History

Augustin-Louis Cauchy claimed in 1821 that a convergent series of continuous functions has a continuous sum, as the page on the uniform limit theorem records.
Niels Henrik Abel gave counterexamples among Fourier series in 1826.
In modern terms, Cauchy's argument needs uniform convergence, and the modern proof of the corrected theorem is an epsilon over three argument.

### Common errors

1. A student chooses $N$ after $x$, so that $N$ depends on $x$. The middle term then has no fixed function, and its $\delta$ is not defined.
2. A student proves the outer terms small only at the point $c$, and not at $x$. Uniform convergence is needed at both points.
3. A student writes the three terms with the wrong signs or points, for example $\lvert f(x) - f_N(c) \rvert$. The terms must form a chain $f(x) \to f_N(x) \to f_N(c) \to f(c)$, where each step changes one thing.

## Explanations

### L1 human

Suppose we want to know that two people live close to each other, but we cannot measure the distance between them directly.
We know that each of them lives next to a bus stop, and the two bus stops are close.
Then the people live close too: the distance is at most the walk to the first stop, plus the ride between the stops, plus the walk from the second stop.
If each part is less than $1$ kilometre, the total is less than $3$ kilometres.
The epsilon over three argument does this with numbers: the bus stops are the values of a simple function that is close to the hard one.

### L2 human

We prove the uniform limit theorem in a special case, to see the order of the choices.
Let $f_n(x) = x + \frac{\sin(nx)}{n}$ on $\mathbb{R}$, and let $f(x) = x$.

1. The convergence is uniform: $\lvert f_n(x) - f(x) \rvert = \frac{\lvert \sin(nx) \rvert}{n} \le \frac1n$ for all $x$.
2. Let $c \in \mathbb{R}$ and $\varepsilon > 0$. Choose an integer $N > 3/\varepsilon$. Then $\lvert f_N(y) - f(y) \rvert \le \frac1N < \frac{\varepsilon}{3}$ for all $y$.
3. The function $f_N$ is continuous at $c$, so there is $\delta > 0$ with $\lvert f_N(x) - f_N(c) \rvert < \varepsilon/3$ when $\lvert x - c \rvert < \delta$.
4. For such $x$, the triangle inequality gives $\lvert f(x) - f(c) \rvert < \frac{\varepsilon}{3} + \frac{\varepsilon}{3} + \frac{\varepsilon}{3} = \varepsilon$.

Here we already know that $f(x) = x$ is continuous, so the example only shows the mechanics.
The typical use of the argument is the case where $f$ is known only as a limit.
Examples are the sum of a power series and the sum of a uniformly convergent Fourier series.
A trap is to choose $N$ in step 2 in a way that depends on $x$: then step 3 has no fixed function to work with.

### L3 human

The epsilon over three argument is the proof that the set of functions with a given continuity property is closed under uniform limits.
In the language of metric spaces, it shows that $C(X)$ is closed in the space $B(X)$ of bounded functions with the supremum norm, and so $C(X)$ is complete.
The same structure proves that the uniform closure of an algebra of continuous functions is an algebra, a step in the [[Stone-Weierstrass theorem|1P8D3MK79H]].
The [[density argument|J2J35J3055]] uses the same three terms in another order: it approximates an arbitrary element by an element of a dense class, applies a property there, and returns.
A general form is the Moore-Osgood theorem on the interchange of two limits, of which the uniform limit theorem is a special case.
In functional analysis the pattern proves that a uniform limit of compact operators is compact.
In probability it gives the step from a dense class of test functions to all bounded continuous functions.
