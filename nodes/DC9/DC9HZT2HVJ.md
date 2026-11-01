---
tag: DC9HZT2HVJ
kind: statement
role: theorem
name: Optional stopping theorem
msc: [60G42, 60G40]
uses: [0CDVK9RQBH, EQ055QMACW, WND87FBAKC, NG35MGYDZR, 0DCT0QZVQ1]
about: [0D0GBNDKDH, WND87FBAKC]
sources:
  - url: https://en.wikipedia.org/wiki/Optional_stopping_theorem
same_as:
  wikidata: Q2027347
  wikipedia: Optional stopping theorem
---

## Statement

Let $(X_n)_{n \ge 0}$ be a [[martingale|0CDVK9RQBH]] with respect to a [[filtration|HNK1Y62G7V]] $(\mathcal{F}_n)_{n \ge 0}$, and let $\tau$ be a [[stopping time|WND87FBAKC]] for $(\mathcal{F}_n)$.
Assume that one of the following holds:

1. There is a constant $N$ with $\tau \le N$ almost surely.
2. $E[\tau] < \infty$, and there is a constant $c$ with $E\bigl[\abs{X_{n+1} - X_n} \mid \mathcal{F}_n\bigr] \le c$ almost surely on the event $\{\tau > n\}$, for all $n \ge 0$.
3. $\tau < \infty$ almost surely, and there is a constant $c$ with $\abs{X_{n \wedge \tau}} \le c$ almost surely for all $n \ge 0$.

Then $X_\tau$ is integrable and $E[X_\tau] = E[X_0]$.
If $(X_n)$ is only a [[submartingale|EQ055QMACW]], the same hypotheses give $E[X_\tau] \ge E[X_0]$.

## Remarks

The [[stopped process|NG35MGYDZR]] $(X_{n \wedge \tau})_{n \ge 0}$ is again a martingale, so $E[X_{n \wedge \tau}] = E[X_0]$ for every $n$.
Each hypothesis lets one pass to the limit $n \to \infty$.
In case 1 take $n = N$.
In cases 2 and 3 use dominated convergence, with the bound $\abs{X_0} + \sum_{k < \tau} \abs{X_{k+1} - X_k}$ in case 2 and the constant $c$ in case 3.
Example: let $S_n$ be the simple symmetric random walk from $0$, let $a, b$ be positive integers, and let $\tau$ be the first time $S_n \in \{-a, b\}$.
Case 3 applies, so $0 = E[S_\tau] = b\,P(S_\tau = b) - a\,(1 - P(S_\tau = b))$, which gives $P(S_\tau = b) = a/(a + b)$.
Some hypothesis is needed: if $\tau$ is the first time the same walk hits $1$, then $\tau < \infty$ almost surely but $E[S_\tau] = 1 \ne 0 = E[S_0]$; here $E[\tau] = \infty$ and the stopped walk is unbounded below.

## Explanations

### L1 human

In a fair game, no rule for deciding when to quit can give you an expected profit.
This is true as long as the rule only uses the past, and the game cannot drag on in an uncontrolled way.
The theorem makes "uncontrolled" precise with three alternative conditions.
Without such conditions, the strategy "play until you are one unit ahead" would beat a fair game, but it may take an unbounded time and unbounded credit.

### L2 human

The theorem is the main tool for computing hitting probabilities and expected hitting times of random walks and Brownian motion.
For example, applying it to the martingale $S_n^2 - n$ in the gambler's ruin gives $E[\tau] = ab$.
It gives a short proof of [[Doob's martingale inequality|4G53E7BRXF]].
In continuous time the same result holds for right-continuous martingales.
For uniformly integrable martingales it holds for all stopping times, with $X_\infty$ the limit from [[Doob's martingale convergence theorems|MRXBC4ZNRR]].
