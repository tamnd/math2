---
tag: C170QFW8QB
kind: example
name: Curve fitting and linear regression by least squares
msc: ["15A06", "62J05", "65F20"]
topics: [K0FNC6CWZN]
audience: ug1
instance_of: [0BYTQ4X1HC]
illustrates: [4D7MRG4D91, V9AH43ZY91, 0MCDDSCB9Z]
uses: [0BYTQ4X1HC, 4D7MRG4D91, V9AH43ZY91, 0B8KZRT28M, 0MCDDSCB9Z]
sources:
  - book: isbn:9780321982384
    locator: Section 6.6
  - url: https://en.wikipedia.org/wiki/Linear_least_squares
    locator: Fitting a parabola
  - url: https://en.wikipedia.org/wiki/Coefficient_of_determination
    locator: Definitions
---

## Example

An experiment measures a response $y$ at five settings $s$ and gets
$$(s, y) = (-2, 0),\ (-1, 0),\ (0, 0),\ (1, 1),\ (2, 4).$$
No line and no parabola passes through all five points, because measured data rarely fits a model exactly.
So we ask for the line, and then the parabola, that makes the sum of the squared vertical errors as small as possible.
This is the [[least-squares problem|0BYTQ4X1HC]] for $A x \approx y$, and its answer is the orthogonal projection of $y$ onto the column space of $A$.
For each fit we also compute $R^2$, the share of the spread of the data that the fit explains, as a ratio of squared lengths.

**The regression line $y = c + m s$.**

1. The unknowns are $x = (c, m)$, and the columns of $A$ are $\mathbf{1} = (1, 1, 1, 1, 1)$ and $s = (-2, -1, 0, 1, 2)$, with $y = (0, 0, 0, 1, 4)$.
2. The two columns are independent, so the least-squares solution is unique, by [[existence and uniqueness of least-squares solutions|V9AH43ZY91]].
3. The [[normal equations|4D7MRG4D91]] $A^{\mathsf T} A x = A^{\mathsf T} y$ need the sums $\sum 1 = 5$, $\sum s = 0$, $\sum s^2 = 10$, $\sum y = 5$ and $\sum s y = 1 + 8 = 9$.
4. So we solve
$$\begin{pmatrix} 5 & 0 \\ 0 & 10 \end{pmatrix} \begin{pmatrix} c \\ m \end{pmatrix} = \begin{pmatrix} 5 \\ 9 \end{pmatrix}, \qquad c = 1, \quad m = 0.9.$$
5. The fitted values $\hat y = 1 + 0.9 s$ are $(-0.8, 0.1, 1, 1.9, 2.8)$, and the residual is $r = y - \hat y = (0.8, -0.1, -1, -0.9, 1.2)$.
6. Check: $r \cdot \mathbf 1 = 0$ and $r \cdot s = -1.6 + 0.1 + 0 - 0.9 + 2.4 = 0$.
   So $r$ is orthogonal to the column space, as the normal equations require.
7. The residual sum of squares is $\norm{r}^2 = 0.64 + 0.01 + 1 + 0.81 + 1.44 = 3.9$.

**The parabola $y = a + b s + c s^2$.**

1. Add the column $s^2 = (4, 1, 0, 1, 4)$ to $A$.
   The three columns are independent, because a nonzero polynomial of degree at most $2$ has at most $2$ roots and here $s$ takes $5$ values.
2. The new sums are $\sum s^3 = 0$, $\sum s^4 = 16 + 1 + 1 + 16 = 34$ and $\sum s^2 y = 1 + 16 = 17$.
3. The normal equations are
$$\begin{pmatrix} 5 & 0 & 10 \\ 0 & 10 & 0 \\ 10 & 0 & 34 \end{pmatrix} \begin{pmatrix} a \\ b \\ c \end{pmatrix} = \begin{pmatrix} 5 \\ 9 \\ 17 \end{pmatrix}.$$
4. The second row gives $b = 0.9$, and the first row gives $a = 1 - 2c$.
   Put this into the third row: $10 - 20 c + 34 c = 17$, so $c = 0.5$ and $a = 0$.
5. The fitted parabola is $y = 0.9 s + 0.5 s^2$, with the fitted values $(0.2, -0.4, 0, 1.4, 3.8)$.
6. The residual is $(-0.2, 0.4, 0, -0.4, 0.2)$, and its squared length is $0.04 + 0.16 + 0 + 0.16 + 0.04 = 0.4$.

**$R^2$ as a projection length.**

1. The mean of $y$ is $\bar y = 1$, and the centered data $y - \bar y \mathbf 1 = (-1, -1, -1, 0, 3)$ has squared length $12$.
2. Both models contain the constant column $\mathbf 1$.
   So $\hat y - \bar y \mathbf 1$ is the [[orthogonal projection|0B8KZRT28M]] of $y - \bar y \mathbf 1$ onto the model space, and it is orthogonal to $r$.
3. The Pythagorean theorem then gives
$$\norm{y - \bar y \mathbf 1}^2 = \norm{\hat y - \bar y \mathbf 1}^2 + \norm{r}^2.$$
4. For the line, $\hat y - \bar y \mathbf 1 = 0.9\, s$ has squared length $0.81 \cdot 10 = 8.1$.
   Check: $8.1 + 3.9 = 12$, and $R^2 = 8.1 / 12 = 0.675$.
