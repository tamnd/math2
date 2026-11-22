---
tag: MC068WVGWS
kind: example
name: The product of (2k − 1)/(2k) is at most 1/√(3n + 1)
msc: ["00A35", "26D15"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [F94KJC2RXP, 0ASJVEFA9J]
uses: [F94KJC2RXP, 0ASJVEFA9J, 0JPH2Y4DFV]
sources:
  - url: https://en.wikipedia.org/wiki/Central_binomial_coefficient
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Example

For each integer $n \ge 1$, let
$$P_n = \prod_{k=1}^{n} \frac{2k - 1}{2k} = \frac12 \cdot \frac34 \cdot \frac56 \cdots \frac{2n - 1}{2n}.$$
We want the claim $P_n < \dfrac{1}{\sqrt{3n}}$ for every $n \ge 1$.
A plain [[induction|0ASJVEFA9J]] on this claim fails, and we see why first.
Then we [[strengthen the induction hypothesis|F94KJC2RXP]] to $P_n \le \dfrac{1}{\sqrt{3n + 1}}$, and the induction goes through.

**The plain attempt.**
Assume $P_n < 1/\sqrt{3n}$, and multiply by the next factor:
$$P_{n+1} = P_n \cdot \frac{2n + 1}{2n + 2} < \frac{2n + 1}{(2n + 2)\sqrt{3n}}.$$
To reach $P_{n+1} < 1/\sqrt{3n + 3}$ from here, we need $(2n + 1)^2 (3n + 3) \le (2n + 2)^2 \cdot 3n$, that is, $(2n + 1)^2 (n + 1) \le (2n + 2)^2 n$.
Expand both sides:
$$(2n + 1)^2(n + 1) = 4n^3 + 8n^2 + 5n + 1, \qquad (2n + 2)^2 n = 4n^3 + 8n^2 + 4n.$$
The left side is larger by $n + 1$, so the needed inequality is false for every $n \ge 1$, and the step cannot be completed this way.

**The strengthened induction**, with $Q(n)$: $P_n \le \dfrac{1}{\sqrt{3n + 1}}$.

1. Base case $n = 1$.
   We have $P_1 = \tfrac12$ and $\dfrac{1}{\sqrt{3 + 1}} = \tfrac12$, so $Q(1)$ holds with equality.
2. Induction step.
   Let $n \ge 1$, and assume $Q(n)$.
   Multiply by the next factor:
   $$P_{n+1} = P_n \cdot \frac{2n + 1}{2n + 2} \le \frac{2n + 1}{(2n + 2)\sqrt{3n + 1}}.$$
3. Since $3(n + 1) + 1 = 3n + 4$, it suffices to show that the right side is at most $1/\sqrt{3n + 4}$.
   Both numbers are positive, so we may square them and clear the positive denominators:
   $$(2n + 1)^2 (3n + 4) \le (2n + 2)^2 (3n + 1).$$
4. Expand both sides:
   $$(4n^2 + 4n + 1)(3n + 4) = 12n^3 + 28n^2 + 19n + 4, \qquad (4n^2 + 8n + 4)(3n + 1) = 12n^3 + 28n^2 + 20n + 4.$$
   The right side is larger by $n > 0$, so the inequality of step 3 holds, and $Q(n + 1)$ follows.
5. By induction, $Q(n)$ holds for every $n \ge 1$.
6. Since $3n + 1 > 3n$, we get $P_n \le \dfrac{1}{\sqrt{3n + 1}} < \dfrac{1}{\sqrt{3n}}$, which is the claim.

The first values, with decimals rounded to $4$ places, are in the table.

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| $P_n$ | $1/2 = 0.5000$ | $3/8 = 0.3750$ | $5/16 = 0.3125$ | $35/128 = 0.2734$ | $63/256 = 0.2461$ |
| $1/\sqrt{3n + 1}$ | $0.5000$ | $0.3780$ | $0.3162$ | $0.2774$ | $0.2500$ |
| $1/\sqrt{3n}$ | $0.5774$ | $0.4082$ | $0.3333$ | $0.2887$ | $0.2582$ |

## Remarks

The weak claim is true, but it is too loose to carry its own step.
The strong claim is closer to the truth, and the small margin $n$ in step 4 is exactly what the step needs.
So a sharper bound can be easier to prove than a weaker one, which is the whole idea of strengthening.

The product has a closed form: $P_n = \binom{2n}{n} / 4^n$, the [[central binomial coefficient|0JPH2Y4DFV]] divided by $4^n$.
So the example also proves $\binom{2n}{n} \le 4^n / \sqrt{3n + 1}$.
Check at $n = 3$: $\binom{6}{3} = 20$ and $20/64 = 5/16$.
For large $n$, $P_n$ is about $1/\sqrt{\pi n}$, and since $\pi > 3$ this agrees with the bound.

The constant $1$ in $3n + 1$ cannot grow.
For a bound $1/\sqrt{3n + c}$ the base case needs $\tfrac12 \le 1/\sqrt{3 + c}$, that is, $c \le 1$.
So a further strengthening to $1/\sqrt{3n + 2}$ is false already at $n = 1$, where $\tfrac12 > 1/\sqrt{5}$.

## Explanations

### L1 human

We multiply the fractions one half, three quarters, five sixths, and so on.
The product gets smaller, and we want to show that it shrinks at least as fast as one over the square root of $3n$.
A step-by-step proof with exactly that target does not work, because the target leaves no room to pass from one $n$ to the next.
A slightly tighter target, one over the square root of $3n + 1$, does pass from each $n$ to the next.
The tighter target lies below the first one, so the first claim follows.

### L2 human

We run the step from $n = 2$ to $n = 3$ with squares, to avoid roots.
The hypothesis says $P_2^2 \le \tfrac17$, and indeed $P_2^2 = \tfrac{9}{64} \le \tfrac17$ because $63 \le 64$.
Multiply by the square of the next factor, $\left(\tfrac56\right)^2 = \tfrac{25}{36}$:
$$P_3^2 \le \frac17 \cdot \frac{25}{36} = \frac{25}{252}.$$
The target is $P_3^2 \le \tfrac{1}{10}$, and $\tfrac{25}{252} \le \tfrac{1}{10}$ because $250 \le 252$.
The margin $252 - 250 = 2$ equals $n = 2$, as step 4 of the strengthened induction predicts.

The usual use of such a strengthening is an estimate of a product or a sum, where we adjust a constant in the bound until the step closes.
Watch out: adjust it too far and the base case fails, as with $1/\sqrt{3n + 2}$.
