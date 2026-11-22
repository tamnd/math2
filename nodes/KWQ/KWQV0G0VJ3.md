---
tag: KWQV0G0VJ3
kind: concept
name: Sharp and best possible results
aliases: [sharp-bound, best-possible-constant, tight-bound]
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
uses: [0S60DVMVPN, 0R3H5PANRQ, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
  - url: https://en.wikipedia.org/wiki/Bernoulli%27s_inequality
    locator: Integer exponent
---

## Summary

A bound is sharp when nobody can improve it in the form in which it is stated.
You meet the word in sentences such as "for all real $a$ and $b$, $2ab \le a^2 + b^2$, and the inequality is sharp": the constant $1$ in front of $a^2 + b^2$ cannot be made smaller, because $a = b = 1$ gives $2 = 2$.

Here is the exact meaning.
Let a theorem state a bound $f(x) \le C\, g(x)$ for every $x$ in a class $X$, where $g(x) > 0$ and $C$ is a constant.
The constant $C$ is *sharp*, or *best possible*, if no smaller constant works: for every $C' < C$ there is an $x \in X$ with $f(x) > C'\, g(x)$.
Equivalently, $C$ is the [[supremum|0R3H5PANRQ]] of the ratio $f(x)/g(x)$ over $X$.
The bound is *attained* if $f(x_0) = C\, g(x_0)$ for some $x_0 \in X$, and such an $x_0$ is an *equality case* or an *extremal case*.
A lower bound is sharp when no larger constant works, and a hypothesis is sharp when the theorem fails as soon as the hypothesis is weakened.

## Motivation

An [[upper bound|0S60DVMVPN]] answers one question and leaves another open: is the bound the truth, or only a safe estimate?
The inequality $x^2 + 1 \ge 0$ holds for every real $x$, but so does $x^2 + 1 \ge 1$, so the first inequality throws information away.
The word "sharp" marks the bounds that throw nothing away.

A claim of sharpness always has two parts.
The first part proves the bound.
The second part gives an example, or a sequence of examples, that defeats every better bound of the same form.
That second part is a kind of [[counterexample|0ED72CTBNP]]: it refutes each improved bound at once.
When a result is sharp, further progress must change the form of the bound, for example by adding a hypothesis or a new term.
The page on [[stronger and weaker statements|KCK4AQ469Q]] gives the logic behind this: a sharp result has no stronger statement of the same shape.

## Notation

No symbol marks sharpness.
Authors write "the constant is sharp", "the bound is best possible", "the inequality is optimal" or "the estimate is tight"; "tight" is the usual word in computer science, optimization and combinatorics.
The word "sharp" itself has two readings, and you must tell them apart.
In one reading the constant cannot be lowered: "$|a + b| \le |a| + |b|$ is sharp" means that no factor below $1$ works.
In the other reading only the order of growth cannot be lowered: "the bound $O(n \log n)$ is sharp" means that no bound $O(g)$ with $g$ growing more slowly works, and the constant may still be poor.
To tell which one an author means, look at the sharpness proof: one equality case shows the exact constant, while a family of examples whose ratio stays above a fixed number shows only the order.
Careful authors write "sharp up to a constant" for the second reading.

## Remarks

### A first sharpness proof

Take the triangle inequality for real numbers, which [[the triangle inequality is sharp|23C4T641PC]] works out in full.
The bound $|a + b| \le |a| + |b|$ holds for all real $a$ and $b$.
At $a = 2$ and $b = 3$ both sides are equal:
$$|2 + 3| = 5 = |2| + |3|.$$
Now try a smaller constant $c < 1$.
At $a = 1$ and $b = 0$ the bound $|a + b| \le c(|a| + |b|)$ would say $1 \le c$, which is false.
So the constant $1$ is best possible.

The [[AM-GM inequality for two numbers|KRHB5XFDVA]] follows the same pattern.
For $a, b \ge 0$ we have $\sqrt{ab} \le \tfrac{1}{2}(a + b)$, and $a = b = 1$ gives $1 = 1$, so the constant $\tfrac{1}{2}$ cannot be lowered.
In graph theory the [[four color theorem|0M406JC8J1]] says that every finite planar graph can be colored with $4$ colors, and the complete graph $K_4$ is planar and needs all $4$, so the number $4$ is sharp.

### Sharp but never attained

A sharp constant need not be reached.
For every $x > 0$ we have $\frac{x}{1 + x} < 1$, so no $x$ gives equality.
Still, no constant $C' < 1$ works.
For $0 < C' < 1$, take any $x > \frac{C'}{1 - C'}$ and rearrange:
$$x(1 - C') > C' \quad \Longleftrightarrow \quad x > C'(1 + x) \quad \Longleftrightarrow \quad \frac{x}{1 + x} > C'.$$
Check: with $C' = 0.9$ the threshold is $9$, and $x = 10$ gives $\frac{10}{11} \approx 0.909 > 0.9$.

So the sharp constant is the supremum $1$ of the ratio, and a sequence $x_k \to \infty$ proves sharpness in place of a single equality case.
In general, attained implies sharp: if $f(x_0) = C\, g(x_0)$ with $g(x_0) > 0$, then $f(x_0) > C'\, g(x_0)$ for each $C' < C$.
The converse fails, as this case shows.

### A sharp hypothesis: Bernoulli's inequality

[[Bernoulli's inequality|0M1MX28VXK]] $(1 + x)^n \ge 1 + n x$ is usually stated for integers $n \ge 1$ and real $x \ge -1$.
The hypothesis $x \ge -1$ is not sharp: the inequality also holds for $-2 \le x < -1$.
For $n = 1$ both sides equal $1 + x$.
For $n \ge 2$, put $y = 1 + x$, so $-1 \le y < 0$ and $y^n \ge -1$.
Since $x < -1$, we get $1 + n x < 1 - n \le -1 \le (1 + x)^n$.

The threshold $-2$ is sharp.
Let $x = -2 - t$ with $t > 0$, and take $n$ odd with $n \ge 3$ and $n > 4/t^2$.
The binomial theorem and $n t^2 > 4$ give
$$(1 + t)^n \ge 1 + n t + \tfrac{1}{2} n (n - 1) t^2 > 1 + n t + 2(n - 1).$$
Since $n$ is odd, $(1 + x)^n = -(1 + t)^n < 1 - 2n - n t = 1 + n x$, so the inequality fails.
Check: $x = -3$ and $n = 5$ give $(-2)^5 = -32$ and $1 - 15 = -14$, and $-32 < -14$.

### Bounds that are not sharp

[[The bound $x^2 + 1 \ge 0$ is true but not sharp|28W5EM2SG8]], because the larger lower bound $1$ also holds and is attained at $x = 0$.
The bound $\pi(x) \le x$ on the [[prime-counting function|0RQSNVTFVZ]] is true for $x \ge 1$ and far from sharp.
The [[prime number theorem|0EHBY5Y84N]] gives $\pi(x)/x \to 0$, so for each $c > 0$ the bound $\pi(x) \le c x$ holds for all large $x$.

Sharpness is always relative to a form.
The triangle inequality is sharp among the bounds $C(|a| + |b|)$, but at $a = 1$ and $b = -1$ the left side is $0$ and the right side is $2$.
So a sharp bound can be far from the truth for many single inputs; it is only unbeatable over the whole class.

### Watch out

The first error is to treat "sharp" as "attained".
The bound $\frac{x}{1 + x} < 1$ is sharp and never attained, so a proof that searches for one equality case will fail, and a sequence is needed.

The second error is to use an equality case that breaks a hypothesis.
For the AM-GM inequality, $a = b = -1$ would give $\sqrt{1} = 1 > -1 = \tfrac{1}{2}(a + b)$, but negative numbers are outside the class, so this shows nothing about the constant.

The third error is to test a bound on random inputs and conclude that it is not sharp.
Random inputs rarely land near the equality case: random pairs $(a, b)$ almost never have $a = b$, and the AM-GM ratio is $1$ only there.

### History

The study of best constants and of the cases of equality is a main theme of the book *Inequalities* by Hardy, Littlewood and Pólya, first published in 1934.
The constant in [[Hardy's inequality|S7A8YFGG8X]] is a standard case of a best possible constant that no nonzero sequence attains.

### Try it

First, find the sharp constant $C$ in $|a - b| \le C(|a| + |b|)$ over all real $a$ and $b$.
The bound holds with $C = 1$ by the triangle inequality applied to $a + (-b)$, and $a = 1$, $b = -1$ gives $2 = 2$, so $C = 1$ is sharp.

Second, is the bound $\sin x \le 1$ over the real numbers sharp, and is it attained?
It is sharp and attained, since $\sin(\pi/2) = 1$.

Third, is $e^{-x} > 0$ over $x \ge 0$ a sharp lower bound?
Yes: $e^{-x}$ tends to $0$, so no constant $c > 0$ is a lower bound, but no $x$ gives $e^{-x} = 0$.

## Explanations

### L1 human

A bound is sharp when it cannot be made any better.
Every rectangle with perimeter $4$ has area at most $1$.
This bound is sharp, because the square with side $1$ has perimeter $4$ and area exactly $1$.
If someone claims "the area is at most $0.9$", the square shows that the claim is false.
The bound "the area is at most $100$" is also true, but it is not sharp.

### L2 human

We find the best constant $C$ such that $2ab \le C(a^2 + b^2)$ for all real $a$ and $b$.
Start from a square, which is never negative, and expand it:
$$0 \le (a - b)^2 = a^2 - 2ab + b^2, \qquad \text{so} \qquad 2ab \le a^2 + b^2.$$
So $C = 1$ works.

Now test a smaller constant $C' < 1$ at $a = b = 1$.
The left side is $2$, and the right side is $2C' < 2$, so the bound with $C'$ fails.
Hence $C = 1$ is the sharp constant, and the equality cases are exactly the pairs with $a = b$, because $(a - b)^2 = 0$ only then.

The example shows the usual two steps of a sharpness proof: prove the bound, then exhibit the input where it is tight.
The proof of the bound often tells you where to look, since equality holds exactly where the square in the proof vanishes.

### L3 human

The sharp constant in $f \le C g$ is the value of an optimization problem, often the norm of an operator, so a proof of sharpness is a lower bound for that value.
In analysis, sharp constants in functional inequalities, such as the [[isoperimetric inequality|KBX8RBZ626]] and Hardy's inequality, lead to the study of extremal functions.
They also lead to questions of stability: how close must a function be to an extremal one when the inequality is almost an equality?
In combinatorics, an upper bound is often matched by a construction, and the result is tight when the construction meets the bound exactly, or "tight up to a constant" when only the order of growth matches.
For hypotheses, the same idea appears as a counterexample that satisfies every hypothesis except a weakened one, and it shows that the hypothesis cannot be relaxed.
