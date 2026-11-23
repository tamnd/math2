---
tag: 9R232GGWSB
kind: example
name: Unpacking "strictly increasing" and "injective"
msc: ["00A35", "26A48"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [41JZ39GE3F]
uses: [41JZ39GE3F, 011EJQWWJS, 09NWETVTNY, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Monotonic_function
    locator: In calculus and analysis
  - url: https://en.wikipedia.org/wiki/Injective_function
    locator: lead section
---

## Example

Let $f \colon \mathbb{R} \to \mathbb{R}$ be a function.
The claim is that if $f$ is strictly increasing, then $f$ is injective.
The claim has two defined terms, and the method of [[unpacking definitions|41JZ39GE3F]] replaces each one by its condition.

1. "$f$ is [[strictly increasing|011EJQWWJS]]" means that for all real $x$ and $y$, if $x < y$, then $f(x) < f(y)$.
   This is the given.
2. "$f$ is [[injective|09NWETVTNY]]" means that for all real $x$ and $y$, if $f(x) = f(y)$, then $x = y$.
   This is the goal.
3. The goal starts with "for all" and then "if", so the proof starts with "Let $x, y \in \mathbb{R}$ with $f(x) = f(y)$", and the new goal is $x = y$.
4. We stop at the order $<$ of the real numbers, because one known property finishes the proof.
   That property is trichotomy: for real $x$ and $y$, exactly one of $x < y$, $x = y$ and $y < x$ holds.

The final proof reads as follows.

> Let $x, y \in \mathbb{R}$ with $f(x) = f(y)$.
> Suppose, for a contradiction, that $x \ne y$.
> By trichotomy, $x < y$ or $y < x$.
> If $x < y$, then $f(x) < f(y)$, because $f$ is strictly increasing, and this contradicts $f(x) = f(y)$.
> If $y < x$, then $f(y) < f(x)$ for the same reason, which again contradicts $f(x) = f(y)$.
> So $x = y$, and $f$ is injective.
> $\square$

The first sentence is the unpacked goal, an arbitrary pair with equal values.
The given is used twice, once for each order of $x$ and $y$, and the whole argument is a [[proof by contradiction|0J0XBKG64S]] inside the frame that the unpacked goal gives.

Check: $f(x) = x^3$ is strictly increasing, and $f(y) = f(2) = 8$ forces $y^3 = 8$, so $y = 2$.

## Remarks

Before unpacking, "increasing implies injective" seems to need a picture of a graph.
After unpacking, it is a statement about $<$ and $=$, and the proof uses only trichotomy.
The real numbers could be unpacked further, for example into Dedekind cuts, but trichotomy is a known result, and the method stops at known results.

The converse is false.
The function $f(x) = -x$ is injective, because $-x = -y$ gives $x = y$, but it is decreasing.
The word "strictly" is needed too.
The constant function $f(x) = 0$ satisfies $f(x) \le f(y)$ whenever $x < y$, so it is increasing in the weak sense, but $f(0) = f(1)$.

## Explanations

### L1 human

"Strictly increasing" means that a bigger input always gives a bigger output, as for the rule "double the number".
"Injective" means that two different inputs never give the same output.
Once we write out these two meanings, the proof is short.
If two inputs are different, one of them is smaller.
The smaller input then has the smaller output, so the outputs are different too.

### L2 human

We unpack and prove: if $f, g \colon \mathbb{R} \to \mathbb{R}$ are strictly increasing, then $g \circ f$ is strictly increasing.
The givens say that $x < y$ implies $f(x) < f(y)$, and that $u < v$ implies $g(u) < g(v)$.
The goal says that $x < y$ implies $g(f(x)) < g(f(y))$.

So let $x < y$.
The given for $f$ yields $f(x) < f(y)$.
The given for $g$, applied with $u = f(x)$ and $v = f(y)$, yields $g(f(x)) < g(f(y))$, which is the goal.

Check: $f(x) = 2x$ and $g(x) = x + 1$ give $g(f(1)) = 3 < 5 = g(f(2))$.
Watch out: if you unpack the given and not the goal, you will not see that the proof must start with an arbitrary pair $x < y$.
