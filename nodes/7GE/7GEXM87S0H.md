---
tag: 7GEXM87S0H
kind: example
name: The exponential map from the additive reals to the positive reals
msc: [20A05]
topics: [BAZT8JJ70S]
audience: school
instance_of: [08MG7H8JW5, 0JYTG5K9Y4]
illustrates: [0N2P0XRTDF]
uses: [0RMVS7RXZX, 08J2M1JYAG, 085PND4KNT, 0J0FCWV32D, 04DXAFN2ES, 0JYTG5K9Y4]
sources:
  - url: https://en.wikipedia.org/wiki/Group_isomorphism
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Group_homomorphism
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Slide_rule
    locator: lead section
---

## Example

Let $(\mathbb{R}, +)$ be the [[real numbers|08J2M1JYAG]] with addition.
Let $(\mathbb{R}_{>0}, \times)$ be the positive real numbers with multiplication.
Both are [[groups|G5S1M9]]: the identity of the first is $0$, and the identity of the second is $1$.
We show that the [[exponential function|0J0FCWV32D]] $\exp \colon \mathbb{R} \to \mathbb{R}_{>0}$, $x \mapsto e^x$, is an [[isomorphism|08MG7H8JW5]], and that the [[natural logarithm|04DXAFN2ES]] is its inverse.

1. The map is well defined: $\exp(x) > 0$ for each real $x$, so $\exp(x) \in \mathbb{R}_{>0}$.
2. The law of exponents gives $\exp(x + y) = \exp(x) \exp(y)$ for all $x, y \in \mathbb{R}$. So $\exp$ is a [[group homomorphism|0JYTG5K9Y4]] from $(\mathbb{R}, +)$ to $(\mathbb{R}_{>0}, \times)$.
3. The [[kernel|0W88CEGQP1]] is the set of $x$ with $\exp(x) = 1$, the identity of the target. The function $\exp$ is strictly increasing and $\exp(0) = 1$, so the kernel is $\{0\}$.
4. A homomorphism with kernel equal to the identity alone is injective, by [[this statement|0N2P0XRTDF]]. So $\exp$ is injective.
5. For each $y > 0$, the number $\ln y$ is a real number with $\exp(\ln y) = y$, because [[the logarithm is the inverse of the exponential|0RKW2X63YR]]. So $\exp$ is surjective.
6. By steps 2, 4 and 5, $\exp$ is a bijective homomorphism, that is, an isomorphism.
7. The inverse map is $\ln \colon \mathbb{R}_{>0} \to \mathbb{R}$. It is also a homomorphism: $\ln(ab) = \ln a + \ln b$ for all $a, b > 0$, by [[the logarithm of a product|0K2FNY6DYV]].

So $(\mathbb{R}, +) \cong (\mathbb{R}_{>0}, \times)$, and $\exp$ and $\ln$ are inverse isomorphisms.

## Remarks

### What the example shows

An isomorphism can join two groups whose operations look different.
Under $\exp$, the sum $x + y$ becomes the product $e^x e^y$, the identity $0$ becomes $1$, and the inverse $-x$ becomes $1 / e^x$.
The two groups are the same group, written in two different ways.

### A finite case: the sign group

The group $\mathbb{Z}/2 = \{0, 1\}$ of [[integers modulo 2|03VFZ2WETT]] under addition is isomorphic to $\{1, -1\}$ under multiplication.
The map is $\varphi(k) = (-1)^k$, so $\varphi(0) = 1$ and $\varphi(1) = -1$.
Here are the two tables.

| $+$ | $0$ | $1$ |
|---|---|---|
| $0$ | $0$ | $1$ |
| $1$ | $1$ | $0$ |

| $\times$ | $1$ | $-1$ |
|---|---|---|
| $1$ | $1$ | $-1$ |
| $-1$ | $-1$ | $1$ |

We check $\varphi(a + b) = \varphi(a)\varphi(b)$ for the four pairs.

