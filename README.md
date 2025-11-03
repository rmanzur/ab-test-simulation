# A/B test simulation

Simulating A/B tests for a given baseline conversion rate (control conversion rate = 0.15), significance level (alpha = 0.05), and split ratio (50/50). 

H_0: difference in means = 0, H_A: difference in means ≠ 0 (two-sample, two-tailed Z test (note: in most settings, one-tailed test is the recommended approach, but two-tailed test is used here for illustrative purposes)

Results summarized below:

<img width="1368" height="936" alt="Image" src="https://github.com/user-attachments/assets/e444fcad-c0b6-4246-b5e7-d12af932bdbf" />

### Key Takeaways:

1) To detect a 5% relative lift (absolute lift = 0.75% with baseline conversion rate being 15%) with power at 80% and significance level = 5%, the minimum total sample size is ~72.6K (36.3K per variant)
   - To detect a smaller minimum detectable effect (<5% relative lift), the sample size required increases, as shown by the Total Sample Size vs. Relative Lift curve
2) The power curve was derived from 10K simulations of the A/B test using different sample sizes and calculating the proportion of significant tests. It shows the sample size needed to achieve different power levels for a given significance level (5%) and effect size (lift = 5%). It is a nonlinear curve with diminishing returns as the sample size increases.
3) Monte Carlo simulation was done to generate sampling distributions of the conversion rates in the two variants. The three charts at the bottom show these distributions with a total sample size set to achieve 80% power.
