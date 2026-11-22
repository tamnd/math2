---
tag: KRHB5XFDVA
kind: example
name: The AM-GM inequality for two numbers is sharp
msc: ["00A35", "26D15"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [KWQV0G0VJ3]
uses: [0DRF0F3XC9, KWQV0G0VJ3]
sources:
  - url: https://en.wikipedia.org/wiki/AM%E2%80%93GM_inequality
    locator: lead section
---

## Example

The [[inequality of arithmetic and geometric means|0DRF0F3XC9]] for two numbers states
$$\sqrt{ab} \le \tfrac{1}{2}(a + b) \quad \text{for all real } a, b \ge 0.$$
We show that the constant $\tfrac{1}{2}$ is [[sharp|KWQV0G0VJ3]], and we find all the equality cases.

1. The bound holds.
   For $a, b \ge 0$ the square roots $\sqrt{a}$ and $\sqrt{b}$ are real, and a square is never negative:
   $$0 \le (\sqrt{a} - \sqrt{b})^2 = a - 2\sqrt{ab} + b.$$
   Move $2\sqrt{ab}$ to the left and divide by $2$ to get the inequality.
2. The bound is attained.
   At $a = b = 1$ the left side is $\sqrt{1} = 1$ and the right side is $\tfrac{1}{2}(1 + 1) = 1$.
3. No smaller constant works.
   Let $c < \tfrac{1}{2}$.
   At $a = b = 1$ the bound $\sqrt{ab} \le c(a + b)$ would say $1 \le 2c$, but $2c < 1$.
4. We find the equality cases.
   Equality in step 1 holds exactly when $(\sqrt{a} - \sqrt{b})^2 = 0$, that is, when $\sqrt{a} = \sqrt{b}$, that is, when $a = b$.

Check: at $a = 4$ and $b = 9$ the two sides are $\sqrt{36} = 6$ and $6.5$, and $6 < 6.5$ as step 4 predicts for $a \ne b$.

So the constant $\tfrac{1}{2}$ is best possible, and the extremal cases are the pairs $(a, a)$ with $a \ge 0$.

## Remarks

The example shows the usual shape of a sharpness proof: a proof of the bound, then one equality case that blocks every smaller constant.
The proof of the bound also points to the equality case, since equality needs the square in step 1 to vanish.

The equality case $a = b = 0$ blocks an additive improvement too.
The bound cannot become $\sqrt{ab} \le \tfrac{1}{2}(a + b) - \varepsilon$ for a fixed $\varepsilon > 0$, because at $a = b = 0$ it would give $0 \le -\varepsilon$.

For $n$ numbers the constant $\tfrac{1}{n}$ in $\sqrt[n]{x_1 \cdots x_n} \le \tfrac{1}{n}(x_1 + \dots + x_n)$ is sharp for the same reason: all $x_i = 1$ give equality.
The class matters.
If we allow only pairs with $a \ge 2b > 0$, the equality case $a = b$ is gone, and the best constant on that class is smaller than $\tfrac{1}{2}$: the ratio $\sqrt{ab}/(a + b)$ is largest at $a = 2b$, where it equals $\sqrt{2}/3 \approx 0.471$.

## Explanations

### L1 human

The average of two numbers is never smaller than their geometric mean.
For $4$ and $9$ the average is $6.5$ and the geometric mean is $\sqrt{36} = 6$.
For $5$ and $5$ both means equal $5$.
Because the two sides can be equal, no better general bound of this kind exists.

### L2 human

A rectangle with sides $a$ and $b$ has area $ab$ and perimeter $P = 2(a + b)$, so $a + b = P/2$.
Square the inequality and use this:
$$ab \le \tfrac{1}{4}(a + b)^2 = \frac{P^2}{16}.$$
The square with $a = b = P/4$ has area $P^2/16$, so the bound is attained.
Hence among all rectangles with perimeter $P$, the square has the largest area.
This is the typical use of a sharp inequality in optimization: the bound gives the maximum, and the equality case gives the point where the maximum is reached.
The equality case must lie in the class, and here the square with side $P/4$ does.
