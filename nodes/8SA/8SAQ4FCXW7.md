---
tag: 8SAQ4FCXW7
kind: statement
role: proposition
name: Theis solution
msc: [76S05, 86A05, 35K05]
uses: [64DSSBPT5E, EV6ZDQ0NDY, 579J5K9K5Z]
about: [64DSSBPT5E]
sources:
  - url: https://en.wikipedia.org/wiki/Aquifer_test
---

## Statement

Consider a confined aquifer that is horizontal, infinite, homogeneous and isotropic.
Let it have constant transmissivity $T > 0$ and storativity $S > 0$, and let it obey the two-dimensional [[groundwater flow equation|64DSSBPT5E]].
Let the head be uniform at time $0$.
From time $0$ on, let a well at the origin through the full thickness pump water at the constant rate $Q > 0$.
Let the drawdown $s(r, t)$ be the decline of head at distance $r > 0$ from the well.
That is, $s$ satisfies
$$S \frac{\partial s}{\partial t} = T \Big( \frac{\partial^2 s}{\partial r^2} + \frac{1}{r} \frac{\partial s}{\partial r} \Big), \qquad s(r, 0) = 0, \qquad s(r, t) \to 0 \text{ as } r \to \infty, \qquad \lim_{r \to 0} 2 \pi r T \frac{\partial s}{\partial r} = -Q.$$
Then
$$s(r, t) = \frac{Q}{4 \pi T} \, W(u), \qquad u = \frac{r^2 S}{4 T t},$$
where $W(u) = E_1(u) = \int_u^\infty \frac{e^{-x}}{x} \, dx$ is the *well function*, the [[exponential integral|EV6ZDQ0NDY]] $E_1$.

## Remarks

The idea of the proof: the problem has no length or time scale except through $r^2 S / (T t)$, so one looks for a [[similarity solution|579J5K9K5Z]] $s = F(u)$.
The equation becomes $u F'' + (1 + u) F' = 0$, so $F'(u) = -c \, e^{-u} / u$, and $F(\infty) = 0$ gives $F = c \, E_1(u)$.
Since $r \, \partial_r s = 2 u F'(u) = -2 c e^{-u}$, the condition at the well fixes $c = Q / (4 \pi T)$, and $s(r, 0) = 0$ holds because $u \to \infty$ as $t \to 0$.

Example: for small $u$, $W(u) = -\gamma - \ln u + O(u)$, with $\gamma \approx 0.5772$ the Euler–Mascheroni constant.
So at late times $s \approx \frac{Q}{4 \pi T} \ln \frac{2.25 \, T t}{r^2 S}$, since $e^{-\gamma} \cdot 4 \approx 2.25$; this is the Cooper–Jacob approximation.
A plot of drawdown against $\ln t$ is then a straight line of slope $Q / (4 \pi T)$, which gives $T$ from a pumping test.

The infinite extent is needed: in a bounded aquifer with a fixed-head boundary, the drawdown tends to a steady state instead of growing like $\ln t$.

## Explanations

### L1 human

When a well starts pumping, the water level in the ground around it drops, and the dip spreads outward and deepens with time.
The Theis solution gives the exact shape of this dip, for an idealised uniform aquifer.
Its main use runs backward.
By measuring the dip in nearby wells during a pumping test, hydrogeologists find how easily water moves through the aquifer and how much it stores.
Charles Vernon Theis published the solution in 1935, using the analogy between groundwater flow and the flow of heat.

### L2 human

The drawdown depends on $r$ and $t$ only through $r^2 / t$, so curves at different distances collapse onto one type curve $W(u)$.
Matching measured data to this curve gives $T$ and $S$.
The same function solves the problem of a line source of heat in an infinite plane, which is the classical source of the analogy.
Extensions handle leaky aquifers (Hantush–Jacob), unconfined aquifers, and wells of finite radius.