5. For the parabola, $\hat y - \bar y \mathbf 1 = (-0.8, -1.4, -1, 0.4, 2.8)$ has squared length $11.6$.
   Check: $11.6 + 0.4 = 12$, and $R^2 = 11.6 / 12 = \tfrac{29}{30} \approx 0.967$.
6. So $R^2$ is the squared cosine of the angle between the centered data and its projection onto the model space.

## Remarks

### What the example shows

The parabola fits better than the line, and this always happens for nested models.
The model space of the line lies inside the model space of the parabola.
So by the [[best approximation theorem|0MCDDSCB9Z]], the residual of the parabola is never longer than the residual of the line.
This is why $R^2$ alone cannot choose between models: adding a column never lowers $R^2$.
Whether the extra coefficient is worth having is a question for statistics.

### Why the sums were so easy

The settings $s$ are centered, with $\sum s = 0$ and $\sum s^3 = 0$.
This makes the column $s$ orthogonal to the columns $\mathbf 1$ and $s^2$, so $A^{\mathsf T} A$ has many zeros and the normal equations split into smaller systems.
For settings that are not centered, subtract their mean first, or solve the full system.
For example, the settings $0, 1, 2, 3, 4$ become $-2, -1, 0, 1, 2$ after you subtract $2$.

### When the columns are dependent

If $s$ takes fewer distinct values than the number of coefficients, the columns of $A$ are dependent.
For example, a parabola fitted to data at only the two settings $s = 0$ and $s = 1$ has the columns $\mathbf 1$, $s$ and $s^2 = s$, and the last two are equal.
Then the least-squares solution is not unique, although the fitted values $\hat y$ are still unique, because the projection is.

### Watch out

The formula $R^2 = 1 - \norm{r}^2 / \norm{y - \bar y \mathbf 1}^2$ needs a constant column in the model.
Without it, $\hat y - \bar y \mathbf 1$ need not be orthogonal to $r$, and the Pythagorean split of step 3 fails.
For example, the model $y \approx m s$ with no constant fits our data with $m = 0.9$, and the residual $y - 0.9 s$ has squared length $8.9$.
Then $\norm{0.9 s - \mathbf 1}^2 = 13.1$, and $13.1 + 8.9 = 22 \ne 12$.

### Where the theory lives

The statistical meaning of the fit belongs to [[linear regression|41FVC4P5JB]], and the meaning of $R^2$ belongs to the [[coefficient of determination|B45RMKMVZ5]].
That includes the noise model, confidence intervals and tests.
A smaller case with the line only is [[a least-squares line through four points|H2D0QA4AXV]].

### Try it

First, fit the line $y = c + m s$ to the points $(-1, 1)$, $(0, 2)$, $(1, 6)$.
The sums are $\sum s = 0$, $\sum s^2 = 2$, $\sum y = 9$ and $\sum s y = 5$, so $c = 3$ and $m = 2.5$.

Second, compute the residual of that fit and check that it is orthogonal to both columns.
The fitted values are $(0.5, 3, 5.5)$, so $r = (0.5, -1, 0.5)$, and $r \cdot \mathbf 1 = 0$ and $r \cdot s = -0.5 + 0.5 = 0$.

## Explanations

### L1 human

Data from an experiment rarely lies exactly on a line.
Least squares picks the line that makes the total of the squared vertical misses as small as possible.
For the five points here, the best line is $y = 1 + 0.9 s$, and the best parabola is $y = 0.9 s + 0.5 s^2$.
The number $R^2$ says how much of the spread of the data the fit explains: about $68\%$ for the line and about $97\%$ for the parabola.

### L2 human

Here is the general recipe, seen through the example.
For a model $y \approx x_1 f_1(s) + \dots + x_k f_k(s)$, column $j$ of $A$ holds the values of $f_j$ at the data points, so the parabola had the columns $\mathbf 1$, $s$ and $s^2$.
You then solve $A^{\mathsf T} A x = A^{\mathsf T} y$, compute the residual $r = y - A x$, and check that $A^{\mathsf T} r = 0$.
The model must be linear in the unknown coefficients, but not in $s$, so a parabola is still a linear model.
For large or badly scaled problems, forming $A^{\mathsf T} A$ loses accuracy, and a QR factorization of $A$ gives the same answer more safely.

### L3 human

Least squares is the orthogonal projection of $y$ onto the column space of $A$ in the inner product $\sum_i u_i v_i$.
A weighted inner product $\sum_i w_i u_i v_i$ gives weighted least squares, with the normal equations $A^{\mathsf T} W A x = A^{\mathsf T} W y$.
With one predictor and a constant, $R^2$ is the square of the correlation coefficient of $s$ and $y$: here $9^2 / (10 \cdot 12) = 0.675$.
The projection matrix $A (A^{\mathsf T} A)^{-1} A^{\mathsf T}$ is the hat matrix of statistics, and its trace is the number of coefficients.
The same projection idea returns in [[image compression by the SVD|9QB82PPEMV]], where the best subspace is chosen as well.
