# breast_cancer_EDA

![Image text](https://camo.githubusercontent.com/d9cdf50f50321eecb31dc14606132b5889c4b3d1fdb2b04225a89315046da60f/68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f6b6167676c652d64617461736574732d696d616765732f3138302f3338342f33646132353130353831663964336239303233303766663864303666653332372f646174617365742d636f7665722e6a7067)

## About the Dataset:
The Breast Cancer Diagnostic data is available on the UCI Machine Learning Repository. This database is also available through the UW CS ftp server.

Features are computed from a digitized image of a fine needle aspirate (FNA) of a breast mass. They describe characteristics of the cell nuclei present in the image. n the 3-dimensional space is that described in: [K. P. Bennett and O. L. Mangasarian: "Robust Linear Programming Discrimination of Two Linearly Inseparable Sets", Optimization Methods and Software 1, 1992, 23-34].

## Attribute Information:

* ID number
* Diagnosis (M = malignant, B = benign) 3-32)

### Ten real-valued features are computed for each cell nucleus:

1. radius (mean of distances from center to points on the perimeter)
2. texture (standard deviation of gray-scale values)
3. perimeter
4. area
5. smoothness (local variation in radius lengths)
6. compactness (perimeter^2 / area - 1.0)
7. concavity (severity of concave portions of the contour)
8. concave points (number of concave portions of the contour)
9. symmetry
10. fractal dimension ("coastline approximation" - 1)
11. The mean, standard error and "worst" or largest (mean of the three largest values) of these features were computed for each image, resulting in 30 features. For instance, field 3 is Mean Radius, field 13 is Radius SE, field 23 is Worst Radius.

* **All feature values are recoded with four significant digits.**
* **Missing attribute values: none**
* **Class distribution: 357 benign, 212 malignant**
