---
tag: TDBBJNW91Z
kind: definition
name: Multiple integral
msc: [26B15]
defines: FE1ZZJ8QW2
uses: [0JAEHXTVV5, 0W29TBTY12, 0KTGJW1ZTH, 0WAR4F23B4, 0698M7C7AX]
sources:
  - url: https://en.wikipedia.org/wiki/Multiple_integral
---

## Definition

Let $n \ge 1$ and let $B = [a_1, b_1] \times \cdots \times [a_n, b_n]$ be a closed box in $\R^n$ with $a_i < b_i$.
Its volume is $\abs{B} = (b_1 - a_1) \cdots (b_n - a_n)$.
A partition $P$ of $B$ is given by a partition of each interval $[a_i, b_i]$; it cuts $B$ into finitely many subboxes $B_1, \dots, B_N$.
The mesh of $P$ is the largest diameter of the $B_j$.
A tagged partition also chooses a point $\xi_j \in B_j$ for each $j$.
For a function $f \colon B \to \R$, the [[Riemann sum|0JAEHXTVV5]] of a tagged partition is $\sum_{j=1}^N f(\xi_j) \abs{B_j}$.

The function $f$ is *Riemann integrable* on $B$ if there is a real number $I$ with the following property.
For each $\varepsilon > 0$ there is $\delta > 0$ such that every tagged partition of mesh less than $\delta$ has a Riemann sum within $\varepsilon$ of $I$.
Then $I$ is the *multiple integral* of $f$ over $B$, written
$$\int_B f \, dV = \int \cdots \int_B f(x_1, \dots, x_n) \, dx_1 \cdots dx_n.$$

Let $A \subseteq \R^n$ be bounded and let $f \colon A \to \R$.
Let $f_A$ be the function on a closed box $B \supseteq A$ that equals $f$ on $A$ and $0$ on $B \setminus A$.
Then $f$ is integrable on $A$ if $f_A$ is integrable on $B$, and $\int_A f \, dV = \int_B f_A \, dV$.
This does not depend on the choice of $B$.

## Remarks

For $n = 1$ this is the [[Riemann integral|0W29TBTY12]]; for $n = 2$ and $n = 3$ it is the [[double integral|0WAR4F23B4]] and the [[triple integral|0698M7C7AX]].
A bounded set $A$ is [[Jordan measurable|0KTGJW1ZTH]] exactly when the constant $1$ is integrable on $A$, and then $\int_A 1 \, dV$ is the Jordan measure of $A$.

Example: $f(x, y) = xy$ on $B = [0, 1]^2$.
The function is continuous, so it is integrable, and computing it as an iterated integral gives $\int_0^1 \int_0^1 xy \, dx \, dy = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$.

Non-example: let $f$ on $[0, 1]^2$ be $1$ at points with both coordinates rational and $0$ elsewhere.
Every subbox contains points of both kinds, so some tagged partitions of any mesh have Riemann sum $1$ and others have Riemann sum $0$.
No number $I$ satisfies the condition, so $f$ is not Riemann integrable.
