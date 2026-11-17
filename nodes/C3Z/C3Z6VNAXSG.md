---
tag: C3Z6VNAXSG
kind: example
name: Adding numerators and denominators is not well defined
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug1
not_instance_of:
  - target: HNGZEBKVY2
    note: the result depends on the fractions chosen to represent the rational numbers
uses: [HNGZEBKVY2, KF8H084HDE, 0NCJ5WXN6Z]
sources:
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: Independence of representative
---

## Example

Write each [[rational number|0NCJ5WXN6Z]] as a fraction $\tfrac{a}{b}$ with $b > 0$.
The proposed operation is
$$\frac{a}{b} \oplus \frac{c}{d} := \frac{a + c}{b + d}.$$
We show that $\oplus$ is not [[well defined|HNGZEBKVY2]] on $\mathbb{Q}$.

1. The rule uses the fractions, not only the numbers. So we must test whether equal numbers with different fractions give equal results.
2. Take $\tfrac12$ and $\tfrac13$. The rule gives $\tfrac{1 + 1}{2 + 3} = \tfrac25$.
3. Now write the first number as $\tfrac24$. This is the same rational number, because $1 \cdot 4 = 2 \cdot 2$, by the [[definition of rational numbers by abstraction|KF8H084HDE]].
4. The rule gives $\tfrac24 \oplus \tfrac13 = \tfrac{2 + 1}{4 + 3} = \tfrac37$.
5. The numbers $\tfrac25$ and $\tfrac37$ differ, because $2 \cdot 7 = 14$ and $5 \cdot 3 = 15$.
6. So one pair of inputs gives two different outputs, and $\oplus$ is not an operation on $\mathbb{Q}$.

## Remarks

1. The failure needs only one pair of representatives. One counterexample is enough to show that a rule is not well defined.
2. Without the condition $b > 0$, the rule fails in a second way. The fractions $\tfrac11$ and $\tfrac{1}{-1}$ give $\tfrac{2}{0}$, which is not a fraction.
3. The fraction $\tfrac{a + c}{b + d}$ is called the mediant of $\tfrac{a}{b}$ and $\tfrac{c}{d}$. It is useful for the Farey sequences, where each fraction is written in lowest terms. With this fixed choice of representative it is a function, but it is not compatible with the equality of fractions.
4. The correct sum $\tfrac{ad + bc}{bd}$ passes the test: $\tfrac12 + \tfrac13 = \tfrac56$, and $\tfrac24 + \tfrac13 = \tfrac{10}{12} = \tfrac56$.

## Explanations

### L1 human

A common mistake with fractions is to add the tops and add the bottoms.
One half plus one third would then be two fifths.
But one half is also two quarters, and the same rule now gives three sevenths.
Two fifths and three sevenths are different numbers.
So the rule gives different answers for the same question, and it is not a real way of adding numbers.

### L2 human

We show that the test of step 5 always detects the problem, by a general criterion.

1. The rule $\oplus$ is well defined only if $\tfrac{ka}{kb} \oplus \tfrac{c}{d} = \tfrac{a}{b} \oplus \tfrac{c}{d}$ for each integer $k \geq 1$.
2. The left side is $\tfrac{ka + c}{kb + d}$, and the right side is $\tfrac{a + c}{b + d}$.
3. They are equal exactly when $(ka + c)(b + d) = (a + c)(kb + d)$.
4. Expand both sides and cancel the common terms $kab + cd$. The condition becomes $kad + bc = ad + kbc$, that is, $(k - 1)(ad - bc) = 0$.
5. For $k = 2$, this holds only when $ad = bc$, that is, when $\tfrac{a}{b} = \tfrac{c}{d}$.

So $\oplus$ fails whenever the two inputs are different numbers.
The typical use of this kind of test: multiply the numerator and denominator of one input by $k$, and compare.
A trap is to test only with fractions in lowest terms: then the rule looks like a function, and the failure stays hidden.
