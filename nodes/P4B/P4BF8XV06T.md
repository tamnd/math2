---
tag: P4BF8XV06T
kind: example
name: The triangle inequality for real numbers by cases
msc: ["00A35", "26A03"]
topics: [958EF46EYJ]
audience: school
instance_of: [0WCP0PVET6]
uses: [0WCP0PVET6, 00S7C68D51, 03HF5PMY5T]
sources:
  - url: https://en.wikipedia.org/wiki/Triangle_inequality
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Absolute_value
    locator: Real numbers
---

## Example

Statement: for all real numbers $x$ and $y$, $|x + y| \le |x| + |y|$.
This is the [[triangle inequality|03HF5PMY5T]] on the real line.
The [[absolute value|00S7C68D51]] is itself defined by cases: $|t| = t$ if $t \ge 0$, and $|t| = -t$ if $t < 0$.
We give a [[proof by cases|0WCP0PVET6]].

1. First we show that $t \le |t|$ and $-t \le |t|$ for every real $t$.
   If $t \ge 0$, then $t = |t|$ and $-t \le 0 \le |t|$.
   If $t < 0$, then $-t = |t|$ and $t < 0 < |t|$.
2. Let $x$ and $y$ be real numbers.
   Either $x + y \ge 0$ or $x + y < 0$, so two cases cover everything.
3. Case $x + y \ge 0$.
   Then $|x + y| = x + y$, and step 1 gives $x \le |x|$ and $y \le |y|$.
   Adding the two inequalities gives $|x + y| \le |x| + |y|$.
4. Case $x + y < 0$.
   Then $|x + y| = -(x + y) = (-x) + (-y)$, and step 1 gives $-x \le |x|$ and $-y \le |y|$.
   Adding the two inequalities gives $|x + y| \le |x| + |y|$.
5. The inequality holds in both cases, so it holds for all real $x$ and $y$.

Check: for $x = 3$ and $y = -5$ we are in case 4, and $|{-2}| = 2 \le 8 = 3 + 5$.

## Remarks

The split follows the definition of $|x + y|$, the expression on the left side.
A split by the signs of $x$ and $y$ also works, but it gives four cases, and the two cases with opposite signs each need a further split.
Choosing the split that matches the definition keeps the proof short.

Equality holds exactly when $x$ and $y$ do not have opposite signs, that is, when $xy \ge 0$.
For $x = 3$ and $y = 5$ both sides are $8$, while for $x = 3$ and $y = -5$ they are $2$ and $8$.
The [[proof of the triangle inequality for real numbers|HRTKMX90SJ]] avoids the second split by adding the bounds $-|x| \le x \le |x|$ and $-|y| \le y \le |y|$, but it still uses the case split of step 1 to get those bounds.

## Explanations

### L1 human

On a number line, $|x|$ is the distance from $0$ to $x$.
Walk $x$ steps and then $y$ steps, and you end at $x + y$.
The distance from the start to the end is at most the total number of steps walked, $|x| + |y|$.
If both walks go the same way, the two numbers are equal, for example $3 + 5 = 8$.
If the walks go in opposite directions, part of the walk is undone: $3$ steps right and $5$ steps left end only $2$ steps from the start.

### L2 human

The same two-case pattern proves the reverse triangle inequality $\big| |x| - |y| \big| \le |x - y|$ for all real $x$ and $y$.
Apply the triangle inequality to $x - y$ and $y$:
$$|x| = |(x - y) + y| \le |x - y| + |y|, \quad \text{so} \quad |x| - |y| \le |x - y|.$$
Exchange $x$ and $y$ to get $|y| - |x| \le |y - x| = |x - y|$.
Now split by the sign of $|x| - |y|$.
If it is at least $0$, the left side of the claim is $|x| - |y|$, and the first bound gives the claim.
If it is negative, the left side is $|y| - |x|$, and the second bound gives the claim.
This is the typical use: an absolute value on one side of an inequality gives two cases, one for each sign of the expression inside it.
Watch out: in case 4 of the example, $|x + y| = -(x + y) = -x - y$, not $-x + y$, because the minus sign applies to the whole sum.
