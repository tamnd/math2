---
tag: QXDY7STQWG
kind: definition
name: Missing data mechanisms
msc: [62D10]
defines: ES4MC30ZES
uses: [0DKRR22AEQ, 0QB913WM5E, 05FSTXM92W]
sources:
  - url: https://en.wikipedia.org/wiki/Missing_data
---

## Definition

Let $Y$ be the complete data, a [[random variable|0DKRR22AEQ]] with values in a product space, split as $Y = (Y_{\mathrm{obs}}, Y_{\mathrm{mis}})$ into its observed and its missing parts.
Let $R$ be the missingness indicator: $R_j = 1$ if entry $j$ of $Y$ is observed and $R_j = 0$ otherwise.
The *missing data mechanism* is the conditional [[distribution|0QB913WM5E]] of $R$ given $Y$, written $p(r \mid y; \phi)$ with a parameter $\phi$.

1. The data are *missing completely at random* (MCAR) if $p(r \mid y; \phi) = p(r; \phi)$ for all $y$, that is, $R$ does not depend on $Y$.
2. The data are *missing at random* (MAR) if $p(r \mid y_{\mathrm{obs}}, y_{\mathrm{mis}}; \phi) = p(r \mid y_{\mathrm{obs}}; \phi)$ for all $y_{\mathrm{mis}}$, that is, $R$ depends on $Y$ only through the observed part.
3. The data are *missing not at random* (MNAR) if they are not MAR.

## Remarks

MCAR implies MAR.

Example: let $Y = (Y_1, Y_2)$, where $Y_1$ (age) is always observed and $Y_2$ (income) is missing with probability $h(Y_1)$ for a function $h$ that is not constant.
Then $p(r \mid y)$ depends only on $y_1 = y_{\mathrm{obs}}$, so the data are MAR, but not MCAR.

Non-example: let $Y_2$ be missing with probability $h(Y_2)$ for a function $h$ that is not constant.
Then $p(r \mid y)$ depends on the missing value itself, so clause 2 fails and the data are MNAR.

Assume the data are MAR and the parameters $\theta$ of the data model and $\phi$ of the mechanism are distinct, that is, they vary in a product set.
Then the mechanism is called *ignorable*.
In that case, the [[likelihood|05FSTXM92W]] of $\theta$ based on $(y_{\mathrm{obs}}, r)$ is proportional to the likelihood based on $y_{\mathrm{obs}}$ alone.
