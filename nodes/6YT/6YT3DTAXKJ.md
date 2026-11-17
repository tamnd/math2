---
tag: 6YT3DTAXKJ
kind: example
name: Two forms of the tangent of a half angle
msc: ["00A35", "97G60"]
topics: [MEKKHHQTKB]
audience: school
instance_of: [XP5SDYKJX0]
uses: [XP5SDYKJX0, 03H7WZ4T3K, 08WFZP6P89]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_trigonometric_identities
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Tangent_half-angle_substitution
    locator: lead section
---

## Example

We prove the [[identity|XP5SDYKJX0]]
$$\frac{1 - \cos x}{\sin x} = \frac{\sin x}{1 + \cos x}$$
for every real $x$ that is not an integer multiple of $\pi$.
Here $\sin$ and $\cos$ are the [[sine and cosine|08WFZP6P89]] functions.

1. Let $x$ be a real number that is not a multiple of $\pi$. Then $\sin x \neq 0$, because the zeros of $\sin$ are exactly the multiples of $\pi$. So the left side is defined.
2. We also have $1 + \cos x \neq 0$. Indeed, $\cos x = -1$ only when $x$ is an odd multiple of $\pi$, and $x$ is not a multiple of $\pi$. So the right side is defined.
3. Since $1 + \cos x \neq 0$, the quotient $\frac{1 + \cos x}{1 + \cos x}$ equals $1$. We multiply the left side by it:
$$\frac{1 - \cos x}{\sin x} = \frac{(1 - \cos x)(1 + \cos x)}{\sin x \, (1 + \cos x)}.$$
4. The numerator is a product of a difference and a sum, so it equals $1 - \cos^2 x$.
5. By the [[Pythagorean trigonometric identity|03H7WZ4T3K]] $\sin^2 x + \cos^2 x = 1$, we have $1 - \cos^2 x = \sin^2 x$.
6. So the left side equals $\frac{\sin^2 x}{\sin x \, (1 + \cos x)}$.
7. Since $\sin x \neq 0$ by step 1, we cancel one factor $\sin x$. The result is $\frac{\sin x}{1 + \cos x}$, the right side.

A check: at $x = \frac{\pi}{3}$ the left side is $\frac{1 - 1/2}{\sqrt3/2} = \frac{1}{\sqrt3}$, and the right side is $\frac{\sqrt3/2}{3/2} = \frac{\sqrt3}{3} = \frac{1}{\sqrt3}$.

## Remarks

1. The steps 3 and 7 multiply and divide by expressions that can be $0$ for other values of $x$. Steps 1 and 2 show that they are not $0$ on the domain, so the chain of equalities is valid on the whole domain.
2. Both sides equal $\tan \frac{x}{2}$ where they are defined. This is the quantity $t$ of the [[tangent half-angle substitution|0W8ETY2AZ6]].
3. At $x = 0$ both sides of the identity are not defined, but the right side has the value $0$ there. So the right side extends the left side, and the two expressions are different functions on $\mathbb{R}$.
4. At $x = \pi$ neither side is defined. At $x = 2\pi$ the right side is $0$ and the left side is not defined, as at $x = 0$.
5. The same proof works from right to left: multiply the right side by $\frac{1 - \cos x}{1 - \cos x}$, which needs $\cos x \neq 1$, again true off the multiples of $\pi$.

## Explanations

### L1 human

The two fractions look different, but they give the same number for each allowed angle.
For an angle of $90$ degrees, $\cos$ is $0$ and $\sin$ is $1$, so both fractions are $1$.
The trick of the proof is to multiply the top and the bottom of the first fraction by the same number, $1 + \cos x$.
Then the rule $\sin^2 x + \cos^2 x = 1$ turns the top into $\sin^2 x$, and one $\sin x$ cancels.
We must avoid angles where we would divide by zero.

### L2 human

We prove the related identity $\frac{1}{1 + \cos x} + \frac{1}{1 - \cos x} = \frac{2}{\sin^2 x}$ for $x$ not a multiple of $\pi$.

1. By step 2 of the example, $1 + \cos x \neq 0$, and in the same way $1 - \cos x \neq 0$, since $\cos x = 1$ only at even multiples of $\pi$.
2. The common denominator is $(1 + \cos x)(1 - \cos x) = 1 - \cos^2 x$.
3. The sum of the numerators is $(1 - \cos x) + (1 + \cos x) = 2$.
4. So the left side is $\frac{2}{1 - \cos^2 x} = \frac{2}{\sin^2 x}$, by the Pythagorean identity.

The typical use of such identities is the simplification of an integrand before integration.
A trap is to cross-multiply the claimed identity, $(1 - \cos x)(1 + \cos x) = \sin^2 x$, and to stop there.
That equation is true for every real $x$, also where the original fractions are not defined, so it does not show the domain of the identity.
