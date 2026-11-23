---
tag: YKA0ADKYFR
kind: concept
name: Bootstrapping
aliases: [bootstrapping-argument, bootstrap-argument, bootstrap-principle, continuity-argument]
msc: ["00A35", "35B65"]
topics: [MEKKHHQTKB, G9JFJGY4TQ]
audience: grad
specializes: [0B94TKFQJX]
uses: [1JJCDJB7FM, 0X3WGX95FE, 0ASJVEFA9J, 0NHGY0N0JB]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
    locator: lead section
---

## Summary

Bootstrapping proves a strong property of an object from a weaker property of the same object, by showing that the weak property improves itself.

Here is the pattern on a real goal.
Let $u \colon [0, T] \to [0, \infty)$ be [[continuous|0X3WGX95FE]] with $u(0) = 0$ and $u(t) \le 1 + \tfrac18 u(t)^2$ for every $t$.
We show $u(t) \le \tfrac32$ for every $t$.
Assume the weak bound $u(t) \le 2$ at some time $t$.
Then $u(t)^2 \le 4$, so $u(t) \le 1 + \tfrac48 = \tfrac32$, which is strictly better than $2$.
Let $S$ be the set of times where $u \le 2$.
It contains $0$, it is closed because $u$ is continuous, and it is open because $u(t) \le \tfrac32$ keeps $u < 2$ near $t$.
The [[open-closed argument|1JJCDJB7FM]] on the interval gives $S = [0, T]$, and then the improved bound $u \le \tfrac32$ holds everywhere.

The method has two forms.
In the *continuity argument*, as above, a weak bound implies a strictly stronger bound, and continuity in time spreads it over an interval.
In the *regularity bootstrap*, an equation shows that a solution of class $C^k$ has class $C^{k+1}$, and [[mathematical induction|0ASJVEFA9J]] puts it in every class.

## Motivation

An a priori estimate often has the form $u \le A + \varepsilon u^2$, with the unknown quantity on both sides.
Such an inequality alone does not bound $u$: in the opening goal it holds for $u = 0$ and for $u = 7$.
It forbids a middle zone of values, here $4 - 2\sqrt2 < u < 4 + 2\sqrt2$.
A quantity that moves continuously and starts below the zone cannot jump over it, so it stays below.
The continuity argument turns this picture into a proof.

Differential equations show the second form.
If $f' = x f$, then each degree of smoothness of $f$ gives one more degree of smoothness of $f'$, and so of $f$.
The name comes from the phrase "to pull oneself up by one's bootstraps", since the argument seems to lift itself by its own hypothesis.

## Notation

In a continuity argument, the weak bound that we assume is the *bootstrap hypothesis*, and the strong bound that we prove is the *bootstrap conclusion*.
$C^k$ is the class of functions with $k$ continuous derivatives, and $C^\infty = \bigcap_k C^k$.
The [[Sobolev spaces|M4CEZ5K9HP]] $H^m$ measure smoothness by square-integrable [[weak derivatives|C3EC148VZD]], and regularity bootstraps for partial differential equations usually move from $H^m$ to $H^{m+1}$ or $H^{m+2}$.
Moving a term such as $\tfrac12 u$ from the right side to the left side is called *absorbing* the term.

## Remarks

### Why the estimate must improve

The bootstrap conclusion must be strictly better than the bootstrap hypothesis.
If $u \le 2$ gave back only $u \le 2$, nothing would push $u$ below $2$ near a time where $u = 2$, and openness would fail.
The constants decide this.
For $u \le A + \varepsilon u^2$, the hypothesis $u \le 2A$ gives $u \le A(1 + 4\varepsilon A)$, which is below $2A$ exactly when $4\varepsilon A < 1$.

Continuity is the second requirement.
[[A bootstrap without continuity fails|5Y9D4SWRCF]] uses a function that jumps from $0$ to $7$: it satisfies $u \le 1 + \tfrac18 u^2$ at every time and still breaks the bound $u \le 2$.

The regularity form needs a real gain as well.
In $f(x) = 1 + \int_0^x t f(t)\, dt$, the integral is one derivative smoother than its integrand, by the [[fundamental theorem of calculus|0NHGY0N0JB]].
An identity such as $f' = f'$ gains nothing, and the induction never starts.

### Absorbing a term

If a real number $x \ge 0$ satisfies $x \le A + \tfrac12 x$, then $\tfrac12 x \le A$, so $x \le 2A$.
This step needs $x$ to be finite.
The value $x = +\infty$ satisfies $x \le 1 + \tfrac12 x$ in the extended reals, and $x \le 2$ is false.
A correct proof first shows that the quantity is finite, for example on a shorter time interval or for a cut-off version, and then absorbs.

### Sharpening the constant

