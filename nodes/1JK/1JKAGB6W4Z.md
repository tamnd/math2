---
tag: 1JKAGB6W4Z
kind: example
name: The sum rule for the complements of two lines in R3
msc: [15A63]
topics: [8GQVME4SZZ]
audience: ug1
instance_of: [0XJXTBCB2T]
illustrates: [T5Q51M5BAK]
uses: [079D68S3AW, 0RMKABS2S5, 05HQYM0R4G]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: Properties
---

## Example

In $\R^3$ with the [[dot product|05HQYM0R4G]], let $U = \R(1, 1, 0)$ and $W = \R(0, 1, 1)$.
We check the sum rule $(U + W)^\perp = U^\perp \cap W^\perp$ of the [[basic properties|T5Q51M5BAK]] by computing both sides.

1. The [[orthogonal complement|079D68S3AW]] $U^\perp$ is the plane $x_1 + x_2 = 0$, because $x \cdot (1, 1, 0) = x_1 + x_2$.
2. In the same way, $W^\perp$ is the plane $x_2 + x_3 = 0$, because $x \cdot (0, 1, 1) = x_2 + x_3$.
3. The intersection $U^\perp \cap W^\perp$ is the solution set of both equations. With $x_3 = t$ we get $x_2 = -t$ and $x_1 = t$, so $U^\perp \cap W^\perp = \R(1, -1, 1)$.
4. The [[sum|0RMKABS2S5]] $U + W$ is the plane spanned by $(1, 1, 0)$ and $(0, 1, 1)$, since the two vectors are not parallel.
5. By [[the plane example|38S0WYCSA3]], the complement of this plane is $\R(1, -1, 1)$.
6. Steps 3 and 5 give the same line, so $(U + W)^\perp = U^\perp \cap W^\perp$ here.

## Remarks

The two sides are computed in different ways, and that is the point of the rule.
The left side needs the sum $U + W$ first, while the right side treats each line on its own and then intersects.
Each of $U^\perp$ and $W^\perp$ is a plane, and two different planes through $0$ in $\R^3$ meet in a line, which is why the answer is a line.

If we change $W$ to $U$, then $U + W = U$, and both sides are the plane $x_1 + x_2 = 0$.
The union $U \cup W$ is not a subspace, but its complement is still the line $\R(1, -1, 1)$, as the rule $(S \cup T)^\perp = S^\perp \cap T^\perp$ for subsets says.

## Explanations

### L1 human

A vector is at a right angle to two lines exactly when it is at a right angle to the whole plane that the two lines span.
For the lines through $(1, 1, 0)$ and $(0, 1, 1)$, that vector lies on the line through $(1, -1, 1)$.

### L2 human

The rule turns one question about a sum into two easier questions, one for each part.
In matrix form, both sides lead to the null space of the matrix with rows $(1, 1, 0)$ and $(0, 1, 1)$, which is why they agree here.
Watch out: the rule with the roles swapped, $(U \cap W)^\perp = U^\perp \cap W^\perp$, is false.
Here $U \cap W = \{0\}$, so the left side is all of $\R^3$, while the right side is the line $\R(1, -1, 1)$.
The correct rule for intersections in finite dimension is $(U \cap W)^\perp = U^\perp + W^\perp$, and indeed the two planes $U^\perp$ and $W^\perp$ add up to $\R^3$.
