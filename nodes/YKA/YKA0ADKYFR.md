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

Bootstrapping is the method of using a weak property of an object to prove a stronger property of the same object, and then using the stronger property in the same way again.
It has two main forms.
In the *regularity bootstrap*, an equation shows that each solution in a class $C_k$ lies in a better class $C_{k+1}$, and [[mathematical induction|0ASJVEFA9J]] then puts the solution in every class $C_k$.
In the *continuity argument*, we prove a bound $Q(t)$ for all times $t$ in an interval.
We show that the weaker bound $Q'(t)$ implies the stronger bound $Q(t)$, and that $Q(t)$ implies $Q'$ near $t$.
We also show that $Q$ survives limits, and that $Q$ holds at one time.
The [[open-closed argument|1JJCDJB7FM]] on the interval then gives $Q(t)$ for all $t$.
The method matters because it lets an estimate prove itself: the bound that we want is used as a hypothesis, and the continuity of the quantity makes this legal.

## Motivation

An a priori estimate often has the form $u \le A + \varepsilon u^2$, with the unknown quantity $u$ on both sides.
Such an inequality alone does not bound $u$, because both small and large values of $u$ satisfy it.
If $u$ depends continuously on a time $t$ and starts small, it cannot jump from the small values to the large values, and so it stays small.
The continuity argument makes this picture into a proof.
In the same way, a differential equation often expresses a derivative of a solution through the solution itself, as in $f' = x f$.
Then each degree of smoothness of $f$ gives one more degree of smoothness of $f'$, and so of $f$.
The name comes from the phrase "to pull oneself up by one's bootstraps": the argument seems to lift itself by its own hypothesis.

## Notation

1. In a continuity argument, the weak bound that we assume is called the *bootstrap hypothesis*, and the strong bound that we prove is called the *bootstrap conclusion*.
2. $C^k$ is the class of functions with $k$ continuous derivatives, and $C^\infty = \bigcap_k C^k$.
3. The [[Sobolev spaces|M4CEZ5K9HP]] $H^m$ measure regularity by square-integrable [[weak derivatives|C3EC148VZD]]. Regularity bootstraps in PDE usually move from $H^m$ to $H^{m+1}$ or $H^{m+2}$.
4. The step "a term $\tfrac12 u$ on the right side moves to the left side" is called *absorbing* the term. It is a bootstrap step that needs $u$ to be finite.

## Remarks

### Examples

