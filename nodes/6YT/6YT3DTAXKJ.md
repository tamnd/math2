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
for every real $x$ that is not an integer multiple of $\pi$, where $\sin$ and $\cos$ are the [[sine and cosine|08WFZP6P89]].

1. Let $x$ be real and not a multiple of $\pi$.
   The zeros of $\sin$ are exactly the multiples of $\pi$, so $\sin x \ne 0$ and the left side is defined.
2. Also $\cos x = -1$ only at odd multiples of $\pi$, so $1 + \cos x \ne 0$ and the right side is defined.
3. Since $1 + \cos x \ne 0$, we may multiply the left side by $\frac{1 + \cos x}{1 + \cos x} = 1$:
   $$\frac{1 - \cos x}{\sin x} = \frac{(1 - \cos x)(1 + \cos x)}{\sin x \, (1 + \cos x)} = \frac{1 - \cos^2 x}{\sin x \, (1 + \cos x)}.$$
4. The [[Pythagorean identity|03H7WZ4T3K]] $\sin^2 x + \cos^2 x = 1$ turns the numerator into $\sin^2 x$.
5. Since $\sin x \ne 0$ by step 1, we cancel one factor $\sin x$ and reach $\frac{\sin x}{1 + \cos x}$, the right side.

Check at $x = \frac{\pi}{3}$: the left side is $\frac{1 - 1/2}{\sqrt3/2} = \frac{1}{\sqrt3}$, and the right side is $\frac{\sqrt3/2}{3/2} = \frac{1}{\sqrt3}$.

## Remarks

Steps 3 and 5 multiply and divide by expressions that vanish for some $x$.
Steps 1 and 2 show that they do not vanish on the domain, and that is what makes the chain valid there.
The same proof runs from right to left: multiply the right side by $\frac{1 - \cos x}{1 - \cos x}$, which needs $\cos x \ne 1$, again true off the multiples of $\pi$.

Both sides equal $\tan \frac{x}{2}$ where they are defined, the variable $t$ of the [[tangent half-angle substitution|0W8ETY2AZ6]].
At the edges of the domain the two expressions part ways.
At $x = 0$ and $x = 2\pi$ the left side is undefined, while the right side is $0$, so the right side extends the left side.
At $x = \pi$ neither side is defined.
So the two expressions are different functions on $\mathbb{R}$, even though they agree wherever both make sense.

## Explanations

### L1 human

The two fractions look different, but they give the same number for every allowed angle.
For an angle of $90$ degrees, $\cos$ is $0$ and $\sin$ is $1$, so both fractions are $1$.
The trick of the proof is to multiply the top and the bottom of the first fraction by the same number, $1 + \cos x$.
Then the rule $\sin^2 x + \cos^2 x = 1$ turns the top into $\sin^2 x$, and one $\sin x$ cancels.
You must avoid angles where you would divide by zero.

### L2 human

We prove $\frac{1}{1 + \cos x} + \frac{1}{1 - \cos x} = \frac{2}{\sin^2 x}$ for $x$ not a multiple of $\pi$.

1. As in the example, $1 + \cos x \ne 0$, and $1 - \cos x \ne 0$ because $\cos x = 1$ only at even multiples of $\pi$.
2. The common denominator is $(1 + \cos x)(1 - \cos x) = 1 - \cos^2 x$.
3. The numerators add to $(1 - \cos x) + (1 + \cos x) = 2$.
4. So the left side is $\frac{2}{1 - \cos^2 x} = \frac{2}{\sin^2 x}$, by the Pythagorean identity.

Identities like this simplify an integrand before you integrate.
Watch out: cross-multiplying the claim gives $(1 - \cos x)(1 + \cos x) = \sin^2 x$, which is true for every real $x$, so it hides the points where the fractions are undefined.
