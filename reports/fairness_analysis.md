# Subgroup Performance and Fairness Limitations

## Evaluation method

The saved Random Forest pipeline was evaluated on the held-out test set at the project's default classification threshold of 0.50. The model test data contained 302 adults. Demographic attributes were joined to the model test rows by `SEQN`; all 302 rows matched one-to-one.

Sensitivity is the share of participants with the study-defined kidney marker that the model classified as positive. Specificity is the share without the marker that the model classified as negative. The race/ethnicity groups use NHANES `RIDRETH3` categories. Race/ethnicity and sex were used for subgroup auditing, not as model input features.

## Results

| Subgroup | Test n | Positive cases | Sensitivity | Specificity |
|---|---:|---:|---:|---:|
| Female | 141 | 61 | 57.4% | 77.5% |
| Male | 161 | 70 | 64.3% | 60.4% |
| Age 20–44 | 33 | 10 | 20.0% | 73.9% |
| Age 45–64 | 143 | 48 | 41.7% | 74.7% |
| Age 65+ | 126 | 73 | 79.5% | 54.7% |
| Mexican American | 40 | 13 | 46.2% | 55.6% |
| Other Hispanic | 34 | 11 | 72.7% | 60.9% |
| Non-Hispanic White | 91 | 45 | 75.6% | 76.1% |
| Non-Hispanic Black | 84 | 37 | 70.3% | 70.2% |
| Non-Hispanic Asian | 36 | 15 | 26.7% | 81.0% |
| Other race, including multiracial | 17 | 10 | 20.0% | 42.9% |

The largest observed differences are in sensitivity across age and race/ethnicity groups. The model detected 20.0% of positive cases in the 20–44 age group and 26.7% in the Non-Hispanic Asian group, compared with 79.5% among adults aged 65+ and 75.6% among Non-Hispanic White participants. The 65+ group also had lower specificity (54.7%), showing a different false-positive/false-negative balance at the chosen threshold.

These differences are signals for further investigation; they do not by themselves establish systematic bias or explain why the groups differ.

## Sample-size and interpretation limitations

- The evaluation includes only 302 held-out participants from this project dataset. Some subgroup metrics have small denominators: positive cases range from 10 to 73. Sensitivity based on 10–15 positive cases can change substantially when only a few predictions change.
- The “Other race, including multiracial” group has only 17 participants. Its rates are especially unstable and should not be used to make a firm comparison.
- These are unweighted sample-level metrics. NHANES documentation specifies special sample weights for population estimates; this audit did not apply those weights and should not be described as nationally representative.
- Results depend on the project's study-defined target, one train/test split, and the default 0.50 threshold, which was not separately tuned for each subgroup.
- The target represents a marker defined for this academic project. Model classifications and probability estimates are not diagnoses and should not guide care.

## Conclusion

This preliminary audit shows variation in model performance across the reported subgroups. Because the test set and positive-case counts are limited, further evaluation on larger samples, with uncertainty intervals and an appropriate NHANES survey design, is needed before drawing conclusions about fairness. The dashboard is an academic demonstration and is not a medical diagnostic tool.

## Data source

The `RIDRETH3` category labels and NHANES weighting notes follow the [CDC NHANES 2017–March 2020 Demographic Variables documentation](https://wwwn.cdc.gov/Nchs/Data/Nhanes/Public/2017/DataFiles/P_DEMO.htm).
