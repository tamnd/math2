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

Five [[mathematical fallacies|S2BW0FDHV8]] of analysis treat an infinite process as if it were a finite one.
For each one we give the argument, the step that fails, and the correct rule.

### Grandi's series

The argument:

1. Let $S = 1 - 1 + 1 - 1 + \cdots$.
2. Group the terms in pairs: $S = (1 - 1) + (1 - 1) + \cdots = 0 + 0 + \cdots = 0$.
3. Group them in another way: $S = 1 + (-1 + 1) + (-1 + 1) + \cdots = 1 + 0 + 0 + \cdots = 1$.
4. So $0 = S = 1$.

The check:

1. The partial sums of [[Grandi's series|5V9ZHDZ0EZ]] are $1, 0, 1, 0, \ldots$, so they have no limit. The series is a [[divergent series|0JWMJSTBSG]].
2. So step 1 is invalid: the symbol $S$ names no real number, and steps 2 and 3 compute with an object that does not exist.
3. The correct rule is: if a series converges to $S$, then each grouping of its terms into finite blocks converges to $S$. The proof is that the partial sums of the grouped series form a subsequence of the partial sums of the original series.
4. For a divergent series, groupings can converge to different limits. Here the grouping of step 2 has the partial sums $0, 0, \ldots$, and the grouping of step 3 has the partial sums $1, 1, \ldots$.

A third argument writes $S = 1 - (1 - 1 + 1 - \cdots) = 1 - S$ and gets $S = \frac{1}{2}$.
It makes the same error, because it assumes that $S$ exists.
The value $\frac{1}{2}$ is the value that Cesàro and Abel summation assign, but it is not a sum in the sense of limits of partial sums.

### Rearranging a conditionally convergent series

The argument:

1. The [[alternating harmonic series|0JQ5Y3WWVE]] converges: $1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \cdots = \ln 2$.
2. Write its terms in the order "one odd term, then two even terms": $L = 1 - \frac{1}{2} - \frac{1}{4} + \frac{1}{3} - \frac{1}{6} - \frac{1}{8} + \frac{1}{5} - \frac{1}{10} - \frac{1}{12} + \cdots$.
3. Assume that the new order has the same sum, so $L = \ln 2$.
4. Combine each odd term with the next term: $\left(1 - \frac{1}{2}\right) - \frac{1}{4} + \left(\frac{1}{3} - \frac{1}{6}\right) - \frac{1}{8} + \cdots = \frac{1}{2} - \frac{1}{4} + \frac{1}{6} - \frac{1}{8} + \cdots$.
5. This is half of the original series, so $L = \frac{1}{2}\ln 2$.
6. So $\ln 2 = \frac{1}{2}\ln 2$, and $\ln 2 = 0$.

The check:

1. Steps 4 and 5 are valid. The block number $k$ of three terms is $\frac{1}{2k - 1} - \frac{1}{4k - 2} - \frac{1}{4k} = \frac{1}{4k - 2} - \frac{1}{4k} = \frac{1}{2}\left(\frac{1}{2k - 1} - \frac{1}{2k}\right)$. The terms tend to $0$, so the partial sums inside a block also tend to $\frac{1}{2}\ln 2$.
2. Step 3 is invalid. The series of step 1 [[converges conditionally|02YRQXZDCS]]: it converges, but $\sum \frac{1}{n}$ diverges.
3. By the [[Riemann rearrangement theorem|0E7VBYGFF7]], a conditionally convergent series has rearrangements with any real sum. So a rearrangement can change the sum, and here it does.
4. The correct rule is: if $\sum |a_n|$ converges, then every rearrangement of $\sum a_n$ converges to the same sum.

### Integration by parts of $\int \frac{dx}{x}$

The argument:

1. Integrate by parts with $u = \frac{1}{x}$ and $v' = 1$, so $u' = -\frac{1}{x^2}$ and $v = x$.
2. This gives $\int \frac{dx}{x} = \frac{1}{x} \cdot x - \int x \cdot \left(-\frac{1}{x^2}\right) dx = 1 + \int \frac{dx}{x}$.
3. Subtract $\int \frac{dx}{x}$ from both sides: $0 = 1$.

The check:

1. Step 2 is valid as an equation between families of [[antiderivatives|1EXDA8HQP5]]. The symbol $\int \frac{dx}{x}$ denotes all functions $\ln|x| + C$ on an interval that does not contain $0$, and [[antiderivatives differ by a constant|QFCQQTBFWC]].
2. Step 3 is invalid. The two symbols $\int \frac{dx}{x}$ in step 2 can denote antiderivatives that differ by a constant, so we cannot cancel them as numbers.
3. The correct form is the [[integration by parts|08Y1BBQTK9]] formula for a definite integral on $[a, b]$ with $0 < a < b$: $\int_a^b \frac{dx}{x} = \left[\frac{1}{x} \cdot x\right]_a^b + \int_a^b \frac{dx}{x}$.
4. The bracket is $1 - 1 = 0$, so the definite form gives $\int_a^b \frac{dx}{x} = \int_a^b \frac{dx}{x}$, which is true and gives no information.

### A negative integral of a positive function

The argument:

1. An antiderivative of $\frac{1}{x^2}$ is $-\frac{1}{x}$.
2. So $\int_{-1}^{1} \frac{dx}{x^2} = \left[-\frac{1}{x}\right]_{-1}^{1} = -1 - 1 = -2$.
3. But $\frac{1}{x^2} > 0$ for every $x \neq 0$, so an integral of it over $[-1, 1]$ cannot be negative.

The check:

1. Step 2 uses the [[fundamental theorem of calculus|0NHGY0N0JB]], which needs an integrand that is continuous on the whole interval $[-1, 1]$.
2. The function $\frac{1}{x^2}$ is not defined at $0$, and it is unbounded near $0$. So step 2 is invalid.
3. The integral is an [[improper integral|05KQ3F99BQ]] at $0$. For $0 < t < 1$, $\int_t^1 \frac{dx}{x^2} = \frac{1}{t} - 1$, which tends to $+\infty$ as $t \to 0^+$.
4. So the integral diverges to $+\infty$, and it is not $-2$.

### Interchanging limits

The argument:

1. Let $a_{m,n} = \frac{m}{m + n}$ for positive integers $m$ and $n$.
2. For fixed $m$, $\lim_{n \to \infty} a_{m,n} = 0$. So $\lim_{m \to \infty} \lim_{n \to \infty} a_{m,n} = 0$.
3. For fixed $n$, $\lim_{m \to \infty} a_{m,n} = 1$. So $\lim_{n \to \infty} \lim_{m \to \infty} a_{m,n} = 1$.
4. "The order of limits does not matter", so $0 = 1$.

The check:

1. Steps 2 and 3 are valid computations: $\frac{m}{m + n} \to 0$ as $n \to \infty$, and $\frac{m}{m + n} = \frac{1}{1 + n/m} \to 1$ as $m \to \infty$.
2. Step 4 is invalid. Two iterated limits can both exist and differ.
3. A correct rule is the [[Moore-Osgood theorem|QN2210XCST]]: if both inner limits exist and one of them is uniform in the other variable, then the two iterated limits exist and are equal.
4. Here neither inner limit is uniform, because $a_{m,m} = \frac{1}{2}$ for every $m$. For example, $\sup_n \left|a_{m,n} - 1\right| = 1$ for every $m$, since $a_{m,n} \to 0$ as $n \to \infty$.

The same error for double series: let $a_{m,n} = 1$ when $n = m$, $a_{m,n} = -1$ when $n = m + 1$, and $a_{m,n} = 0$ otherwise, for $m, n \ge 1$.
Each row $m$ contains one $1$ and one $-1$, so each row sum is $0$, and the sum of the row sums is $0$.
Column $1$ contains only $a_{1,1} = 1$, and each column $n \ge 2$ contains $a_{n,n} = 1$ and $a_{n-1,n} = -1$, so the sum of the column sums is $1$.
[[Fubini's theorem for series|WW53KG71KH]] allows the exchange only when $\sum_{m,n} |a_{m,n}|$ converges, and here this sum is infinite.

## Remarks

### What the examples show

Each infinite operation is a limit, and each rule for finite sums or for numbers holds for limits only under a condition.
The conditions are the following.

1. For grouping, the series converges.
2. For rearranging and for exchanging two sums, the series converges absolutely.
3. For the fundamental theorem of calculus, the integrand is continuous on the closed interval.
4. For exchanging two limits, one of the limits is uniform.

The [[quantifier shift fallacy|CRW82NARQV]] is the logical form of the last error: a pointwise statement is used as if it were uniform.

### How the examples change

If we replace the alternating harmonic series by the absolutely convergent series $\sum_{n \ge 1} \frac{(-1)^{n+1}}{n^2}$, the rearrangement of step 2 has the same sum as the original series.
If we replace $[-1, 1]$ by $[1, 2]$ in the fourth argument, the integrand is continuous on the interval, and $\int_1^2 \frac{dx}{x^2} = \left[-\frac{1}{x}\right]_1^2 = \frac{1}{2}$ is correct.

## Explanations

### L1 human

An infinite sum is not an ordinary sum: it is the value that the finite sums approach.
For $1 - 1 + 1 - 1 + \cdots$ the finite sums are $1, 0, 1, 0, \ldots$, and they approach nothing.
So the infinite sum has no value, and arguments that give it the value $0$, $1$ or $\frac{1}{2}$ compute with something that does not exist.
For $1 - \frac{1}{2} + \frac{1}{3} - \cdots$ the finite sums do approach a value, but a new order of the terms can approach another value.
Rules from finite sums need a proof before we use them for infinite sums.

### L2 human

We test the claim "$\lim_{n \to \infty} \int_0^1 f_n = \int_0^1 \lim_{n \to \infty} f_n$" on $f_n(x) = n^2 x e^{-nx}$.

1. For fixed $x > 0$, $n^2 x e^{-nx} \to 0$ as $n \to \infty$, because the exponential decays faster than $n^2$ grows. Also $f_n(0) = 0$. So the limit function is $0$, and its integral is $0$.
2. Substitute $t = nx$: $\int_0^1 n^2 x e^{-nx}\,dx = \int_0^n t e^{-t}\,dt$.
3. Integration by parts gives $\int_0^n t e^{-t}\,dt = 1 - (n + 1)e^{-n}$, which tends to $1$.
4. So the limit of the integrals is $1$, and the integral of the limit is $0$.

The typical use of such a test is to check a step "take the limit inside the integral" before we trust it.
The correct tools are uniform convergence on $[0, 1]$, or the [[dominated convergence theorem|BYNV84PF86]], and neither applies here.
The convergence is not uniform, because $f_n(1/n) = n/e$ is unbounded, and no integrable function dominates all $f_n$, because the theorem would then give the false equality.
A trap is to check only that each $f_n$ is continuous and that $f_n \to f$ pointwise: here both hold, and the exchange fails.
