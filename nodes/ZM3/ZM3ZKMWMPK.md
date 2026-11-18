---
tag: ZM3ZKMWMPK
kind: example
name: Unit intervals defined by [B]⊥ over the natural numbers
msc: ["03B44"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [991B5RR6X4]
uses: [991B5RR6X4, 0MWKJ44V5A, 2W4S2H4VYA]
sources:
  - url: https://en.wikipedia.org/wiki/Allen%27s_interval_algebra
    locator: section Relations
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
---

## Example

Use the strict semantics of [[interval temporal logic|991B5RR6X4]]: intervals are $[a, b]$ with $a < b$.
The modality $\langle B \rangle$ is true at $[a, b]$ when its argument is true at some $[a, c]$ with $a < c < b$.
We work over the [[natural numbers|0MWKJ44V5A]] $(\mathbb{N}, <)$.

1. $[B]\bot$ is true at $[a, b]$ if and only if no $c$ satisfies $a < c < b$.
2. In $\mathbb{N}$, this holds if and only if $b = a + 1$. So $[B]\bot$ defines the intervals of length one.
3. Let $\lambda_2 = \langle B \rangle [B]\bot \wedge [B][B]\bot$.
4. $\langle B \rangle [B]\bot$ at $[a, b]$ says that some $[a, c]$ with $a < c < b$ has length one, that is $a + 1 < b$.
5. $[B][B]\bot$ says that every $[a, c]$ with $a < c < b$ has length one. So $c = a + 1$ is the only such $c$, and $b \le a + 2$.
6. Together, $\lambda_2$ holds exactly at the intervals $[a, a + 2]$.
7. Put $\lambda_1 = [B]\bot$ and $\lambda_{n+1} = \langle B \rangle \lambda_n \wedge [B](\lambda_1 \vee \dots \vee \lambda_n)$.
8. By induction on $n$, with the argument of steps 4 and 5, $\lambda_n$ holds exactly at the intervals $[a, a + n]$. For $n = 2$ this is the formula of step 3.

## Remarks

Over a [[dense order|2W4S2H4VYA]] such as $\mathbb{Q}$, every interval $[a, b]$ contains a point $c$ with $a < c < b$.
So $[B]\bot$ is false everywhere there.
So the validity of $\langle B \rangle\top$ characterizes density among linear orders, for the strict semantics.
In the non-strict semantics, $[B]\bot$ holds exactly at the point intervals $[a, a]$.

## Explanations

### L1 human

Over whole numbers, the shortest stretches of time go from one number to the next.
"No shorter stretch starts here" is true exactly for these unit stretches.
Over fractions there is no shortest stretch, so the same sentence is never true.

### L2 human

1. Take $[3, 4]$ in $\mathbb{N}$. There is no $c$ with $3 < c < 4$, so $[B]\bot$ is true.
2. Take $[3, 5]$. The interval $[3, 4]$ begins it, so $\langle B \rangle\top$ is true and $[B]\bot$ is false.
3. At $[3, 5]$, the only beginning interval is $[3, 4]$, which has length one, so $\lambda_2$ is true.

A trap: $[B]\bot$ is not a contradiction; a box of $\bot$ is true where there are no accessible intervals.
