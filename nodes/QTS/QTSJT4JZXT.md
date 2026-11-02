---
tag: QTSJT4JZXT
kind: statement
role: theorem
name: John–Nirenberg inequality
msc: [42B35, 30H35]
uses: [QJYTXFT8Y4, 2Z2QVWZ262, K1YKXVPVDG]
about: [QJYTXFT8Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_mean_oscillation
---

## Statement

Let $n \ge 1$.
There are constants $c_1, c_2 > 0$, depending only on $n$, with the following property.
Let $f$ be a function of [[bounded mean oscillation|QJYTXFT8Y4]] on $\R^n$ that is not constant, with norm $\norm{f}_{\mathrm{BMO}}$.
Let $Q \subseteq \R^n$ be a cube with sides parallel to the axes, let $\abs{E}$ denote [[Lebesgue measure|2Z2QVWZ262]], and let $f_Q = \frac{1}{\abs{Q}}\int_Q f$.
Then for every $\lambda > 0$,
$$\abs{\set{x \in Q : \abs{f(x) - f_Q} > \lambda}} \le c_1 \abs{Q} \exp\left( - \frac{c_2 \lambda}{\norm{f}_{\mathrm{BMO}}} \right).$$

## Remarks

The proof applies the [[Calderón–Zygmund lemma|K1YKXVPVDG]] to $f - f_Q$ on the cube $Q$, at a height of about $2\norm{f}_{\mathrm{BMO}}$.
On the selected subcubes $Q_k$ the mean $f_{Q_k}$ differs from $f_Q$ by at most a constant times $\norm{f}_{\mathrm{BMO}}$, and their total measure is at most half of $\abs{Q}$.
Repeating the argument inside each $Q_k$ shows that the set where $\abs{f - f_Q}$ exceeds $C m \norm{f}_{\mathrm{BMO}}$ has measure at most $2^{-m}\abs{Q}$, which is the exponential decay.

Consequences: for $c < c_2$ the function $\exp(c \abs{f - f_Q}/\norm{f}_{\mathrm{BMO}})$ has average over $Q$ bounded by a constant depending on $n$ and $c$.
Also, for every $1 \le p < \infty$, the quantity $\sup_Q \left( \frac{1}{\abs{Q}} \int_Q \abs{f - f_Q}^p \right)^{1/p}$ is a norm on BMO equivalent to $\norm{f}_{\mathrm{BMO}}$.

Example: $f(x) = \log \abs{x}$ on $\R$ and $Q = [-1, 1]$, where $f_Q = -1$.
The set $\set{\abs{f + 1} > \lambda}$ contains $\set{\abs{x} < e^{-1 - \lambda}}$, of measure $2 e^{-1 - \lambda}$.
So the exponential decay in $\lambda$ cannot be improved to a faster decay for all BMO functions.

## Explanations

### L1 human

A BMO function can be unbounded, but only in a mild way.
The inequality says that on any cube, the set where $f$ is far from its average is exponentially small in the distance.
So BMO functions behave like logarithms: they can blow up, but only very slowly.

### L2 human

The inequality shows that BMO functions are locally integrable to every power, and even exponentially integrable after subtracting means.
It is used to show that $\log w$ is in BMO for every Muckenhoupt weight $w$, and conversely that $e^{\delta b}$ is a Muckenhoupt weight for $b \in$ BMO and $\delta$ small.
It enters the proof of Fefferman's duality theorem and of the boundedness of commutators with BMO functions.
