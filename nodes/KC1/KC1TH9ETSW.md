---
tag: KC1TH9ETSW
kind: example
name: Kleene's quantifier gives the Heaviside function
msc: ["03B30", "03F35", "26A15"]
topics: [BY8AAFN7C5]
audience: research
instance_of: [NPDRXTBW5W]
uses: [NPDRXTBW5W, 09C4JP7Y0M, 0X3WGX95FE, 0PWX18FM4G, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Use of higher-order arithmetic
  - url: https://en.wikipedia.org/wiki/Heaviside_step_function
    locator: lead section
---

## Example

No continuous procedure can tell from a stream of approximations whether a real is positive, and a functional that can see a whole stream at once does tell.
We work in $\mathsf{RCA}_0^\omega$ with Kleene's axiom $(\exists^2)$, and we fix $\varphi$ of type $2$ with $\varphi(g) = 0 \leftrightarrow \exists n\, g(n) = 0$ for all $g$ of type $1$.
A [[real number|08J2M1JYAG]] $x$ is given by a fast [[Cauchy sequence|0PWX18FM4G]] of rationals $(q_n)$, so that $\lvert q_n - x \rvert \le 2^{-n}$ for all $n$.
Two such sequences may represent the same real, and a function $F \colon \mathbb{R} \to \mathbb{R}$ must give equal outputs on equal reals.
We use the standard fact that $x > 0$ if and only if $x > 2^{-m}$ for some $m$.
We build the [[Heaviside function|09C4JP7Y0M]] $H$, with $H(x) = 1$ for $x > 0$ and $H(x) = 0$ for $x \le 0$, and show that it is discontinuous.

### Deciding positivity

1. Claim: $x > 0$ if and only if $q_n > 2^{-n+1}$ for some $n$.
2. Suppose $q_n > 2^{-n+1}$.
   Then $x \ge q_n - 2^{-n} > 2^{-n+1} - 2^{-n} = 2^{-n} > 0$.
3. Suppose $x > 0$, and take $m$ with $x > 2^{-m}$.
   Put $n = m + 2$, so that $x > 2^{-n+2} = 4 \cdot 2^{-n}$.
   Then $q_n \ge x - 2^{-n} > 3 \cdot 2^{-n} > 2^{-n+1}$.
4. Define $g_x(n) = 0$ if $q_n > 2^{-n+1}$, and $g_x(n) = 1$ otherwise.
   The comparison of two rationals is decidable, so $g_x$ is given by a term of $\mathsf{RCA}_0^\omega$ applied to the representation of $x$.
5. By step 1 and the choice of $\varphi$, $\varphi(g_x) = 0$ if and only if $x > 0$.

### The function and its jump

6. Define $F(x)$ as the real with constant representation $1$ if $\varphi(g_x) = 0$, and $0$ otherwise.
7. $F$ respects equality of reals.
   If $x$ and $y$ are two representations of the same real, then $x > 0 \leftrightarrow y > 0$, so $\varphi(g_x) = 0 \leftrightarrow \varphi(g_y) = 0$ by step 5.
   So $F(x) = F(y)$, although $g_x$ and $g_y$ may differ.
8. By step 5, $F(x) = 1$ for $x > 0$ and $F(x) = 0$ for $x \le 0$, so $F = H$.
9. $F$ is not [[continuous|0X3WGX95FE]] at $0$.
   We have $F(0) = 0$, and for each $k$ the point $2^{-k}$ is positive, so $F(2^{-k}) = 1$.
10. For $\varepsilon = 1$ and any $\delta > 0$, choose $k$ with $2^{-k} < \delta$.
    Then $\lvert 2^{-k} - 0 \rvert < \delta$ but $\lvert F(2^{-k}) - F(0) \rvert = 1$, which is not less than $\varepsilon$.

So $\mathsf{RCA}_0^\omega + (\exists^2)$ proves that a discontinuous function $\mathbb{R} \to \mathbb{R}$ exists.

## Remarks

Kohlenbach proved the converse: over $\mathsf{RCA}_0^\omega$, the existence of any discontinuous function $\mathbb{R} \to \mathbb{R}$ implies $(\exists^2)$.
The proof uses Grilliot's trick, which turns a point of discontinuity into a functional that decides $\exists n\, g(n) = 0$.
So $(\exists^2)$ is equivalent to "some function $\mathbb{R} \to \mathbb{R}$ is discontinuous", a reversal that second-order arithmetic cannot state, since it has no names for discontinuous functions.
Step 5 is the step that needs $\varphi$.
No continuous procedure can decide $x > 0$ from the representation of $x$, because a finite part of a representation of $0$ is also a finite part of a representation of some small positive real.

## Explanations

### L1 human

A real number is given as a list of better and better fractions.
To decide whether it is positive, one may have to read the whole infinite list, since the fractions near $0$ do not settle the question.
Kleene's quantifier is an oracle that looks at a whole infinite list at once and says whether some entry is $0$.
With it one can decide "is $x$ positive?" and so build the step function that jumps from $0$ to $1$.
A step function is not continuous, and this is the point of the example.

### L2 human

We test step 1 on $x = 2^{-3} = 0.125$ with the constant representation $q_n = 0.125$.

1. For $n = 3$ we have $2^{-n+1} = 0.25$, and $0.125 > 0.25$ fails, so $g_x(3) = 1$.
2. For $n = 5$ we have $2^{-n+1} = 0.0625$, and $0.125 > 0.0625$ holds, so $g_x(5) = 0$.
3. So $g_x$ has a zero, $\varphi(g_x) = 0$, and $F(x) = 1$.
4. For $x = 0$ with $q_n = 0$, the test $0 > 2^{-n+1}$ fails for every $n$.
   So $g_x$ is constantly $1$, $\varphi(g_x) \ne 0$, and $F(0) = 0$.

The typical use: building a discontinuous function from $(\exists^2)$ is the first step of most reversals in higher-order reverse mathematics.
The trap: the test $q_n > 0$ without the margin $2^{-n+1}$ fails, because a representation of $0$ may have $q_n = 2^{-n-1} > 0$.

### L3 human

Any functional that decides $x > 0$ for all reals $x$ gives a discontinuous function in the same way, so by Kohlenbach's converse it gives $(\exists^2)$.
In the model of the continuous functionals every functional is continuous, so $(\exists^2)$ fails there and so does the existence of $H$.
Grilliot's trick makes the converse precise, and together the two directions make $(\exists^2)$ the exact strength of "discontinuity exists".
