# Learning Probability Density Function using GAN

## What is this assignment about?
The goal of this assignment is to learn the probability density function of a transformed random variable using data samples only. Since no analytical form of the distribution is provided, a Generative Adversarial Network (GAN) is used to learn the distribution implicitly.

## Dataset
The NO₂ concentration values are taken from the India Air Quality dataset available on Kaggle.

## Data Transformation
Each NO₂ value x is transformed into z using the given transformation:
z = x + a_r * sin(b_r * x)

The values of a_r and b_r are calculated based on the university roll number.

## Why scaling is required
Before training the GAN, the transformed values z are scaled to the range [−1, 1]. This helps in stable GAN training and matches the output range of the generator network.

## GAN Architecture
The GAN consists of a simple fully connected generator and discriminator. The generator takes random noise sampled from a normal distribution and produces fake z samples, while the discriminator tries to distinguish between real and fake samples.

## PDF Estimation
After training, a large number of samples are generated from the generator. The probability density function is then approximated using histogram/KDE.
<img width="708" height="470" alt="image" src="https://github.com/user-attachments/assets/0a2ae951-022d-469f-b915-129f404f4fd5" />


## Observations
- The GAN was able to capture the overall shape of the data distribution.
- Some instability was observed during early training.
- Mode coverage improved after tuning the learning rate.

## Conclusion
This experiment shows that GANs can be used to learn unknown probability distributions directly from data without assuming any parametric form.

