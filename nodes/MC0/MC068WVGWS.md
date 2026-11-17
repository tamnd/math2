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
Claim: $P_n < \dfrac{1}{\sqrt{3n}}$ for every $n \ge 1$.
A plain induction on this claim fails, as we show first.
Then we [[strengthen the induction hypothesis|F94KJC2RXP]] to $P_n \le \dfrac{1}{\sqrt{3n + 1}}$, and the [[induction|0ASJVEFA9J]] goes through.

The plain attempt.

1. Assume $P_n < 1/\sqrt{3n}$. Then $P_{n+1} = P_n \cdot \dfrac{2n + 1}{2n + 2} < \dfrac{2n + 1}{(2n + 2)\sqrt{3n}}$.
2. To reach $P_{n+1} < 1/\sqrt{3n + 3}$, it suffices that $\dfrac{(2n + 1)^2}{(2n + 2)^2 \, 3n} \le \dfrac{1}{3n + 3}$, that is, $(2n + 1)^2 (n + 1) \le (2n + 2)^2 n$.
3. Expand: $(2n + 1)^2(n + 1) = 4n^3 + 8n^2 + 5n + 1$ and $(2n + 2)^2 n = 4n^3 + 8n^2 + 4n$.
4. The left side exceeds the right side by $n + 1 > 0$. So the needed inequality is false for every $n \ge 1$, and this step fails.

The strengthened induction, with $Q(n)$: $P_n \le \dfrac{1}{\sqrt{3n + 1}}$.

1. Base case $n = 1$: $P_1 = \tfrac12$ and $\dfrac{1}{\sqrt{3 + 1}} = \tfrac12$. So $Q(1)$ holds, with equality.
2. Induction step: let $n \ge 1$, and assume $Q(n)$. Then $P_{n+1} = P_n \cdot \dfrac{2n + 1}{2n + 2} \le \dfrac{2n + 1}{(2n + 2)\sqrt{3n + 1}}$.
3. It suffices to show $\dfrac{2n + 1}{(2n + 2)\sqrt{3n + 1}} \le \dfrac{1}{\sqrt{3n + 4}}$. Both sides are positive, so we may square them.
4. After squaring and clearing the positive denominators, the inequality reads $(2n + 1)^2 (3n + 4) \le (2n + 2)^2 (3n + 1)$.
5. Expand the left side: $(4n^2 + 4n + 1)(3n + 4) = 12n^3 + 28n^2 + 19n + 4$.
6. Expand the right side: $(4n^2 + 8n + 4)(3n + 1) = 12n^3 + 28n^2 + 20n + 4$.
7. The right side exceeds the left side by $n \ge 1$. So the inequality of step 4 holds, and $Q(n + 1)$ holds by steps 2 and 3, since $3(n + 1) + 1 = 3n + 4$.
8. By induction, $Q(n)$ holds for every $n \ge 1$.
9. Since $3n + 1 > 3n$, we get $P_n \le \dfrac{1}{\sqrt{3n + 1}} < \dfrac{1}{\sqrt{3n}}$. This proves the claim.

The first values are in the table, with decimals rounded to $4$ places.

| $n$ | $1$ | $2$ | $3$ | $4$ | $5$ |
|---|---|---|---|---|---|
| $P_n$ | $1/2 = 0.5000$ | $3/8 = 0.3750$ | $5/16 = 0.3125$ | $35/128 = 0.2734$ | $63/256 = 0.2461$ |
| $1/\sqrt{3n + 1}$ | $0.5000$ | $0.3780$ | $0.3162$ | $0.2774$ | $0.2500$ |
| $1/\sqrt{3n}$ | $0.5774$ | $0.4082$ | $0.3333$ | $0.2887$ | $0.2582$ |

A check by computer with exact fractions confirms $P_n^2 (3n + 1) \le 1$ for $n = 1$ to $29$.

## Remarks

1. The weak claim is true, but it is not strong enough to carry its own induction step. The strong claim is closer to the truth, and it carries its step.
2. The product equals $\binom{2n}{n} / 4^n$, the [[central binomial coefficient|0JPH2Y4DFV]] divided by $4^n$. So the example bounds $\binom{2n}{n} \le 4^n / \sqrt{3n + 1}$.
3. The true size of $P_n$ is about $1/\sqrt{\pi n}$ for large $n$. Since $\pi > 3$, this is below $1/\sqrt{3n + 1}$ for large $n$, in agreement with the example.
4. A strengthening to $1/\sqrt{3n + 2}$ is false at the base: $P_1 = \tfrac12 > 1/\sqrt{5}$. The constant $1$ in $3n + 1$ is the largest constant $c$ for which $P_1 \le 1/\sqrt{3 + c}$.

## Explanations

### L1 human

We multiply the fractions one half, three quarters, five sixths, and so on.
The product gets smaller and smaller, and we want to show that it shrinks at least as fast as one over the square root of three times $n$.
A proof step by step does not work with this exact target, because the target is too loose to pass from one $n$ to the next.
A slightly tighter target, one over the square root of three times $n$ plus one, does pass from each $n$ to the next.
The tighter target is below the first one, so the first claim follows.

### L2 human

We do the step from $n = 2$ to $n = 3$ with numbers.

1. The hypothesis says $P_2 \le 1/\sqrt{7}$. Indeed $P_2^2 = \tfrac{9}{64}$ and $\tfrac{9}{64} \le \tfrac17$, because $63 \le 64$.
2. Then $P_3^2 = P_2^2 \cdot \tfrac{25}{36} \le \tfrac17 \cdot \tfrac{25}{36} = \tfrac{25}{252}$.
3. The target is $P_3^2 \le \tfrac{1}{10}$, and $\tfrac{25}{252} \le \tfrac{1}{10}$ because $250 \le 252$.
4. The margin $252 - 250 = 2$ equals $n = 2$, as step 7 of the strengthened induction predicts.

The typical use of such a strengthening is an estimate of a product or a sum, where the exact constant in the bound is adjusted so that the step closes.
A trap is to adjust the constant so far that the base case fails, as with $1/\sqrt{3n + 2}$.