1. [[A continuity argument for a quadratic a priori bound|7094T3DFW2]]: a continuous $u \ge 0$ with $u(0) \le A$ and $u \le A + \varepsilon u^2$, where $4 \varepsilon A < 1$, stays below $2A$.
2. [[A continuous solution of an integral equation is smooth|8X1RZXWP62]]: continuity gives $f \in C^1$, then $f \in C^2$, and by induction $f \in C^\infty$.
3. [[Elliptic regularity|2PVQY9PCT4]]: a weak solution $u \in H^1$ of $Lu = f$ with smooth coefficients and $f \in H^m$ lies in $H^{m+2}$ in the interior. For $f$ smooth, induction on $m$ gives a smooth $u$. For a nonlinear equation $\Delta u = F(u)$, the right side improves each time $u$ improves, and the same induction works.
4. Absorbing a term: if a finite real number $x \ge 0$ satisfies $x \le A + \tfrac12 x$, then $x \le 2A$.
5. [[Grönwall's inequality|07EJHQYR9A]] is often the step "weak bound gives strong bound" in a continuity argument for an ordinary differential equation.

### Non-examples

1. [[A bootstrap without continuity fails|5Y9D4SWRCF]]: a function $u$ that jumps from $0$ to $7$ satisfies $u \le 1 + u^2/8$ and $u(0) \le 1$, but not $u \le 2$.
2. Absorbing a term in an infinite quantity is not a bootstrap step. The value $x = +\infty$ satisfies $x \le 1 + \tfrac12 x$ in the extended reals, but $x \le 2$ is false.
3. A regularity "bootstrap" that does not gain anything is circular. From $f' = f'$ one learns nothing, and induction does not start.

### Basic properties

1. The continuity argument is an instance of the [[open-closed argument|1JJCDJB7FM]]. Let $S$ be the set of times $t$ where the bootstrap conclusion holds. The implication "hypothesis gives a strictly better conclusion" makes $S$ open, the continuity of $u$ makes $S$ closed, and the start time is in $S$.
2. The bootstrap conclusion must be strictly stronger than the bootstrap hypothesis. If $u \le 2A$ gave only $u \le 2A$ again, openness would fail.
3. A regularity bootstrap is an induction on the class: the base case is the given regularity, and the step is the gain from the equation.
4. A bootstrap can be iterated to sharpen a constant. From $u \le 2A$ and $u \le A + \varepsilon u^2$ one gets $u \le A(1 + 4\varepsilon A)$, and repeating gives bounds that decrease to the smaller root of $\varepsilon u^2 - u + A = 0$.

### History

The name comes from the English phrase about pulling oneself up by one's own bootstraps.
Thomas Hakon Grönwall published his inequality in 1919, and it became a standard step in continuity arguments for differential equations.
Regularity bootstraps are the standard route from weak solutions to smooth solutions in the theory of elliptic equations.

### Common errors

1. A student forgets to check continuity in time. Without it, the quantity can jump over the forbidden zone, as in non-example 1.
2. A student absorbs a term without knowing that the quantity is finite, as in non-example 2. A correct proof first shows finiteness, for example by a cut-off or on a shorter time interval.
3. A student proves that the bootstrap hypothesis implies the same hypothesis again. The conclusion must be strictly better, so that a neighbourhood of each good time is good.

## Explanations

### L1 human

Imagine a ball that rolls along a valley floor between two hills.
A rule says: whenever the ball is lower than the hilltops, it is in fact near the valley floor.
The ball starts on the floor and moves without jumps.
To get over a hill it would have to pass the hilltop, but just below the hilltop the rule already puts it back near the floor.
So the ball stays near the floor for all time.
The rule alone is not enough: a ball that can teleport could appear on the other side of the hill.

### L2 human

We test the constants of a continuity argument.
Let $u \colon [0, T] \to [0, \infty)$ be continuous with $u(0) = 0$.

1. First assume only $u(t) \le 1 + \tfrac14 u(t)^2$ for each $t$, and try to prove $u(t) \le 2$.
2. The hypothesis says $u^2 - 4u + 4 \ge 0$, that is $(u - 2)^2 \ge 0$. This holds for every real $u$, so the hypothesis carries no information.
3. So the claim is false: $u(t) = 3t$ on $[0, 1]$ satisfies the hypothesis, and $u(1) = 3 > 2$. Here $4 \varepsilon A = 4 \cdot \tfrac14 \cdot 1 = 1$, and the method needs $4 \varepsilon A < 1$.
4. Now assume $u(t) \le 1 + \tfrac18 u(t)^2$ for each $t$, so $4 \varepsilon A = \tfrac12 < 1$. Let $S = \{ t \in [0, T] : u(t) \le 2 \}$.
5. $0 \in S$, because $u(0) = 0$. $S$ is closed, because it is the preimage of the closed set $(-\infty, 2]$ under the continuous function $u$.
6. Let $t \in S$. Then $u(t)^2 \le 4$, so $u(t) \le 1 + \tfrac18 \cdot 4 = \tfrac32$. By continuity $u < 2$ on a neighbourhood of $t$, so $S$ is open.
7. The interval $[0, T]$ is connected, so $S = [0, T]$. In fact step 6 gives the better bound $u(t) \le \tfrac32$ for all $t$.

The typical use is a global existence proof for a nonlinear evolution equation: the bootstrap hypothesis is a bound on the solution, and the energy estimate improves it.
The trap is step 3: when the constants are too large, the bootstrap conclusion is not better than the hypothesis, and the argument does not close.

### L3 human

The continuity argument is the open-closed argument on a time interval.
In this form it is the backbone of global existence and stability proofs for nonlinear dispersive and hyperbolic equations.
A local existence theorem extends a solution while a norm stays bounded, and the bootstrap shows that the norm never reaches the bound.
The regularity bootstrap combines a linear regularity theorem, such as [[elliptic regularity|2PVQY9PCT4]] or Schauder estimates, with [[Sobolev embedding|GZTT6FT18G]] and the structure of the nonlinearity, and it is the standard proof that weak solutions of many [[semilinear equations|RCNY89A4NY]] are smooth.
The same idea appears outside analysis: in algebra, a property of a structure that improves itself under a construction is proved by induction on the construction.
In statistics, the word "bootstrap" names a different resampling method that shares only the image of self-support.
