---
tag: 6F5B8KPEGH
kind: statement
role: theorem
name: Carlson's theorem
msc: ["30D15"]
uses: [0DG0Z72CQD, 9P8D8YAHQS]
about: [9P8D8YAHQS]
sources:
  - url: https://en.wikipedia.org/wiki/Carlson%27s_theorem
same_as:
  wikidata: Q5042898
  wikipedia: Carlson's theorem
---

## Statement

Let $f$ be a continuous function on the closed half-plane $\operatorname{Re} z \ge 0$ that is [[holomorphic|0DG0Z72CQD]] on the open half-plane $\operatorname{Re} z > 0$.
Assume that:

1. there are constants $C, \tau > 0$ such that $\abs{f(z)} \le C e^{\tau \abs{z}}$ for $\operatorname{Re} z \ge 0$;
2. there are constants $C' > 0$ and $c < \pi$ such that $\abs{f(iy)} \le C' e^{c \abs{y}}$ for all real $y$;
3. $f(n) = 0$ for every integer $n \ge 0$.

Then $f$ is identically zero.

## Remarks

Condition 1 says that $f$ has [[exponential type|9P8D8YAHQS]] in the half-plane.
The proof compares $f$ with $\sin(\pi z)$, which vanishes at the integers, and uses the Phragmén–Lindelöf principle to bound $f(z)/\sin(\pi z)$.
The bound $c < \pi$ in condition 2 is sharp: $f(z) = \sin(\pi z)$ satisfies conditions 1 and 3, and $\abs{\sin(\pi i y)} = \abs{\sinh(\pi y)}$, which grows like $e^{\pi \abs{y}}/2$.
Applied to a difference, the theorem shows that two functions of this kind that agree at all nonnegative integers are equal.

## Explanations

### L1 human

A function on the integers can be extended to the complex plane in many ways, for example by adding $\sin(\pi z)$.
Carlson's theorem says that the extension becomes unique once its growth is limited.
The function may grow exponentially, but on the imaginary axis more slowly than $\sin(\pi z)$.

### L2 human

The theorem justifies many formulas that are first proved for integer values and then used for complex values.
For example, two expressions in $z$ that agree for $z = 0, 1, 2, \dots$ and satisfy the growth conditions agree everywhere.
It is used for interpolation of sequences and for questions of uniqueness of Newton series.
Like the [[Paley–Wiener theorem|THY12GPZ8C]], it shows how the exponential type of an entire function controls its behaviour.