1. $\varphi(0 + 0) = \varphi(0) = 1$ and $\varphi(0)\varphi(0) = 1 \cdot 1 = 1$.
2. $\varphi(0 + 1) = \varphi(1) = -1$ and $\varphi(0)\varphi(1) = 1 \cdot (-1) = -1$.
3. $\varphi(1 + 0) = \varphi(1) = -1$ and $\varphi(1)\varphi(0) = (-1) \cdot 1 = -1$.
4. $\varphi(1 + 1) = \varphi(0) = 1$, since $1 + 1 = 0$ in $\mathbb{Z}/2$, and $\varphi(1)\varphi(1) = (-1)(-1) = 1$.

The map $\varphi$ is a bijection, so it is an isomorphism.
When we rename $0$ as $1$ and $1$ as $-1$, the first table becomes the second.
The group $\{1, -1\}$ is the [[group of square roots of unity|0WX11EA3F3]], and the [[sign of a permutation|02DKV69ZH0]] takes its values in it.

### An application: the slide rule

The logarithm $\log_{10} x = \ln x / \ln 10$ is also an isomorphism from $(\mathbb{R}_{>0}, \times)$ to $(\mathbb{R}, +)$, because $\log_{10}(xy) = \log_{10} x + \log_{10} y$.
A slide rule has two scales on which each number $x$ is marked at the distance $\log_{10} x$ from the mark $1$.
To multiply $x$ by $y$, we put the mark $1$ of the second scale at $x$ on the first scale.
The mark $y$ of the second scale is then at the distance $\log_{10} x + \log_{10} y = \log_{10}(xy)$ from the mark $1$ of the first scale.
So we read the product $xy$ there.
For example, $\log_{10} 2 \approx 0.301$ and $\log_{10} 3 \approx 0.477$, and their sum $0.778$ is $\log_{10} 6$ to three places.
The isomorphism changes a hard operation, multiplication, into an easy one, addition of lengths.
Before electronic calculators, engineers used slide rules and printed tables of logarithms for this reason.

### Changes to the example

The map $\exp$ is not an isomorphism from $(\mathbb{R}, +)$ to $(\mathbb{R} \setminus \{0\}, \times)$, because no real $x$ has $\exp(x) = -1$.
In fact the two groups are not isomorphic: $-1$ has order $2$ in $(\mathbb{R} \setminus \{0\}, \times)$, but in $(\mathbb{R}, +)$ the equation $x + x = 0$ gives $x = 0$, so no element has order $2$.
For any base $b > 0$ with $b \ne 1$, the map $x \mapsto b^x$ is also an isomorphism from $(\mathbb{R}, +)$ to $(\mathbb{R}_{>0}, \times)$.

## Explanations

### L1 human

The exponential turns adding into multiplying: $e^{2 + 3} = e^2 \cdot e^3$.
The logarithm does the opposite and turns multiplying into adding.
So a problem about products of positive numbers can be changed into a problem about sums, and back again.
For example, $\log_{10} 100 = 2$ and $\log_{10} 1000 = 3$, and $\log_{10}(100 \cdot 1000) = 2 + 3 = 5$, because $100 \cdot 1000 = 100000$.
A slide rule uses this: it multiplies two numbers by putting two lengths end to end.
In the language of groups, adding real numbers and multiplying positive numbers are the same group in two disguises.

### L2 human

We check the homomorphism rule and the inverse at two numbers.

1. Take $x = \ln 2$ and $y = \ln 5$. Then $\exp(x) = 2$ and $\exp(y) = 5$.
2. The rule says $\exp(x + y) = \exp(x)\exp(y) = 2 \cdot 5 = 10$, so $x + y = \ln 10$.
3. This agrees with $\ln 2 + \ln 5 = \ln(2 \cdot 5) = \ln 10$.
4. The inverse of $x$ in $(\mathbb{R}, +)$ is $-x = -\ln 2$, and $\exp(-\ln 2) = 1/2$.
5. The inverse of $2$ in $(\mathbb{R}_{>0}, \times)$ is $1/2$, so $\exp$ sends inverses to inverses.

The typical use of this example is to show that two groups with different operations can be isomorphic.
It also shows the general fact that a homomorphism with trivial kernel is injective.
A trap is to treat $\exp$ as a homomorphism from $(\mathbb{R}, +)$ to $(\mathbb{R}, +)$.
This fails, because $\exp(0 + 0) = 1$ but $\exp(0) + \exp(0) = 2$.
