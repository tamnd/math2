---
tag: KDXKVT5K1E
kind: example
name: Fallacies with infinite series and integrals
aliases: [fallacies-with-infinite-series, fallacies-in-analysis]
msc: ["00A35", "97I30", "40A05"]
topics: [T6QQ749DM5]
audience: ug1
instance_of: [S2BW0FDHV8]
uses: [S2BW0FDHV8, 0JWMJSTBSG, 0E7VBYGFF7, 08Y1BBQTK9, 0NHGY0N0JB, WW53KG71KH, QN2210XCST]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_fallacy
    locator: Analysis
  - url: https://en.wikipedia.org/wiki/Grandi%27s_series
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Riemann_series_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Iterated_limit
    locator: lead section
---

## Example

Analysis is full of infinite processes, and its [[mathematical fallacies|S2BW0FDHV8]] treat an infinite process as if it were a finite one.
The oldest is a false proof that $0 = 1$ from [[Grandi's series|5V9ZHDZ0EZ]]; find the bad step first.

1. Let $S = 1 - 1 + 1 - 1 + \cdots$.
2. Group the terms in pairs: $S = (1 - 1) + (1 - 1) + \cdots = 0 + 0 + \cdots = 0$.
3. Group them another way: $S = 1 + (-1 + 1) + (-1 + 1) + \cdots = 1 + 0 + 0 + \cdots = 1$.
4. So $0 = S = 1$.

The bad step is step 1, before any arithmetic happens.
The partial sums of the series are $1, 0, 1, 0, \ldots$, and they have no limit, so the series is a [[divergent series|0JWMJSTBSG]] and the letter $S$ names no number.
Steps 2 and 3 then compute with an object that does not exist.

The correct rule about grouping has a hypothesis.
If a series converges to $S$, then every grouping of its terms into finite blocks also converges to $S$, because the partial sums of the grouped series are a subsequence of the old partial sums.
For a divergent series the groupings can disagree: the grouping of step 2 has partial sums $0, 0, \ldots$, and that of step 3 has partial sums $1, 1, \ldots$.

A third argument writes $S = 1 - (1 - 1 + 1 - \cdots) = 1 - S$ and gets $S = \frac{1}{2}$.
It makes the same error, since it assumes that $S$ exists.
The number $\frac{1}{2}$ does have a meaning: it is the Cesàro sum, the limit of the averages of the partial sums, and the averages $1, \frac{1}{2}, \frac{2}{3}, \frac{2}{4}, \ldots$ tend to $\frac{1}{2}$.
But the Cesàro sum is a new definition, not the sum of the series in the usual sense, and the series still diverges.

## Remarks

### Rearranging a series

Here is a false proof that $\ln 2 = 0$.

1. The [[alternating harmonic series|0JQ5Y3WWVE]] converges: $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \ln 2$.
2. Reorder it as one odd term, then two even terms: $L = 1 - \frac{1}{2} - \frac{1}{4} + \frac{1}{3} - \frac{1}{6} - \frac{1}{8} + \cdots$.
3. The new order uses the same terms, so $L = \ln 2$.
4. Combine each odd term with the next term: $L = \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \cdots = \frac{1}{2}\ln 2$.
5. So $\ln 2 = \frac{1}{2}\ln 2$, and $\ln 2 = 0$.

Step 4 is correct, since block number $k$ is
$$\frac{1}{2k - 1} - \frac{1}{4k - 2} - \frac{1}{4k} = \frac{1}{2}\left(\frac{1}{2k - 1} - \frac{1}{2k}\right).$$
Step 3 is the bad one.
The series [[converges conditionally|02YRQXZDCS]]: it converges, but $\sum \frac{1}{n}$ diverges.
By the [[Riemann rearrangement theorem|0E7VBYGFF7]], such a series can be reordered to converge to any real number, so the order matters.
The correct rule needs absolute convergence: if $\sum |a_n|$ converges, then every rearrangement of $\sum a_n$ has the same sum.

### Integration by parts of $\int \frac{dx}{x}$

A false proof that $0 = 1$.
[[Integrate by parts|08Y1BBQTK9]] with $u = \frac{1}{x}$ and $dv = dx$, so $du = -\frac{dx}{x^2}$ and $v = x$:
$$\int \frac{dx}{x} = \frac{1}{x} \cdot x - \int x \cdot \left(-\frac{1}{x^2}\right) dx = 1 + \int \frac{dx}{x}.$$
Now subtract $\int \frac{dx}{x}$ from both sides to get $0 = 1$.

The display is correct; the subtraction is the bad step.
An indefinite integral is defined only up to a constant, since [[antiderivatives differ by a constant|QFCQQTBFWC]].
The symbol $\int \frac{dx}{x}$ stands for any function $\ln|x| + C$ on an interval without $0$, so its two copies in the display may differ by $1$, and indeed they must.
The correct version uses a definite integral on $[a, b]$ with $0 < a < b$:
$$\int_a^b \frac{dx}{x} = \Big[\tfrac{1}{x} \cdot x\Big]_a^b + \int_a^b \frac{dx}{x} = (1 - 1) + \int_a^b \frac{dx}{x}.$$
This is true and says nothing new.

### A negative integral of a positive function

A false computation: an antiderivative of $\frac{1}{x^2}$ is $-\frac{1}{x}$, so
$$\int_{-1}^{1} \frac{dx}{x^2} = \Big[-\tfrac{1}{x}\Big]_{-1}^{1} = -1 - 1 = -2.$$
But $\frac{1}{x^2} > 0$ for every $x \neq 0$, so the integral cannot be negative.
The bad step uses the [[fundamental theorem of calculus|0NHGY0N0JB]], which needs an integrand that is continuous on the whole of $[-1, 1]$, and $\frac{1}{x^2}$ is not even defined at $0$.
The integral is an [[improper integral|05KQ3F99BQ]], and for $0 < t < 1$,
$$\int_t^1 \frac{dx}{x^2} = \frac{1}{t} - 1 \to +\infty \quad \text{as } t \to 0^+.$$
So the integral diverges to $+\infty$.
On $[1, 2]$ the same theorem applies, and $\int_1^2 \frac{dx}{x^2} = -\frac{1}{2} + 1 = \frac{1}{2}$ is correct.

### Exchanging two limits

A false proof that $0 = 1$.
Let $a_{m,n} = \frac{m}{m + n}$ for positive integers $m$ and $n$.
For fixed $m$, $a_{m,n} \to 0$ as $n \to \infty$, so $\lim_m \lim_n a_{m,n} = 0$.
For fixed $n$, $a_{m,n} = \frac{1}{1 + n/m} \to 1$ as $m \to \infty$, so $\lim_n \lim_m a_{m,n} = 1$.
"The order of limits does not matter", so $0 = 1$.

The two iterated limits are computed correctly; the quoted rule is the bad step.
Two iterated limits can both exist and differ.
A correct rule is the [[Moore-Osgood theorem|QN2210XCST]]: if one inner limit is uniform in the other variable and the other inner limit exists, then both iterated limits exist and agree.
Here neither inner limit is uniform, since $a_{m,m} = \frac{1}{2}$ for every $m$, so the diagonal never gets close to $0$ or $1$.

### Exchanging two sums

Let $a_{m,n} = 1$ when $n = m$, $a_{m,n} = -1$ when $n = m + 1$, and $a_{m,n} = 0$ otherwise, for $m, n \ge 1$.
Each row contains one $1$ and one $-1$, so every row sum is $0$, and the total of the row sums is $0$.
Column $1$ contains only $a_{1,1} = 1$, and each later column $n$ contains $a_{n,n} = 1$ and $a_{n-1,n} = -1$.
So the column sums are $1, 0, 0, \ldots$, and their total is $1$.
[[Fubini's theorem for series|WW53KG71KH]] allows the exchange only when $\sum_{m,n} |a_{m,n}|$ converges, and here that sum is infinite.

### What the examples share

Every infinite operation is a limit, and a rule for finite sums survives the limit only under a hypothesis.
Grouping needs convergence, and reordering or exchanging two sums needs absolute convergence.
The fundamental theorem of calculus needs continuity on the closed interval, and exchanging two limits needs uniformity.
The [[quantifier shift fallacy|CRW82NARQV]] is the logical form of the last error: a pointwise statement used as if it were uniform.

### Try it

Does $\sum_{n \ge 1} \frac{(-1)^{n+1}}{n^2}$ keep its sum under the reordering of the rearrangement example?
Yes: $\sum \frac{1}{n^2}$ converges, so the series converges absolutely and every rearrangement has the same sum.

What is wrong with $\int_0^2 \frac{dx}{(x - 1)^2} = \Big[-\frac{1}{x - 1}\Big]_0^2 = -1 - 1 = -2$?
The integrand is unbounded at $x = 1$ inside the interval, and the improper integral diverges to $+\infty$.

## Explanations

### L1 human

An infinite sum is not an ordinary sum: it is the value that the finite sums approach.
For $1 - 1 + 1 - 1 + \cdots$ the finite sums are $1, 0, 1, 0, \ldots$, and they approach nothing.
So the infinite sum has no value, and arguments that give it the value $0$, $1$ or $\frac{1}{2}$ compute with something that does not exist.
For $1 - \frac{1}{2} + \frac{1}{3} - \cdots$ the finite sums do approach a value, but a new order of the same terms can approach another value.
Rules for finite sums need a new proof before they work for infinite sums.

### L2 human

We test the step "take the limit inside the integral" on $f_n(x) = n^2 x e^{-nx}$ on $[0, 1]$.
For fixed $x > 0$, $f_n(x) \to 0$, because the exponential decays faster than $n^2$ grows, and $f_n(0) = 0$.
So the limit function is $0$, and its integral is $0$.
Now integrate first, with the substitution $t = nx$ and then integration by parts:
$$\int_0^1 n^2 x e^{-nx}\,dx = \int_0^n t e^{-t}\,dt = 1 - (n + 1)e^{-n} \to 1.$$
So the limit of the integrals is $1$, while the integral of the limit is $0$.

Check: for $n = 1$ the integral is $1 - 2e^{-1} \approx 0.264$.
The tools that permit the exchange are uniform convergence and the [[dominated convergence theorem|BYNV84PF86]], and neither applies.
The convergence is not uniform, because $f_n(\frac{1}{n}) = \frac{n}{e}$ grows without bound.
Watch out: each $f_n$ is continuous and $f_n \to 0$ at every point, and the exchange still fails.