A bootstrap can be repeated to improve a bound.
Put $b_0 = 2A$ and $b_{k+1} = A + \varepsilon b_k^2$.
From $u \le b_k$ the inequality gives $u \le b_{k+1}$, and when $4\varepsilon A < 1$ the numbers $b_k$ decrease to the smaller root of $\varepsilon r^2 - r + A = 0$.
For $A = 1$ and $\varepsilon = \tfrac18$ they are $2$, $1.5$, $1.28125$, and so on, with limit $4 - 2\sqrt2 \approx 1.172$.
[[A continuity argument for a quadratic a priori bound|7094T3DFW2]] carries out the details.

### Where the pattern appears

[[A continuous solution of an integral equation is smooth|8X1RZXWP62]] is the simplest regularity bootstrap: continuity gives $C^1$, then $C^2$, and by induction $C^\infty$.
[[Elliptic regularity|2PVQY9PCT4]] puts a weak solution $u \in H^1$ of $Lu = f$, with smooth coefficients and $f \in H^m$, in $H^{m+2}$ in the interior, and for smooth $f$ induction on $m$ makes $u$ smooth.
For a nonlinear equation $\Delta u = F(u)$, the right side improves each time $u$ improves, with [[Sobolev embedding|GZTT6FT18G]] controlling $F(u)$.
In ordinary differential equations, [[Grönwall's inequality|07EJHQYR9A]] often supplies the step from weak bound to strong bound.
For nonlinear evolution equations, the continuity argument extends a local solution for all time: the bootstrap hypothesis bounds a norm, and an energy estimate improves it.

### Watch out

The most common slip forgets continuity in time, and then the quantity can jump over the forbidden zone.
A second slip proves that the hypothesis implies itself again, with no strict gain.
A third absorbs a term into a quantity not yet known to be finite.
In a regularity bootstrap, do not differentiate the equation before knowing that the solution is differentiable: the first gain must come from the equation as it stands.

### History

The name comes from the English phrase about pulling oneself up by one's own bootstraps.
Thomas Hakon Grönwall published his inequality in 1919, and it became a standard step in continuity arguments for differential equations.

### Try it

Let $u \colon [0, 1] \to [0, \infty)$ be continuous with $u(0) = 0$ and $u \le 1 + \tfrac14 u^2$.
Does $u \le 2$ follow?
No: the hypothesis is $(u - 2)^2 \ge 0$, true for every $u$, and $u(t) = 3t$ reaches $3$; here $4\varepsilon A = 1$.

Suppose $f$ is continuous on $\mathbb{R}$ and $f(x) = \int_0^x f(t)\, dt$.
Show that $f$ is smooth, then that $f = 0$.
The integral makes $f \in C^1$ with $f' = f$, induction gives $C^\infty$, and $(f e^{-x})' = 0$ with $f(0) = 0$ gives $f = 0$.

## Explanations

### L1 human

Imagine a ball that rolls on a valley floor between two hills.
A rule says: whenever the ball is lower than the hilltops, it is in fact near the valley floor.
The ball starts on the floor and moves without jumps.
To get over a hill it would have to pass the hilltop, but just below the hilltop the rule already puts it back near the floor.
So the ball stays near the floor for all time.
The rule alone is not enough: a ball that could teleport might appear on the other side of the hill.

### L2 human

We test the constants with $u \le 1 + \varepsilon u^2$, $u$ continuous on $[0, 1]$ and $u(0) = 0$, aiming for $u \le 2$.

1. The hypothesis $u \le 2$ gives $u \le 1 + 4\varepsilon$.
2. For $\varepsilon = \tfrac18$ this is $u \le \tfrac32 < 2$, a strict gain, and the argument closes.
3. For $\varepsilon = \tfrac15$ it is $u \le 1.8 < 2$, still a strict gain, and the argument closes.
4. For $\varepsilon = \tfrac14$ it is $u \le 2$, no gain at all.
   The function $u(t) = 3t$ satisfies $3t \le 1 + \tfrac94 t^2$, since $(\tfrac32 t - 1)^2 \ge 0$, and it reaches $3$.

So the dividing line is exactly $4\varepsilon A = 1$, with $A = 1$ here.
Check: $1.8^2 = 3.24$ and $1 + \tfrac15 \cdot 3.24 = 1.648$, so a second round improves the bound again.
Watch out: an estimate that only reproduces the hypothesis proves nothing, however close it comes.

### L3 human

The continuity argument is the open-closed argument on a time interval.
It is the backbone of global existence and stability proofs for nonlinear dispersive and hyperbolic equations.
A local existence theorem extends a solution while a norm stays bounded, and the bootstrap shows that the norm never reaches the bound.
The regularity bootstrap combines a linear regularity theorem, such as [[elliptic regularity|2PVQY9PCT4]] or Schauder estimates, with Sobolev embedding and the structure of the nonlinearity.
It is the standard proof that weak solutions of many [[semilinear equations|RCNY89A4NY]] are smooth.
In statistics, the word "bootstrap" names a different resampling method that shares only the image of self-support.
