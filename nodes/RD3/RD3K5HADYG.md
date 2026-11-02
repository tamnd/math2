---
tag: RD3K5HADYG
kind: definition
name: Matching pursuit
msc: [41A46, 94A12, 41A65]
defines: 8KJ9P9KQ5H
uses: [HM2HHE3J51, GEK0NP5WQM]
sources:
  - url: https://en.wikipedia.org/wiki/Matching_pursuit
---

## Definition

Let $H$ be a real or complex [[Hilbert space|HM2HHE3J51]] with inner product $\ip{\cdot}{\cdot}$ and norm $\norm{\cdot}$.
Let $\mathcal{D} \subseteq H$ be a dictionary of unit vectors, and let $f \in H$.
*Matching pursuit* produces residuals $r_k$, elements $g_k \in \mathcal{D}$ and approximants $f_k$ as follows.

1. Set $r_0 = f$ and $f_0 = 0$.
2. For $k \ge 1$, choose $g_k \in \mathcal{D}$ with $\abs{\ip{r_{k-1}}{g_k}} = \sup\set{\abs{\ip{r_{k-1}}{g}} : g \in \mathcal{D}}$.
3. Set $r_k = r_{k-1} - \ip{r_{k-1}}{g_k} g_k$ and $f_k = f_{k-1} + \ip{r_{k-1}}{g_k} g_k$.

## Remarks

By construction $f = f_k + r_k$, and $f_k$ is an [[n-term approximant|GEK0NP5WQM]] with $n = k$.
Since $r_k$ is orthogonal to $g_k$, $\norm{r_k}^2 = \norm{r_{k-1}}^2 - \abs{\ip{r_{k-1}}{g_k}}^2$, so the residual norms never increase.
When the supremum in clause 2 is not attained, one uses a weak version that only asks for a fixed fraction $t \in (0, 1]$ of it.
Example: in $\R^2$ with $\mathcal{D} = \set{e_1, e_2, u}$, $u = (1, 1)/\sqrt{2}$, and $f = (2, 1)$.
The correlations are $2$, $1$ and $3/\sqrt{2} \approx 2.12$, so $g_1 = u$, $f_1 = (3/2, 3/2)$ and $r_1 = (1/2, -1/2)$.
Then $\ip{r_1}{u} = 0$ and $\abs{\ip{r_1}{e_1}} = \abs{\ip{r_1}{e_2}} = 1/2$; choosing $g_2 = e_1$ gives $r_2 = (0, -1/2)$, and $g_3 = e_2$ gives $r_3 = 0$.
Non-example: choosing $g_1 = e_1$ at the first step fails clause 2, since $\abs{\ip{f}{e_1}} = 2 < 3/\sqrt{2}$.
*Orthogonal matching pursuit* replaces clause 3 by taking $f_k$ to be the orthogonal projection of $f$ onto the span of $g_1, \dots, g_k$ and $r_k = f - f_k$.
