---
tag: A1NXVMGPG0
kind: example
name: Euler's evaluation of the Basel sum as plausible reasoning
msc: ["00A35", "11M06"]
topics: [DME0TPC348]
audience: ug2
instance_of: [8DHD3H1CJ9]
uses: [8DHD3H1CJ9, 0DMY75D6FV, 0XCYA4YERS]
sources:
  - url: https://en.wikipedia.org/wiki/Basel_problem
    locator: Euler's approach
  - url: https://en.wikipedia.org/wiki/Mathematics_and_Plausible_Reasoning
    locator: lead section
---

## Example

The [[Basel problem|0DMY75D6FV]] asks for the exact value of
$$1 + \frac{1}{4} + \frac{1}{9} + \frac{1}{16} + \cdots = \sum_{n=1}^{\infty} \frac{1}{n^2}.$$
Leonhard Euler found $\pi^2/6$ by an argument that was not a proof in his time.
We follow it as [[plausible reasoning|8DHD3H1CJ9]]: an analogy gives a conjecture, and checks of its consequences make it more credible.

1. A fact about polynomials.
   If $p$ has degree $m$, the value $p(0) = 1$ and the nonzero roots $a_1, \ldots, a_m$, then $p(x) = (1 - x/a_1) \cdots (1 - x/a_m)$, because both sides have the same roots and the same value at $0$.
   The coefficient of $x$ is $-(1/a_1 + \cdots + 1/a_m)$, from the term $-x/a_i$ of one factor times $1$ from the others.
2. The function.
   The sine series gives
   $$\frac{\sin x}{x} = 1 - \frac{x^2}{6} + \frac{x^4}{120} - \cdots,$$
   with value $1$ at $x = 0$ and zeros at $\pm \pi, \pm 2\pi, \pm 3\pi, \ldots$.
3. The analogy.
   Euler treated $\sin x / x$ as a polynomial of infinite degree, so step 1 suggests
   $$\frac{\sin x}{x} = \prod_{n=1}^{\infty} \left(1 - \frac{x}{n\pi}\right)\left(1 + \frac{x}{n\pi}\right) = \prod_{n=1}^{\infty} \left(1 - \frac{x^2}{n^2 \pi^2}\right).$$
4. The conjecture.
   The coefficient of $x^2$ is $-1/6$ on the left and $-\sum_n 1/(n^2 \pi^2)$ on the right, so
   $$\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}.$$
5. A numerical check.
   The sum of the first $1000$ terms is $1.6439345\ldots$, and the tail beyond $1000$ is about $1/1000$.
   The total $1.6449345\ldots$ agrees with $\pi^2/6 = 1.6449340\ldots$ to the accuracy of the tail estimate.
6. A check of a new kind.
   Put $x = \pi/2$ in step 3, where $\sin(\pi/2) = 1$:
   $$\frac{2}{\pi} = \prod_{n=1}^{\infty} \left(1 - \frac{1}{4n^2}\right).$$
   This is the [[Wallis product|0XCYA4YERS]], which was already a theorem.

Each check is a true consequence of the analogy, so the analogy and its conclusion become more credible.
The Wallis product carries the most weight, because it was proved by other means and is a different kind of fact from a sum of numbers.

## Remarks

### Where the argument has a gap

Step 3 is not valid as it stands.
The function $e^x \sin x / x$ has the same zeros and the same value at $0$, but it is a different function.
So "same zeros and same value at $0$" does not determine an infinite product, and the analogy needs a theorem to become a proof.
Today the [[Weierstrass factorization theorem|11VC51YHQJ]], together with the growth of the sine, supplies that theorem, and Euler himself later gave other proofs.

### More consequences of the same analogy

The coefficient of $x^4$ gives a second test.
On the left it is $1/120$.
On the right a term $x^4$ comes from two different factors $m < n$, so the coefficient is $\sum_{m < n} 1/(m^2 n^2 \pi^4)$, and
$$\sum_{m < n} \frac{1}{m^2 n^2} = \frac{\pi^4}{120}.$$
Squaring the sum of step 4 gives $\left(\pi^2/6\right)^2 = \sum 1/n^4 + 2 \cdot \pi^4/120$, so
$$\sum_{n=1}^{\infty} \frac{1}{n^4} = \frac{\pi^4}{36} - \frac{\pi^4}{60} = \frac{\pi^4}{90} = 1.0823232\ldots,$$
and a numerical sum agrees.
The coefficient of $x^6$ predicts $\sum 1/n^6 = \pi^6/945$, which is also true.

### Watch out

The checks raise confidence in the method, but they do not repair the gap in step 3.
A pattern that holds in many cases is not a proof, and here all the cases come from one unproved analogy.
An analogy can also mislead: a product that misses a zero, or adds a factor like $e^x$, passes the value test at $0$ and gives wrong coefficients.

### Try it

Check $\sum 1/n^4 = \pi^4/90$ with three terms.
The terms $1 + 1/16 + 1/81 = 1.0748\ldots$, against $\pi^4/90 = 1.0823\ldots$, and the gap shrinks as you add terms.

What does $x = \pi/3$ give in the product of step 3?
It gives $\dfrac{3\sqrt{3}}{2\pi} = \prod_{n \ge 1} \left(1 - \dfrac{1}{9n^2}\right)$, since $\sin(\pi/3) = \sqrt{3}/2$.

## Explanations

### L1 human

Euler wanted the exact value of $1 + \frac14 + \frac19 + \frac1{16} + \cdots$.
He guessed it with an idea that was not fully justified: he treated the sine function like a very long polynomial.
The idea gave $\pi^2/6$, which is about $1.645$.
He then tested the idea in other ways, by adding many terms on paper and by getting an old formula for $\pi$ from it.
Every test agreed, so he became confident, even before a full proof existed.

### L2 human

We check the Wallis product of step 6 with its first factors.
The factors are
$$1 - \frac{1}{4} = \frac{3}{4}, \quad 1 - \frac{1}{16} = \frac{15}{16}, \quad 1 - \frac{1}{36} = \frac{35}{36},$$
and their product is $\frac{3 \cdot 15 \cdot 35}{4 \cdot 16 \cdot 36} = \frac{1575}{2304} \approx 0.6836$.
The target is $2/\pi \approx 0.6366$, and more factors move the product down toward it.
The typical use: a heuristic that gives one result also gives others, and checking those others tests the heuristic.
